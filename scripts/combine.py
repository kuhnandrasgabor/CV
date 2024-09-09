import os
import json
import shutil


def generate_github_link(language, section, section_path, is_nested=False):
    """Generate the correct link to the section, respecting the folder structure."""
    if is_nested:
        return f'../sections/{section_path}/{section}'
    return f'../generated/sections/{section_path}/{section}'


def adjust_image_paths(content, current_depth, target_depth):
    adjustment = "../" * (target_depth - current_depth)
    return content.replace("../../../", f"../{adjustment}")


def process_content_list(content_list, language_suffix, index_file):
    for content in content_list:
        if 'link' not in content and 'content' not in content:
            # the content is a simple file we need to include
            # we need to make sure the file exists first
            content_filepath = f'../sections/{content["file"]}{language_suffix}.md'
            if os.path.exists(content_filepath):
                with open(content_filepath, 'r') as content_file:
                    content_text = content_file.read()
                    content_text = adjust_image_paths(content_text, 10, 2)
                    index_file.write(content_text)
            else:
                current = os.getcwd()
                print(f'File inclusion not found at ({content_filepath}) from {current}')

        elif 'link' in content and 'content' not in content:
            # the content is a simple file we need to link to
            # we need to make sure the file exists first
            content_filepath = f'../sections/{content["file"]}{language_suffix}.md'
            if os.path.exists(content_filepath):
                index_file.write(f'{content["link"][language_suffix]}({content_filepath})\n\n')
            else:
                current = os.getcwd()
                print(f'File linking not found at ({content_filepath}) from {current}')

        elif 'link' not in content and 'content' in content:
            # the content is a nested list of content
            process_content_list(content['content'], language_suffix, index_file)

        elif 'link' in content and 'content' in content:
            # the content is linking to a file and also has nested content
            # the file in this case will be the filename of the section we will generate and link to
            generated_section_path = generate_section(content['file'], language_suffix, content['content'])

            index_file.write(f'{content["link"][language_suffix]}({generated_section_path})\n\n')


def generate_section(filename, language_suffix, content):
    """Generate a section file based on the section name and content."""
    section_filepath = f'../generated/sections/{filename}{language_suffix}.md'
    os.makedirs(os.path.dirname(section_filepath), exist_ok=True)

    with open(section_filepath, 'x') as section_file:
        section_file.write(f'# {filename}\n\n')
        process_content_list(content, language_suffix, section_file)

    return section_filepath


def combine_index(profile='demo'):
    """Main function to combine the content based on the profile and language."""
    with open('cv_config.json', 'r') as config_file:
        config = json.load(config_file)

    if profile not in config:
        print(f'Profile {profile} not found in configuration.')
        return

    language_suffixes = {'en': '_en', 'hu': '_hu'}

    for language in ['en', 'hu']:
        language_suffix = language_suffixes[language]
        sections = config[profile]['content']

        output_file = os.path.join('../generated', f'{profile}_output{language_suffix}.md')
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            # Process all content recursively, passing the section path for folder structure
            process_content_list(sections, language_suffix, index_file)

        print(f'Combined sections into {output_file}')


# delete generated folder
shutil.rmtree('../generated', ignore_errors=True)
combine_index(profile='demo')
