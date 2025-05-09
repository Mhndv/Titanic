
# 🚢 Titanic EDA Dashboard

This project is a data exploration dashboard built with **Streamlit** and **Plotly** to visualize insights from the Titanic dataset. The dashboard allows interactive filtering, dynamic visualizations, and maps the Titanic's historical route.

---

## 📌 Features

- **Interactive Filters**  
  Filter passengers by gender, survival status, ticket class, and age range from the sidebar.

- **Passenger Summary Metrics**  
  Displays total passengers, average age, and average fare for selected filters.

- **📍 Route Map**  
  Shows the Titanic's journey using Plotly map visualization:
  - Belfast (Construction)
  - Southampton (Start)
  - Cherbourg
  - Queenstown
  - Iceberg Warning Zone
  - Wreck Site
  - New York City (Destination)

- **📊 Visual Insights**  
  - Gender Distribution (Pink for Female, Blue for Male)
  - Survival Rates (Green = Survived, Red = Died)
  - Passenger Class Distribution
  - Fare by Class and Gender
  - Age Distribution by Gender
  - Survival by Class and Gender
  - Survival by Family Size
  - Passenger Count by Embarkation Port
  - Correlation Heatmap of Numeric Features

- **🧠 Key Takeaways Section**  
  Highlights important insights from the analysis.

---

## 🧰 Tech Stack

- Python
- Streamlit
- Pandas
- Plotly

---

## 🚀 Getting Started

1. **Clone this repository:**
   ```bash
   git clone https://github.com/Mhndv/titanic-eda-dashboard.git
   cd titanic-eda-dashboard
   ```

2. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

---

## 📁 Project Structure

```
📦 titanic-eda-dashboard
├── app.py                # Main Streamlit app
├── titanic_data.csv      # Dataset file
├── README.md             # Project documentation
└── requirements.txt      # Dependencies list
```

---

## 🧠 Key Insights

- Majority of passengers were in 3rd class.
- Women had a significantly higher survival rate than men.
- 1st class women and children had the highest survival rates.
- Most passengers boarded from Southampton.
- Fare prices increase with ticket class.
- Survival rate is correlated with gender, class, and age.

---

## 📬 Author

Developed by **Muhannad Alsahaf**  

---
