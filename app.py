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


# Dropdown untuk memilih agensi
company = st.selectbox("Pilih Agensi:", ["All"] + list(df['Company'].dropna().unique()))

# Filter DataFrame berdasarkan pilihan agensi
if company != "All":
    df_company = df[df['Company'] == company]
else:
    df_company = df

# Menampilkan tabel grup dari agensi yang dipilih
st.subheader(f"Group dari Agensi: {company}")
st.dataframe(df_company[['Group']].drop_duplicates())
