Feature: List questions/posts
    As a student user, I want to be able to list all the questions that I have posted.
Scenario: As a user, I want to be able to view all note entries that I posted
    Given that I am on the home page
    When I click on the “My Notes” link
    Then I should be on the “My Notes” page
    And I should be able to see a list of notes that I have posted
