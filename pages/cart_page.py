from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for the SauceDemo Cart Page."""

    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")
        self.cart_item = page.locator(".cart_item")

    def proceed_to_checkout(self):
        """Click the checkout button."""
        self.checkout_button.click()

    def get_cart_item_count(self) -> int:
        """Return the number of items in the cart."""
        return self.cart_item.count()