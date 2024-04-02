from playwright.sync_api import sync_playwright


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


def after_scenario(context, scenario):
    context.page.close()


def after_all(context):
    context.browser.close()
