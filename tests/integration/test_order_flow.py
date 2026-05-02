from src.order_service import create_order_for_user
import pytest

def test_order_flow_success():
    order = create_order_for_user("Badhon", "Laptop")

    assert order["user"]["name"] == "Badhon"
    assert order["item"] == "Laptop"
    assert order["status"] == "created"

def test_order_flow_invalid_user():
    with pytest.raises(ValueError):
        create_order_for_user("", "Laptop")