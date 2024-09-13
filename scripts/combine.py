import os
import json
import shutil
import re

import markdown2
from xhtml2pdf import pisa


def adjust_image_paths(content_text, index_file_path):
    # we need to find all the image tags and replace the relative backsteps to point to the images folder from the new index file <img src="../images/profile.jpg" alt="profile_picture" width="400">
    image_tags = content_text.split('<img')
    for i, tag in enumerate(image_tags):
        if i == 0:
            continue
        src_start = tag.find('src="') + 5
        src_end = tag.find('" ', src_start)
        original_src = tag[src_start:src_end]
        removed_back_steps_src = original_src.replace('../', '')
        depth_from_index = index_file_path.count('/')
        back_steps = '../' * depth_from_index
        new_src = f'{back_steps}{removed_back_steps_src}'
        content_text = content_text.replace(original_src, new_src)

    return content_text


def process_content_list(content_list, language_suffix, index_file):
    for content in content_list:
        if 'generate' in content and 'file' not in content:
            if 'link' in content and 'content' in content:
                # the content is linking to a file and also has nested content,
                # the 'generate' section will be used to place and generate the content

                generated_section_path = generate_section(content['generate'], language_suffix, content['content'])
                back_steps = index_file.name.count('/') - 2
                steps = "../" * back_steps
                index_file.write(f'{content["link"][language_suffix]}({steps}{generated_section_path})\n\n')

        elif 'generate' in content and 'file' in content:
            # the config file has both a 'generate' section and a 'file' section that's not supported
            print(f'Both generate and file sections are not supported in the same content at '
                  f'content:{content['content']}'
                  f'file:{content['file']}')

        elif 'generate' not in content and 'file' not in content:
            # the config file is missing a 'generate' section and a 'file' section that's not supported
            print(f'Both generate and file sections are missing in the same content at {content}')

        elif 'generate' not in content and 'file' in content:
            if 'link' not in content and 'content' not in content:
                # the content is a simple file we need to include
                # we need to make sure the file exists first
                content_filepath = f'../sections/{content["file"]}{language_suffix}.md'
                if os.path.exists(content_filepath):
                    with open(content_filepath, 'r') as content_file:
                        content_text = content_file.read()
                        working_file_path = os.path.dirname(index_file.name)
                        content_text = adjust_image_paths(content_text, working_file_path)
                        index_file.write(content_text+'\n\n')
                else:
                    current = os.getcwd()
                    print(f'File inclusion not found at ({content_filepath}) from {current}')

            elif 'link' in content and 'content' not in content:
                # the content is a simple file we need to link to
                # we need to make sure the file exists first
                content_filepath = f'../sections/{content["file"]}{language_suffix}.md'
                if os.path.exists(content_filepath):
                    back_steps = index_file.name.count('/') - 2
                    steps = "../" * back_steps
                    index_file.write(f'{content["link"][language_suffix]}({steps}{content_filepath})\n\n')
                else:
                    current = os.getcwd()
                    print(f'File linking not found at ({content_filepath}) from {current}')

            elif 'link' not in content and 'content' in content:
                # the content is a nested list of content
                process_content_list(content['content'], language_suffix, index_file)


def generate_section(filename, language_suffix, content):
    """Generate a section file based on the section name and content."""
    section_filepath = f'../generated/sections/{filename}{language_suffix}.md'
    os.makedirs(os.path.dirname(section_filepath), exist_ok=True)

    with open(section_filepath, 'x') as section_file:
        section_file.write(f'\n')
        process_content_list(content, language_suffix, section_file)

    return section_filepath


def combine_index(profile='demo', languages=None):
    """Main function to combine the content based on the profile and language."""
    if languages is None:
        languages = ['en']
    with open('cv_config.json', 'r') as config_file:
        config = json.load(config_file)

    if 'supported_languages' not in config:
        print(f'Language support and suffixes not found in configuration.')
        return

    if profile not in config:
        print(f'Profile {profile} not found in configuration.')
        return

    for language in languages:
        language_suffix = config['supported_languages'][language]
        sections = config[profile]['content']

        output_file = os.path.join('../generated', f'{profile}_output{language_suffix}.md')
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            # Process all content recursively, passing the section path for folder structure
            process_content_list(sections, language_suffix, index_file)

        print(f'Combined sections into {output_file}')


def convert_md_to_html(md_content):
    """Convert markdown content to HTML."""
    return markdown2.markdown(md_content)


def convert_html_to_pdf(html_content, pdf_output_path):
    """Convert HTML content to PDF using xhtml2pdf (pisa)."""
    with open(pdf_output_path, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_content, dest=result_file)
    return pisa_status.err


def convert_local_links_to_hosted_pdfs(content_text, github_repo_url):
    """Convert local markdown links to GitHub-hosted PDF links, while leaving image src untouched."""

    # Pattern to match Markdown links (e.g., [Go to web development project](../sections/...))
    link_pattern = r'\[(.*?)\]\((.*?)\)'

    def replace_link(match):
        link_text = match.group(1)
        link_url = match.group(2)

        # If the link is to a markdown file, adjust it to point to the hosted PDF
        if link_url.startswith("../sections/") or link_url.startswith("../generated/sections/"):
            hosted_link = link_url.replace("../", "").replace("generated/", "")
            # blob/main/sections/ -> raw/main/generated/sections/ so that the link points to the PDF file download instead of the GitHub preview
            hosted_link = hosted_link.replace("sections/", f"{github_repo_url}/raw/main/generated/sections/")
            hosted_link = hosted_link.replace(".md", ".pdf")
            return f'[{link_text}]({hosted_link}) [↓]'

        # Otherwise, return the original link (e.g., external links)
        return match.group(0)

    # Apply the link replacement only to markdown links, not image sources
    updated_content = re.sub(link_pattern, replace_link, content_text)

    return updated_content


def generate_pdf_from_md(md_filepath, pdf_output_path, github_repo_url=None):
    """Convert a markdown file to PDF."""
    # Read the markdown file with UTF-8 encoding
    with open(md_filepath, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Optionally replace local links with web-based links
    if github_repo_url:
        md_content = convert_local_links_to_hosted_pdfs(md_content, github_repo_url)
        md_content_adjusted = adjust_image_paths(md_content, md_filepath)

    # Convert Markdown to HTML
    html_content = convert_md_to_html(md_content_adjusted)

    # Convert the HTML content to PDF
    error = convert_html_to_pdf(html_content, pdf_output_path)

    if not error:
        print(f"PDF generated successfully at: {pdf_output_path}")
    else:
        print(f"Error generating PDF at: {pdf_output_path}")


def traverse_and_generate_pdfs(source_dir, target_dir, github_repo_url=None):
    """Traverse through the source directory, generate PDFs for .md files, and place them in the target directory."""

    # Walk through the directory structure
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                # Get the full path of the markdown file
                md_filepath = os.path.join(dirpath, filename)

                # Determine the relative path to maintain folder structure
                relative_path = os.path.relpath(md_filepath, source_dir)

                # Generate the corresponding PDF output path in the target directory
                pdf_output_path = os.path.join(target_dir, relative_path).replace('.md', '.pdf')

                # Ensure the target directory exists
                os.makedirs(os.path.dirname(pdf_output_path), exist_ok=True)

                # Convert the markdown file to PDF
                generate_pdf_from_md(md_filepath, pdf_output_path, github_repo_url)

                print(f"Converted {md_filepath} to {pdf_output_path}")


# One-step process to combine sections and generate PDFs

# clean generated folder
shutil.rmtree('../generated', ignore_errors=True)

# Combine sections for the demo profile and default languages
combine_index(profile='demo')
combine_index(profile='default', languages=['en', 'hu'])

# Generate PDFs for all markdown files
source_dir = '../sections'
target_dir = '../generated/sections'

source_dir2 = '../generated'
target_dir2 = '../generated'

with open('cv_config.json', 'r') as config_file:
    config = json.load(config_file)
    github_repo_url = config['github-repo-url']

traverse_and_generate_pdfs(source_dir2, target_dir2, github_repo_url)
traverse_and_generate_pdfs(source_dir, target_dir, github_repo_url)
