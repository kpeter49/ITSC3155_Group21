# features for our project
  # Team 21: Connor Frunzi, Karl Peterson, Dalton Propst, Drew Moore
@List Questions/Posts
Scenario Test: List Questions/Posts
  Given that I am on the home page
  When I click on "My Notes" Link
  Then I should be on the “My Notes” page
  And I should be able to see a list of notes that I have posted

@View Question/Post
  Scenario Test: Viewing a specific question and its details
  Given that the student and instructor are members of a class
  When I click on the note title
  Then I should be able to view the note’s details, including the title, text, date, and the user that posted the question

@Create a question/post
  Given I am logged in
  And I am a member of a class
  When I click on the post button
  And I fill the field for the post title
  And I fill the field for post description
  Then I get redirected to the class page
  And a post gets added to the database
  And I can see my post on the class page

@Edit a question/post
  Scenario Test: Adding question to forum
  Given that I am logged in
  And I am the original author of the post
  When I select the post
  And I click the edit button
  And I enter my changes to the description field
  And I click the “Post Edit” button
  Then I get redirected to the class page
  And the post gets updated in the database
  And I can see my new changes when I open the post

@Reply to a question/post
  Given that a post has been selected
  And that there is a post available to reply to
  And I click the “Reply” Button
  And I enter my comments or answer to the description field
  And I click “Send”
  Then I get redirected to the class page
  And the post gets updated in the database

@Delete a question/post
  Scenario Test: Deleting a question/post
  Given I have a post
  When I click on the trash icon
  Then I should see a confirmation to delete prompt
  When I confirm to delete the post
  Then the post should be deleted

@Register a user
  Scenario Test: I want to be able to register so I can ask questions
  Given I don’t already have an account
  And I am on the “sign-in” screen
  When I click the “Create Account” link
  Then it should redirect me to the “create account” page
  When I input my username into the “username” text field
  And I input my password into the “password” text field
  And I press the “register” button
  Then my account should be created
  And I should be redirected to the “list questions/posts” page

@User sign-in
  Scenario Test: Signing into an already existing account
  Given I am on the “sign-in page”
  When I input the username into the “username” text field
  And I input the password into the “password” text field
  And I press the “sign-in” button
  Then I should be signed in
  And I should be redirected to the “list questions/posts” page

@Filtering
  Scenario Test: Filtering responses
  Given that I am on the “My Notes” page
  And I have people reply to my notes
  When I click the "Filter" button or arrow
  Then it should filter and organize responses by a specific category
  And I should see a different arrangement of responses

@Attaching an image to question/post
  Scenario Test: Uploading an image file to a post
  Given that I am on the post creation screen
  And I have a valid image file
  When I click the add image button
  And I select the image file I am uploading
  And I click the “Upload” button
  And I click the “Post” button
  Then I am redirected to the class page
  And I can see the new post
  And I can see my image attached to the post

@User log
  Scenario Test: Viewing my prior history on the server
  Given that a user or multiple users have posted notes and replies
  When I click on the “server history” link
  Then I should see the database of important information

@Pinning question/post
  Scenario Test: I want to be able to pin important messages to the class
  Given that there is a post available to be pinned
  When I press the pin icon
  Then the post should be added to a group of pinned posts at the top of the page
