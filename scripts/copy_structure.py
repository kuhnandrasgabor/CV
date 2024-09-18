import os
import shutil


def make_copies_in_place(source, search_string, replace_string):
    for root, dirs, files in os.walk(source):
        for file in files:
            if search_string in file:
                new_file = file.replace(search_string, replace_string)
                shutil.copyfile(os.path.join(root, file), os.path.join(root, new_file))


# Define the source and destination directories
source = f'../sections'
search_string = f'_en.md'
replace_string = f'_hu.md'
make_copies_in_place(source, search_string, replace_string)
