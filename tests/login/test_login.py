import os
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv
from selenium.common.exceptions import NoSuchElementException

from utils.android_utils import android_get_desired_capabilities

load_dotenv()


@pytest.mark.parametrize(
    "email, password, expected",
    [
        ("mail@gmail.com", "123456", "failure"),
        (os.getenv("EMAIL"), os.getenv("PASSWORD"), "success"),
    ],
)
def test_login(user_login_fixture, email, password, expected):
    login_page = user_login_fixture
    if login_page.driver.session_id:
        login_page.driver.quit()
    login_page.driver.start_session(android_get_desired_capabilities())  # TODO:FIND BETTER WAY TO AVOID InvalidSessionIdException

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
    