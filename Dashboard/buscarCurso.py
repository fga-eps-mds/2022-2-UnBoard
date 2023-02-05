import pandas as pd

year = 16

df = pd.read_excel(f"../databases/VESTUNB_{year}.xlsx")

global Nome
global Vazia

Nome = "Direito (Bacharelado)" #nome que deseja pesquisar