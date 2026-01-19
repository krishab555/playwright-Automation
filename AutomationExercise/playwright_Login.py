#login with correct credentials and delete account
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

        # login details
        page.fill("input[data-qa='login-email']", "krisha@123.com")
        page.fill("input[data-qa='login-password']", "kri123")
        page.click("button[data-qa='login-button']")
        print("Login button clicked")
        time.sleep(2)


        # delete account
        page.click("a[href='/delete_account']")
        page.wait_for_selector("text=Account Deleted!", timeout=30000)
        print("Account Deleted!")
        time.sleep(5) 
         
        browser.close()

if __name__ == "__main__":
    run()


#login with invalid credentials
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

            # invalid login details
            page.fill("input[data-qa='login-email']", "invalid@example.com")
            page.fill("input[data-qa='login-password']", "invalidpassword")
            page.click("button[data-qa='login-button']")
            time.sleep(2)

            browser.close()
if __name__ == "__main__":
      run()
