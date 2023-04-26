import os
import time
from playwright.sync_api import sync_playwright

def parse_cookies(cookie_str, domain, path):
    cookies = []
    for cookie in cookie_str.split(";"):
        name, value = cookie.strip().split("=", 1)
        cookies.append({"name": name, "value": value, "domain": domain, "path": path})
    return cookies

def run(playwright):
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    # Parse the COOKIES string from the environment variable and add domain and path
    cookies = parse_cookies(os.environ['COOKIES'], ".hoyolab.com", "/")

    # Set the cookies
    context.add_cookies(cookies)
    # Open the URL
    page = context.new_page()
    page.goto("https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&lang=en&plat_type=pc")
    #Close the annoying dialog
    time.sleep(3)
    dialog = page.locator(".components-pc-assets-__dialog_---dialog-close---3G9gO2")
    if dialog.is_visible():
        dialog.click()
    # Click the load more
    page.click(".components-pc-assets-__prize-list_---arrow---14hvWv")

    # Click all days to login
    for element in page.query_selector_all(".components-pc-assets-__prize-list_---item---F852VZ"):
        element.click()
    
    # Evaluate JavaScript code and log the result
    check = page.locator(".m-dialog-body")
    if check.is_visible():
        text = page.evaluate('document.querySelector(".m-dialog-body").textContent.trim()')
        print(text)

    # Close the browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
