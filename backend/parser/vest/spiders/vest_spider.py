import typing
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import re


class VestSpider():

    base_url = "https://www.cebraspe.org.br/vestibulares"

    def request(self, browser: str, path: str = "") -> str:
        if browser.lower() == 'firefox':
            self.options = webdriver.FirefoxOptions()
            self.options.headless = True
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(f"{self.base_url}/{path}")
            sleep(1)
            self.page = BeautifulSoup(self.driver.page_source, 'html.parser')
            self.driver.quit()
            return str(self.page)

        if browser.lower() == "chrome":
            self.options = webdriver.ChromeOptions()
            self.options.headless = True
            self.driver = webdriver.Chome(options=self.options)
            self.driver.get(f"{self.base_url}/{path}")
            sleep(1)
            self.page = BeautifulSoup(self.driver.page_source, 'html.parser')
            self.driver.quit()
            return str(self.page)

        else:
            return ""

    def parser(self, body: str) -> typing.List[str]:

        self.ul = BeautifulSoup(body, 'html.parser').find_all("ul", {"class" : "q_circles_holder five_columns no_line"})
        self.li = self.ul[0].find_all("li")
        self.links = []
        for i in range(len(self.li)):
            self.link = self.li[i].find('a', href=True)['href']
            if re.search(r'VESTUNB_[0-9]+$|VESTUNB_[0-9]+_[0-9]$', self.link):
                self.links.append(self.link)

        return self.links
