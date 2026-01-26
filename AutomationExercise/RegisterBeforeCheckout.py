from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        
        page.click("text=signup / login")
        print("Navigated to Signup / Login page")
        time.sleep(2)

        name = "Krisha"       #enter name email
        email = f"krisha{int(time.time())}@example.com"     
        page.fill("input[data-qa='signup-name']", name)
        page.fill("input[data-qa='signup-email']", email)
        print("Entered name and email for signup")
        time.sleep(1)
        page.click("button[data-qa='signup-button']")
        page.wait_for_selector("input[id='password']", timeout=30000)
        print("Signup page loaded")
        time.sleep(2)
        # Fill details
        page.check("input[id='id_gender2']")
        page.fill("input[id='password']", "Krish@123")
        page.select_option("select[id='days']", "29")
        page.select_option("select[id='months']", "7")          
        page.select_option("select[id='years']", "2003")
        page.check("input[id='newsletter']")
        page.check("input[id='optin']")
        time.sleep(1)
        page.fill("input[id='first_name']", "Krisha")
        page.fill("input[id='last_name']", "Shah")
        page.fill("input[id='company']", "ABC Pvt Ltd")
        page.fill("input[id='address1']", "123, Main Street")
        page.fill("input[id='address2']", "Apt 4B")
        page.select_option("select[id='country']", "Canada")
        page.fill("input[id='state']", "Ontario")
        page.fill("input[id='city']", "Toronto")
        page.fill("input[id='zipcode']", "M4B1B3")
        page.fill("input[id='mobile_number']", "+1234567890")
        time.sleep(1)

        page.click("button[data-qa='create-account']")
        page.wait_for_selector("text=Account Created!", timeout=30000)
        print("Account Created!")
        time.sleep(2)

         # login
        page.click("a[data-qa='continue-button']")
        page.wait_for_selector(f"text=Logged in as {name}", timeout=30000)
        print(f"Logged in as {name}")
        time.sleep(2)

        Add_to_Cart = page.locator("text=Add to cart").first
        Add_to_Cart.click()
        print("Product added to cart")
        time.sleep(2)

        page.click("text=View Cart")
        print("Navigated to Cart page")
        time.sleep(2)

        page.click("text=Proceed To Checkout")
        print("Proceeded to Checkout...")
        time.sleep(2)   

        page.click("text=place order")
        print("Order placed successfully")
        time.sleep(2)

        page.fill("input[name='name_on_card']", "Krisha Bhandari")
        page.fill("input[name='card_number']", "4111111111111111")
        page.fill("input[name='cvc']", "123")
        page.fill("input[name='expiry_month']", "12")
        page.fill("input[name='expiry_year']", "2025")  
        time.sleep(3)
        page.click("button[id='submit']")
        print("Payment details submitted")
        time.sleep(3)

        page.click("text= Delete Account")
        print("Account deletion Successful ")
        time.sleep(2)
        page.click("text=Continue")


if __name__ == "__main__":
    run()        