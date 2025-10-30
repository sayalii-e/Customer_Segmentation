import streamlit as st
import pandas as pd
import numpy as np
import joblib

kmeans = joblib.load('kmeans_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("Customer Segmentation App")
st.write("Enter Customer Details to Predict Segment")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Annual Income", min_value=0, max_value=20000000, value=50000)
total_spending = st.number_input("Total Spending", min_value=0, max_value=1000000, value=1000)
num_web_puchases = st.number_input("Number of Web Purchases", min_value=0, max_value=1000, value=10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=1000, value=5)
num_web_visits = st.number_input("Number of Web Visits per Month", min_value=0, max_value=1000, value=20)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)

input_data = pd.DataFrame({
    'Age': [age],
    'Income': [income],
    'Total_Spending': [total_spending],
    'NumWebPurchases': [num_web_puchases],
    'NumStorePurchases': [num_store_purchases],
    'NumWebVisitsMonth': [num_web_visits],
    'Recency': [recency]
})

scalaled_data = scaler.transform(input_data)

if st.button("Predict Segment"):
    cluster = kmeans.predict(scalaled_data)
    st.success(f"The predicted customer segment is: Cluster {cluster}")
    st.write("""
    Cluster Descriptions:
    - Cluster 0: High-value customers with high income and spending.
    - Cluster 1: Budget-conscious customers with moderate income and spending.  
    - Cluster 2: Occasional shoppers with low income and spending.
    - Cluster 3: Frequent shoppers with moderate income and high spending.
    - Cluster 4: New customers with low spending and high recency.
    - Cluster 5: Loyal customers with high spending and low recency.
    - Cluster 6: Inactive customers with low spending and high recency.
         """)