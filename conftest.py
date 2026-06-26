import pytest
import pytest_html
from login_page import LoginPage
from playwright.sync_api import Page
from dotenv import load_dotenv
import os
load_dotenv()

LOGIN_URL = "https://the-internet.herokuapp.com/login"
BASE_URL = os.environ["BASE_URL"]
AUTH_FILE = "tests/.auth/state.json"
VALID_USERNAME = os.environ["VALID_USERNAME"]
VALID_PASSWORD = os.environ["VALID_PASSWORD"]

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

@pytest.fixture(scope="session")
def auth_state(browser):
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    context.storage_state(path=AUTH_FILE)
    context.close()

    return AUTH_FILE

@pytest.fixture
def authenticated_page(browser, auth_state) -> Page:
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()
