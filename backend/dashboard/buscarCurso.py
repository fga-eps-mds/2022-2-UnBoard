import pandas as pd
from altera import altera_curso, altera_ano

global Vazia
global year
year = 23

year = altera_ano()
df = pd.read_excel(f"../databases/VESTUNB_{year}.xlsx")


Nome = altera_curso()
