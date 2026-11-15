import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_end_to_end_purchase_flow(page):
    """Verify standard user can log in, add item to cart, and complete checkout successfully."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # 1. Login
    login_page.navigate_to_login()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url

    # 2. Add first product to cart from inventory
    add_to_cart_btn = page.locator("button[data-test^='add-to-cart']").first
    add_to_cart_btn.click()

    # 3. Go to Cart
    page.locator(".shopping_cart_link").click()
    assert cart_page.get_cart_item_count() == 1

    # 4. Proceed to Checkout
    cart_page.proceed_to_checkout()
    assert "checkout-step-one.html" in page.url

    # 5. Fill Customer Info and Continue
    checkout_page.fill_customer_info("Anamay", "Brahme", "10115")
    assert "checkout-step-two.html" in page.url

    # 6. Finish Order
    checkout_page.complete_checkout()
    
    # 7. Assert Success
    assert "checkout-complete.html" in page.url
    assert "Thank you for your order!" in checkout_page.get_success_message()