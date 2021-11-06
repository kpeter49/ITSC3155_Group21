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
