import os
import json


def generate_github_link(language, section):
    base_url = 'https://github.com/kuhnandrasgabor/CV/blob/main'
    return f'{base_url}/sections/{section}'


def combine_index(profile='general'):
    # Load the configuration from the JSON file
    with open('cv_config.json', 'r') as config_file:
        config = json.load(config_file)

    if profile not in config:
        print(f'Profile {profile} not found in configuration.')
        return

    # Define the language suffixes
    language_suffixes = {
        'en': '_en',
        'hu': '_hu'
    }

    for language in ['en', 'hu']:
        language_suffix = language_suffixes[language]

        sections = config[profile]['sections']

        output_file = f'../generated/CV_{profile.capitalize()}_{language.capitalize()}.md'

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            for section in sections:
                section_file = f'{section["file"]}{language_suffix}.md'
                section_path = f'../sections/{section_file}'

                if os.path.exists(section_path):
                    if section.get('include', False):
                        # Include the content directly
                        with open(section_path, 'r') as section_content:
                            index_file.write(section_content.read() + '\n\n')
                    else:
                        # Add a link to the section
                        if section.get('externally-link', False):
                            # Generate an external link to the GitHub version
                            index_file.write(
                                f"\n ### [More on {section.get('title')}]({generate_github_link(language, section_file)})\n"
                            )
                        else:
                            # Generate an internal relative link (relative to the generated file)
                            relative_link = f'../sections/{section_file}'
                            index_file.write(
                                f"{section.get('button-text')[language_suffix]}({relative_link})\n"
                            )
                else:
                    print(f'Section file {section_file} does not exist')

        print(f'Combined sections into {output_file}')


# Example usage to generate the 'general' profile
combine_index(profile='general')
combine_index(profile='devops')
combine_index(profile='ml-focused')


# You can generate other profiles like 'devops' or 'ml-focused' by changing the profile argument
# combine_index(profile='devops')
# combine_index(profile='ml-focused')
