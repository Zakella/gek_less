import json
import itertools


def parse_files():
    with open("users.csv", 'r', encoding="utf-8") as users:
        with open("hobby.csv", 'r', encoding="utf-8") as hobby:
            if sum(1 for line in hobby) > sum(1 for line in users):
                exit(1)
            else:
                hobby.seek(0)
                users.seek(0)

            users_list = users.readlines()
            content = [x.strip() for x in users_list]

            hobby_list = hobby.readlines()
            hobby_list = [x.strip() for x in hobby_list]

            dict_temp = dict(itertools.zip_longest(content, hobby_list, fillvalue=None))
            list = []
            for key, value in dict_temp.items():
                list.append({"Фамилия": key.split(',')[0],
                             "Имя": key.split(',')[1],
                             "Отчество": key.split(',')[2].replace("\n", "").lstrip(),
                             "Хобби": value

                             })


    with open('users_hobbys.json', 'w', encoding='utf-8') as users_hobbys:
                json.dump(list, users_hobbys, ensure_ascii=False)

    with open('users_hobbys.json', 'r', encoding='utf-8') as users_hobbys:
        print(users_hobbys.readlines())


if __name__ == "__main__":
 parse_files()
