from contextlib import contextmanager
from typing import Any, Iterator, List, Optional

import sqlite3
from cryptography.fernet import Fernet

from config import Config
from ..models.models import Contact

DATABASE_PATH = Config.DATABASE_PATH
fernet = Fernet(Config.DB_TOKEN)

def __decrypt_database():
    try:
        with open(DATABASE_PATH, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(DATABASE_PATH, "wb") as file:
            file.write(decrypted_data)
    except:
        pass


def __encrypt_database():
    with open(DATABASE_PATH, "rb") as file:
        file_data = file.read()
        encrypted_data = fernet.encrypt(file_data)
    
    with open(DATABASE_PATH, "wb") as file:
        file.write(encrypted_data)


@contextmanager
def __get_cursor() -> Iterator[sqlite3.Cursor]:

    __decrypt_database()
    connection: sqlite3.Connection = sqlite3.connect(DATABASE_PATH)
    cursor: sqlite3.Cursor = connection.cursor()
    try:    
        yield cursor
        connection.commit()
    finally:                     
        cursor.close()
        connection.close()
        __encrypt_database()
        


def fetch_one(query: str, parameters: Optional[List[str]] = None) -> Any:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchone()


def fetch_all(query: str, parameters: Optional[List[str]] = None) -> List:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchall()


def fetch_none(query: str, parameters: Optional[List[str]] = None) -> None:
    if parameters is None:
        parameters = []
    
    with __get_cursor() as cursor:
        cursor.execute(query, parameters)


def fetch_lastrow_id(query: str, parameters: Optional[List[str]] = None) -> int:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.lastrowid


def reset_table() -> None:
    query = "DROP TABLE IF EXISTS contacts"
    fetch_none(query)

    fields = """(first_name text, last_name text, address text, city text, 
                 state text, zip_code integer, phone text, email text)"""
    query = f"CREATE TABLE IF NOT EXISTS contacts {fields}"

    fetch_none(query)

    query = "INSERT INTO contacts VALUES (:first_name, :last_name, :address, :city, :state, :zip_code, :phone, :email)"
    parameters = {'first_name': 'Larry',  'last_name': 'Danny', 
                  'address': '123 str', 'city': 'Dhaka', 'state': 'Dhaka',
                  'zip_code': 1212, 'phone': '1234567', 'email': 'larry@gmail.com',
                 }

    fetch_none(query, parameters)                    
