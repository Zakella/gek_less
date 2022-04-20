import os
import shutil


def check_and_create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


dir = "my_project/settings/templates"
root_dir = "my_project"

for root, dirs, files in os.walk(root_dir):
    list_path = []
    for file in files:
        extension = file.split('.')[-1]
        if extension == "html":
            path = os.path.join(root, file)
            path_cat = os.path.normpath(path).split('\\')
            file_name = path_cat[-1]
            parent = path_cat[-2]
            dir_path = os.path.join(dir, parent)
            check_and_create_folder(dir_path)
            file_dir = os.path.join(root, file)
            try:
                shutil.copy(file_dir, dir_path)
            except Exception:
               pass
