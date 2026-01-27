from playwright.sync_api import sync_playwright
import time     

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")

        page.click("text= Signup / Login")
        print("Navigated to Signup / Login page")
        time.sleep(2)

        email = "krisha@123.com"
        password = "Kri123"
        page.fill("input[data-qa='login-email']", email)
        page.fill("input[data-qa='login-password']", password)  
        page.click("button[data-qa='login-button']")
        print("Login successful")
        time.sleep(2)

        browser.close()
if __name__ == "__main__":
    run()
         