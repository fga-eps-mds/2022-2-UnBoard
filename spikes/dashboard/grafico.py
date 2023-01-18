from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import leituraPlanilha
from leituraPlanilha import *

app = Dash(__name__)

df = pd.DataFrame({
    "COTAS": ["Negros", "Negros", 
    "Estudantes deficientes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo", 
    "Estudantes deficientes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo", 
    "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo", 
    "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
    "Estudantes deficientes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes deficientes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes deficientes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
    "Estudantes deficientes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
    "Estudantes de deficientes escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes de deficientes escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
    "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",],
    "Quantidade": [vagas_cotas_negros_diurno, inscritos_cotas_negros_diurno, 
    vagas_cotas_escolaPublica_negros_def_rendaInf_diurno, inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno,
    vagas_cotas_escolaPublica_negros_rendaInf_diurno, inscritos_cotas_escolaPublica_negros_rendaInf_diurno
    , vagas_cotas_escolaPublica_negros_def_rendaSup_diurno, inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno
    , vagas_cotas_escolaPublica_negros_rendaSup_diurno, inscritos_cotas_escolaPublica_negros_rendaSup_diurno
    , vagas_cotas_escolaPublica_def_rendaInf_diurno, inscritos_cotas_escolaPublica_def_rendaInf_diurno
    , vagas_cotas_escolaPublica_rendaInf_diurno, inscritos_cotas_escolaPublica_rendaInf_diurno
    , vagas_cotas_escolaPublica_def_rendaSup_diurno, inscritos_cotas_escolaPublica_def_rendaSup_diurno
    , vagas_cotas_escolaPublica_rendaSup_diurno, inscritos_cotas_escolaPublica_rendaSup_diurno],
    "Legenda": ["Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", 
    "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos"]
})

fig = px.bar(df, x="COTAS", y="Quantidade", color="Legenda", barmode="group")
fig.update_layout(yaxis_type='linear')

app.layout = html.Div(children=[
    html.H1(children='Grafico cotas'),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
