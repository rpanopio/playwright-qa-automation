
from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_link = page.locator(
            '[data-test="shopping-cart-link"]'
        )

        self.product_name = page.locator(
            '[data-test="inventory-item-name"]'
        )

        self.product_price = page.locator(
            '[data-test="inventory-item-price"]'
        )

        self.product_quantity = page.locator(
            '[data-test="item-quantity"]'
        )

    def open_cart(self):
        self.cart_link.click()

    
    def verify_product_name(self, name):
        expect(self.product_name).to_have_text(name)

    def verify_product_price(self, price):
        expect(self.product_price).to_have_text(price)

    def verify_quantity(self, quantity):
        expect(self.product_quantity).to_have_text(
            str(quantity)
        )

    
    def remove_backpack(self):
        self.page.locator(
            '[data-test="remove-sauce-labs-backpack"]'
        ).click()

    def verify_product_removed(self):
        expect(
            self.page.get_by_text(
                "Sauce Labs Backpack", exact=True
            )
        ).to_have_count(0)

    def verify_cart_empty(self):
        expect(
            self.page.locator(".cart_item")
        ).to_have_count(0)

        expect(
            self.page.locator(".shopping_cart_badge")
        ).to_have_count(0)

