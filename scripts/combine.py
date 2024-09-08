import os
import json


def generate_github_link(language, section):
    base_url = 'https://github.com/kuhnandrasgabor/CV/blob/main'
    return f'{base_url}/sections/{section}'


def combine_index():
    # Define the language suffixes
    language_suffixes = {
        'en': '_en',
        'hu': '_hu'
    }

    for language in ['en', 'hu']:
        language_suffix = language_suffixes[language]

        sections = [
            {"file": f'personal-info{language_suffix}.md', "include": True},
            {"file": f'experience{language_suffix}.md', "include": True},
            {"file": f'experience/experience-summary{language_suffix}.md', "include": True},
            {"file": f'experience/pzartech-header{language_suffix}.md', "include": True},
            {"file": f'experience/pzartech-summary{language_suffix}.md', "include": True},
            {"file": f'experience/pzartech-webdev{language_suffix}.md', "include": True},
            {"file": f'experience/pzartech-ml{language_suffix}.md', "include": False, "title": "Machine Learning",
             "externally-link": False},
            {"file": f'experience/pzartech-ml{language_suffix}.md', "include": False, "title": "Machine Learning",
             "externally-link": True},
        ]

        output_file = f'../generated/CV_{language.capitalize()}.md'

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            for section in sections:
                section_path = f'../sections/{section["file"]}'
                if os.path.exists(section_path):
                    if section.get('include'):
                        # Include the content directly
                        with open(section_path, 'r') as section_file:
                            index_file.write(section_file.read() + '\n\n')
                    else:
                        # Add a link to the section
                        if section.get('externally-link'):
                            # Generate an external link to the GitHub version
                            index_file.write(
                                f"\n ### [More on {section.get('title')}]({generate_github_link(language, section['file'])})\n")
                        else:
                            # Generate an internal relative link (relative to the generated file in 'generated/')
                            relative_link = f'../sections/{section["file"]}'
                            index_file.write(
                                f"\n ### [More on {section.get('title')}]({relative_link})\n")
                else:
                    print(f'Section file {section["file"]} does not exist')

        print(f'Combined sections into {output_file}')


combine_index()
