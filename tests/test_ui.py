from pages.google_page import GooglePage


def test_google_title(browser):

    google_page = GooglePage(browser)

    google_page.open()

    assert "Google" in google_page.get_title()


def test_google_url(browser):

    google_page = GooglePage(browser)

    google_page.open()

    assert "google.com" in browser.current_url


def test_google_search_box_visible(browser):

    google_page = GooglePage(browser)

    google_page.open()

    search_box = google_page.search_box()

    assert search_box.is_displayed()


def test_google_search(browser):

    google_page = GooglePage(browser)

    google_page.open()

    google_page.search("Python Selenium")

    assert google_page.is_search_results_page()