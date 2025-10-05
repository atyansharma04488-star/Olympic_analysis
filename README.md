# 🏅 Olympic Data Analysis Web App

This project is a Python-based data analytics dashboard that provides deep insights into over 120 years of Olympic Games history. It allows users to explore country-wise performance, athlete trends, event growth, gender participation, and more.

> Built using **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**, **Plotly**, and **Streamlit**.

---

## 🔍 Project Overview

This dashboard helps visualize and understand historical Olympic data, including:
- Which countries performed best in each edition
- Growth of events, sports, and participation over time
- Most successful athletes
- Gender-based participation analysis
- Physical metrics like height vs. weight by sport

---

## 🚀 Features

### 📊 Overall Analysis
- Top statistics (editions, hosts, sports, athletes, nations)
- Growth of events and athletes over time
- Most successful athletes by sport

### 🌍 Country-wise Analysis
- Medal tally by year
- Heatmap of sports vs year for a country
- Top athletes from a selected country

### 🧑‍🤝‍🧑 Athlete-wise Analysis
- Age distribution (general and medalists)
- Height vs weight analysis by sport
- Male vs female participation over time

### 🏅 Medal Tally
- Filter by year and/or country
- See total medal breakdown: Gold, Silver, Bronze

---

## 🗂️ Folder Structure

```
Olympic_analysis/
│
├── app.py                 # Main Streamlit application
├── helper.py              # All analysis functions
├── preprocessor.py        # Data preprocessing logic
├── athlete_events.csv     # Primary dataset
├── noc_regions.csv        # NOC-region mapping dataset
└── README.md              # Project documentation
```

---

## 🧠 How It Works

1. Load and preprocess the dataset using `preprocessor.py`
2. Perform data aggregation and analysis using functions in `helper.py`
3. Display results interactively with `Streamlit` through `app.py`

---

## 💻 How to Run

### Step 1: Clone the repository
```bash
git clone https://github.com/nipungoel24/Olympic_analysis.git
cd Olympic_analysis
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, manually install:
```bash
pip install pandas numpy matplotlib seaborn plotly streamlit
```

### Step 3: Run the application
```bash
streamlit run app.py
```

---

## 🖼️ Screenshots

> (Add screenshots to an `assets/` folder and update the links below)

### 📌 Medal Tally View
![Medal Tally](assets/medal_tally.png)

### 📌 Athlete Age Distribution
![Age Distribution](assets/age_distribution.png)

### 📌 Height vs Weight Plot
![Height vs Weight](assets/height_weight.png)

---

## 🛠️ Tech Stack

- **Python**
- **Pandas & NumPy** – Data manipulation
- **Matplotlib & Seaborn** – Static visualizations
- **Plotly** – Interactive charts
- **Streamlit** – Web interface and deployment

---

## 📦 Datasets Used

- 📁 [120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results)

---

## 🙏 Acknowledgements

- Inspired by [CampusX YouTube Lecture](https://youtu.be/5nQXhusiu7s?si=R1ra8lDn7ZIL0-VI)
- Thanks to the open-source and data science communities

---

## 📬 Contact

Made with ❤️ by [Aryan Sharma](https://github.com/nipungoel24)

- 📧 Email: atyansharma04488@gmail.com
- 🌐 [LinkedIn](https://www.linkedin.com/in/nipungoel24/)
- 🧠 [GitHub](https://github.com/nipungoel24)
