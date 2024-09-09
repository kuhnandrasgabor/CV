import os
import json

def generate_github_link(language, section, is_nested=False):
    """Generate the correct link to the section. Handle nested files to avoid double ../generated/"""
    if is_nested:
        return f'../sections/{section}'
    return f'../generated/sections/{section}'

def adjust_image_paths(content, current_depth, target_depth):
    adjustment = "../" * (target_depth - current_depth)
    return content.replace("../../../", f"../{adjustment}")

def process_content(content_list, language_suffix, index_file, depth=1, profile="", is_nested=False):
    """Process the content recursively. Ensure that both linked and included content are handled correctly."""
    for content in content_list:
        if 'file' in content:
            content_file = f'{content["file"]}{language_suffix}.md'
            content_path = f'../sections/{content_file}'

            if os.path.exists(content_path):
                if 'link-text' not in content:
                    # Include the content directly
                    with open(content_path, 'r') as content_file:
                        content_data = content_file.read()
                        content_data = adjust_image_paths(content_data, len(content["file"].split('/')), depth)
                        index_file.write(content_data + '\n\n')
                else:
                    # Link the content, generate section if necessary
                    section_file = generate_section(content, language_suffix, profile)
                    link = generate_github_link(language_suffix, os.path.basename(section_file), is_nested=is_nested)
                    index_file.write(f"{content['link-text'][language_suffix]}({link})\n")
            else:
                print(f'Content file {content_file} does not exist')

        # Check if "content" exists and process it recursively
        if 'content' in content:
            if 'link-text' in content:
                # Generate the content as a standalone section if it's to be linked
                section_file = generate_section(content, language_suffix, profile)
                link = generate_github_link(language_suffix, os.path.basename(section_file), is_nested=is_nested)
                index_file.write(f"{content['link-text'][language_suffix]}({link})\n")
            else:
                # Directly include the nested content
                process_content(content['content'], language_suffix, index_file, depth + 1, profile, is_nested)

def generate_section(content, language_suffix, profile):
    """Generate a section file dynamically and return the path"""
    section_file = f'../generated/sections/{profile}_{content["file"]}{language_suffix}.md'
    os.makedirs(os.path.dirname(section_file), exist_ok=True)  # Ensure the directory exists

    if os.path.exists(section_file):
        os.remove(section_file)

    with open(section_file, 'x') as section_index:
        # If there is content, process it recursively
        if 'content' in content:
            process_content(content['content'], language_suffix, section_index, profile=profile, is_nested=True)
        else:
            # If there's no nested content, just include the section's own file content
            content_file = f'../sections/{content["file"]}{language_suffix}.md'
            if os.path.exists(content_file):
                with open(content_file, 'r') as original_content:
                    section_index.write(original_content.read() + '\n\n')

    return section_file

def combine_index(profile='demo'):
    """Main function to combine the content based on the profile and language"""
    with open('cv_config.json', 'r') as config_file:
        config = json.load(config_file)

    if profile not in config:
        print(f'Profile {profile} not found in configuration.')
        return

    language_suffixes = {'en': '_en', 'hu': '_hu'}

    for language in ['en', 'hu']:
        language_suffix = language_suffixes[language]
        sections = config[profile]['content']

        output_file = f'../generated/demo_output{language_suffix}.md'
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            # Process all content recursively
            process_content(sections, language_suffix, index_file, profile=profile)

        print(f'Combined sections into {output_file}')


# Example usage
combine_index(profile='demo')
