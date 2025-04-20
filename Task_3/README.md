# 🗺️ Tourist Attractions Scraper using OpenStreetMap Overpass API

This project is a Python-based data extraction tool that uses the OpenStreetMap Overpass API to fetch **tourist attractions** for a **given city**. It retrieves details such as **name**, **type**, **latitude**, and **longitude**, and saves the data to a CSV file. This can be extremely useful for data science tasks involving location-based analysis, tourism trend prediction, or geographic data visualization.

---

## 📌 Project Description

Many tourist-focused applications, city guides, and travel recommendation systems rely on geographical data. This script provides a streamlined method to **programmatically retrieve structured location data** from the open-source OpenStreetMap database using its Overpass API.

You input a city name (like *Delhi*, *Mumbai*, or *Jaipur*), and the script does the following:
- Identifies the geographical boundary of the city
- Fetches all map nodes tagged as **tourist attractions**, including monuments, museums, parks, and more
- Stores the cleaned and structured data in a `.csv` file

---

## 🎯 Use Cases

- Building a **travel recommendation system**
- Creating **maps or visualizations** for tourism data
- Feeding data into a **machine learning model** for location-based insights
- Learning how to work with **APIs and JSON data structures**
- Practicing **data cleaning and export**

---

## 📦 Technologies Used

- Python 3.7+
- `requests` – for API calls
- `csv` – for saving the data
- OpenStreetMap Overpass API – for open geodata
- JSON – data parsing

---

## 🚀 How to Use

### 1. Install Requirements

```bash
pip install requests
```

### 2. Run the Script

```bash
python main.py
```

When prompted:

```
Enter the name of the city: Jaipur
```

### 3. Output

The script generates a CSV file named after the city, e.g., `jaipur_tourist_attractions.csv`.

Each row contains:

- Name (original name from OpenStreetMap, may include Hindi or local scripts)
- Type of attraction (e.g., museum, monument)
- Latitude
- Longitude

---

## 🖼️ Sample Output (CSV)

```csv
Name,Type,Latitude,Longitude
लाल किला,attraction,28.6562,77.2410
India Gate,monument,28.6129,77.2295
```

---

## 📚 What You’ll Learn

- Interfacing with REST APIs
- Writing efficient JSON queries
- Parsing geospatial data
- Automating data collection pipelines
- Exporting and analyzing structured datasets

---

## 🌍 Future Enhancements

- Add support for multiple cities in batch
- Include category filters (religious, natural, historical, etc.)
- Integrate with mapping libraries (like Folium or Leaflet.js)
- Convert to a web dashboard

---

## 🙌 Author

Made with ❤️ by Rishit Mishra for a Data Science Internship Assignment.

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

Happy Scraping! ✨