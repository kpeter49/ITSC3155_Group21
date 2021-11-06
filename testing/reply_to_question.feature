Feature: Reply to a question/post
    As a user, I want to be able to reply to a question/post someone made so that I can answer their question.
    As an instructor, I would like to be able to reply to a question/post so that I can answer one of my students' questions.
Scenario: Replying to a post in the forum
    Given that a post has been selected
    And that there is a post available to reply to
    And I click the “Reply” Button
    And I enter my comments or answer to the description field
    And I click “Send”
    Then I get redirected to the class page
    And the post gets updated in the database
