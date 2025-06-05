
# 🍓 Fruit API Data ETL Project

This project demonstrates a complete **ETL (Extract, Transform, Load)** process using the Fruityvice API. It focuses on real-world data engineering practices with Python and pandas.

---

## 📦 What It Does

- **Extracts** fruit data from the Fruityvice public API (archived endpoint).
- **Transforms** JSON data into structured pandas DataFrames.
- **Loads** data into multiple `.csv` files including:
  - All fruits
  - Individual fruits (e.g., Banana, Mango)
  - Combined fruit dataset (Banana + Mango)

---

## 📁 Project Files

| File Name           | Description                                 |
|---------------------|---------------------------------------------|
| `fruitAPI.py`       | Main Python script for the ETL process      |
| `fruits.csv`        | Complete fruit dataset from the API         |
| `banana.csv`        | Filtered data for Banana                    |
| `mango.csv`         | Filtered data for Mango                     |
| `banana_mango.csv`  | Combined data of Banana and Mango           |

---

## 🛠️ Technologies Used

- Python
- Pandas
- Requests
- JSON
- CSV File Handling

---

## 🔧 How to Run

1. Clone the repository  
   ```bash
   git clone https://github.com/miqdad-dev/Fruit-API-Data-ETL.git
   cd Fruit-API-Data-ETL
   ```

2. Run the script  
   ```bash
   python fruitAPI.py
   ```

3. View the generated `.csv` files in the same directory.

---

## 🙋‍♂️ Author

**Miqdad Issa** — aspiring data engineer on a mission to master Python, APIs, and real-world ETL pipelines.

---

## 🌐 API Used

[Archived Fruityvice API](https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all)

---

## 📌 Note

This project is part of my 30-day data engineering challenge, combining learning with real, hands-on implementation.
