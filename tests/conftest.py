
from config import TEST_URL, TEST_USERNAME, TEST_PASSWORD
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage



@pytest.fixture
def login_page(page: Page):
    page.goto(TEST_URL)
    return page



@pytest.fixture
def logged_in_page(page: Page):
    login = LoginPage(page)
    page.goto(TEST_URL)
    login.login(TEST_USERNAME, TEST_PASSWORD)
    return page


@pytest.fixture
def cart_with_backpack(logged_in_page: Page):
    page = logged_in_page

    inventory_page = InventoryPage(page)
    inventory_page.verify_products_page()
    inventory_page.add_backpack_to_cart()
    inventory_page.verify_cart_count(1)

    cart_page = CartPage(page)
    cart_page.open_cart()

    return page
