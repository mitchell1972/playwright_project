import time

from behave import given, when, then

from pages import home_page
from pages.home_page import HomePage
from pages.pagination_utility import PaginationUtility


@given('the user is on the compare the market home page')
def step_user_is_on_home_page(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate_to_comparethemarket_homepage()
    expected_url = "https://www.comparethemarket.com/"
    current_url = context.page.url
    assert expected_url in current_url, f"Expected URL to be {expected_url}, but got {current_url}"


@when('the user clicks on find my vehicle button')
def step_user_clicks_find_my_vehicle(context):
    context.home_page.click_find_my_vehicle_button()


@then('the vehicle details page is opened')
def step_vehicle_details_page_opens(context):
    assert context.home_page.is_vehicle_details_page_open(), "Vehicle details page did not open."


@when('the user searches for the registration "{registration}"')
def step_user_searches_for_registration(context, registration):
    context.home_page.click_compare_car_insurance_button()
    context.home_page.fill_car_registration_field(registration)
    #time.sleep(1)


@then('all job listings with the title "test automation" should be displayed')
def step_jobs_with_title_displayed(context):
    assert context.job_listings_page.are_jobs_with_title_displayed("test automation"), \
        "Listings with the title 'test automation' are not displayed."


@when('the user sets a filter on the sidebar')
def step_user_sets_filter(context):
    context.job_listings_page.set_filter()


@then('the job listings should be updated to reflect the filters set')
def step_listings_reflect_filters(context):
    assert context.job_listings_page.do_listings_reflect_filters(), "Listings do not reflect the filters set."


@when('the user clicks on the pagination control for the next page')
def step_user_clicks_pagination_next(context):
    context.job_listings_page.go_to_next_page()


@then('the user should be taken to the corresponding page of job listings')
def step_user_is_on_correct_page(context):
    assert context.job_listings_page.is_on_correct_page(), "User is not on the correct page."


@given('the user is on the first page of job listings')
def step_user_is_on_first_page_of_job_listings(context):
    PaginationUtility.navigate_to_first_page(context.page)
