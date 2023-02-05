import pandas as pd
import buscarCurso_15
from buscarCurso_15 import *

#variaveis globais diurno
global vagas_cotas_negros_diurno
global inscritos_cotas_negros_diurno
global vagas_cotas_escolaPublica_negros_rendaInf_diurno
global inscritos_cotas_escolaPublica_negros_rendaInf_diurno
global vagas_cotas_escolaPublica_negros_rendaSup_diurno
global inscritos_cotas_escolaPublica_negros_rendaSup_diurno
global vagas_cotas_escolaPublica_rendaInf_diurno
global inscritos_cotas_escolaPublica_rendaInf_diurno
global vagas_cotas_escolaPublica_rendaSup_diurno
global inscritos_cotas_escolaPublica_rendaSup_diurno
global vagas_universais_diurno
global inscritos_universais_diurno

#filtra apenas os diurnos
linha_diurno = df.loc[(df[1] == Nome) & (df[0] >= 19) & (df[0] <= 76)]
if linha_diurno.shape[0] != 0:
    indice_linha_curso_diurno = linha_diurno.index[0]
    
    vagas_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 4]
    inscritos_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 5]

    vagas_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 7]
    inscritos_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 8]
    
    vagas_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 13]
    inscritos_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 14]
    
    vagas_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 10]
    inscritos_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 11]
    
    vagas_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 16]
    inscritos_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 17]

    vagas_universais_diurno = df.at[indice_linha_curso_diurno, 19]
    inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 20]