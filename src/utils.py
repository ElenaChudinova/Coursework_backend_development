import os
import json
import datetime

operations_path = os.path.join("operations.json")

def load_operations(path):
    # Функция загружает список банковских операций из файла JSON
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def find_operations_executed(operations):
    '''Функция получает словарь с данными по выполненным банковским операциям.
    Пример вывода для одной операции:
    14.10.2018 Перевод организации
    7000 79** **** 6361 -> Счет **9638
    82771.72 руб.'''
    operations_my_dir = {}
    for i in range(len(operations)):
        if operations[i]["state"] == "EXECUTED":
            operations_my_dir["date"] = operations[i]["date"]
            operations_my_dir["description"] = operations[i]["description"]
            operations_my_dir["from"] = operations[i]["from"]
            operations_my_dir["to"] = operations[i]["to"]
            operations_my_dir["amount"] = operations[i]["operationAmount"]["amount"]
            operations_my_dir["name"] = operations[i]["operationAmount"]["currency"]["name"]
            return operations_my_dir

def datetime_operations(all_operations):
    # Функция форматирует дату в формат: 14.10.2018
    for inf in range(len(all_operations)):
        date_time_str = all_operations[inf]["date"]
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%dT%H:%M:%S.%f')
        return f'{date_time_obj:%d.%m.%Y}'

def number_card_cod(all_operations):
    # Функция зашифровывает номер карты в формат: Visa Platinum 7000 79** **** 6361
    for inf in range(len(all_operations)):
        card = all_operations[inf]["from"]
        card_number = card.split()[-1]
        sicret_number = card_number[:6] + (len(card_number[6:-4]) * '*') + card_number[-4:]
        section, section_size = len(sicret_number), len(sicret_number)//4
        return " ".join([sicret_number[i:i + section_size] for i in range(0, section, section_size)])

def number_check_cod(all_operations):
    # Функция зашифровывает номер счета в формат: Счет **9638
    for inf in range(len(all_operations)):
        check = all_operations[inf]["to"]
        return "*" * (len(check) -4) + check[-4:]
