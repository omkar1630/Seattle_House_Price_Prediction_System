# 🏠 Seattle House Price Prediction System

## 📌 Overview

The Seattle House Price Prediction System is a Machine Learning web application that predicts house prices based on key property features such as bedrooms, bathrooms, house size, lot size, and zip code.

The application uses a K-Nearest Neighbors (KNN) Regression model and provides instant price predictions through an interactive Streamlit interface.

---

## 🚀 Live Demo

Add your Render deployment link here:

[https://your-render-link.onrender.com/](https://seattle-house-price-prediction-system-1.onrender.com/)

---

## 🎯 Features

- Predict house prices instantly
- User-friendly Streamlit interface
- KNN Regression-based prediction model
- Responsive and attractive design
- Real-time property valuation
- Easy deployment on Render

---

## 📊 Input Features

The model uses the following features:

| Feature | Description |
|----------|------------|
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| House Size | Area of the house (sq ft) |
| Lot Size | Land area (sq ft) |
| Zip Code | Property location zip code |

---

## 🧠 Machine Learning Model

### Algorithm Used

- K-Nearest Neighbors (KNN) Regression

### Objective

Predict the estimated market price of a house based on its characteristics.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Libraries

- Streamlit
- Scikit-learn
- NumPy
- Pandas

### Deployment

- Render

---

## 📂 Project Structure

```text
Seattle-House-Price-Prediction-System/
│
├── app.py
├── KNNRG.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Seattle-House-Price-Prediction-System.git
```

### Navigate to Project Folder

```bash
cd Seattle-House-Price-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🌐 Render Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 📈 Dataset

Dataset Source:

Seattle House Price Prediction Dataset

The dataset contains information about residential properties in Seattle, including property characteristics and house prices used for machine learning-based price estimation.

---

## 📷 Application Workflow

1. Enter property details.
2. Click **Predict House Price**.
3. The model processes the input values.
4. Estimated house price is displayed instantly.
5. Results are shown in a clean and interactive format.

---

## 🔮 Future Enhancements

- Interactive price trend dashboard
- Property recommendation system
- House price visualization charts
- Feature importance analysis
- Advanced ensemble machine learning models
- Location-based analytics

---

## 👨‍💻 Author

**Omkar Raut**

Aspiring Data Analyst | Machine Learning Enthusiast | Full Stack Developer

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub.

---

## 📜 License

This project is intended for educational and portfolio purposes.
