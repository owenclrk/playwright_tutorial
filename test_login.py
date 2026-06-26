from playwright.sync_api import Page, expect
from login_page import LoginPage
import pytest
import os
from dotenv import load_dotenv
load_dotenv()



BASE_URL = os.environ["BASE_URL"]
VALID_USERNAME = os.environ["VALID_USERNAME"]
VALID_PASSWORD = os.environ["VALID_PASSWORD"]


def test_login_page_loads(login_page: Page):
    page_obj = LoginPage(login_page)
    expect(login_page).to_have_title("The Internet")

    page_obj.login(VALID_USERNAME, VALID_PASSWORD)

    success_message = login_page.locator("#flash")
    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text("You logged into a secure area")



@pytest.mark.parametrize(
        "username, password, expected_error",
        [
            ("wrong_user","wrong_password","Your username is invalid"),
            ("tomsmith", "wrong_password", "Your password is invalid"),
            ("","", "Your username is invalid"),
        ],
)
def test_fails_with_invalid_creditentials(login_page: Page, username, password, expected_error):
    page_obj = LoginPage(login_page)
    page_obj.login(username, password)

    expect(page_obj.flash_message).to_be_visible()
    expect(page_obj.flash_message).to_contain_text(expected_error)
    
def test_secure_area_accessible_with_saved_sessions(authenticated_page: Page):
    authenticated_page.goto(f"{BASE_URL}/secure")
    expect(authenticated_page.locator("h2")).to_contain_text("Secure Area")