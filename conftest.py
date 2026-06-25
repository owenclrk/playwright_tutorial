import pytest
import pytest_html
from playwright.sync_api import Page

LOGIN_URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def login_page(page: Page, request: pytest.FixtureRequest) -> Page:
    page.goto(LOGIN_URL)
    yield page
    screenshot_path = f"tests/screenshots/{request.node.name}.png"
    page.screenshot(path=screenshot_path)

    extra =