from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, base_url: str):
        self.page.goto(f"{base_url}/login")

    def login(self, username: str, password: str):
            self.page.get_by_label("Username").fill(username)
            self.page.get_by_label("Password").fill(password)
            self.page.get_by_role("button", name="Login").click()

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()
    
    @property
    def flash_messaging(self):
        return self.page.locator("#flash")