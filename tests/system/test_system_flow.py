from src.system import place_order
import pytest

def test_full_system_success():
    result = place_order("Badhon", "Phone")
    assert result == "Order for Badhon placed successfully"

def test_full_system_invalid_user():
    with pytest.raises(ValueError):
        place_order("", "Phone")