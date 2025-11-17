import pytest
from src.dec2bin_converter.converter import decimal_to_binary, binary_to_decimal


def test_decimal_to_binary():
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(255) == "11111111"


def test_binary_to_decimal():
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("11111111") ==  255

def test_invalid_inputs():
    with pytest.raises(ValueError):
        decimal_to_binary("hello")

    with pytest.raises(ValueError):
        binary_to_decimal("1021")  

#print(test_decimal_to_binary())

#print(test_binary_to_decimal())

#print(test_invalid_inputs())