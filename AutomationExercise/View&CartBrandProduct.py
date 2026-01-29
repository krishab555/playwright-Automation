from playwright.sync_api import sync_playwright
import time 
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        time.sleep(2)

        page.click("text= Products")
        print("Navigated to Products page")
        time.sleep(2)

        side_bar = page.locator("text=Brand")
        side_bar.scroll_into_view_if_needed()
        print("Scrolled to Brand section......")
        time.sleep(3)

        click_brand = page.locator("a[href='/brand_products/H&M']")
        click_brand.scroll_into_view_if_needed()
        click_brand.click()
        print("Clicked on H&M brand")
        time.sleep(3)
        browser.close()

if __name__ == "__main__":
    run()   