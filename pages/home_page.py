import time

from playwright.sync_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_comparethemarket_homepage(self):
        self.page.goto("https://www.comparethemarket.com/")
        self.page.wait_for_load_state('networkidle')

    def click_compare_car_insurance_button(self):
        accept_button_selector = 'text="Accept all cookies"'
        # Wait for the selector to be available before clicking
        self.page.wait_for_selector(accept_button_selector)
        self.page.click(accept_button_selector)
        self.page.click('text="Compare car insurance"')

    def fill_keywords_search_field(self, search_query):
        input_xpath = '//*[@id="keywords"]'
        self.page.fill(f'xpath={input_xpath}', search_query)

    def fill_car_registration_field(self, registration_number):
        input_xpath = '//*[@id="CarInsurance_YourVehicle_VehicleLookup_RegistrationNumber"]'
        self.page.wait_for_selector('//*[@id="CarInsurance_YourVehicle_VehicleLookup_RegistrationNumber"]',
                                    state='attached')
        is_visible = self.page.is_visible(input_xpath)
        print(f"The car registration input field visibility status is: {is_visible}")
        self.page.screenshot(path='screenshot.png')
        if is_visible:
            self.page.type(input_xpath, registration_number)
            print(f"Filled in the car registration number: {registration_number}")

    def click_find_my_vehicle_button(self):
        # Selector for the 'Find vehicle' button
        button_selector = 'text="Find vehicle"'

        # Wait for the button to be in the DOM and visible
        is_visible = self.page.is_visible(button_selector)

        # Print the visibility status
        print("Is the 'Find vehicle' button visible:", is_visible)

        if not is_visible:
            raise AssertionError(f"The button with selector '{button_selector}' is not visible.")

        # Click on the button
        self.page.click(button_selector)
        time.sleep(0.5)

    def click_apply_button(self):
        self.page.click('text="Apply"')

    def is_application_form_open(self):
        return self.page.is_visible("form.application-form")

    def add_jobs_to_basket(self):
        self.page.click('button:has-text("Add to Basket")')

    def view_basket(self):
        self.page.click('text="View Basket"')

    def are_jobs_displayed_in_basket(self):
        return self.page.is_visible("ul.jobs-in-basket")

    def print_all_text_from_page(self):
        text_content = self.page.inner_text('body')
        print(text_content)

    def are_jobs_with_title_displayed(self, job_title):
        search_results = self.page.inner_text('div.search-results')
        return job_title in search_results

    def set_filter(self):
        self.page.check('input[name="full-time"]')
        self.page.wait_for_selector('div.search-results')

    def do_listings_reflect_filters(self):
        self.page.wait_for_selector('div.search-results:not(.loading)')
        return True

    def go_to_next_page(self):
        self.page.click('text="Next"', timeout=5000)

    def is_on_correct_page(self):
        current_url = self.page.url
        return 'page=2' in current_url or self.page.is_visible('a.pagination-current[aria-current="page"]')

    def is_vehicle_details_page_open(self):
        # Text that uniquely identifies the Vehicle Details page
        unique_text = "We’ve found your vehicle."

        # Wait for the text to be visible on the page
        is_unique_text_visible = self.page.is_visible(f"text='{unique_text}'")

        # Check for other unique elements like registration number or button, etc.
        is_registration_visible = self.page.is_visible("text='WF18KZS'")
        are_details_correct_buttons_visible = self.page.is_visible("text='Yes'") and self.page.is_visible("text='No'")

        # If all unique elements are visible, return True, otherwise return False
        return is_unique_text_visible and is_registration_visible and are_details_correct_buttons_visible
