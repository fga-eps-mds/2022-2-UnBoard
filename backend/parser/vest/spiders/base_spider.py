import typing
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re


class VestSpider():

    base_url = "https://www.cebraspe.org.br"

    def request(self, path: str = "/vestibulares") -> str:
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get(f"{self.base_url}{path}")
        sleep(2)
        page = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return str(page)

    def parser(self, body: str) -> typing.List[str]:
        
        self.ul = BeautifulSoup(body, 'html.parser').find_all("ul", {"class" : "q_circles_holder five_columns no_line"})
        self.li = self.ul[0].find_all("li")
        links = []
        for i in range(len(self.li)):
            link = self.li[i].find('a', href=True)['href']
            if re.search(r'VESTUNB_[0-9]+$|VESTUNB_[0-9]+_[0-9]$', link):
                links.append(link)

        return links

    def get_urls(self) -> typing.List[str]:
        self.andamento = self.request()
        self.encerrado = self.request("/vestibulares/encerrado")
        self.links_andamento = self.parser(self.andamento)
        self.links_encerrado = self.parser(self.encerrado)

        return self.links_andamento + self.links_encerrado
