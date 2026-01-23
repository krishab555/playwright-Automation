from playwright.sync_api import sync_playwright
import time 

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")

        page.click("text=Cart")
        print("Navigated to Cart page")
        time.sleep(2)

        scroll_target = page.locator("div[class='footer-widget']")
        scroll_target.scroll_into_view_if_needed()
        print("Scrolled to footer section")
        time.sleep(3)

        email_input = page.locator("#susbscribe_email")
        email_input.click()
        email_input.type("test@example.com", delay=150)  
        time.sleep(1)
        email_input.press("Enter")
        print("Subscription form submitted")
        time.sleep(3)

        browser.close()

if __name__ == "__main__":
    run()