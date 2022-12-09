from pandas import *
import time
import sqlite3 as sql3
import abc

class VestibularInfo:
    def __init__(self) -> None:
        self.pdf =  open("spikes/results", "rt", encoding="utf-8")
        self.darcy = {
            "diurno": DataFrame(index=range(63), columns=range(33) , dtype=Float64Dtype),
            "noturno": DataFrame(index=range(29), columns=range(33), dtype=Float64Dtype),
        }
        self.fce = DataFrame(index=range(7), columns=range(33), dtype=Float64Dtype)
        self.fga = DataFrame(index=range(2), columns=range(33), dtype=Float64Dtype)
        self.fup = {
            "diurno": DataFrame(index=range(3), columns=range(33), dtype=Float64Dtype),
            "noturno": DataFrame(index=range(3),columns=range(33), dtype=Float64Dtype),
        }
        self.total_geral = Series(dtype=Float64Dtype)
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

        # process
        # Dacy - Diurno
        skip(5)
        self.darcy["diurno"].index = get_sequence()
        # Darcy - Noturno
        skip(1)
        self.darcy["noturno"].index = get_sequence()
        # Ceilandia - FCE
        skip(2)
        self.fce.index = get_sequence()
        # Gama - FGA
        skip(3)
        self.fga.index = get_sequence()
        # FUP - Diurno
        skip(3)
        self.fup["diurno"].index = get_sequence()
        # FUP - Noturno
        skip(1)
        self.fup["noturno"].index = get_sequence()

    def _set_tables():
        
        
        


start = time.time()
vest23 = VestibularInfo()
print(vest23.fup["noturno"].head())
print(time.time() - start)
