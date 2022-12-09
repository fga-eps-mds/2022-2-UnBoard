import sqlite3 as sql3
import abc
from enum import Enum


class Campus(Enum):
    DARCY = "darcy"
    PLANALTINA = "fup"
    GAMA = "fga"
    CEILANDIA = "fce"


class CampusInfo():
    def __init__(self, nome : Campus, integral: bool = True) -> None:
        self._connection = sql3.connect(f"./databases/{nome.value}.db")
        self._cursor = self._connection.cursor()
        for table in ():
            self._cursor.executemany("""--sql
            CREATE TABLE
            """ )
        self._connection.commit()