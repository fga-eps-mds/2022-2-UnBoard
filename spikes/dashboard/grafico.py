from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import leituraPlanilha
from leituraPlanilha import *
from buscarCurso import *

app = Dash(__name__)


if cont == 1:
    df = pd.DataFrame({
        "TIPO": ["Negros", "Negros", 
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
        "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
        "Universal", "Universal"],
        "Quantidade": [vagas_cotas_negros_diurno, inscritos_cotas_negros_diurno, 
        vagas_cotas_escolaPublica_negros_def_rendaInf_diurno, inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno,
        vagas_cotas_escolaPublica_negros_rendaInf_diurno, inscritos_cotas_escolaPublica_negros_rendaInf_diurno
        , vagas_cotas_escolaPublica_negros_def_rendaSup_diurno, inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno
        , vagas_cotas_escolaPublica_negros_rendaSup_diurno, inscritos_cotas_escolaPublica_negros_rendaSup_diurno
        , vagas_cotas_escolaPublica_def_rendaInf_diurno, inscritos_cotas_escolaPublica_def_rendaInf_diurno
        , vagas_cotas_escolaPublica_rendaInf_diurno, inscritos_cotas_escolaPublica_rendaInf_diurno
        , vagas_cotas_escolaPublica_def_rendaSup_diurno, inscritos_cotas_escolaPublica_def_rendaSup_diurno
        , vagas_cotas_escolaPublica_rendaSup_diurno, inscritos_cotas_escolaPublica_rendaSup_diurno, vagas_universais_diurno, 
        inscritos_universais_diurno],
        "Legenda": ["Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", 
        "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos"]
    })

fig = px.bar(df, x="TIPO", y="Quantidade", color="Legenda", barmode="group")
#fig.update_layout(yaxis_type='linear')
#fig.update_layout(yaxis_type='linear', yaxis_range=[0, 15])
fig.update_layout(yaxis_type='linear', yaxis_range=[0, 15], 
                  annotations=[dict(x=i, y=j, text=str(j),font=dict(color='black')) for i,j in zip(df['TIPO'], df['Quantidade'])],
                  xaxis=dict(title='TIPO'), yaxis=dict(title='Quantidade'))


app.layout = html.Div(children=[
    html.H1(children='Grafico vagas e inscritos'),
    html.H2(children=Nome),
    html.Div(children='Clique em Autoscale para ver o grafico completo', style={'textAlign': 'right'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
