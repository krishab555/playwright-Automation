from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com", )
        print("Website opened successfully")

        page.click("text=Products")
        print("Navigated to Products page")

        view_product = page.locator("a[href='/product_details/1']")
        view_product.wait_for(state="visible", timeout=100)
        view_product.click()
        print("Clicked on the view product")
        
        page.click("text=Add to Cart")
        print("Clicked on Add to Cart button")
        time.sleep(3)

if __name__ == "__main__":
    run()