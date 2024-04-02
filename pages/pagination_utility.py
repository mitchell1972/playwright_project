from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


class PaginationUtility:

    @staticmethod
    def navigate_to_first_page(browser):
        try:
            first_page_button = browser.find_element_by_xpath("//a[text()='1']")
            active_page = browser.find_element_by_xpath("//a[@class='active']")

            if first_page_button != active_page:
                first_page_button.click()
                time.sleep(3)

            active_page = browser.find_element_by_xpath("//a[@class='active']")
            if active_page.text != '1':
                raise AssertionError("Not on the first page of job listings after clicking.")

        except NoSuchElementException:
            # If the first page button is not found, assume we're on the first page
            # or there is only one page.
            pass
