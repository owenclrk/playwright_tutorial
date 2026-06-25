from playwright.sync_api import Page, expect
import pytest



def test_login_page_loads(login_page: Page):
    expect(login_page).to_have_title("The Internet")

    username_field = login_page.locator("#username")
    username_field.fill("tomsmith")

    password_field = login_page.locator("#password")
    password_field.fill("SuperSecretPassword!")

    login_page.locator("button[type='submit']").click()

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
    login_page.locator('#username').fill("wrong_username")
    login_page.locator('#password').fill("wrong_password")
    login_page.locator("button[type='submit']").click()

    error_message = login_page.locator("#flash")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Your username is invalid!")
    