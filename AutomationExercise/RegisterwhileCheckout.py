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

        page.click("text=Add to Cart")
        print("Clicked on Add to Cart button")
        time.sleep(2)

        page.click("text=View Cart")
        print("Navigated to Cart page to verify quantity")
        time.sleep(2)

        page.click("text=Proceed To Checkout")
        print("Proceeded to Checkout page")
        time.sleep(1)

                # Wait for checkout modal
        page.wait_for_selector("#checkoutModal", state="visible", timeout=30000)

        # Click Register / Login inside modal
        page.locator("#checkoutModal a[href='/login']").click()

        # Wait for login page
        page.wait_for_url("**/login")
        print("Register / Login page loaded")

        name = "Krisha"       #enter name email
        email = f"krisha{int(time.time())}@example.com"

        page.fill("input[data-qa='signup-name']", name)
        page.fill("input[data-qa='signup-email']", email)

        # Click Signup
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

        # Fill address info
        page.fill("input[id='first_name']", "Krisha")
        page.fill("input[id='last_name']", "Bhandari")
        page.fill("input[id='company']", "MyCompany")
        page.fill("input[id='address1']", "Toronto, Canada")
        page.fill("input[id='address2']", "Tinkune")
        page.select_option("select[id='country']", "Canada")  
        page.fill("input[id='state']", "Ontario")
        page.fill("input[id='city']", "Toronto")
        page.fill("input[id='zipcode']", "M5V 3L9")
        page.fill("input[id='mobile_number']", "+14161234567")
        time.sleep(1)

        # Create Account
        page.click("button[data-qa='create-account']")
        page.wait_for_selector("text=Account Created!", timeout=30000)
        print("Account Created!")
        time.sleep(2)

        # login
        page.click("a[data-qa='continue-button']")
        page.wait_for_selector(f"text=Logged in as {name}", timeout=30000)
        print(f"Logged in as {name}")
        time.sleep(2)

        page.click("text=Cart")
        print("Proceeded to Cart page after login")
        time.sleep(2)

        page.click("text=Proceed To Checkout")
        print("Proceeded to Checkout page after login")
        time.sleep(2)   

        Scroll_target = page.locator("text=Place Order")
        Scroll_target.scroll_into_view_if_needed()
        time.sleep(1)

        page.click("text=Place Order")
        print("Proceeded to Place Order page")
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


        browser.close()

if __name__ == "__main__":
    run()