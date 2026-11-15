from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for the SauceDemo Checkout Flow."""

    def __init__(self, page):
        super().__init__(page)
        # Customer Information Form
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        
        # Overview & Confirmation
        self.finish_button = page.locator("#finish")
        self.success_header = page.locator(".complete-header")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        """Fill out customer shipping details."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def complete_checkout(self):
        """Finalize the order."""
        self.finish_button.click()

    def get_success_message(self) -> str:
        """Get the order confirmation success message."""
        return self.success_header.inner_text()