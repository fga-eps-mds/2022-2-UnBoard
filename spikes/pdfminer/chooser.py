import sqlite3 as sql3
from enum import Enum

class Quotas(Enum):
    UNIVERSAL = "Universal"
    NEGROS = "Cotas para negros"
    ESCOLA_PÚBLICA = "Sistema de Cotas para Escolas Públicas"
    TOTAL = "Total"
    TUDO = "*"

def create_chooser():
    con = sql3.connect("./databases/chooser.db")
    cur = con.cursor()
    if len(cur.execute("SELECT name FROM sqlite_master").fetchall()) == 0:
        cur.execute("""--sql
        CREATE TABLE Seletor(
            Codigo_de_Tabela VARCHAR(100),
            Cotas VARCHAR(100),
            Pobre INTEGER,
            Preto_Pardo_Indigena INTEGER,
            Deficiente INTEGER
        );""")
        cur.executemany("""--sql
        INSERT INTO Seletor
        VALUES (?, ?, ?, ?, ?);
        """, [("N000", Quotas.NEGROS.value, 0, 0, 0),
        ("U000", Quotas.UNIVERSAL.value, 0, 0, 0),
        ("P111", Quotas.ESCOLA_PÚBLICA.value, 1, 1, 1),
        ("P110", Quotas.ESCOLA_PÚBLICA.value, 1, 1, 0),
        ("P011", Quotas.ESCOLA_PÚBLICA.value, 0, 1, 1),
        ("P010", Quotas.ESCOLA_PÚBLICA.value, 0, 1, 0),
        ("P101", Quotas.ESCOLA_PÚBLICA.value, 1, 0, 1),
        ("P100", Quotas.ESCOLA_PÚBLICA.value, 1, 0, 0),
        ("P001", Quotas.ESCOLA_PÚBLICA.value, 0, 0, 1),
        ("P000", Quotas.ESCOLA_PÚBLICA.value, 0, 0, 0),
        ("T000", Quotas.TOTAL.value, 0, 0, 0),
        ])
    con.commit()
    con.close()

def getTables(quota: Quotas, is_poor: bool=False, is_black_brown_or_native: bool=False, is_deficient: bool=False) -> list or None:
    """ if your quota is not ESCOLA PÚBLICA, ignore the others parameters except from quota.
    """
    con = sql3.connect("./databases/chooser.db")
    cur = con.cursor()
    if quota.value == Quotas.TUDO.value:
        return cur.execute("""--sql
        SELECT Codigo_de_Tabela
        FROM Seletor;""").fetchall()
    else: 
        return cur.execute("""--sql
        SELECT Codigo_de_Tabela
        FROM Seletor
        WHERE Cotas = ? AND Pobre = ? AND Preto_Pardo_Indigena = ? AND Deficiente = ?;
        """, (quota.value, int(is_poor), int(is_black_brown_or_native), int(is_deficient))).fetchall()


if __name__ == "__main__":
    create_chooser()
    print(getTables(Quotas.TUDO, False, False, False)[0][0])