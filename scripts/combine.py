import os


def combine_index():
    for language in ['en', 'hu']:

        sections = [
            f'../{language}/sections/personal-info.md',
            f'../{language}/sections/summary.md',
            f'../{language}/sections/experience.md',
            f'../{language}/sections/education.md',
            f'../{language}/sections/skills.md'
        ]

        output_file = f'../{language}/index.md'

        if os.path.exists(output_file):
            os.remove(output_file)

        with open(output_file, 'x') as index_file:
            for section in sections:
                if os.path.exists(section):
                    with open(section, 'r') as section_file:
                        index_file.write(section_file.read() + '\n\n')  # Adding extra newline between sections
                else:
                    print(f'Section file {section} does not exist')

        print(f'Combined sections into {output_file}')


combine_index()
