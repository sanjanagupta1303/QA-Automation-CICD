from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:

    URL = "https://www.google.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def search_box(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "q")
            )
        )

    def search(self, text):
        search_box = self.search_box()
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)

    def get_title(self):
        return self.driver.title

    def is_search_results_page(self):
        return "Google Search" in self.driver.title