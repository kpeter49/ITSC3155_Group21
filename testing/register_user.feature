Feature: Register a user
    As a user, it will be beneficial to create a user, as I will be able to contribute and post questions with my own personal username and account, and everyone will know who I am.
Scenario: I want to be able to register so I can ask questions
    Given I don’t already have an account
    And I am on the “sign-in” screen
    When I click the “Create Account” link
    Then it should redirect me to the “create account” page
    When I input my username into the “username” text field
    And I input my password into the “password” text field
    And I press the “register” button
    Then my account should be created
    And I should be redirected to the “list questions/posts” page
