def create_user(name):
    if not name:
        raise ValueError("Name cannot be empty")
    return {"name": name}