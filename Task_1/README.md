# 🏋️‍♂️ Gym Scraper - Ahmedabad (MagicPin)

This project is part of a Data Science Internship assignment. It scrapes a list of **gyms located in Ahmedabad** from [MagicPin](https://magicpin.in), extracts structured data, and saves it into a clean CSV file.

---

## 📄 Project Description

The script automates data extraction from the dynamically loaded MagicPin webpage that lists gyms in Ahmedabad. It collects key details such as:

- Gym Name
- Address
- Area
- City (Ahmedabad)
- State (Gujarat)
- Phone Number *(optional)*
- Timings *(optional)*

The final data is saved to `gyms_ahmedabad.csv`.

---

## 🧰 Technologies Used

- Python 3
- Selenium with `undetected-chromedriver`
- BeautifulSoup (optional, not used in current script)
- pandas

---

## ⚙️ Setup Instructions

### 1. Clone the Repository or Copy the Script

You can clone this repository or copy the script file directly.

```bash
git clone https://github.com/yourusername/gym-scraper.git
cd gym-scraper
```

### 2. Install Required Packages

It is recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Then install dependencies:

```bash
pip install undetected-chromedriver selenium pandas
```

> **Note:** You must have **Google Chrome** installed on your system.

---

## ▶️ How to Run

Simply run the Python script:

```bash
python gym_scraper.py
```

This will:
- Open the MagicPin Ahmedabad Gym listings page
- Scroll down multiple times to load more listings
- Scrape data from all visible cards
- Save the cleaned data to `gyms_ahmedabad.csv`

---

## 📝 Sample Output

**gyms_ahmedabad.csv**

| GYM Name     | Address                     | Area            | City       | State   | Phone Number | Timings |
|--------------|-----------------------------|------------------|------------|---------|---------------|---------|
| Gold's Gym   | Satellite Road, Satellite    | Satellite        | Ahmedabad | Gujarat | N/A           | N/A     |
| FitZone Gym  | Prahlad Nagar, Ahmedabad     | Prahlad Nagar    | Ahmedabad | Gujarat | N/A           | N/A     |

---

## 🛡 Disclaimer

This project is intended **strictly for educational and internship evaluation purposes**. All data belongs to [MagicPin](https://magicpin.in) and its respective businesses.

---

## 📬 Contact

If you have any questions or would like to contribute, feel free to reach out at:

**Name**: *Rishit Mishra*  
**Email**: *rishitmishra05@gmail.com*  
**LinkedIn**: *https://www.linkedin.com/in/rishit-mishra/*
