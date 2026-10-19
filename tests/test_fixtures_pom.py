
from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Test 1: Verify successful login
def test_login_using_fixture(logged_in_page: Page):

    inventory_page = InventoryPage(logged_in_page)

    inventory_page.verify_products_page()


# Test 2: Verify product in cart
def test_cart_using_fixture(cart_with_backpack: Page):

    cart_page = CartPage(cart_with_backpack)

    cart_page.verify_product_name(
        "Sauce Labs Backpack"
    )

    cart_page.verify_quantity(1)


# Test 3: Complete checkout using fixture
def test_checkout_using_fixture(cart_with_backpack: Page):

    checkout_page = CheckoutPage(cart_with_backpack)

    checkout_page.start_checkout()

    checkout_page.enter_customer_information(
        "John",
        "Tester",
        "21236"
    )

    checkout_page.continue_checkout()

    expect(
        cart_with_backpack.locator('[data-test="title"]')
    ).to_have_text("Checkout: Overview")

    checkout_page.finish_checkout()

    checkout_page.verify_order_confirmation()
