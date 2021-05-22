from contextlib import contextmanager
from typing import Any, Iterator, List, Optional

import sqlite3

from config import Config
from .security import _encrypt_decrypt

DATABASE_PATH = Config.DATABASE_PATH


@contextmanager
@_encrypt_decrypt
def __get_cursor() -> Iterator[sqlite3.Cursor]:
    connection: sqlite3.Connection = sqlite3.connect(DATABASE_PATH)
    cursor: sqlite3.Cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def _fetch_one(query: str, parameters: Optional[List[str]] = None) -> Any:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchone()


def _fetch_all(query: str, parameters: Optional[List[str]] = None) -> List:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.fetchall()


def _fetch_none(query: str, parameters: Optional[List[str]] = None) -> None:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)


def _fetch_lastrow_id(query: str, parameters: Optional[List[str]] = None) -> int:
    if parameters is None:
        parameters = []

    with __get_cursor() as cursor:
        cursor.execute(query, parameters)
        return cursor.lastrowid
