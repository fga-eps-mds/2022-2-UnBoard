import typing
import re
from bs4 import BeautifulSoup
from base_spider import VestSpider


class PdfSpider(VestSpider):
    
    def get_pdf(self, body: str) -> str:
        self.page = BeautifulSoup(body, 'html.parser')
        self.link = self.page.find('a', text = re.compile('Demanda de (candidato|candidatos) por vaga$|Demanda de candidato por vaga - atualizada'))
        return self.link['href']
    
    def get_links(self) -> typing.List[str]:
        links = []
        urls = self.get_urls()
        
        for url in urls:
            page = self.request(url)
            link_pdf = self.get_pdf(page)
            links.append(link_pdf)
        
        return links


teste = PdfSpider()
list_pdf = teste.get_links()
print(list_pdf)
