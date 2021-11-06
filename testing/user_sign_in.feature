Feature: User sign-in
    When using a service, having a sign-in is preferred, as I can personalize the site my own way, either by having my own saved/followed people or accounts, as well as being able to design and customize my own account. The sign-in is the first step into the process, letting me protect my account with a password.
Scenario: Signing into an already existing account
    Given I am on the “sign-in page”
    When I input the username into the “username” text field
    And I input the password into the “password” text field
    And I press the “sign-in” button
    Then I should be signed in
    And I should be redirected to the “list questions/posts” page
