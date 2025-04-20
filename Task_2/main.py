from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# ----- SETUP -----
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options=options)

BASE_URL = "https://www.amazon.in/"
MAX_PRODUCTS = 10  # Change this as needed
WAIT = 3
all_data = []

# ----- GO TO AMAZON -----
driver.get(BASE_URL)
time.sleep(WAIT)

# ----- GET CATEGORY LIST -----
dropdown = driver.find_element(By.ID, "searchDropdownBox")
options_list = dropdown.find_elements(By.TAG_NAME, "option")[6:]

categories = []
for option in options_list:
    name = option.text.strip()
    categories.append(name)

print(f"Found {len(categories)} categories")

# ----- LOOP OVER CATEGORIES -----
for category in categories:
    print(f"\n🔍 Searching category: {category}")
    try:
        driver.get(BASE_URL)
        time.sleep(WAIT)

        input_search = driver.find_element(By.ID, "twotabsearchtextbox")
        input_search.clear()
        input_search.send_keys(category)
        input_search.send_keys(Keys.RETURN)
        time.sleep(WAIT)

        # Get subcategory from breadcrumb or result line
        try:
            subcategory_elem = driver.find_element(By.XPATH, "//span[contains(text(),'results for')]")
            subcategory = subcategory_elem.text
        except:
            subcategory = "N/A"

        # Fetch product cards
        product_cards = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")[:MAX_PRODUCTS]

        for card in product_cards:
            try:
                title = card.find_element(By.TAG_NAME, "h2").text
                link = card.find_element(By.TAG_NAME, "a").get_attribute("href")
                try:
                    price = card.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
                except:
                    price = "N/A"
                try:
                    rating = card.find_element(By.XPATH, ".//span[contains(@class, 'a-icon-alt')]").text
                except:
                    rating = "N/A"

                all_data.append({
                    "Category": category,
                    "Subcategory": subcategory,
                    "Title": title,
                    "Price": price,
                    "Rating": rating,
                    "URL": link
                })
            except Exception as e:
                continue
    except Exception as e:
        print(f"Error with category {category}: {e}")
        continue

# ----- SAVE TO CSV -----
df = pd.DataFrame(all_data)
df.to_csv("amazon_category_subcategory_data.csv", index=False)
print("\nData saved to amazon_category_subcategory_data.csv")

driver.quit()
