Feature: Pinning question/post
    As an instructor, I want to be able to pin a post to signify its importance.
Scenario: I want to be able to pin important messages to the class
    Given that there is a post available to be pinned
    When I press the pin icon
    Then the post should be added to a group of pinned posts at the top of the page
