import json
from operator import itemgetter


def get_last_5():
    with open('operations.json', "r", encoding="utf-8") as file:
        file = json.load(file)
    file = sort_by_date(file)
    res = []
    flag = 0
    for i in range(100):
        if file[i]["state"] == "EXECUTED":
            res.append(file[i])
            flag += 1
            if flag >= 5:
                break
    return res


def sort_by_date(file):
    i = 0
    i_numb = 0
    j_numb = 0
    new_file = []
    for i in file:
        if "state" in i.keys():
            if i["state"] == "EXECUTED":
                new_file.append(i)
    for i in range(len(new_file)):
        for j in range(len(new_file)):
            if new_file[i]["date"] > new_file[j]["date"]:
                x = new_file[j]
                new_file[j] = new_file[i]
                new_file[i] = x
    return new_file


def is_account(text):
    if "Счет" in text:
        return 1
    else:
        return 0


def make_numb_card(text):
    numb = ""
    j = 0
    for i in text:

        if i.isdigit():
            break

        j += 1

    text = text[j:]
    j = 0

    for i in text:
        numb += i
        j += 1

        if j == 4:
            numb += " "

        if j == 6:
            break

    numb += "** **** "
    numb += text[-4:]

    return numb


def make_numb_account(text):
    numb = "**"
    j = 0

    for i in text:

        if i.isdigit():
            break

        j += 1

    text = text[j:]
    numb += text[-4:]
    return numb


def remake_numb(file):

    for i in range(len(file)):

        if "from" in file[i].keys():
            j = 0
            text = file[i]["from"]

            for b in text:

                if b.isdigit():
                    break

                j += 1

            if is_account(text):

                file[i]["from"] = file[i]["from"][:j] + make_numb_account(text)

            else:
                file[i]["from"] = file[i]["from"][:j] + make_numb_card(text)

    for i in range(len(file)):
        j = 0
        text = file[i]["to"]

        for b in text:

            if b.isdigit():
                break

            j += 1

        if is_account(text):
            file[i]["to"] = file[i]["to"][:j] + make_numb_account(text)

        else:
            file[i]["to"] = file[i]["to"][:j] + make_numb_card(text)

    return file


def remake_date(file):
    for i in range(len(file)):
        text = file[i]["date"]
        text = text[:10]
        res = text.split('-')
        year = res[0]
        month = res[1]
        day = res[2]
        file[i]["date"] = day + "." + month + "." + year
    return file


def show_info(file):
    for i in file:
        print(f'{i["date"]} {i["description"]}')
        if "from" in i.keys():
            print(f'{i["from"]} -> {i["to"]}')
        else:
            print(i["to"])
        print(f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n')
