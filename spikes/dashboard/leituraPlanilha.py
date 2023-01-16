import pandas as pd

df = pd.read_excel("../../pdfs/VESTUNB_23.xlsx")

Nome = "Administração (Bacharelado)" #nome que deseja pesquisar
Vazia = "Unnamed: 0" #nome da coluna vazia

#filtra apenas os diurnos
linha_diurno = df.loc[(df[0] == Nome) & (df[Vazia] <= 71)]

#filtra apenas os noturnos
linha_noturno = df.loc[(df[0] == Nome) & (df[Vazia] > 71)]


print(linha_diurno)
