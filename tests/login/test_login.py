import os
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from dotenv import load_dotenv

from utils.android_utils import android_get_desired_capabilities
from utils.components import wrong_creds_message, add_hub_button

load_dotenv()


@pytest.mark.parametrize(
    "email, password, expected_element",
    [
        ("mail@gmail.com", "123456", wrong_creds_message),
        (os.getenv("EMAIL"), os.getenv("PASSWORD"), add_hub_button),
    ],
)
def test_login(user_login_fixture, email, password, expected_element):
    login_page = user_login_fixture
    if login_page.driver.session_id:
        login_page.driver.quit()
    login_page.driver.start_session(android_get_desired_capabilities())  # TODO:FIND BETTER WAY TO AVOID InvalidSessionIdException

    login_page.click_element(login_page.login_button())
    login_page.enter_email(email)
    login_page.enter_password(password)
    login_page.click_element(login_page.submit_button())
    time.sleep(5)
    
    assert login_page.find_element(by=AppiumBy.XPATH, value=expected_element)
