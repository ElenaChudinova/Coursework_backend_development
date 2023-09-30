from src.utils import find_operations_executed, datetime_operations, number_card_cod, number_check_cod, load_operations

def test_load_operations():
    assert load_operations("id") == 441945886
    assert load_operations("state") == "EXECUTED"
    assert load_operations("date") == "2019-08-26T10:50:58.294041"
    assert load_operations("description") == "Перевод организации"
    assert load_operations("from") == "Maestro 1596837868705199"
    assert load_operations("to") == "Счет 64686473678894779589"
    assert load_operations("operationAmount")("amount") == "31957.58"
    assert load_operations("operationAmount")("name") == "руб."


def test_find_operations_executed():
    assert find_operations_executed("date") == "2019-08-26T10:50:58.294041"
    assert find_operations_executed("description") == "Перевод организации"
    assert find_operations_executed("from") == "Maestro 1596837868705199"
    assert find_operations_executed("to") == "Счет 64686473678894779589"
    assert find_operations_executed("operationAmount")("amount") == "31957.58"
    assert find_operations_executed("operationAmount")("name") == "руб."


def test_datetime_operations():
    assert datetime_operations('%d.%m.%Y') == '20.02.2023'
    assert datetime_operations('%Y-%m-%dT%H:%M:%S.%f') == '2019-08-26T10:50:58.294041'

def test_number_card_cod():
    assert number_card_cod("Maestro 1596837868705199") == "1596 83** **** 5199"

def test_number_check_cod():
    assert number_check_cod("Счет 64686473678894779589") == "****************9589"
