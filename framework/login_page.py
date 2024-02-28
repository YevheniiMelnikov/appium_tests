from appium.webdriver import WebElement
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains

from utils import components
from .page import Page


class LoginPage(Page):

    def login_button(self) -> WebElement:
        return self.find_element(AppiumBy.XPATH, components.login_button)

    def email_field(self) -> WebElement:
        return self.find_element(AppiumBy.XPATH, components.email_field)

    def password_field(self) -> WebElement:
        return self.find_element(AppiumBy.XPATH, components.password_field)
    
    def submit_button(self) -> WebElement:
        return self.find_element(AppiumBy.XPATH, components.submit_button)
    
    def click_element(self, element: WebElement) -> None:
        element.click()
    
    def enter_email(self, email: str) -> None:
        self.click_element(self.email_field())
        actions = ActionChains(self.driver)
        actions.send_keys(email)
        actions.perform()
    
    def enter_password(self, password: str) -> None:
        self.click_element(self.password_field())
        actions = ActionChains(self.driver)
        actions.send_keys(password)
        actions.perform()
        