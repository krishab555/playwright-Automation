# Register login and delete account.
from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("http://automationexercise.com") #open website
        time.sleep(2)

        page.click("text=Signup / Login")   
        time.sleep(2)

        name = "Krisha"       #enter name email
        email = f"krisha{int(time.time())}@example.com"
        print(f"Using email: {email}")

        page.fill("input[data-qa='signup-name']", name)
        page.fill("input[data-qa='signup-email']", email)

        # Click Signup
        page.click("button[data-qa='signup-button']")
        page.wait_for_selector("input[id='password']", timeout=30000)
        print(f"Using password: {'Krish@123'}")
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

        # # Delete Account
        # page.click("a[href='/delete_account']")
        # page.wait_for_selector("text=Account Deleted!", timeout=30000)
        # print("Account Deleted!")
        # time.sleep(2)

        page.click("a[data-qa='continue-button']") #continue after delete

        browser.close()
        print("Test completed successfully!")

if __name__ == "__main__":
    run()
