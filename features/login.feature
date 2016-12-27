Feature: test log in function

  Scenario: Test login with regular user
    Given Login page is opened
    When Regular user logs in
    Then Default page is displayed

  Scenario: Login to system with incorrect email
    Given Login page is opened
    When I enter email incorrect_email@ukr.net into Email field
    And I enter password please into Password field
    And I press 'Sign in' button
    Then Error message Invalid email or password. will appear on Login page

  Scenario: Login to system with incorrect password
    Given Login page is opened
    When I enter email afrider@intelliarts.com into Email field
    And I enter password please1 into Password field
    And I press 'Sign in' button
    Then Error message Invalid email or password. will appear on Login page


