Feature: Filtering
    As a user, I would like to filter responses that fall under a certain category so that I can get the best possible explanation of the answer.
Scenario:
    Given I am on the "list questions/posts" page
    And I am signed in
    When I enter text into the filter textbox
    And I click the "filter" button
    Then I should only see questions or posts containing the text in the filter textbox
