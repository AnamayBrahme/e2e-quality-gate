from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page."""

    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def navigate_to_login(self):
        """Navigate to the SauceDemo homepage."""
        self.navigate("https://www.saucedemo.com")

    def login(self, username: str, password: str):
        """Fill credentials and click login."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        """Retrieve error banner text if present."""
        return self.error_message.inner_text()