from src.user_service import create_user
import pytest

def test_create_user():
    user = create_user("Badhon")
    assert user["name"] == "Badhon"

def test_empty_user():
    with pytest.raises(ValueError):
        create_user("")