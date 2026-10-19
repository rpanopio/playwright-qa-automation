
from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_backpack_to_cart(page: Page):

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

    # Step 7: Verify shopping cart count
    inventory_page.verify_cart_count(1)
