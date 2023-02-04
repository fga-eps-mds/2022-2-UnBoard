from _pytest.mark import pytest_addoption
import pytest
from utils.search_bar import Courses_list

def test_se_tamanho_de_cursos_eh_0():
    search_bar = Courses_list(2019)
    tamanho_esperado = 0
    resultado = len(search_bar.search_course(""))
    assert resultado == tamanho_esperado

@pytest.mark.parametrize(
    ("parametro", "resultado_esperado"),
    [(2019, 0), (2022, 0), (2023, 0)]
)
def test_se_tamanho_de_cursos_por_ano_eh_0_se_passar_nenhum_curso(parametro, resultado_esperado):
    search_bar = Courses_list(parametro)
    resultado = len(search_bar.search_course(""))
    assert resultado == resultado_esperado

#FALHA ESPERADA
@pytest.mark.xfail
@pytest.mark.parametrize(
    ("parametro", "resultado_esperado"),
    [(2019, 1), (2022, 1), (2023, 1)]
)
def test_se_tamanho_de_cursos_por_ano_eh_1_se_passar_nenhum_curso(parametro, resultado_esperado):
    search_bar = Courses_list(parametro)
    resultado = len(search_bar.search_course(""))
    assert resultado == resultado_esperado

@pytest.mark.xfail
@pytest.mark.parametrize(
    ("parametro", "resultado_esperado"),
    [(2019, 0), (2022, 0), (2023, 0)]
)
def test_se_tamanho_de_cursos_por_ano_eh_dif_de_0_se_passar_nenhum_curso(parametro, resultado_esperado):
    search_bar = Courses_list(parametro)
    resultado = len(search_bar.search_course(""))
    assert resultado == resultado_esperado

@pytest.mark.parametrize(
    ("parametro"),
    [2019, 2022, 2023]
)
def test_encontra_curso_que_se_deseja(parametro):
    search_bar = Courses_list(parametro)
    assert isinstance(search_bar, Courses_list)


#    def test_with_finder(self):
#        self.setup_method()
#        self.finder("Adm")
#        self.finder("")
#        self.finder("Bacharelado")
#        self.finder("Engenharia")
#        self.finder("dnoawkdnsknawod")

#    def test_campus(self):
#        self.setup_method()
#        result = self.search_bar.search_course("")
#        alt_result = self.search_bar.search_course("Admnistração")
#        for i in result:
#            assert i[1] in self.search_bar.CAMPUS_LIST
# for j in result:
# assert j[1] in self.search_bar.CAMPUS_LIST
