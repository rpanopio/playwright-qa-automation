
from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        # Checkout buttons
        self.checkout_button = page.locator(
            '[data-test="checkout"]'
        )

        self.continue_button = page.locator(
            '[data-test="continue"]'
        )

        self.finish_button = page.locator(
            '[data-test="finish"]'
        )

        # Customer information fields
        self.first_name = page.locator(
            '[data-test="firstName"]'
        )

        self.last_name = page.locator(
            '[data-test="lastName"]'
        )

        self.postal_code = page.locator(
            '[data-test="postalCode"]'
        )

        # Order confirmation
        self.confirmation_message = page.locator(
            '[data-test="complete-header"]'
        )

    def start_checkout(self):
        self.checkout_button.click()

    def enter_customer_information(
        self, first_name, last_name, postal_code
    ):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postal_code.fill(postal_code)

    def continue_checkout(self):
        self.continue_button.click()

    def finish_checkout(self):
        self.finish_button.click()

    def verify_order_confirmation(self):
        expect(self.confirmation_message).to_have_text(
            "Thank you for your order!"
        )

    # Negative Checkout Testing Using POM + Pytest
    def verify_checkout_error(self, expected_message):
        error = self.page.locator(
            '[data-test="error"]'
        )

        expect(error).to_be_visible()
        expect(error).to_contain_text(
            expected_message
        )

    def verify_still_on_information_page(self):
        expect(self.page).to_have_url(
            "https://www.saucedemo.com/checkout-step-one.html"
        )
