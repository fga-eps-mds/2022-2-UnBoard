import pandas as pd
import typing
import json

class SearchCourses():

    def lista_por_ano(self, ano: int) -> typing.List[typing.Dict[str,str]]:
    
        df = pd.read_excel(f"../databases/VESTUNB_{ano}.xlsx")
        
        if ano == 15:
            return [{"nome_curso":curso} for curso in df.iloc[9:67][1].tolist()]
        elif ano == 16:
            return [{"nome_curso":curso} for curso in df.iloc[18:77][1].tolist()]
        elif ano == 17:
            return [{"nome_curso":curso} for curso in df.iloc[9:68][1].tolist()]
        elif ano == 18:
            return [{"nome_curso":curso} for curso in df.iloc[9:68][1].tolist()]
        elif ano == 19:
            return [{"nome_curso":curso} for curso in df.iloc[11:70][1].tolist()]
        elif ano == 22:
            return [{"nome_curso":curso} for curso in df.iloc[12:73][1].tolist()]
        elif ano == 23:
            return [{"nome_curso":curso} for curso in df.iloc[12:74][1].tolist()]
        else:
            return [{}]

    def lista_cursos(self)-> typing.Dict[str, typing.List[typing.Dict[str,str]]]:
        
        anos = [15 ,16, 17, 18, 19, 22, 23]
        chave_anos = [f"ano20{ano}" for ano in anos]
        
        lista_curso_por_ano = [self.lista_por_ano(ano) for ano in anos]
        return dict(zip(chave_anos, lista_curso_por_ano))
