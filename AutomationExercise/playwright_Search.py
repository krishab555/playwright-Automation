from playwright.sync_api import sync_playwright
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

        search_input = page.locator("input[id='search_product']")
        search_input.wait_for(state="visible", timeout=10000)
        search_input.fill("Tshirt")
        time.sleep(1)

        search_button = page.locator("button[id='submit_search']")
        search_button.click()

        scroll_target = page.locator("div[class='features_items']")
        scroll_target.wait_for(state="visible", timeout=10000)
        scroll_target.scroll_into_view_if_needed()      
        print("Search executed for 'Tshirt'")
        time.sleep(5)

        browser.close()
if __name__ == "__main__":
    run()