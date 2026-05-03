from src.order_service import create_order_for_user

def place_order(username, item):
    order = create_order_for_user(username, item)

    # simulate business logic
    order["payment_status"] = "paid"
    order["delivery_status"] = "processing"

    return f"Order for {order['user']['name']} placed successfully"