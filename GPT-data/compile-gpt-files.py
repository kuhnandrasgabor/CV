import os
import shutil

from scripts.combine import generate_pdf_from_md


def compile_gpt_files():

    print("Compiling GPT files...")

    # delete the generated directory if it exists
    if os.path.exists("generated/"):
        shutil.rmtree("generated/")

    # Create a directory to store the thoughts
    os.makedirs("generated/", exist_ok=True)

    values_filepath = f"values.md"
    readme_writings_filepath = f"readme-writings.md"
    cv_writings_filepath = f"cv-writings.md"

    structured_thoughts_filepath = f"generated/structured-thoughts.md"
    writing_styles_samples_filepath = f"generated/writing-styles-samples.md"

    # find every line of of the source file that hast the indented "- Thoughts:" in it and remove it, and put the rest into the structured thoughts file
    with open(values_filepath, "r") as values_file:
        with open(structured_thoughts_filepath, "w") as structured_thoughts_file:
            for line in values_file:
                if "- Thoughts:" in line:
                    continue
                structured_thoughts_file.write(line)

    # concatenate vales.md, cv-writings.md, and readme-writings.md into writing-styles-samples.md

    with open(writing_styles_samples_filepath, "w") as writing_styles_samples_file:

        with open(values_filepath, "r") as values_file:
            for line in values_file:
                writing_styles_samples_file.write(line)

        with open(readme_writings_filepath, "r") as readme_writings_file:
            for line in readme_writings_file:
                writing_styles_samples_file.write(line)

        with open(cv_writings_filepath, "r") as cv_writings_file:
            for line in cv_writings_file:
                writing_styles_samples_file.write(line)

    print("GPT MD files compiled successfully!")

    # generate pdf from the markdown files
    generate_pdf_from_md(structured_thoughts_filepath, structured_thoughts_filepath.replace(".md", ".pdf"), "https://github.com/kuhnandrasgabor/cv")
    generate_pdf_from_md(writing_styles_samples_filepath, writing_styles_samples_filepath.replace(".md", ".pdf"), "https://github.com/kuhnandrasgabor/cv")


compile_gpt_files()
