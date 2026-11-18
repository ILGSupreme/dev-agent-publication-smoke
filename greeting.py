def greet(name: str) -> str:
    if not name.strip():
        name = "stranger"
    return f"Hello, {name}!"
