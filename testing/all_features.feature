Feature: List questions/posts
    As a student user, I want to be able to list all the questions that I have posted.
Scenario: As a user, I want to be able to view all note entries that I posted
    Given that I am on the home page
    When I click on the “My Notes” link
    Then I should be on the “My Notes” page
    And I should be able to see a list of notes that I have posted

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

Feature: Delete a question/post
    As a student, I want to be able to delete a question/post that I made in the event that I no longer need assistance with a problem.
Scenario: Deleting a post
    Given I have a post
    When I click on the trash icon
    Then I should see a confirmation to delete prompt
    When I confirm to delete the post
    Then the post should be deleted

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

Feature: User sign-in
    When using a service, having a sign-in is preferred, as I can personalize the site my own way, either by having my own saved/followed people or accounts, as well as being able to design and customize my own account. The sign-in is the first step into the process, letting me protect my account with a password.
Scenario: Signing into an already existing account
    Given I am on the “sign-in page”
    When I input the username into the “username” text field
    And I input the password into the “password” text field
    And I press the “sign-in” button
    Then I should be signed in
    And I should be redirected to the “list questions/posts” page

Feature: Filtering
    As a user, I would like to filter responses that fall under a certain category so that I can get the best possible explanation of the answer.
Scenario:
    Given I am on the "list questions/posts" page
    And I am signed in
    When I enter text into the filter textbox
    And I click the "filter" button
    Then I should only see questions or posts containing the text in the filter textbox

Feature: Attaching an image to question/post
    As a student user, I want to be able to include images in my questions/posts so that I can give examples of what I am posting about instead of trying to describe all of the details with text only
Scenario: Uploading an image file to a post
    Given that I am on the post creation screen
    And I have a valid image file
    When I click the add image button
    And I select the image file I am uploading
    And I click the “Upload” button
    And I click the “Post” button
    Then I am redirected to the class page
    And I can see the new post
    And I can see my image attached to the post

Feature: User log
    As a user, the user log has very little importance to me, however, I will be part of this log in the grand scheme of the database, and be able to view my prior history and viewed questions. For the creators of the app, this is useful as they can find any information necessary from my account.
Scenario: Viewing my prior history on the server
    Given that a user or multiple users have posted notes and replies
    When I click on the “server history” link
    Then I should see the database of important information

Feature: Pinning question/post
    As an instructor, I want to be able to pin a post to signify its importance.
Scenario: I want to be able to pin important messages to the class
    Given that there is a post available to be pinned
    When I press the pin icon
    Then the post should be added to a group of pinned posts at the top of the page
