def thesaurus_adv(*args, sort=True):
    arg_list = list(args)
    dict_filt = {}
    for item in arg_list:
        key = str(item).split()[-1][0]
        if key not in dict_filt:
            dict_filt[key] = []
        if key == str(item).split()[-1][0]:
            dict_filt[key].append(item)

    for key, val in dict_filt.items():
        name_dict = {}
        for x in val:
            first_let_in_name = x.split()[0][0]
            if not first_let_in_name in name_dict:
                name_dict[first_let_in_name] = []
                for names in val:
                    n = names.split()[0][0]
                    if n == first_let_in_name:
                        name_dict[first_let_in_name].append(names)

        dict_filt[key] = name_dict

    if sort:
        dictionary_items = dict_filt.items()
        print(sorted(dictionary_items))
    else:
        print(dict_filt)


def thesaurus(*args):
    dict_names = {}
    for val in args:
        if val[0] not in dict_names:
            dict_names[val[0]] = []
        if val[0] in dict_names.keys():
            dict_names[val[0]].append(val)
    return dict_names


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
