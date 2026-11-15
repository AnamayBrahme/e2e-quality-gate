# tests/ui/test_login.py
import pytest
from pages.base_page import BasePage

@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_homepage_title(page):
    """Verify that the SauceDemo login page loads successfully."""
    base_page = BasePage(page)
    base_page.navigate("https://www.saucedemo.com")
    
    # Assert page title matches Swag Labs
    assert "Swag Labs" in base_page.get_title()