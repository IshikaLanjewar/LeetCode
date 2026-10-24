
from pathlib import Path
from typing import Iterator

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


LOGIN_PAGE = Path(__file__).with_name("login.html").resolve().as_uri()


@pytest.fixture
def browser() -> Iterator[webdriver.Chrome]:
    """Start a fresh Chrome browser for a test and always close it afterward."""
    driver = webdriver.Chrome()

    try:
        driver.get(LOGIN_PAGE)
        yield driver
    finally:
        driver.quit()


def submit_login(
    browser: webdriver.Chrome,
    username: str,
    password: str,
) -> str:
    """Enter credentials, submit the form, and return the displayed message."""

    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "password").send_keys(password)
    browser.find_element(By.ID, "loginBtn").click()

    message = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    WebDriverWait(browser, 5).until(
        lambda _driver: message.text.strip() != ""
    )

    return message.text.strip()


def test_login_with_valid_credentials_shows_success(
    browser: webdriver.Chrome,
) -> None:
    """Valid credentials display the success message."""

    assert submit_login(
        browser, "admin", "admin123"
    ) == "Login successful!"


def test_login_with_invalid_credentials_shows_error(
    browser: webdriver.Chrome,
) -> None:
    """Incorrect credentials display the invalid-credentials message."""

    assert submit_login(
        browser, "admin", "wrong123"
    ) == "Invalid username or password."


def test_login_with_empty_credentials_shows_required_message(
    browser: webdriver.Chrome,
) -> None:
    """Empty username and password display the required-fields message."""

    assert submit_login(
        browser, "", ""
    ) == "Please enter username and password."
