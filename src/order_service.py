def create_order(user, item):
    if not user or not item:
        raise ValueError("Invalid order")
    return {"user": user, "item": item}