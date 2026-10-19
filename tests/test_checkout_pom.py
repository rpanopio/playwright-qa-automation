import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.smoke
def test_complete_checkout(page: Page):

    # Step 1: Create LoginPage object
    login_page = LoginPage(page)

    # Step 2: Navigate to SauceDemo
    login_page.navigate()

    # Step 3: Login with valid credentials
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Step 4: Create InventoryPage object
    inventory_page = InventoryPage(page)

    # Step 5: Verify Products page
    inventory_page.verify_products_page()

    # Step 6: Add backpack to cart
    inventory_page.add_backpack_to_cart()

    # Step 7: Verify cart count
    inventory_page.verify_cart_count(1)

    # Step 8: Create CartPage object
    cart_page = CartPage(page)

    # Step 9: Open shopping cart
    cart_page.open_cart()

    # Step 10: Verify backpack
    cart_page.verify_product_name(
        "Sauce Labs Backpack"
    )

    # Step 11: Create CheckoutPage object
    checkout_page = CheckoutPage(page)

    # Step 12: Click Checkout
    checkout_page.start_checkout()

    # Step 13: Enter customer information
    checkout_page.enter_customer_information(
        "John",
        "Tester",
        "21236"
    )

    # Step 14: Click Continue
    checkout_page.continue_checkout()

    # Step 15: Verify order overview
    expect(
        page.locator('[data-test="title"]')
    ).to_have_text("Checkout: Overview")

    # Step 16: Click Finish
    checkout_page.finish_checkout()

    # Step 17: Verify order confirmation
    checkout_page.verify_order_confirmation()

    # Step 18: Pause browser for manual inspection
    #page.pause()

    # Intentional failure for reporting practice
    # expect(
    #     page.locator('[data-test="complete-header"]')
    # ).to_have_text("Payment failed!")