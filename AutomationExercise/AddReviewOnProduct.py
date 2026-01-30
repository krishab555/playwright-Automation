from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        time.sleep(2)


        page.click("a[href='/products']")
        print("Navigated to Products page")
        time.sleep(2)

        page.click("a[href='/product_details/1']")
        print("Clicked on the view product")
        time.sleep(2)

        page.locator("#reviews").scroll_into_view_if_needed()
        print("Scrolled to Reviews section")
        time.sleep(2)

        page.fill("input[id='name']", "Krisha")
        page.fill("input[id='email']", "krisha@example.com")
        page.fill("textarea[id='review']", "This is a great product!")
        page.click("button[type='submit']")
        print("Review submitted successfully")
        time.sleep(2)

if __name__ == "__main__":  
    run()
