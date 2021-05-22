from contextlib import suppress
from typing import Callable

from config import Config

from cryptography.fernet import Fernet, InvalidToken

DATABASE_PATH = Config.DATABASE_PATH
ENCRYPT_DB = Config.ENCRYPT_DB
fernet = Fernet(Config.DB_TOKEN)


def _encrypt_decrypt(func) -> Callable:

    def helper(*args, **kwargs):
        __decrypt_database()
        yield from func(*args, **kwargs)
        __encrypt_database()

    return helper


def __decrypt_database() -> None:
    with suppress(InvalidToken, FileNotFoundError):
        with open(DATABASE_PATH, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(DATABASE_PATH, "wb") as file:
            file.write(decrypted_data)


def __encrypt_database() -> None:
    if not ENCRYPT_DB:
        return

    with open(DATABASE_PATH, "rb") as file:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)

    with open(DATABASE_PATH, "wb") as file:
        file.write(encrypted_data)
