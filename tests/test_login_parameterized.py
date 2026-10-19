
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.parametrize(
    "username,password,expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("standard_user", "wrong_password", "invalid"),
        ("invalid_user", "secret_sauce", "invalid"),
        ("", "secret_sauce", "username_required"),
        ("standard_user", "", "password_required"),
    ],
)
def test_login_scenarios(
    page: Page, username, password, expected_result
):
    # Step 1: Navigate to the website
    page.goto("https://saucedemo.com/")

    # Step 2: Enter username
    page.get_by_placeholder("Username").fill(username)

    # Step 3: Enter password
    page.get_by_placeholder("Password").fill(password)

    # Step 4: Click Login
    page.get_by_role("button", name="Login").click()

    # Debugging information
    print("Current URL:", page.url)
    print(
        "Error message:",
        page.locator('[data-test="error"]').all_text_contents()
    )

    # Step 5: Verify expected result
    if expected_result == "success":
        expect(page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )

        expect(
            page.get_by_text("Products", exact=True)
        ).to_be_visible()

    else:
        error = page.locator('[data-test="error"]')
        expect(error).to_be_visible()

        if expected_result == "invalid":
            expect(error).to_contain_text(
                "Username and password do not match"
            )

        elif expected_result == "username_required":
            expect(error).to_contain_text(
                "Username is required"
            )

        elif expected_result == "password_required":
            expect(error).to_contain_text(
                "Password is required"
            )

        # Verify user remains on login page
        expect(page).to_have_url(
            "https://www.saucedemo.com/"
        )
