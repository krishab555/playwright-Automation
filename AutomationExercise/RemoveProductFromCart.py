from playwright.sync_api import sync_playwright
import time 

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")

        Add_to_Cart = page.locator("text=Add to cart").first
        Add_to_Cart.click()
        print("Product added to cart")
        time.sleep(2)
        
        page.click("text= View Cart")
        print("Navigated to Cart page")
        time.sleep(2)

        page.wait_for_selector("tr[id='product-1']", state="visible", timeout=10000)    
        page.click("tr[id='product-1'] a[class='cart_quantity_delete']")
        print("Product removed from cart")
        time.sleep(2)

        browser.close()

if __name__ == "__main__":
    run()