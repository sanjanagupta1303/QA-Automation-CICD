import os
import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):

    driver = webdriver.Chrome()

    yield driver

    # Take screenshot if test failed
    if request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)

        screenshot_path = os.path.join(
            "screenshots",
            f"{request.node.name}.png"
        )

        driver.save_screenshot(screenshot_path)

        print(f"\nScreenshot saved: {screenshot_path}")

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield

    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)