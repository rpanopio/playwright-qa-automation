
# Python Playwright QA Automation Framework

A hands-on QA automation project using Python, Playwright,
Pytest, and the Page Object Model (POM).

## Technologies

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Pytest Fixtures
- Parameterized Testing
- HTML Reporting
- Environment Variables

## Automated Test Coverage

- Login: Positive and negative scenarios
- Product inventory verification
- Add to cart
- Remove from cart
- Checkout workflow
- Negative checkout validation
- Smoke and regression testing

## Practice Application

https://www.saucedemo.com/

## Installation

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install the required Python packages.
4. Install Playwright Chromium.
5. Create a local .env file with the required test configuration.

## Running Tests

Run all tests:

    python -m pytest

Run smoke tests:

    python -m pytest -m smoke

Run regression tests:

    python -m pytest -m regression

## Reporting

The framework supports pytest-html reports,
Playwright screenshots, and traces for debugging.

## Project Purpose

This project demonstrates practical skills in Python
QA automation and test framework development.
