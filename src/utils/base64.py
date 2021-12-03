from base64 import b64encode, b64decode


def base64encode(text: str) -> str:
    return b64encode(text.encode()).decode()


def base64decode(text: str) -> str:
    return b64decode(text.encode()).decode()
