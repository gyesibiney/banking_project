import streamlit as st
import pandas as pd
import joblib

# Title and description
st.title("Banking Campaign Outcome Prediction App")
st.markdown("""
Welcome to the **Banking Campaign Outcome Prediction App**!  
This tool predicts whether a customer will respond positively to a banking campaign based on their demographic and transactional information.  
Please input the required details below to get a prediction.
""")


# Load the trained model
model = joblib.load("DTC.joblib")


# Input features
st.header("Enter the details for prediction:")

# Numeric inputs
age = st.number_input("Age", min_value=18, max_value=100, step=1)
call_duration_seconds = st.number_input("Call Duration (in seconds)", min_value=0, step=1)
contacts_during_campaign = st.number_input("Number of Contacts During Campaign", min_value=0, step=1)
days_since_last_contact = st.number_input("Days Since Last Contact", min_value=0, step=1)
previous_contacts = st.number_input("Number of Previous Contacts", min_value=0, step=1)
employment_variation_rate = st.number_input("Employment Variation Rate", format="%.2f")
consumer_price_index = st.number_input("Consumer Price Index", format="%.2f")
consumer_confidence_index = st.number_input("Consumer Confidence Index", format="%.2f")
euribor_3m_rate = st.number_input("Euribor 3M Rate", format="%.2f")
number_employed = st.number_input("Number of People Employed", min_value=0, step=1)

# Categorical inputs
job = st.selectbox("Job", ["admin.", "blue-collar", "entrepreneur", "housemaid", "management", "retired", "self-employed", "services", "student", "technician", "unemployed", "unknown"])
marital_status = st.selectbox("Marital Status", ["single", "married", "divorced", "unknown"])
education_level = st.selectbox("Education Level", ["primary", "secondary", "tertiary", "unknown"])
has_default = st.selectbox("Has Default?", ["yes", "no", "unknown"])
has_housing_loan = st.selectbox("Has Housing Loan?", ["yes", "no", "unknown"])
has_personal_loan = st.selectbox("Has Personal Loan?", ["yes", "no", "unknown"])
contact_type = st.selectbox("Contact Type", ["cellular", "telephone"])
contact_month = st.selectbox("Contact Month", ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])
contact_day = st.selectbox("Contact Day", list(range(1, 32)))
previous_outcome = st.selectbox("Previous Outcome", ["success", "failure", "nonexistent"])

# Button for prediction
if st.button("Predict Campaign Outcome"):
    # Combine inputs into a dataframe
    input_data = {
        "Age": [age],
        "Call_Duration_Seconds": [call_duration_seconds],
        "Contacts_During_Campaign": [contacts_during_campaign],
        "Days_Since_Last_Contact": [days_since_last_contact],
        "Previous_Contacts": [previous_contacts],
        "Employment_Variation_Rate": [employment_variation_rate],
        "Consumer_Price_Index": [consumer_price_index],
        "Consumer_Confidence_Index": [consumer_confidence_index],
        "Euribor_3M_Rate": [euribor_3m_rate],
        "Number_Employed": [number_employed],
        "Job": [job],
        "Marital_Status": [marital_status],
        "Education_Level": [education_level],
        "Has_Default": [has_default],
        "Has_Housing_Loan": [has_housing_loan],
        "Has_Personal_Loan": [has_personal_loan],
        "Contact_Type": [contact_type],
        "Contact_Month": [contact_month],
        "Contact_Day": [contact_day],
        "Previous_Outcome": [previous_outcome],
    }
    input_df = pd.DataFrame(input_data)

    # Make prediction
    try:
        forecast = model.predict(input_df)
        if forecast[0] == 1:
            st.success("The customer is likely to respond positively to the campaign!")
        else:
            st.success("The customer is likely to not respond to the campaign.")
    except Exception as e:
        st.error(f"Error making prediction: {e}")

