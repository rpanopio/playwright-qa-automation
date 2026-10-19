
import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name,last_name,postal_code,expected_error",
    [
        ("", "Tester", "21236", "First Name is required"),
        ("John", "", "21236", "Last Name is required"),
        ("John", "Tester", "", "Postal Code is required"),
        ("", "", "", "First Name is required"),
    ],
)
def test_negative_checkout(
    page: Page,
    first_name,
    last_name,
    postal_code,
    expected_error
):

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

    # Step 7: Verify cart badge
    inventory_page.verify_cart_count(1)

    # Step 8: Create CartPage object
    cart_page = CartPage(page)

    # Step 9: Open shopping cart
    cart_page.open_cart()

    # Step 10: Create CheckoutPage object
    checkout_page = CheckoutPage(page)

    # Step 11: Start checkout
    checkout_page.start_checkout()

    # Step 12: Enter test data
    checkout_page.enter_customer_information(
        first_name,
        last_name,
        postal_code
    )

    # Step 13: Click Continue
    checkout_page.continue_checkout()

    # Step 14: Verify validation error
    checkout_page.verify_checkout_error(
        expected_error
    )

    # Step 15: Verify checkout did not advance
    checkout_page.verify_still_on_information_page()

    #input("Press ENTER to close Chromium...")