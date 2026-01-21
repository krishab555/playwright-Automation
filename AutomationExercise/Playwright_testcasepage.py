from playwright.sync_api import sync_playwright, expect
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com", wait_until="domcontentloaded")
        print("Website opened successfully")
        
        page.click("text=Test Cases")   
        print("Navigated to Test Cases page")
        
        time.sleep(2)

        browser.close()

if __name__ == "__main__":
    run()
