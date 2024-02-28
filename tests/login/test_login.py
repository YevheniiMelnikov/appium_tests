import os
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

load_dotenv()


def assert_login_successful(login_page):
    assert login_page.find_element(
        by=AppiumBy.XPATH,
        value='//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
    )


def assert_login_failed(login_page):
    with pytest.raises(NoSuchElementException):
        login_page.find_element(
            by=AppiumBy.XPATH,
            value='//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
        )
        

@pytest.mark.parametrize(
    "email, password, expected",
    [
        (os.getenv("EMAIL"), os.getenv("PASSWORD"), "success"),
        ("mail@gmail.com", "123456", "failure"),
        ("some_email@gmail.com", "qwerty", "failure"),
        ("", "password", "failure"),
    ],
)
def test_user_login(user_login_fixture, email, password, expected):
    login_page = user_login_fixture
    login_page.click_element(login_page.login_button())
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_element(login_page.submit_button())
    time.sleep(5)
    
    match expected:
        case "success":
            assert login_page.find_element(
                by=AppiumBy.XPATH,
                value='//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
            )
        case "failure":
            with pytest.raises(NoSuchElementException):
                login_page.find_element(
                    by=AppiumBy.XPATH,
                    value='//android.widget.ImageView[@resource-id="com.ajaxsystems:id/menuDrawer"]'
                )
