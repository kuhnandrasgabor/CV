import os
import shutil
from combine import generate_pdf_from_md


def compile_gpt_files():
    # delete the generated directory if it exists
    if os.path.exists("../GPT-data/generated/"):
        shutil.rmtree("../GPT-data/generated/")

    # Create a directory to store the thoughts
    os.makedirs("../GPT-data/generated/", exist_ok=True)

    values_filepath = f"../GPT-data/values.md"
    readme_writings_filepath = f"../GPT-data/readme-writings.md"
    cv_writings_filepath = f"../GPT-data/cv-writings.md"

    structured_thoughts_filepath = f"../GPT-data/generated/structured-thoughts.md"
    writing_styles_samples_filepath = f"../GPT-data/generated/writing-styles-samples.md"

    # find every line of of the source file that hast the indented "- Thoughts:" in it and remove it, and put the rest into the structured thoughts file
    with open(values_filepath, "r") as values_file:
        with open(structured_thoughts_filepath, "w") as structured_thoughts_file:
            for line in values_file:
                if "- Thoughts:" in line:
                    continue
                structured_thoughts_file.write(line)

    # concatenate vales.md, cv-writings.md, and readme-writings.md into writing-styles-samples.md

    with open(writing_styles_samples_filepath, "w") as writing_styles_samples_file:

        with open(cv_writings_filepath, "r") as cv_writings_file:
            for line in cv_writings_file:
                writing_styles_samples_file.write(line)

        with open(readme_writings_filepath, "r") as readme_writings_file:
            for line in readme_writings_file:
                writing_styles_samples_file.write(line)

        with open(values_filepath, "r") as values_file:
            for line in values_file:
                writing_styles_samples_file.write(line)

    print("GPT files compiled successfully!")

    # generate pdf from the markdown files
    generate_pdf_from_md(structured_thoughts_filepath, structured_thoughts_filepath.replace(".md", ".pdf"), "https://github.com/kuhnandrasgabor/cv")
    generate_pdf_from_md(writing_styles_samples_filepath, writing_styles_samples_filepath.replace(".md", ".pdf"), "https://github.com/kuhnandrasgabor/cv")


compile_gpt_files()
