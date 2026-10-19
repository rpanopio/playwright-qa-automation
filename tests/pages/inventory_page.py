
from playwright.sync_api import Page, expect


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        # Page locators
        self.products_title = page.get_by_text(
            "Products", exact=True
        )

        self.backpack_button = page.locator(
            "#add-to-cart-sauce-labs-backpack"
        )

        self.cart_badge = page.locator(
            ".shopping_cart_badge"
        )

    def verify_products_page(self):
        expect(self.products_title).to_be_visible()

    def add_backpack_to_cart(self):
        self.backpack_button.click()

    def verify_cart_count(self, expected_count):
        expect(self.cart_badge).to_have_text(
            str(expected_count)
        )
