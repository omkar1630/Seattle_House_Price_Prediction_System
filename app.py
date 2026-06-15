import streamlit as st
import pickle
import numpy as np

# Load Model
with open("KNNRG.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(
    page_title="HomeValue AI",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align:center;
    color:#1E3A8A;
    font-size:42px;
    font-weight:bold;
}

.subtitle {
    text-align:center;
    color:#555;
    font-size:18px;
    margin-bottom:25px;
}

.metric-box {
    background:#ffffff;
    padding:15px;
    border-radius:15px;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}

.stButton>button {
    width:100%;
    background:linear-gradient(90deg,#2563EB,#1D4ED8);
    color:white;
    border:none;
    border-radius:10px;
    height:3em;
    font-size:18px;
    font-weight:bold;
}

.result {
    padding:20px;
    border-radius:15px;
    text-align:center;
    font-size:30px;
    font-weight:bold;
    background:#DCFCE7;
    color:#166534;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🏠 HomeValue AI</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Seattle House Price Prediction System using KNN Regression</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Inputs
col1, col2 = st.columns(2)

with col1:
    beds = st.number_input(
        "🛏 Number of Bedrooms",
        min_value=1,
        max_value=20,
        value=3
    )

    baths = st.number_input(
        "🛁 Number of Bathrooms",
        min_value=1.0,
        max_value=20.0,
        value=2.0
    )

    size = st.number_input(
        "📐 House Size (sq ft)",
        min_value=200,
        max_value=20000,
        value=2000
    )

with col2:
    lot_size = st.number_input(
        "🌳 Lot Size (sq ft)",
        min_value=500,
        max_value=100000,
        value=5000
    )

    zip_code = st.number_input(
        "📍 Zip Code",
        min_value=10000,
        max_value=99999,
        value=98101
    )

st.markdown("")

if st.button("💰 Predict House Price"):

    features = np.array([[
        beds,
        baths,
        size,
        lot_size,
        zip_code
    ]])

    prediction = model.predict(features)[0]

    st.markdown(
        f"""
        <div class="result">
        Estimated House Price<br>
        💵 ${prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.info(
    "Enter property details to estimate the house price using a K-Nearest Neighbors Regression model."
)
