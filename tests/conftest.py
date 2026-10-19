from config import TEST_URL, TEST_USERNAME, TEST_PASSWORD
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.fixture
def logged_in_page(page: Page):

    login_page = LoginPage(page)

    # Navigate using environment configuration
    page.goto(TEST_URL)

    # Login using environment credentials
    login_page.login(
        TEST_USERNAME,
        TEST_PASSWORD
    )

    return page


@pytest.fixture
def logged_in_page(page: Page):

    login_page = LoginPage(page)

    login_page.navigate()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    return page


@pytest.fixture
def cart_with_backpack(logged_in_page: Page):

    # The user is already logged in
    page = logged_in_page

    # Create InventoryPage object
    inventory_page = InventoryPage(page)

    # Verify Products page
    inventory_page.verify_products_page()

    # Add backpack to cart
    inventory_page.add_backpack_to_cart()

    # Verify cart count
    inventory_page.verify_cart_count(1)

    # Create CartPage object
    cart_page = CartPage(page)

    # Open shopping cart
    cart_page.open_cart()

    # Return the page with backpack in cart
    return page
