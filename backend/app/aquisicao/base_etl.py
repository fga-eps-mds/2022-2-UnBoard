import abc
import typing
from pathlib import Path
import pandas as pd


class BaseETL(abc.ABC):
    """
    Estrutura como qualquer objeto ETL deve funcionar
    """

    path_input: Path
    path_output: Path
    _data_input: typing.Dict[str, pd.DataFrame]
    _data_output: typing.Dict[str, pd.DataFrame]

    @property
    def data_input(self) -> typing.Dict[str, pd.DataFrame]:
        """
        Acessa o atributo de dados de entrada

        :return: dicionario com nome do arquivo e um dataframe associado
        """
        if self._data_input is None:
            self.extract()
        return self._data_input

    @property
    def data_output(self) -> typing.Dict[str, pd.DataFrame]:
        """
        Acessa o atributo de dados de saida

        :return: dicionario com nome do arquivo e um dataframe associado
        """
        if self._data_output is None:
            self.extract()
        return self._data_output

    def __init__(self, input: str, output: str, create_path: bool = True) -> None:
        """
        
        """
        self.path_input = Path(input)
        self.path_output = Path(output)

        if create_path:
            self.path_input.mkdir(parents=True, exist_ok=True)
            self.path_output.mkdir(parents=True, exist_ok=True)

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
