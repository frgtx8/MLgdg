import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    df['season_label'] = df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
    df['year_label'] = df['yr'].map({0: 2011, 1: 2012})
    return df

df = load_data()

# Sidebar
st.sidebar.title("🚴 Bike Sharing Dashboard")
st.sidebar.markdown("**Fadhil Rahman**")
selected_year = st.sidebar.multiselect("Pilih Tahun", df['year_label'].unique(), default=df['year_label'].unique())

# Filter Data
filtered_df = df[df['year_label'].isin(selected_year)]

# Main Page
st.title("Analisis Performa Bike Sharing")

# Metrics
col1, col2 = st.columns(2)
col1.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric("Rata-rata Harian", f"{filtered_df['cnt'].mean():.0f}")

# Chart 1: Season Analysis
st.subheader("Penyewaan Berdasarkan Musim")
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(x='season_label', y='cnt', data=filtered_df, estimator='mean', order=['Spring', 'Summer', 'Fall', 'Winter'], palette='viridis', ax=ax1)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Sewa")
st.pyplot(fig1)

# Chart 2: Daily Trend
st.subheader("Tren Penyewaan Harian")
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.lineplot(x='dteday', y='cnt', data=filtered_df, hue='year_label', palette='coolwarm', ax=ax2)
ax2.set_xlabel("Tanggal")
ax2.set_ylabel("Jumlah Sewa")
st.pyplot(fig2)

st.caption("Copyright (c) Fadhil Rahman 2025")