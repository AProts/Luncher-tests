"""
Base Element page object
"""
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
import settings


def stale(func):
    def wrapper(base_element, waitajax=settings.WAIT_CONST, wait_ajax_for_wait_element = True):
        wait = 10
        for i in xrange(1, wait):
            try:
                return func(base_element, waitajax, wait_ajax_for_wait_element)
            except StaleElementReferenceException:
                sleep(1)  # wait because page is loading and element reference is stale
                print('Stale exception occurred. %s attempt.' % i)
                if i >= wait:
                    raise Exception("Stale. Can't wait following element on page %s = %s"
                                    % (base_element.by, base_element.value))
    return wrapper


class BaseElement(object):
    def __init__(self, by, value, driver):
        self.drv = driver
        self.by = by
        self.value = value

    def web_element(self):

        """
        Get web_element and return reference to it
        """
        return self.drv.find_element(self.by, self.value)

    def find_child_elements(self, by, value):
        return self.drv.find_elements(by, value)

    def click(self, wait_ajax = True):
        """
        Get element and then click on it
        """
        self.wait_element(wait_ajax_for_wait_element = wait_ajax)
        if wait_ajax:
            self.wait_until_ajax_complete()
        el = self.web_element()
        actions = ActionChains(self.drv)
        actions.move_to_element(el).click(el).perform()

    def send_keys(self, string):
        """
        Send character to the input of the element
        """
        self.wait_element()
        self.web_element().send_keys(string)
        self.wait_until_ajax_complete()

    def get_attribute(self, string):

        self.wait_element()
        return self.web_element().get_attribute(string)


    def is_displayed(self):
        """
        Check if element is displayed
        """
        self.wait_element()
        if self.is_element_hidden():
            return False
        else:
            return True

    def select_drop_down_item_by_text(self, value):
        """
        Select item of the dropdown by text
        """
        self.wait_element()
        sel = Select(self.web_element())
        sel.select_by_visible_text(value)
        self.wait_until_ajax_complete()

    def select_drop_down_item_by_index(self, value):
        """
        Select item of the dropdown by index_value
        """
        self.wait_element()
        sel = Select(self.web_element())
        sel.select_by_index(value)
        self.wait_until_ajax_complete()

    def drop_down_deselect_all(self):
        """
        Deselect all items within dropdown
        """
        self.wait_element()
        sel = Select(self.web_element())
        sel.deselect_all()
        self.wait_until_ajax_complete()

    def select_drop_down_item_by_value(self, value):
        """
        Select item from dropdown by value
        """
        self.wait_element()
        sel = Select(self.web_element())
        sel.select_by_value(value)
        self.wait_until_ajax_complete()
        return sel.first_selected_option.text

    def get_selected_text_from_select(self):
        self.wait_element()
        sel = Select(self.web_element())
        return sel.first_selected_option.text

    @stale
    def wait_element(self, wait=settings.WAIT_CONST, wait_ajax_for_wait_element = True):
        """
        Wait element until it's displayed
        """
        if wait_ajax_for_wait_element:
            self.wait_until_ajax_complete()
        try:
            WebDriverWait(self.drv, wait).until(lambda driver: self.web_element().is_displayed())
        except TimeoutException as e:
            raise Exception("Timeout. Can't wait following element on page --> %s = %s" % (self.by, self.value))

    def wait_element_is_disappeared(self, wait=settings.WAIT_CONST):
        """
        Wait element until it's hidden
        """
        self.wait_until_ajax_complete()
        try:
            WebDriverWait(self.drv, wait).until(lambda driver: self.is_element_hidden())
        except TimeoutException:
            raise Exception("Following element STILL on page -->" + self.by, ' = ' + self.value)

    def is_element_available(self):
        """
        Returns True if element is available
        """
        try:
            self.wait_element()
            web_element = self.web_element()
            if web_element().is_displayed():
                return web_element().is_enabled()
            else:
                return False
        except NoSuchElementException:
            raise Exception("Can't find following element on page -->" + self.by + ' = ' + self.value)

    def is_element_hidden(self):
        """
        Returns True if element is hidden
        """
        try:
            self.wait_element()
            self.web_element()
        except NoSuchElementException:
            return True
        return False

    def is_element_shown(self):
        """
        Returns True if element is hidden
        """
        try:
            self.wait_element()
            self.web_element()
        except NoSuchElementException:
            return False
        return True

    def is_element_checked(self):
        """
        Returns True if element is checked
        """
        self.wait_element()
        if self.web_element().get_attribute("checked") is None:
            return False
        else:
            return True

    def text(self):
        """
        Return the text_value of the element
        """
        self.wait_element()
        return self.web_element().text

    def clear(self):
        """
        Clears the text field
        """
        self.wait_element()
        clear = self.web_element().clear()
        self.wait_until_ajax_complete()
        return clear

    def wait_until_ajax_complete(self):
        def _ajax_complete(driver):
            try:
                return 0 == driver.execute_script("return jQuery.active")
            except WebDriverException:
                pass

        sleep(0.5)  # wait ajax call
        WebDriverWait(self.drv, settings.WAIT_AJAX_CONST).until(_ajax_complete,  "Timeout waiting for ajax load")



