import json
import datetime

def load_operations():
    # Функция загружает список банковских операций из файла JSON
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered_executed(operations):
    '''Функция получает словарь с данными по выполненным банковским операциям.
    #     Пример вывода для одной операции:
    #     14.10.2018 Перевод организации
    #     7000 79** **** 6361 -> Счет **9638
    #     82771.72 руб.'''
    return [x for x in operations if "state" in x and x["state"] == "EXECUTED"]

def get_last_operations(operations):
    # Функция выбирает пять последних выполненных операций и сортирует их по дате
    operations = sorted(operations, key=lambda x: x['date'], reverse=True)[:5]
    return operations

def datetime_operations(data):
    # Функция форматирует дату в формат: 14.10.2018
    for i in data:
        date = datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        return date


def number_card_cod(data):
    # Функция зашифровывает номер карты в формат: Visa Platinum 7000 79** **** 6361)
    for i in data:
        card = i["from"]
        card_number = card.split()[-1]
        sicret_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        section, section_size = len(sicret_number), len(sicret_number)//4
        return " ".join([sicret_number[i:i + section_size] for i in range(0, section, section_size)])


def number_check_cod(data):
    # Функция зашифровывает номер счета в формат: Счет **9638

    for i in data:
        check = i["to"]
        return "*" * (len(check) -4) + check[-4:]
