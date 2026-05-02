from src.user_service import create_user

def create_order_for_user(username, item):
    user = create_user(username)
    return {
        "user": user,
        "item": item,
        "status": "created"
    }