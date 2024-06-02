import pandas as pd
import streamlit as st
import plotly.express as px

# Data dictionary
data = pd.read_csv('kpopidolsv3.csv')

# Membuat DataFrame pandas dari data dictionary
df = pd.DataFrame(data)

# Membuat Streamlit app
st.title("Idol Dashboard")

# Dropdown untuk memilih gender
gender = st.selectbox("Pilih Gender:", ["All", "Male", "Female"])

# Filter DataFrame berdasarkan pilihan gender
if gender != "All":
    df = df[df['Gender'] == gender[0]]

# Membuat scatter plot menggunakan Plotly
fig = px.scatter(df, x='Height', y='Weight', color='Gender', hover_name='Stage Name', title='Height vs Weight')

# Menampilkan plot di Streamlit
st.plotly_chart(fig)
