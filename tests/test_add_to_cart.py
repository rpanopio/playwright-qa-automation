from playwright.sync_api import Page, expect

def test_add_product_to_cart(page: Page):
    # Step 1: Navigate to the website
    page.goto("https://www.saucedemo.com/")

    # Step 2: Enter username
    page.get_by_placeholder("Username").fill("standard_user")

    # Step 3: Enter password
    page.get_by_placeholder("Password").fill("secret_sauce")

    # Step 4: Click Login
    page.get_by_role("button", name="Login").click()

    # Step 5: Verify Products page
    expect(page.get_by_text("Products", exact=True)).to_be_visible()
    