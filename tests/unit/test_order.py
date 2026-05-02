import pytest
from src.order_service import create_order_for_user

def test_create_order():
    order = create_order_for_user("Badhon", "Laptop")
    assert order["item"] == "Laptop"

def test_invalid_order():
    with pytest.raises(ValueError):
        create_order_for_user("", "")