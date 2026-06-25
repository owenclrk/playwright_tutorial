from playwright.sync_api import Page, expect


def test_login_page_loads(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    expect(page).to_have_title("The Internet")

    username_field = page.locator("#username")
    username_field.fill("tomsmith")

    password_field = page.locator("#password")
    password_field.fill("SuperSecretPassword!")

    page.locator("button[type='submit']").click()

    success_message = page.locator("#flash")
    expect(success_message).to_be_visible()
    expect(success_message).to_contain_text("You logged into a secure area")

def test_fails_with_invalid_creditentials(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator('#username').fill("wrong_username")
    page.locator('#password').fill("wrong_password")
    page.locator("button[type='submit']").click()

    error_message = page.locator("#flash")
    expect(error_message).to_be_visible()
    expect(error_message).to_contain_text("Your username is invalid!")