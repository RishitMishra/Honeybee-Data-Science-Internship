
# Amazon Category & Product Scraper using Selenium

This Python script scrapes product details from [Amazon.in](https://www.amazon.in/) by searching for all categories using the search dropdown. It collects product titles, prices, ratings, subcategory names, and product URLs for each category.

## 🔧 Features
- Searches each category using Amazon's search bar
- Extracts product title, price, rating, and product URL
- Retrieves subcategory (breadcrumb-style) from result page
- Saves data to a CSV file
- Uses `Selenium` for browser automation

## 🧪 Requirements
Install dependencies using:

```bash
pip install -r requirements.txt
```

## 🚀 How to Run

1. Clone this repo or copy the script to your local machine.
2. Ensure [Google Chrome](https://www.google.com/chrome/) is installed.
3. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) that matches your Chrome version.
4. Place the ChromeDriver in your PATH or same directory as your script.
5. Run the script using:

```bash
python amazon_scraper.py
```

The script will generate a CSV file named `amazon_category_subcategory_data.csv` in the same directory.

## 📝 Output Format

| Category  | Subcategory | Title | Price | Rating | URL |
|-----------|-------------|-------|-------|--------|-----|

## ⚠️ Disclaimer
This project is intended for educational purposes only. Scraping Amazon violates their Terms of Service. Use responsibly.
