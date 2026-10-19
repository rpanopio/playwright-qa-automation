
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remove_backpack_from_cart(page: Page):

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

    # Step 10: Verify product exists
    cart_page.verify_product_name(
        "Sauce Labs Backpack"
    )

    # Step 11: Remove backpack
    cart_page.remove_backpack()

    # Step 12: Verify product removed
    cart_page.verify_product_removed()

    # Step 13: Verify empty cart
    cart_page.verify_cart_empty()
