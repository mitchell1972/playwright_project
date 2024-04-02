Feature: User Sign Out
  In order to maintain security
  As a logged-in user
  I want to be able to sign out and be redirected to the homepage

  Scenario: User clicks the sign-out link
    Given the user is logged in and on the dashboard page
    When the user clicks on the "Sign Out" link
    Then the user should be logged out
    And redirected to the homepage

