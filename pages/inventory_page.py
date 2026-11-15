from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object for the SauceDemo Product Inventory Catalog Page."""

    def __init__(self, page):
        super().__init__(page)
        self.product_title_header = page.locator(".title")

    def get_page_header(self) -> str:
        """Get the main catalog header title."""
        return self.product_title_header.inner_text()