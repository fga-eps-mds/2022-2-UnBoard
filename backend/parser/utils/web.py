import requests
from pathlib import Path
import typing


def dowload_dados_web(caminho: typing.Union[str, Path], url: str) -> None:

    r = requests.get(url, stream=True)
    with open(caminho, "wb") as arq:
        arq.write(r.content)
