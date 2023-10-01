from src.utils import datetime_operations, number_check_cod, get_filtered_executed, get_last_operations, number_card_cod


def test_get_filtered_executed(test_data):
    data = get_filtered_executed(test_data)
    assert [x["state"] for x in data] == "EXECUTED"

def test_get_last_operations(test_data):
    data = get_last_operations(test_data)
    assert [x["date"] for x in data] == ['2019-08-26T10:50:58.294041', '2019-03-23T01:09:46.296404', '2018-12-20T16:43:26.929246', '2018-03-23T10:45:06.972075', '2018-03-23T10:45:06.972075']


def test_datetime_operations(test_data):
    data = datetime_operations(test_data)
    assert [x["date"] for x in data] == ['26.08.2019']


def test_number_card_cod(test_data):
    data = number_card_cod(test_data)
    assert [x["from"] for x in data] == ['1596 83** **** 5199']

def test_number_check_cod(test_data):
    data = number_check_cod(test_data)
    assert [x["to"] for x in data] == ['*********************9589']
