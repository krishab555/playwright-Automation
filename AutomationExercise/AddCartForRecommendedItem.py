from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        time.sleep(2)

        scroll_target = page.locator("text=Recommended items")
        scroll_target.scroll_into_view_if_needed()
        print("Scrolled to Recommended items section")
        time.sleep(2)

        recommended_item = page.locator("div[class='recommended_items'] div[class='item active'] div[class='col-sm-4']").first
        recommended_item.hover()
        print("Hovered over the first recommended item")
        time.sleep(2)
        recommended_item.locator("text=Add to cart").click()
        print("Clicked on Add to Cart for the recommended item")
        time.sleep(3)

        page.locator("text=View Cart").click()
        print("Navigated to Cart page")
        time.sleep(3)

if __name__ == "__main__":
    run()
