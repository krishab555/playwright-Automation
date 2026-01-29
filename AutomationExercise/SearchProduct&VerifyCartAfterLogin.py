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

        page.fill("input[name='search']", "T-shirt")
        print("Entered search term")
        time.sleep(2)

        search_button = page.locator("button[id='submit_search']")
        search_button.click()
        print("Clicked on search button")
        time.sleep(2)

        scroll_target = page.locator("div[class='features_items']")
        scroll_target.wait_for(state="visible")
        scroll_target.scroll_into_view_if_needed()      
        print("Search executed for 'Tshirt'")
        time.sleep(2)

        Add_to_Cart = page.locator("text=Add to Cart").first
        Add_to_Cart.scroll_into_view_if_needed()
        Add_to_Cart.click()
        print("Product added to cart")
        time.sleep(2)

        page.click("text=View Cart")
        print("Navigated to Cart page")
        time.sleep(2)

        browser.close()
if __name__ == "__main__":
    run()   