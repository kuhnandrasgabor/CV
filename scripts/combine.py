import os
import json
import shutil

import markdown2
from xhtml2pdf import pisa



def adjust_image_paths(content_text, index_file_path):
    # we need to find all the image tags and replace the relative backsteps to point to the images folder from the new index file <img src="../images/profile.jpg" alt="profile_picture" style="max-width:400px;">
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


# # delete generated folder
# shutil.rmtree('../generated', ignore_errors=True)
# combine_index(profile='demo')
# combine_index(profile='default', languages=['en', 'hu'])

def convert_md_to_html(md_content):
    """Convert markdown content to HTML."""
    return markdown2.markdown(md_content)

def convert_html_to_pdf(html_content, pdf_output_path):
    """Convert HTML content to PDF using xhtml2pdf (pisa)."""
    with open(pdf_output_path, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_content, dest=result_file)
    return pisa_status.err

def generate_pdf_from_md(md_filepath, pdf_output_path):
    """Convert a markdown file to PDF."""
    # Read the markdown file with UTF-8 encoding
    with open(md_filepath, 'r', encoding='utf-8') as md_file:
        md_content = md_file.read()

    # Convert Markdown to HTML
    html_content = convert_md_to_html(md_content)

    # Convert the HTML content to PDF
    error = convert_html_to_pdf(html_content, pdf_output_path)

    if not error:
        print(f"PDF generated successfully at: {pdf_output_path}")
    else:
        print(f"Error generating PDF at: {pdf_output_path}")


# Example usage
md_filepath = '../generated/demo_output_en.md'
pdf_output_path = md_filepath.replace('.md', '.pdf')
generate_pdf_from_md(md_filepath, pdf_output_path)

md_filepath = '../generated/default_output_en.md'
pdf_output_path = md_filepath.replace('.md', '.pdf')
generate_pdf_from_md(md_filepath, pdf_output_path)