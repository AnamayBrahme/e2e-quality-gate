# pages/base_page.py
from playwright.sync_api import Page


class BasePage:
    """Base Page class encapsulating common browser interactions

    with built-in auto-waiting.
    """
    
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url)

    def get_title(self) -> str:
        """Get the current page title."""
        return self.page.title()