import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Setup headless Chrome
options = uc.ChromeOptions()
options.add_argument("--headless=new")  # the 'new' headless mode is more human-like
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

# Load MagicPin Gym page
driver.get("https://magicpin.in/india/Ahmedabad/All/Gym/")
wait = WebDriverWait(driver, 10)

# Scroll multiple times to load more gyms
for _ in range(15):
    driver.execute_script("window.scrollBy(0, window.innerHeight);")
    time.sleep(2)

# Wait for gyms to load
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "basic-info")))

# Collect gyms
gyms = driver.find_elements(By.CLASS_NAME, "basic-info")
print(f"Found {len(gyms)} gyms")

print(driver.page_source[:1000])

data = []

for gym in gyms:
    try:
        name = gym.find_element(By.CLASS_NAME, "merchant-name").text.strip()
    except:
        name = "N/A"

    try:
        address_block = gym.find_element(By.CLASS_NAME, "merchant-location")
        address = address_block.find_element(By.TAG_NAME, "span").find_element(By.TAG_NAME, "a").text.strip()
        area = address.split(',')[0].strip()
    except:
        address = area = "N/A"

    entry = {
        "GYM Name": name,
        "Address": address,
        "Area": area,
        "City": "Ahmedabad",
        "State": "Gujarat",
        "Phone Number": "N/A",  # Optional
        "Timings": "N/A"        # Optional
    }

    print(entry)
    data.append(entry)

driver.quit()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("gyms_ahmedabad.csv", index=False)
print("Saved gyms_ahmedabad.csv successfully!")
