import os
from selenium import webdriver
import settings
import platform

CURRENT_DIR = os.getcwd()


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(CURRENT_DIR + settings.CHROME_DRIVER_PATH[platform.system()])


def after_scenario(context, scenario):
    context.driver.quit()