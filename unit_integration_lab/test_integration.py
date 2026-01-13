import pytest
from bank_app import transfer, calculate_interest

def test_transfer_success():
    b1, b2 = transfer(5000, 2000, 1000)
    assert b1 == 4000
    assert b2 == 3000

def test_transfer_insufficient_balance():
    with pytest.raises(ValueError):
        transfer(500, 1000, 2000)

def test_transfer_and_interest():
    b1, b2 = transfer(10000, 2000, 5000)
    interest = calculate_interest(b2, 10, 1)
    assert round(interest,2) == 7700.0
