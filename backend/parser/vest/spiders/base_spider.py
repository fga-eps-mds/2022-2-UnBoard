import typing
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class VestSpider:

    base_url = "https://www.cebraspe.org.br"

    def vest_links(self, path: str = "/vestibulares") -> typing.List[str]:
        driver = webdriver.Firefox()
        driver.get(f"{self.base_url}{path}")
        links = []

        try:
            wait = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CLASS_NAME, "q_circle_outer")
                )
            )
            if wait:
                tags = driver.find_elements(
                    By.CSS_SELECTOR, ".q_circle_text_holder [href]"
                )
                for link in tags:
                    if re.search(
                        r"VESTUNB_[0-9]+$|VESTUNB_[0-9]+_[0-9]$",
                        link.get_attribute("href"),
                    ):
                        links.append(link.get_attribute("href"))

        finally:
            driver.quit()
            return links

    def get_urls(self) -> typing.List[str]:
        self.encerrado = self.vest_links("/vestibulares/encerrado")
        self.andamento = self.vest_links("/vestibulares")
        return list(self.encerrado + self.andamento)
