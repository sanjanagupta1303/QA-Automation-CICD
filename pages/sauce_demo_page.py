from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger import logger


class SauceDemoPage:

    URL = "https://www.saucedemo.com/"

    # Login
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Products
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    # Cart
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")

    # Checkout
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    ORDER_CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        logger.info("Opening SauceDemo")

        self.driver.get(self.URL)

    def login(self, username, password):

        logger.info(f"Attempting login with username: {username}")

        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.LOGIN_BUTTON
        ).click()

        logger.info("Login button clicked")

    def get_products_title(self):

        logger.info("Checking Products page title")

        return self.wait.until(
            EC.visibility_of_element_located(self.PRODUCTS_TITLE)
        ).text

    def get_error_message(self):

        logger.info("Checking login error message")

        return self.wait.until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        ).text

    def add_backpack_to_cart(self):

        logger.info("Adding Sauce Labs Backpack to cart")

        self.wait.until(
            EC.element_to_be_clickable(self.ADD_BACKPACK)
        ).click()

        logger.info("Backpack added to cart")

    def open_cart(self):

        logger.info("Opening shopping cart")

        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

        logger.info("Shopping cart opened")

    def get_cart_item_name(self):

        logger.info("Checking cart item")

        return self.wait.until(
            EC.visibility_of_element_located(self.CART_ITEM)
        ).text

    def click_checkout(self):

        logger.info("Starting checkout")

        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()

        logger.info("Checkout page opened")

    def enter_customer_details(
        self,
        first_name,
        last_name,
        postal_code
    ):

        logger.info("Entering customer details")

        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *self.POSTAL_CODE
        ).send_keys(postal_code)

        logger.info("Customer details entered")

    def click_continue(self):

        logger.info("Continuing to order overview")

        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        ).click()

        logger.info("Order overview displayed")

    def click_finish(self):

        logger.info("Finishing order")

        self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        ).click()

        logger.info("Order completed")

    def get_order_confirmation(self):

        logger.info("Checking order confirmation")

        return self.wait.until(
            EC.visibility_of_element_located(self.ORDER_CONFIRMATION)
        ).text