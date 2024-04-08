import base64
import os
from playwright.sync_api import sync_playwright
from allure_commons.types import AttachmentType
import allure


def before_all(context):
    try:
        playwright = sync_playwright().start()
        context.browser = playwright.chromium.launch(headless=False)
        context.context = context.browser.new_context()
        print("Browser launched in non-headless mode.")
    except Exception as e:
        print(f"An error occurred while launching the browser: {e}")


def before_scenario(context, scenario):
    context.page = context.context.new_page()


def after_step(context, step):
    if step.status == "failed":
        # Assuming `context.page` is your Playwright page instance
        screenshot_bytes = context.page.screenshot()
        # Attach the screenshot to Allure results
        allure.attach(screenshot_bytes, name="screenshot", attachment_type=AttachmentType.PNG)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        # Ensure the screenshots directory exists
        if not os.path.exists('screenshots'):
            os.makedirs('screenshots')

        # Replace any characters in the scenario name that might be invalid in a file name
        filename = scenario.name.replace(' ', '_').replace('/', '_').replace('\\', '_') + '.png'
        screenshot_path = f"screenshots/{filename}"
        context.page.screenshot(path=screenshot_path)
        print(f"Screenshot taken for failed scenario: {scenario.name}")

    # Close the current page after each scenario
    context.page.close()


def after_all(context):
    context.browser.close()
