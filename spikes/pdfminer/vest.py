from pandas import *
import time
import sqlite3 as sql3
from chooser import *
from campus import *
import os

class VestInfo:
    def __init__(self, edition: int) -> None:
        self.edition = edition
        self.uri = f"./databases/vest_{self.edition}"
        try:
            os.mkdir(self.uri)
        except FileExistsError:
            ...
        finally:
            self.pdf =  open(self.uri + ".txt", "rt", encoding="utf-8")
            self.darcy = {
                "diurno": CampusInfo(self.uri, Campus.DARCY, Turno.DIURNO), #DataFrame(index=range(63), columns=range(33) , dtype=Float64Dtype)
                "noturno": CampusInfo(self.uri, Campus.DARCY, Turno.NOTURNO), #DataFrame(index=range(29), columns=range(33), dtype=Float64Dtype),
            }
            self.fce = CampusInfo(self.uri, Campus.CEILANDIA) #DataFrame(index=range(7), columns=range(33), dtype=Float64Dtype)
            self.fga = CampusInfo(self.uri, Campus.GAMA) #DataFrame(index=range(2), columns=range(33), dtype=Float64Dtype)
            self.fup = {
                "diurno": CampusInfo(self.uri, Campus.PLANALTINA, Turno.DIURNO), #DataFrame(index=range(3), columns=range(33), dtype=Float64Dtype),
                "noturno": CampusInfo(self.uri, Campus.PLANALTINA, Turno.NOTURNO), #DataFrame(index=range(3),columns=range(33), dtype=Float64Dtype),
            }
            self.total_geral = CampusInfo(self.uri, Campus.DARCY)
            os.rename(f"./databases/vest_{self.edition}/darcy.db", f"./databases/vest_{self.edition}/total-geral.db")
            
            self.treineiros = int()        
            self._set_axis()

    def _set_axis(self):
        # subfunctions
        def get_sequence() -> list:
            sequence = list()
            while True:
                line = self.pdf.readline()
                if line == "\n":
                    return sequence
                else:
                    sequence.append(line.replace("\n", ""))
        def skip(lines: int) -> None:
            """Skips lines
            
            Args:
                    lines (int): number of lines to be skipped
            """
            for i in range(lines):
                self.pdf.readline()
        def fill_column(table_names: list, campus: CampusInfo, column_name: str, new_values: list, new_row: bool = False) -> None:
            """fill

            Args:
                table_names (list): a list of table's names in the format [("name1"), ("name2"), ...] 
                campus (CampusInfo): the object that contains the database to be modified.
                column_name (str): only one column name is allowed. 
                new_values (list): a list cotaining the new values as its elements
                new_row (bool): default=False. It is important to decide if the method will use "INSERT INTO" or "UPDATE" statement.
 
            Returns:
                None
            """
            for table_name in table_names:
                campus.fill_column(str(table_name[0]), column_name, new_values, new_row=new_row)

        # process
        # Dacy - Diurno
        skip(5)
        fill_column(getTables(Quotas.TUDO), self.darcy["diurno"], "Cursos", get_sequence(), new_row=True )
        # Darcy - Noturno
        skip(1)
        fill_column(getTables(Quotas.TUDO), self.darcy["noturno"], "Cursos", get_sequence(), new_row=True)
        # Ceilandia - FCE
        skip(2)
        fill_column(getTables(Quotas.TUDO), self.fce, "Cursos", get_sequence(), new_row=True)
        # Gama - FGA
        skip(3)
        fill_column(getTables(Quotas.TUDO), self.fga, "Cursos", get_sequence(), new_row=True)
        # FUP - Diurno
        skip(3)
        fill_column(getTables(Quotas.TUDO), self.fup["diurno"], "Cursos", get_sequence(), new_row=True)
        # FUP - Noturno
        skip(1)
        fill_column(getTables(Quotas.TUDO), self.fup["noturno"], "Cursos", get_sequence(), new_row=True)

        # skipping column labels:
        skip(122)
        
        #
        ls = get_sequence()
        fill_column(getTables(Quotas.NEGROS), self.darcy["diurno"], "Vagas", ls)
        #fill_column(getTables(Quotas.NEGROS), self.darcy["noturno"], "Vagas", get_sequence())
        #fill_column(getTables(Quotas.NEGROS), self.fce, "Vagas", get_sequence())
        #tmp = get_sequence()
        #tmp.extend(get_sequence())
        #fill_column(getTables(Quotas.NEGROS), self.fga, "Vagas", tmp)
        #fill_column(getTables(Quotas.NEGROS), self.fup["diurno"], "Vagas", get_sequence())
        #fill_column(getTables(Quotas.NEGROS), self.fup["diurno"], "Vagas", get_sequence())

if __name__ == "__main__":
    vest_23 = VestInfo(23)

