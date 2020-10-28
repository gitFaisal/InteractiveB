import pytest
from emails import getEmailList


def test_check_inputs():
    S = ""
    C = "yahoo"
    result = getEmailList(S, C)
    assert result == "One or more input values missing."


def test_hyphen_removed():
    S = "John Raker-Dale"
    C = "yahoo"
    result = getEmailList(S, C)
    assert result == "John Raker-Dale <JRakerDal@yahoo.com>"


def test_lastname_length():
    S = "John Baker Hollyfield"
    C = "amazon"
    result = getEmailList(S, C)
    assert result == "John Baker Hollyfield <JBHollyfie@amazon.com>"


def test_add_number_repeatedname():
    S = "John Doe, John Doe, John Doe"
    C = "gmail"
    result = getEmailList(S, C)
    assert result == "John Doe <JDoe@gmail.com>, John Doe <JDoe1@gmail.com>, John Doe <JDoe2@gmail.com>"

def test_check_middlename():
    S = "John Ham Sandwich"
    C = "bigdeli"
    result = getEmailList(S,C)
    assert result == "John Ham Sandwich <JHSandwich@bigdeli.com>"
