from pages.sauce_demo_page import SauceDemoPage
import pytest

def test_valid_login(browser):

    sauce_demo = SauceDemoPage(browser)

    sauce_demo.open()

    sauce_demo.login(
        "standard_user",
        "secret_sauce"
    )

    assert sauce_demo.get_products_title() == "Products"


def test_invalid_login(browser):

    sauce_demo = SauceDemoPage(browser)

    sauce_demo.open()

    sauce_demo.login(
        "standard_user",
        "wrong_password"
    )

    error_message = sauce_demo.get_error_message()

    assert "Username and password do not match" in error_message


def test_add_product_to_cart(browser):

    sauce_demo = SauceDemoPage(browser)

    sauce_demo.open()

    sauce_demo.login(
        "standard_user",
        "secret_sauce"
    )

    sauce_demo.add_backpack_to_cart()

    sauce_demo.open_cart()

    assert sauce_demo.get_cart_item_name() == "Sauce Labs Backpack"


def test_complete_checkout(browser):

    sauce_demo = SauceDemoPage(browser)

    sauce_demo.open()

    sauce_demo.login(
        "standard_user",
        "secret_sauce"
    )

    sauce_demo.add_backpack_to_cart()

    sauce_demo.open_cart()

    sauce_demo.click_checkout()

    sauce_demo.enter_customer_details(
        "Sanjana",
        "Gupta",
        "400001"
    )

    sauce_demo.click_continue()

    sauce_demo.click_finish()

    assert sauce_demo.get_order_confirmation() == "Thank you for your order!"

@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("standard_user", "secret_sauce", "success"),
        ("standard_user", "wrong_password", "failure"),
        ("wrong_user", "wrong_password", "failure"),
    ]
)
def test_login_data_driven(browser, username, password, expected):

    sauce_demo = SauceDemoPage(browser)

    sauce_demo.open()

    sauce_demo.login(username, password)

    if expected == "success":

        assert sauce_demo.get_products_title() == "Products"

    else:

        error_message = sauce_demo.get_error_message()

        assert "Username and password do not match" in error_message