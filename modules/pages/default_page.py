from selenium.webdriver.common.by import By
from modules.base_element import BaseElement
import settings


class DefaultPage(object):
    def __init__(self, driver):
        self.monday_button = BaseElement(By.XPATH, ".//*[@id='user-menus-region']//div[@class='week-day'][contains(text(), 'Monday')]", driver)
        self.tuesday_button = BaseElement(By.XPATH, ".//*[@id='user-menus-region']//div[@class='week-day'][contains(text(), 'Tuesday')]", driver)
        self.wednesday_button = BaseElement(By.XPATH, ".//*[@id='user-menus-region']//div[@class='week-day'][contains(text(), 'Wednesday')]", driver)
        self.thursday_button = BaseElement(By.XPATH, ".//*[@id='user-menus-region']//div[@class='week-day'][contains(text(), 'Thursday')]", driver)
        self.friday_button = BaseElement(By.XPATH, ".//*[@id='user-menus-region']//div[@class='week-day'][contains(text(), 'Friday')]", driver)
        self.friday_button.wait_element()