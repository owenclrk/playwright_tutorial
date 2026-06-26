import pytest
import pytest_html
from playwright.sync_api import Page
from dotenv import load_dotenv
import os
load_dotenv()

LOGIN_URL = "https://the-internet.herokuapp.com/login"
BASE_URL = os.environ["BASE_URL"]


@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(f"{BASE_URL}/login")
    yield page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and "page" in item.funcargs:
        page = item.funcargs["page"]
        screenshot_path = f"tests/screenshots/{item.name}.png"
        page.screenshot(path=screenshot_path)

        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.image(screenshot_path))
        report.extras = extras