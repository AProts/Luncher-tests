from selenium.webdriver.common.by import By
from modules.base_element import BaseElement
import settings


class LoginPage(object):
    def __init__(self, driver):
        self.sign_in_button = BaseElement(By.CSS_SELECTOR, '.submit-button.btn', driver)
        self.email_field = BaseElement(By.ID, 'user_email', driver)
        self.password_field = BaseElement(By.ID, 'user_password', driver)
        self.error_message = BaseElement(By.CSS_SELECTOR, '.alert.alert-warning', driver)
        self.remember_me_checkbox = BaseElement(By.ID, 'user_remember_me', driver)
        self.sign_in_button.wait_element()