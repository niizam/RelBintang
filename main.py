import os
import json
import time
from playwright.sync_api import sync_playwright

def parse_cookies(cookie_str, domain, path):
    cookies = []
    for cookie in cookie_str.split(";"):
        name, value = cookie.strip().split("=", 1)
        cookies.append({"name": name, "value": value, "domain": domain, "path": path})
    return cookies

def run(playwright, cookies_str):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Parse the COOKIES string from the environment variable and add domain and path
    cookies = parse_cookies(cookies_str, ".hoyolab.com", "/")

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
    
    #Genshin
    page.goto("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481")
    time.sleep(3)
    x = page.locator(".components-home-assets-__sign-guide_---guide-close---2VvmzE")
    if x.is_visible():
        x.click()

    for div in page.query_selector_all(".components-home-assets-__sign-content_---sign-item---k8WFIr"):
        div.click()
        
    context.close()
    browser.close()
    
    # Evaluate JavaScript code and log the result
#    check = page.locator(".m-dialog-body")
#    if check.is_visible():
#        text = page.evaluate('document.querySelector(".m-dialog-body").textContent.trim()')
#        print(text)
#        context.close()
#        browser.close()
#    else:
#        # Close the browser
#        context.close()
#        browser.close()

with sync_playwright() as playwright:
    cookies_env = os.environ['COOKIES']
    try:
        cookies_list = json.loads(cookies_env)
        if isinstance(cookies_list, list):
            for cookies_str in cookies_list:
                run(playwright, cookies_str)
        else:
            raise ValueError
    except ValueError:
        run(playwright, cookies_env)
