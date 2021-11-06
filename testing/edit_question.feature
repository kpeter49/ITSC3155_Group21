Feature: Edit a question/post
    As a student user, I want to be able to edit my question/post so that I can fix errors in my post or add details to my question that I didn’t include in the initial post
    As an instructor user, I want to be able to edit my post so that I can update announcements in my class to reflect changes as they happen.
Scenario: Editing an existing post in the forum
    Given I am logged in
    And I am the original author of the post
    When I select the post
    And I click the edit button
    And I enter my changes to the description field
    And I click the “Post Edit” button
    Then I get redirected to the class page
    And the post gets updated in the database
    And I can see my new changes when I open the post
