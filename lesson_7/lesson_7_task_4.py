import os
from pathlib import Path
import json


def check_size(file_size, extension, dic):
    for key, val in dic.items():
        if key > file_size:
            val[0] += 1
            val[1].append(extension)
            break


root_dir = "C:/Users/SLAVA/PycharmProjects/gek_less/lesson_7/files_exapmle/some_data"
gr = 10
dic_size = {}

while gr <= 100000:
    gr *= 10
    dic_size[gr] = [0, []]


for root, dirs, files in os.walk(root_dir):
    for file in files:
        path = os.path.join(root, file)
        extension = Path(path).suffixes
        size = os.stat(path).st_size
        check_size(size, extension[0], dic_size)

for key, val in dic_size.items():
    val[1] = list(set(val[1]))
    dic_size[key] = tuple(val)


file_path = f"{os.path.basename(os.getcwd())}_summary.json"
with open(file_path, "w", encoding= "utf-8") as f:
    json.dump(dic_size, f, ensure_ascii=False)


