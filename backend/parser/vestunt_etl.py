import abc
import typing
from backend.parser.vest.spiders.pdf_spider import PdfSpider
from parser.base_etl import BaseETL


class VestUnbETL(BaseETL):
    """
    Estrutura que manipula arquivos referente aos dados
    """

    def __init__(
        self, input: str,
            output: str,
            create_path: bool = True,
            status: bool = True
    ):
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

    @abc.abstractmethod
    def load(self) -> None:
        """
        exporta os dados para um csv
        """
        for arq, df in self.data_output.items():
            df.to_parquet(self.path_output / arq, index=False)

    def pipeline(self) -> None:
        """
        executa o pipeline completo
        """
        self.extract()
        self.transform()
        self.load()
