import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():

    options = Options()

    # Run Chrome without opening a browser window
    options.add_argument("--headless")

    # Required for GitHub Actions/Linux
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Set browser window size
    options.add_argument("--window-size=1920,1080")

    # Create Chrome WebDriver
    driver = webdriver.Chrome(options=options)

    yield driver

    # Close browser after each test
    driver.quit()