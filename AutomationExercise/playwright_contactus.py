from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://automationexercise.com")
        time.sleep(2)

        # contact us
        page.click("text=Contact Us")
        time.sleep(2)
        print("Contact Us form opened")

        page.fill("input[name='name']", "krisha Bhandari")
        page.fill("input[name='email']", "krisha@example.com")
        page.fill("input[name='subject']", "Inquiry about services")    
        page.fill("textarea[name='message']", "Hello, I would like to inquire about...")
        time.sleep(3)

        submit_btn = page.locator("input[data-qa='submit-button']")

        submit_btn.scroll_into_view_if_needed()
        submit_btn.wait_for(state="visible", timeout=10000)

        page.on("dialog", lambda dialog: dialog.accept())

        submit_btn.click()
        print("Submit button clicked")

        page.wait_for_selector(
            "text=Success! Your details have been submitted successfully.",
            timeout=5000
        )
        print("Contact Us form submitted successfully!")

        time.sleep(2)
        browser.close()

if __name__ == "__main__":
    run()
