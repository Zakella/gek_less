import os


def check_and_create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)


def get_path(dict_list, cur_level):
    path = ""
    while cur_level in dict_list:
        path = dict_list[cur_level] + '/' + path
        cur_level = cur_level - 1
    return path


with open("config.yaml", "r", encoding="utf-8") as config:
    dict_list = {}
    for index, line in enumerate(config):
        if line.strip().find(".") > 0:
            file_name = line.strip()
            path = os.path.join(dir_path, file_name)
            with open(path, 'w', encoding= "utf-8"):
                pass
        else:
            folder_name = line.strip().replace("-", "").strip()
            cur_level = len(line.strip().split("-"))-1
            dict_list[cur_level] = folder_name
            if cur_level -1 in dict_list:
                root_folder = get_path(dict_list, cur_level-1)
                dir_path = os.path.join(root_folder, folder_name)
                check_and_create_folder(dir_path)
            else:
                check_and_create_folder(folder_name)


