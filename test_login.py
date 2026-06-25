from playwright.sync_api import Page, expect
import pytest



def test_login_page_loads(login_page: Page):
    expect(login_page).to_have_title("The Internet")

    login_page.get_by_label("Username").fill("tomsmith")

    login_page.get_by_label("Password").fill("SuperSecretPassword!")

    #login_page.locator("button[type='submit']").click()
    login_page.get_by_role("button",name="Login").click()

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
    login_page.get_by_label('Username').fill(username)
    login_page.get_by_label('Password').fill(password)
    login_page.get_by_role("button", name ='Login').click()

    error_message = login_page.locator("#flash")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Your username is invalid!")
    