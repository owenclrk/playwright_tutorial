import pytest
from playwright.sync_api import Page

LOGIN_URL = "https://the-internet.herokuapp.com/login"

@pytest.fixture
def login_page(page: Page) -> Page:
    page.goto(LOGIN_URL)
    return page