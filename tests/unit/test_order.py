from src.order_service import create_order
import pytest

def test_create_order():
    user = {"name": "Badhon"}
    order = create_order(user, "Laptop")
    assert order["item"] == "Laptop"

def test_invalid_order():
    with pytest.raises(ValueError):
        create_order(None, None)