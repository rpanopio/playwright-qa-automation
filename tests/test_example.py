from playwright.sync_api import Page, expect

def test_example_website_title(page: Page):
    # Step 1: Navigate to the website
    page.goto("https://example.com")

    # Step 2: Verify the page title
    expect(page).to_have_title("Example Domain")