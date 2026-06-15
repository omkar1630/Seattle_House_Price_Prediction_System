import streamlit as st
import pickle
import numpy as np

# Load Model
with open("KNNRG.pkl", "rb") as file:
    model = pickle.load(file)

# Page Config
st.set_page_config(
    page_title="Seattle House Price Prediction System",
    page_icon="🏠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f4f8fb;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #0F4C81;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 20px;
}

.prediction-box {
    background-color: #d4edda;
    color: #155724;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    background: linear-gradient(90deg,#0F4C81,#1E88E5);
    color: white;
    border-radius: 10px;
    font-size: 18px;
    height: 3em;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(
    '<div class="title">🏠 Seattle House Price Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict house prices using Machine Learning (KNN Regression)</div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Input Section
st.subheader("📋 Property Information")

col1, col2 = st.columns(2)

with col1:
    beds = st.number_input(
        "🛏 Bedrooms",
        min_value=1,
        max_value=20,
        value=3
    )

    baths = st.number_input(
        "🛁 Bathrooms",
        min_value=1.0,
        max_value=20.0,
        value=2.0
    )

    size = st.number_input(
        "📐 House Size (sq ft)",
        min_value=200,
        value=2000
    )

with col2:
    lot_size = st.number_input(
        "🌳 Lot Size (sq ft)",
        min_value=500,
        value=5000
    )

    zip_code = st.number_input(
        "📍 Zip Code",
        min_value=10000,
        value=98101
    )

st.markdown("")

if st.button("💰 Predict House Price"):

    input_data = np.array([[
        beds,
        baths,
        size,
        lot_size,
        zip_code
    ]])

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="prediction-box">
            Estimated House Price<br><br>
            💵 ${prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("---")

st.info(
    "Enter the property details above and click Predict House Price to estimate the market value."
)
