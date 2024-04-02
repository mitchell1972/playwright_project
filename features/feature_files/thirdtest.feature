Feature: Job Listings Sorting
  In order to sort job listings
  As a user
  I want to select different sorting options

  Scenario Outline: User sorts the job listings
    Given the user is on the job listings page
    When the user selects to sort by "<sort_option>"
    Then the job listings should be sorted by "<sort_option>"

    Examples:
      | sort_option |
      | Best Match  |
      | Date Posted |