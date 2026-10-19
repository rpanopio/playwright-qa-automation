
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_verify_shopping_cart(page: Page):

    # Step 1: Create LoginPage object
    login_page = LoginPage(page)

    # Step 2: Navigate to SauceDemo
    login_page.navigate()

    # Step 3: Login
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

    # Step 7: Create CartPage and open cart
    cart_page = CartPage(page)
    cart_page.open_cart()

    # Verify cart page
    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )

    # Verify product details
    cart_page.verify_product_name(
        "Sauce Labs Backpack"
    )

    cart_page.verify_product_price("$29.99")

    cart_page.verify_quantity(1)
