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

        page.fill("input[data-qa='login-email']", "krisha1769576321@example.com" )
        page.fill("input[data-qa='login-password']", "Krish@123")
        page.click("button[data-qa='login-button']")
        print("Login successful")
        time.sleep(2)   

        Add_to_Cart = page.locator("text=Add to cart").first
        Add_to_Cart.click()
        print("Add to cart clicked")
        time.sleep(2)
        
        page.click("text= View Cart")
        print("Navigated to Cart page")
        time.sleep(2)

        page.click("text= Proceed To Checkout")
        print("Proceeded to Checkout")
        time.sleep(2)

        page.click("text=Place Order")
        print("Order placed successfully")
        time.sleep(2)   

        page.fill("input[name='name_on_card']", "Krisha Bhandari")
        page.fill("input[name='card_number']", "4111111111111111")
        page.fill("input[name='cvc']", "123")       
        page.fill("input[name='expiry_month']", "12")
        page.fill("input[name='expiry_year']", "2025")
        time.sleep(2)

        page.click("button[id='submit']")
        print("Payment details submitted")
        time.sleep(3)   

        page.click("text= Delete Account")
        print("Account deletion Successful ")
        time.sleep(2)   

        page.click("text=continue")
        print("Continuing to homepage") 
        time.sleep(2)

        browser.close()
if __name__ == "__main__":
    run()
         
