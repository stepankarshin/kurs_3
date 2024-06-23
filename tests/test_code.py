from utils import is_account
from utils import make_numb_card
from utils import make_numb_account
from utils import remake_numb
from utils import remake_date
import json
import pytest


def test_is_account_1():
    assert is_account("Счет 12312312313313131") == 1

def test_get_last_2():
    assert is_account("ыфыв 12312312313323123") == 0

def test_make_number_card_1():
    assert make_numb_card("Mastero 1231231345351231") == "1231 23** **** 1231"

def test_make_number_card_2():
    assert make_numb_card("Mastero 7688123123131311231212") == "7688 12** **** 1212"

def test_make_number_account_1():
    assert make_numb_account("Счёт 88005553535") == "**3535"

def test_make_number_account_2():
    assert make_numb_account("Счёт 12345678901234567890") == "**7890"

def test_remake_numb():
    x = [{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]
    x = remake_numb(x)
    assert x[0]["from"] == "Maestro 1596 83** **** 5199" and x[0]["to"] == "Счет **9589"

def test_remake_date():
    x = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    x = remake_date(x)
    assert x[0]["date"] == "26.08.2019"
