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
