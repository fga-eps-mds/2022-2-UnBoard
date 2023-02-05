import abc
import typing
import os
from vest.spiders.pdf_spider import PdfSpider
from base_etl import BaseETL
from utils.web import dowload_dados_web


class VestUnbETL(BaseETL):
    """
    Estrutura que manipula arquivos referente aos dados
    """

    def __init__(self, input: str,
                 output: str,
                 create_path: bool = True,
                 status: bool = True):
        """
        Instancia um objeto ETL
        :param input: string contendo o diretorio dos dados de entrada
        :param output: string contendo o diretorio dos dados de saida
        :patam status: flag que indica se deve ser baixado os dados:w
        :param create_path: flag que indica se um diretorio deve ser criado
        """

        self._status = status
        super().__init__(input, output, create_path)

    def links_vestibular(self) -> typing.Dict[str, str]:
        spider = PdfSpider()
        return spider.get_links()

    def pdfs_para_baixar(self) -> typing.Dict[str, str]:
        pdfs = self.links_vestibular()
        baixados = os.listdir(str(self.path_input))
        return {arq: link for arq, link in pdfs.items() if arq not in baixados}

    def download_pdfs(self) -> None:
        pdfs_para_baixar = self.pdfs_para_baixar()
        for arq in pdfs_para_baixar:
            caminho_arq = self.path_output / arq
            dowload_dados_web(caminho_arq, pdfs_para_baixar[arq])

    @abc.abstractmethod
    def extract(self) -> None:
        """
        Extrai os dados de algum objeto
        """
        pass

    @abc.abstractmethod
    def transform(self) -> None:
        """
        Transforma os dados e os adequa para os formatos
        de saida de interesse
        """
        pass
