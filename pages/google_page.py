from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage:

    URL = "https://www.google.com/"

    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_title(self):
        return self.driver.title

    def search_box(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

    def search(self, text):

        search_box = self.search_box()

        search_box.clear()
        search_box.send_keys(text)
        search_box.submit()

        self.wait.until(
            lambda driver: "search" in driver.current_url
        )

    def is_search_results_page(self):

        try:
            return "search" in self.driver.current_url
        except Exception:
            return False