from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash

app = Dash(__name__)
year = 23
df = pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx")
Nome = "Administração (Bacharelado)" #nome que deseja pesquisar
ano = [2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023]

cursos = df.iloc[12:][1].tolist()

def get_courses(year):
    df = pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx")
    if (year == 15):
        cursos = df.iloc[9:][1].tolist()
        Nome = "Administração (***)"

    if (year == 16):
        cursos = df.iloc[9:][1].tolist()
        Nome = "Administração (Bacharelado)"

    if (year == 17):
        cursos = df.iloc[9:][1].tolist()
        Nome = "Administração (Bacharelado)"

    if (year == 18):
        cursos = df.iloc[9:][1].tolist()
        Nome = "Administração (Bacharelado)"

    if (year == 19):
        cursos = df.iloc[11:][1].tolist()
        Nome = "Administração (Bacharelado)"

    if (year == 22):
        cursos = df.iloc[12:][1].tolist()
        Nome = "Administração (Bacharelado)"

    if (year == 23):
        cursos = df.iloc[12:][1].tolist()
        Nome = "Administração (Bacharelado)"
    return cursos

cont = 0

def get_courses(year):
    df = pd.read_excel(f"../../databases/VESTUNB_{year}.xlsx")
    if (year == 15):
        cursos = df.iloc[9:][1].tolist()

    if (year == 16):
        cursos = df.iloc[9:][1].tolist()

    if (year == 17):
        cursos = df.iloc[9:][1].tolist()

    if (year == 18):
        cursos = df.iloc[9:][1].tolist()

    if (year == 19):
        cursos = df.iloc[11:][1].tolist()

    if (year == 22):
        cursos = df.iloc[12:][1].tolist()

    if (year == 23):
        cursos = df.iloc[12:][1].tolist()
    return cursos

def gerar_grafico(df):
    if 100 in df.columns:
        cont = 1
        
        linha_diurno = df.loc[(df[1] == Nome)]
        indice_linha_curso_diurno = linha_diurno.index[0]
        
        vagas_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 2]
        inscritos_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 3]
        
        vagas_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 100]
        inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 101]

        vagas_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 5]
        inscritos_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 6]

        vagas_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 104]
        inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 105]
        
        vagas_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 11]
        inscritos_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 12]

        vagas_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 102]
        inscritos_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 103]
        
        vagas_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 8]
        inscritos_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 9]

        vagas_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 106]
        inscritos_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 107]
        
        vagas_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 14]
        inscritos_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 15]

        vagas_universais_diurno = df.at[indice_linha_curso_diurno, 17]
        inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 18]

    else:
        linha_diurno = df.loc[(df[1] == Nome)]
        indice_linha_curso_diurno = linha_diurno.index[0]
        
        vagas_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 2]
        inscritos_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 3]
        
        vagas_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 5]
        inscritos_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 6]

        vagas_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 11]
        inscritos_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 12]

        vagas_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 8]
        inscritos_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 9]

        vagas_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 14]
        inscritos_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 15]

        vagas_universais_diurno = df.at[indice_linha_curso_diurno, 17]
        inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 18]

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


    else:
        df = pd.DataFrame({
        "TIPO": ["Negros", "Negros", 
        "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo", 
        "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda inferior ou igual a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
        "Estudantes de escolas publicas <br> nao autodeclarados pretos, pardos ou indígenas <br> com renda superior a 1,5 salario minimo",
        "Universal", "Universal"],
        "Quantidade": [vagas_cotas_negros_diurno, inscritos_cotas_negros_diurno, 
        vagas_cotas_escolaPublica_negros_rendaInf_diurno, inscritos_cotas_escolaPublica_negros_rendaInf_diurno,
        vagas_cotas_escolaPublica_negros_rendaSup_diurno, inscritos_cotas_escolaPublica_negros_rendaSup_diurno,
        vagas_cotas_escolaPublica_rendaInf_diurno, inscritos_cotas_escolaPublica_rendaInf_diurno,
        vagas_cotas_escolaPublica_rendaSup_diurno, inscritos_cotas_escolaPublica_rendaSup_diurno, 
        vagas_universais_diurno, inscritos_universais_diurno],
        "Legenda": ["Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", "Inscritos", "Vagas", 
        "Inscritos", "Vagas", "Inscritos"]
    })
    
    return df
    

newdf = gerar_grafico(df)
fig = px.bar(newdf, x="TIPO", y="Quantidade", color="Legenda", barmode="group")
#fig.update_layout(yaxis_type='linear')
#fig.update_layout(yaxis_type='linear', yaxis_range=[0, 15])
fig.update_layout(yaxis_type='linear',  
                  annotations=[dict(x=i, y=j, text=str(j),font=dict(color='black')) for i,j in zip(newdf['TIPO'], newdf['Quantidade'])],
                  xaxis=dict(title='TIPO'), yaxis=dict(title='Quantidade'))


app.layout = html.Div(style={'background-color': '#003366'},
    children=[
    html.H1(children='Grafico vagas e inscritos' , style={'color': 'white', 'text-align': 'center'}),

    html.Div([
        dcc.Dropdown(
            id="dropdown-cursos",
            options=[{"label": curso, "value": curso} for curso in cursos],
            value=cursos[0]
        ),
        html.Div(id="output")
    ]),

    html.Div([
        dcc.Dropdown(
            id="dropdown-ano",
            options=[2015, 2016, 2017, 2018, 2019, 2020, 2022, 2023],
            value=ano[7]
        ),
        html.Div(id="outputAno")
    ]),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(
    Output('dropdown-cursos','options'),
    [dash.dependencies.Input("dropdown-ano", "value")]
)
def update_year(value):
    year = value-2000
    updated_cursos = get_courses(year)
    return [{"label": curso, "value": curso} for curso in updated_cursos]

@app.callback(
    Output('example-graph','figure'),
    [dash.dependencies.Input("dropdown-cursos", "value")]
)
def update_output(value):
    global Nome
    Nome = value
    newdf = gerar_grafico(df)
    fig = px.bar(newdf, x="TIPO", y="Quantidade", color="Legenda", barmode="group")
    fig.update_layout(yaxis_type='linear',  
                    annotations=[dict(x=i, y=j, text=str(j),font=dict(color='black')) for i,j in zip(newdf['TIPO'], newdf['Quantidade'])],
                    xaxis=dict(title='TIPO'), yaxis=dict(title='Quantidade'))
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
