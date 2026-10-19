
from playwright.sync_api import Page, expect


def test_valid_login(login_page: Page):

    # The fixture already opened SauceDemo
    login_page.get_by_placeholder("Username").fill(
        "standard_user"
    )

    login_page.get_by_placeholder("Password").fill(
        "secret_sauce"
    )

    login_page.get_by_role(
        "button", name="Login"
    ).click()

    # Verify successful login
    expect(login_page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        login_page.get_by_text("Products", exact=True)
    ).to_be_visible()


def test_invalid_login(login_page: Page):

    login_page.get_by_placeholder("Username").fill(
        "standard_user"
    )

    login_page.get_by_placeholder("Password").fill(
        "wrong_password"
    )

    login_page.get_by_role(
        "button", name="Login"
    ).click()

    # Verify invalid login error
    error = login_page.locator('[data-test="error"]')

    expect(error).to_be_visible()

    expect(error).to_contain_text(
        "Username and password do not match"
    )
