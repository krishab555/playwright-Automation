from playwright.sync_api import sync_playwright, expect
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com", wait_until="domcontentloaded")
        print("Website opened successfully")

        page.click("text=Products")
        time.sleep(1)
        print("Navigated to Products page")

        Viewproduct = page.locator("a[href='/product_details/1']")
        Viewproduct.wait_for(state="visible", timeout=10000)
        Viewproduct.scroll_into_view_if_needed()
        time.sleep(2)
        Viewproduct.click()
        print("Clicked on the view product")
        time.sleep(2)

        browser.close()

if __name__ == "__main__":
    run()
