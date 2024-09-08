import os
import json


def generate_github_link(language, section):
    base_url = 'https://github.com/kuhnandrasgabor/CV/blob/main'
    return f'{base_url}/{language}/{section}'


def combine_index():
    for language in ['en', 'hu']:

        sections = [
            {"file": f'../{language}/sections/personal-info.md', "include": True},
            {"file": f'../{language}/sections/experience.md', "include": True},
            {"file": f'../{language}/sections/experience/experience-summary.md', "include": True},
            {"file": f'../{language}/sections/experience/pzartech-header.md', "include": True},
            {"file": f'../{language}/sections/experience/pzartech-summary.md', "include": True},
            {"file": f'../{language}/sections/experience/pzartech-webdev.md', "include": True},
            {"file": f'../{language}/sections/experience/pzartech-ml.md', "include": False, "title": "Machine Learning", "externally-link": False},
            {"file": f'../{language}/sections/experience/pzartech-ml.md', "include": False, "title": "Machine Learning", "externally-link": True},
        ]

        output_file = f'../{language}/index.md'

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            for section in sections:
                if os.path.exists(section.get('file')):
                    if section.get('include'):
                        with open(section.get('file'), 'r') as section_file:
                            index_file.write(section_file.read() + '\n\n')  # Adding extra newline between sections
                    else:
                        # Add a link to the section
                        if section.get('externally-link'):
                            index_file.write(f"\n ### [More on {section.get('title')}]({generate_github_link(language, section.get('file'))})\n")
                        else:
                            index_file.write(f"\n ### [More on {section.get('title')}]({section.get('file')})\n")
                else:
                    print(f'Section file {section} does not exist')

        print(f'Combined sections into {output_file}')


combine_index()
