Feature: View a question/post
    As a student user, I want to be able to view the question/post that I have sent.
    As an instructor user, I want to be able to view any questions that were posted so that I can give important information that will answer the question.
Scenario: Viewing a specific question and its details
    Given that the student and instructor are members of a class
    When I click on the note title
    Then I should be able to view the note’s details, including the title, text, date, and the user that posted the question
    Create a question/post
    As a student user, I want to be able to write a question on an application so that instructors or other students can answer or respond to my question
    As an instructor user, I want to be able to write a post so that I can communicate important information to the class
Scenario: Adding a post to the forum
    Given I am logged in
    And I am a member of a class
    When I click on the post button
    And I fill the field for the post title
    And I fill the field for post description
    Then I get redirected to the class page
    And a post gets added to the database
    And I can see my post on the class page
