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

<<<<<<< HEAD
=======
<<<<<<< HEAD
#variaveis globais noturno
global vagas_cotas_negros_noturno
global inscritos_cotas_negros_noturno
global vagas_cotas_escolaPublica_negros_def_rendaInf_noturno
global inscritos_cotas_escolaPublica_negros_def_rendaInf_noturno
global vagas_cotas_escolaPublica_negros_rendaInf_noturno
global inscritos_cotas_escolaPublica_negros_rendaInf_noturno
global vagas_cotas_escolaPublica_negros_def_rendaSup_noturno
global inscritos_cotas_escolaPublica_negros_def_rendaSup_noturno
global vagas_cotas_escolaPublica_negros_rendaSup_noturno
global inscritos_cotas_escolaPublica_negros_rendaSup_noturno
global vagas_cotas_escolaPublica_def_rendaInf_noturno
global inscritos_cotas_escolaPublica_def_rendaInf_noturno
global vagas_cotas_escolaPublica_rendaInf_noturno
global inscritos_cotas_escolaPublica_rendaInf_noturno
global vagas_cotas_escolaPublica_def_rendaSup_noturno
global inscritos_cotas_escolaPublica_def_rendaSup_noturno
global vagas_cotas_escolaPublica_rendaSup_noturno
global inscritos_cotas_escolaPublica_rendaSup_noturno
global vagas_universais_noturno
global inscritos_universais_noturno

#filtra apenas os diurnos
linha_diurno = df.loc[(df[0] == Nome) & (df[Vazia] <= 71)]
if linha_diurno.shape[0] != 0:
    indice_linha_curso_diurno = linha_diurno.index[0]
    
    vagas_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 1]
    inscritos_cotas_negros_diurno = df.at[indice_linha_curso_diurno, 2]
    
    vagas_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 4]
    inscritos_cotas_escolaPublica_negros_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 5]

    vagas_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 7]
    inscritos_cotas_escolaPublica_negros_rendaInf_diurno = df.at[indice_linha_curso_diurno, 8]

    vagas_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 10]
    inscritos_cotas_escolaPublica_negros_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 11]
    
    vagas_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 13]
    inscritos_cotas_escolaPublica_negros_rendaSup_diurno = df.at[indice_linha_curso_diurno, 14]

    vagas_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 16]
    inscritos_cotas_escolaPublica_def_rendaInf_diurno = df.at[indice_linha_curso_diurno, 17]
    
    vagas_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 19]
    inscritos_cotas_escolaPublica_rendaInf_diurno = df.at[indice_linha_curso_diurno, 20]

    vagas_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 22]
    inscritos_cotas_escolaPublica_def_rendaSup_diurno = df.at[indice_linha_curso_diurno, 23]
    
    vagas_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 25]
    inscritos_cotas_escolaPublica_rendaSup_diurno = df.at[indice_linha_curso_diurno, 26]

    vagas_universais_diurno = df.at[indice_linha_curso_diurno, 28]
    inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 29]

    



#filtra apenas os noturnos
linha_noturno = df.loc[(df[0] == Nome) & (df[Vazia] > 71)]
if linha_noturno.shape[0] != 0:
    indice_linha_curso_noturno = linha_noturno.index[0]

    vagas_cotas_negros_noturno = df.at[indice_linha_curso_noturno, 1]
    inscritos_cotas_negros_noturno = df.at[indice_linha_curso_noturno, 2]

    vagas_cotas_escolaPublica_negros_def_rendaInf_noturno = df.at[indice_linha_curso_noturno, 4]
    inscritos_cotas_escolaPublica_negros_def_rendaInf_noturno = df.at[indice_linha_curso_noturno, 5]

    vagas_cotas_escolaPublica_negros_rendaInf_noturno = df.at[indice_linha_curso_noturno, 7]
    inscritos_cotas_escolaPublica_negros_rendaInf_noturno = df.at[indice_linha_curso_noturno, 8]

    vagas_cotas_escolaPublica_negros_def_rendaSup_noturno = df.at[indice_linha_curso_noturno, 10]
    inscritos_cotas_escolaPublica_negros_def_rendaSup_noturno = df.at[indice_linha_curso_noturno, 11]
    
    vagas_cotas_escolaPublica_negros_rendaSup_noturno = df.at[indice_linha_curso_noturno, 13]
    inscritos_cotas_escolaPublica_negros_rendaSup_noturno = df.at[indice_linha_curso_noturno, 14]

    vagas_cotas_escolaPublica_def_rendaInf_noturno = df.at[indice_linha_curso_noturno, 16]
    inscritos_cotas_escolaPublica_def_rendaInf_noturno = df.at[indice_linha_curso_noturno, 17]
    
    vagas_cotas_escolaPublica_rendaInf_noturno = df.at[indice_linha_curso_noturno, 19]
    inscritos_cotas_escolaPublica_rendaInf_noturno = df.at[indice_linha_curso_noturno, 20]

    vagas_cotas_escolaPublica_def_rendaSup_noturno = df.at[indice_linha_curso_noturno, 22]
    inscritos_cotas_escolaPublica_def_rendaSup_noturno = df.at[indice_linha_curso_noturno, 23]
    
    vagas_cotas_escolaPublica_rendaSup_noturno = df.at[indice_linha_curso_noturno, 25]
    inscritos_cotas_escolaPublica_rendaSup_noturno = df.at[indice_linha_curso_noturno, 26]

    vagas_universais_noturno = df.at[indice_linha_curso_noturno, 28]
    inscritos_universais_noturno = df.at[indice_linha_curso_noturno, 29]
=======
>>>>>>> frontend
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
<<<<<<< HEAD
    inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 18]
=======
    inscritos_universais_diurno = df.at[indice_linha_curso_diurno, 18]
>>>>>>> 155966460183674dd642144e7d62e236fafe67be
>>>>>>> frontend
