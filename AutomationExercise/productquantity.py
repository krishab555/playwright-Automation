from playwright.sync_api import sync_playwright
import time 

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        
        view_product = page.locator("a[href='/product_details/1']")
        view_product.wait_for(state="visible", timeout=10000)
        view_product.scroll_into_view_if_needed()
        time.sleep(0)

        page.click("text=View Product")
        print("Clicked on View Product button")
        product_quantity = page.locator("#quantity")
        product_quantity.fill("4")
        print("Product quantity updated to 4")
        time.sleep(2)

        page.click("text=Add to Cart")
        print("Clicked on Add to Cart button")
        time.sleep(2)

        page.click("text=View Cart")
        print("Navigated to Cart page to verify quantity")
        time.sleep(2)

        browser.close()

if __name__ == "__main__":
    run()