import sqlite3 as sql3
import abc
from enum import Enum
from chooser import getTables, Quotas


class Campus(Enum):
    DARCY = "darcy"
    PLANALTINA = "fup"
    GAMA = "fga"
    CEILANDIA = "fce"

class Turno(Enum):
    
    INTEGRAL = "integral"
    DIURNO = "diurno"
    NOTURNO = "noturno"

class CampusInfo():
    """Represents a Campus with a series of tables on a database.

    Example:
        Object: CampusInfo(VestInfo(23), Campus.DARCY, Turno.DIURNO)
        Database it connects: /databases/vest_23/darcy-diurno.db
    
        Object: CampusInfo(VestInfo(20), Campus.GAMA, Turno.NOTURNO)
        Database it connects: /databases/vest_20/fga-noturno.db

        Object: CampusInfo(VestInfo(15), Campus.PLANALTINA, Turno.INTEGRAL)
        Database it connects: /databases/vest_15/fup.db
    """
    def __init__(self, vest_dir: str, nome : Campus, turno: Turno = Turno.INTEGRAL) -> None:
        if turno != Turno.INTEGRAL:
            self._connection = sql3.connect(vest_dir + f"/{str(nome.value)}-{str(turno.value)}.db")
        else:
            self._connection = sql3.connect(vest_dir + f"/{nome.value}.db")
        self._cursor = self._connection.cursor()
        for table_name in getTables(Quotas.TUDO):
            sql_query = f"""--sql
            CREATE TABLE IF NOT EXISTS {table_name[0]}(
                ID INTEGER PRIMARY KEY,
                Cursos VARCHAR(200),
                Vagas INTEGER,
                Inscritos INTEGER,
                Demanda FLOAT
            )"""
            self._cursor.execute(sql_query)
            self._connection.commit()

    def getTableName(self, quota: Quotas, is_poor: bool=False, is_black_brown_or_native: bool=False, is_deficient: bool=False) -> str or None:
        return str(getTables(quota, is_poor, is_black_brown_or_native, is_deficient)[0][0])
    
    def fill_column(self, table_name: str, column_name: str, new_values: list, new_row: bool= False):
        """ Attention: this method is not protected, so it can suffers from sql injection. Please, correct it.
        
        Args:
            table_name (String): if your don't know, find it with method getTableName().
            column_name (String): It may be "Vagas", "Inscritos" or "Demanda".
            new_values (list): a list cotaining the new values as its elements.
            new_row (bool): default=False. It is important to if the method will use "INSERT INTO" or "UPDATE" statement.
        """
        if new_row:
            for value in new_values:
                self._cursor.execute(f"""--sql
                INSERT INTO {table_name} ({column_name})
                VALUES(?);
                """, (value,))
        else:
            for index in range(1, len(new_values) + 1):
                self._cursor.execute(f"""--sql
                UPDATE {table_name}
                SET {column_name} = ?
                WHERE ID = {index};
                """, (new_values[index - 1],))
        self._connection.commit()