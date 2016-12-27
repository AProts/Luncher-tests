from behave import *
import settings
from behave.matchers import step_matcher
from datetime import datetime,timedelta
from modules.pages.login_page import LoginPage
from modules.pages.default_page import DefaultPage

step_matcher('re')


@given('Login page is opened')
def open_login_page(context):
    context.driver.get(settings.HOST)
    context.login_page = LoginPage(context.driver)


@when('(?P<user>.+) user logs in')
def log_in_user(context,user):
    steps = u'''
        When I enter email %s into Email field
        When I enter password %s into Password field
        AND I press 'Sign in' button
        ''' % (settings.USERS[user]['Username'], settings.USERS[user]['Password'])
    context.execute_steps(steps)


@step("I press 'Sign in' button")
def press_sign_in(context):
    context.login_page.sign_in_button.click()


@when("I enter email (?P<email>.+) into Email field")
def enter_email(context, email):
    context.login_page.email_field.send_keys(email)


@when("I enter password (?P<password>.+) into Password field")
def enter_password(context, password):
    context.login_page.password_field.send_keys(password)


@then("Default page is displayed")
def default_page_displayed(context):
    context.default_page = DefaultPage(context.driver)

@then('Error message (?P<message_text>.+) will appear on Login page')
def validate_error_message(context, message_text):
    login_page = LoginPage(context.driver)
    assert login_page.error_message.text()[2:] == message_text



# @then('check cockie')
# def step_impl(context):
#     cookie = context.driver.getCookieNamed('remember_user_token')
#     time_set = cookie['expiry']
#     min_time = (datetime.now()+timedelta(days = 14, minutes = -1))
#     max_time = (datetime.now()+timedelta(days = 14, minutes = 1))
#     expiration_time = datetime.fromtimestamp(time_set)
#     assert min_time < expiration_time < max_time
