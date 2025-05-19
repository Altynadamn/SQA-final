Feature: Login to StackOverflow

  Scenario: User opens the login page
    Given I open the StackOverflow login page
    When I enter the username 'email@gmail.com' and password 'password'
    And I click the login button
    Then I should be successfully logged into the site
