from playwright.sync_api import sync_playwright
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://automationexercise.com")
        print("Website opened successfully")
        time.sleep(2)

        side_bar = page.locator("text=Category")
        side_bar.scroll_into_view_if_needed()
        print("Scrolled to Category section......")
        time.sleep(2)

        # Click on Women's category
        click_category = page.locator("a[href='#Women']")
        click_category.click()
        print("Clicked on Women's category")
        time.sleep(2)

        click_categorys = page.locator("a[href='/category_products/1']")
        click_categorys.click()
        print("Clicked on Dresses")
        time.sleep(2)

        side_bar = page.locator("text=Category")
        side_bar.scroll_into_view_if_needed()
        print("Scrolled to Category section again")
        time.sleep(2)
       
       # Click on Women's category
        click_category = page.locator("a[href='#Men']")
        click_category.click()
        print("Clicked on Men's category")
        time.sleep(2)

        click_categorys = page.locator("a[href='/category_products/3']")
        click_categorys.click()
        print("Clicked on TSHIRT")
        time.sleep(2)

        browser.close()
if __name__ == "__main__":
    run()