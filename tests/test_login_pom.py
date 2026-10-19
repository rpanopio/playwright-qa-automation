
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login_pom(page: Page):

    # Create the LoginPage object
    login_page = LoginPage(page)

    # Open SauceDemo
    login_page.navigate()

    # Login with valid credentials
    login_page.login("standard_user", "secret_sauce")

    # Verify successful login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


def test_invalid_login_pom(page: Page):

    # Create the LoginPage object
    login_page = LoginPage(page)

    # Open SauceDemo
    login_page.navigate()

    # Login with invalid credentials
    login_page.login("standard_user", "wrong_password")

    # Verify error message
    expect(login_page.error_message).to_be_visible()

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match"
    )
