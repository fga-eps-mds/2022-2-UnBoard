import pandas as pd
import buscarCurso
from buscarCurso import *

#variaveis globais diurno
global vagas_cotas_negros_diurno
global inscritos_cotas_negros_diurno
global vagas_cotas_escolaPublica_negros_def_rendaInf_diurno
global inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno
global vagas_cotas_escolaPublica_negros_rendaInf_diurno
global inscritos_cotas_escolaPublica_negros_rendaInf_diurno
global vagas_cotas_escolaPublica_negros_def_rendaSup_diurno
global inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno
global vagas_cotas_escolaPublica_negros_rendaSup_diurno
global inscritos_cotas_escolaPublica_negros_rendaSup_diurno
global vagas_cotas_escolaPublica_def_rendaInf_diurno
global inscritos_cotas_escolaPublica_def_rendaInf_diurno
global vagas_cotas_escolaPublica_rendaInf_diurno
global inscritos_cotas_escolaPublica_rendaInf_diurno
global vagas_cotas_escolaPublica_def_rendaSup_diurno
global inscritos_cotas_escolaPublica_def_rendaSup_diurno
global vagas_cotas_escolaPublica_rendaSup_diurno
global inscritos_cotas_escolaPublica_rendaSup_diurno
global vagas_universais_diurno
global inscritos_universais_diurno

global cont
cont = 0


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