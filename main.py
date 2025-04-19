
# run that webpage use that command on terminal : streamlit run .\main.py

import streamlit as st
from prediction_helper import predict


# Page config
st.set_page_config(page_title="Health Insurance Premium Predictor", layout="wide")


#Adding style

st.markdown("""
    <style>
        /* Entire app background including top */
        .stApp {
            background-color: #e6eff6;   /* Slightly darker light blue */
            background-image: linear-gradient(to right, #e6eff6, #c2d7e8);
            color: #333333;  /* Darker text for contrast */
        }

        /* Top nav and header area */
        header, .css-18ni7ap {
            background-color: #e6eff6 !important;
            background-image: linear-gradient(to right, #e6eff6, #c2d7e8) !important;
        }

        /* Block layout spacing */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* Input box styles */
        div[data-baseweb="select"], input[type="number"] {
            background-color: #f0f5fb !important;
            color: #333333 !important;
            border-radius: 8px;
            border: 1px solid #a1c1d1;
            padding: 6px;
        }

        div[data-baseweb="select"] * {
            color: #333333 !important;
        }

        div[data-baseweb="menu"] {
            background-color: #f0f5fb !important;
        }

        label {
            color: #444444 !important;
            font-weight: 500;
        }

        /* Button style */
        .stButton>button {
            background-color: #4B8BBE;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1.5em;
            border: none;
        }

        .stButton>button:hover {
            background-color: #366999;
            transition: 0.3s ease;
        }

        /* Result text styling */
        .stAlert {
            background-color: #e1f3f3;
            color: #4B8BBE;
            border: 1px solid #4B8BBE;
        }
    </style>
""", unsafe_allow_html=True)








# Title
st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🏥 Health Insurance Premium Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)


# --- Inputs ---
spacer1, col1, col2, col3, spacer2 = st.columns([2, 2.5, 2.5, 2.5, 2])

with col1:
    age = st.number_input("Age", min_value=1, max_value=100, value=30)
    gender = st.selectbox("Gender", ['Female', 'Male'])
    region = st.selectbox("Region", ['Southeast', 'Northeast', 'Southwest', 'Northwest'])
    marital_status = st.selectbox("Marital Status", ['Unmarried', 'Married'])
    number_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=6, value=1)

with col2:
    bmi_category = st.selectbox("BMI Category", ['Normal', 'Overweight', 'Obesity', 'Underweight'])
    physical_activity = st.selectbox("Physical Activity", ['Medium', 'Low', 'High'])
    stress_level = st.selectbox("Stress Level", ['Medium', 'High', 'Low'])
    smoking_status = st.selectbox("Smoking Status", ['No Smoking', 'Occasional', 'Regular'])
    medical_history = st.selectbox("Medical History", [
        'High blood pressure', 'No Disease', 'Thyroid',
        'High blood pressure & Heart disease', 'Diabetes & Thyroid', 'Diabetes',
        'Heart disease', 'Diabetes & High blood pressure',
        'Diabetes & Heart disease'
    ])

with col3:
    employment_status = st.selectbox("Employment Status", ['Self-Employed', 'Freelancer', 'Salaried'])
    income_level = st.selectbox("Income Level", ['25L - 40L', '10L - 25L', '<10L', '> 40L'])
    income_lakhs = st.number_input("Income (in Lakhs)", min_value=1, max_value=200, value=10)
    insurance_plan = st.selectbox("Insurance Plan", ['Gold', 'Silver', 'Bronze'])



    # Create a dictionary for input values
    
    input_dict = {
        'Age': age,
        'Gender': gender,
        'Region': region,
        'Marital_status': marital_status,
        'Physical_Activity': physical_activity,         
        'Stress_Level': stress_level,                   
        'Number_Of_Dependants': number_of_dependents,
        'BMI_Category': bmi_category,
        'Smoking_Status': smoking_status,
        'Employment_Status': employment_status,
        'Income_Level': income_level,
        'Income_Lakhs': income_lakhs,
        'Medical_History': medical_history,             
        'Insurance_Plan': insurance_plan                
    }


    st.markdown("###")  # vertical spacing

    predict_clicked = st.button("🔍 Predict Premium")


    if predict_clicked:
        
        prediction=predict(input_dict)
        st.success(f"💰 Estimated Premium: ₹ {prediction}")



