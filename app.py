import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("data.pkl", "rb"))

# Page config
st.set_page_config(page_title="Insurance Premium Predictor", layout="wide")

# ---------- UI Styling ----------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #1f4037, #99f2c8);
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #ffffff;
}
.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.2);
}
.stButton>button {
    background-color: #1f77b4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<p class="title">💰 Health Insurance Premium Predictor</p>', unsafe_allow_html=True)
st.write("### Fill your details below 👇")

# ---------- Layout ----------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    age = st.slider("👤 Age (Years)", 18, 65, 25)

    bmi = st.number_input(
        "⚖️ BMI (Body Mass Index)",
        min_value=10.0,
        max_value=50.0,
        value=25.0,
        help="Normal BMI range is 18.5 - 24.9"
    )

    children = st.selectbox(
        "👨‍👩‍👧 Number of Dependents",
        [0, 1, 2, 3, 4, 5]
    )

    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    smoker = st.radio(
        "🚬 Smoking Status",
        ["No", "Yes"]
    )

    st.markdown("### 📊 Risk Insight")
    if smoker == "Yes":
        st.warning("⚠️ Smoking increases premium significantly")
    elif bmi > 30:
        st.warning("⚠️ High BMI may increase premium")
    else:
        st.success("✅ Low risk profile")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Convert Input ----------
smoker_val = 1 if smoker == "Yes" else 0

input_data = np.array([[age, bmi, children, smoker_val]])

# ---------- Prediction ----------
st.markdown("##")

if st.button("💡 Calculate Premium"):
    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div style="background-color:#ffffff;padding:20px;border-radius:15px;text-align:center;">
        <h2 style="color:#1f77b4;">Estimated Premium</h2>
        <h1 style="color:#ff4b2b;">₹ {prediction:,.2f}</h1>
    </div>
    """, unsafe_allow_html=True)

# ---------- Footer ----------
st.markdown("---")
st.markdown("📌 Built with Streamlit | ML Insurance Model")
