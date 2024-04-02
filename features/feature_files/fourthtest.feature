Feature: Applying for a Job
  In order to apply for a job
  As a user
  I want to click the apply button on a job listing

  Scenario: User clicks apply on a job listing after searching for 'test automation'
    Given the user is on the compare the market home page
    When the user searches for the registration "WF18KZS"
    And the user clicks on find my vehicle button
    Then the vehicle details page is opened



#  Scenario: User views their job basket
#    Given the user has added jobs to their basket
#    When the user clicks on the "View Basket" button
#    Then all selected jobs should be displayed in the basket


  Scenario: User searches for a job title
    Given the user is on the job listings page
    When the user searches for "test automation"
    Then all job listings with the title "test automation" should be displayed


  Scenario: User refines job search
    Given the user is on the job listings page
    When the user sets a filter on the sidebar
    Then the job listings should be updated to reflect the filters set


#  Scenario: User navigates to a different page
#    Given the user is on the first page of job listings
#    When the user clicks on the pagination control for the next page
#    Then the user should be taken to the corresponding page of job listings
