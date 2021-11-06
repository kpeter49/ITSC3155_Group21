Feature: Delete a question/post
    As a student, I want to be able to delete a question/post that I made in the event that I no longer need assistance with a problem.
Scenario: Deleting a post
    Given I have a post
    When I click on the trash icon
    Then I should see a confirmation to delete prompt
    When I confirm to delete the post
    Then the post should be deleted
