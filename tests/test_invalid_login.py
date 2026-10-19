from playwright.sync_api import Page, expect

def test_invalid_login(page: Page):
    # Step 1: Navigate to the website
    page.goto("https://www.saucedemo.com/")

    # Step 2: Enter a valid username
    page.get_by_placeholder("Username").fill("standard_user")

    # Step 3: Enter an invalid password
    page.get_by_placeholder("Password").fill("wrong_password")

    # Step 4: Click Login
    page.get_by_role("button", name="Login").click()

    # Step 5: Verify the error message
    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()

    # Step 6: Verify the expected error text
    expect(error_message).to_contain_text("Username and password do not match")

    # Step 7: Verify user remains on login page
    expect(page).to_have_url("https://www.saucedemo.com/")