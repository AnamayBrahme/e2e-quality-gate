import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_valid_user_login(page):
    """Verify standard user can log in and view the product inventory."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")

    # Assert successful redirection and header text
    assert "inventory.html" in page.url
    assert inventory_page.get_page_header() == "Products"


@pytest.mark.ui
def test_locked_out_user_error(page):
    """Verify locked out user receives the correct failure banner

    (State Transition / Negative UI).
    """
    login_page = LoginPage(page)

    login_page.navigate_to_login()
    login_page.login("locked_out_user", "secret_sauce")

    # Assert error banner message
    error_text = login_page.get_error_message()
    assert "Sorry, this user has been locked out" in error_text