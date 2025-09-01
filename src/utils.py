import os

def get_port(default: int = 8080) -> int:
    try:
        return int(os.getenv("PORT", default))
    except ValueError:
        return default
