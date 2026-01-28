#Register user using existing email.
from playwright.sync_api import sync_playwright
import time
def run():
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
    
            page.goto("http://automationexercise.com") #open website
            time.sleep(2)
    
            page.click("text=Signup / Login")   
            time.sleep(2)
    
            name = "Krisha"       #enter name email
            email = "krisha@123.com"
    
            page.fill("input[data-qa='signup-name']", name)
            page.fill("input[data-qa='signup-email']", email)
    
            # Click Signup
            page.click("button[data-qa='signup-button']")
            page.wait_for_selector("input[id='password']", timeout=300)
            print("Signup page loaded")
            time.sleep(2)

            browser.close()

if __name__ == "__main__":
    run() 