Feature: Navigation Tabs Functionality
  In order to navigate to different sections of the site
  As a user
  I want to use navigation tabs

  Scenario Outline: User clicks on a navigation tab
    Given the user is on the dashboard page
    When the user clicks on the "<tab>" tab
    Then the user should be taken to the "<page>" page

    Examples:
      | tab        | page       |
      | Job Search | Job Search |
      | My Account | My Account |
      | Settings   | Settings   |
      | Listings   | Listings   |
      | Help       | Help       |
