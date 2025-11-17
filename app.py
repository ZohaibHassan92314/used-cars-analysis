# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="PakWheels Used Cars Analysis", layout="wide")

st.title("🚗 PakWheels Used Cars Dashboard")

# --- Load CSV ---
@st.cache_data
def load_data():
    df = pd.read_csv("pakwheels_used_cars.csv")
    
    # Clean / format
    df['price'] = df['price'].astype(str).str.replace(",", "").str.extract(r"(\d+)").astype(float)
    df['year'] = df['year'].astype(str).str.extract(r"(\d{4})").astype(float)
    df['city'] = df['city'].astype(str).str.strip().str.title()
    return df

df = load_data()

st.subheader("Sample Data")
st.dataframe(df.head())

# --- Visualization 1: Car Count by City ---
st.subheader("🚙 Car Count by City")
city_counts = df['city'].value_counts()
st.bar_chart(city_counts)

# --- Visualization 2: Cars Listed by Year ---
st.subheader("📅 Cars Listed by Manufacturing Year")
year_counts = df['year'].value_counts().sort_index()
st.line_chart(year_counts)

# --- Visualization 3: Price Distribution ---
st.subheader("💰 Price Distribution")
fig, ax = plt.subplots(figsize=(10,4))
ax.hist(df['price'].dropna(), bins=20, color='skyblue', edgecolor='black')
ax.set_xlabel("Price (PKR)")
ax.set_ylabel("Number of Cars")
ax.set_title("Car Price Distribution")
st.pyplot(fig)

# --- Visualization 4: Top 10 Most Expensive Cars ---
st.subheader("🏆 Top 10 Most Expensive Cars")
top10 = df.nlargest(10, "price")
st.dataframe(top10[['title','model','year','price','city']])

# --- Visualization 5: Average Price by Year ---
st.subheader("📊 Average Price by Year")
avg_price = df.groupby("year")["price"].mean().sort_index()
st.line_chart(avg_price)
