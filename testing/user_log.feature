Feature: User log
    As a user, the user log has very little importance to me, however, I will be part of this log in the grand scheme of the database, and be able to view my prior history and viewed questions. For the creators of the app, this is useful as they can find any information necessary from my account.
Scenario: Viewing my prior history on the server
    Given that a user or multiple users have posted notes and replies
    When I click on the “server history” link
    Then I should see the database of important information
