import typing
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from base_spider import VestSpider


class PdfSpider(VestSpider):
    def get_pdf(self, links: typing.List[str]) -> typing.List[str]:

        driver = webdriver.Firefox()
        pdfs = []

        for link in links:
            driver.get(link)
            try:
                sleep(1)
                wait = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.TAG_NAME, "li"))
                )
                if wait:
                    tag = driver.find_elements(
                        By.XPATH,
                        "//*[contains(text(), 'Demanda de candidato por vaga') or contains(text(), 'Demanda de candidatos por vaga')]",
                    )
                    if len(tag) > 1:
                        tag.pop(0)
                    pdfs.append(tag[0].get_attribute("href"))
            except Exception as exc:
                print("{}: {}".format(type(exc).__name__, exc))

        driver.quit()
        return pdfs

    def get_links(self) -> typing.Dict[str, str]:
        urls = self.get_urls()
        links = self.get_pdf(urls)
        return dict(zip([re.search("[^/]+$",
                                   url).group() for url in urls], links)
                    )
