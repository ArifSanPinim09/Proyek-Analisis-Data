import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
df = pd.read_csv(file_path)


df['dteday'] = pd.to_datetime(df['dteday'])


df['day_type'] = df['workingday'].map({0: "Akhir Pekan", 1: "Hari Kerja"})


st.sidebar.header("📊 Filter Data")
year_filter = st.sidebar.multiselect("📆 Pilih Tahun:", df['yr'].unique(), format_func=lambda x: "2011" if x == 0 else "2012")
day_type_filter = st.sidebar.multiselect("🗓️ Pilih Jenis Hari:", df['day_type'].unique())


df_filtered = df.copy()
if year_filter:
    df_filtered = df_filtered[df_filtered['yr'].isin(year_filter)]
if day_type_filter:
    df_filtered = df_filtered[df_filtered['day_type'].isin(day_type_filter)]


st.title("📊 Dashboard Penyewaan Sepeda")


total_rentals = df_filtered['cnt'].sum()
avg_rentals = int(df_filtered['cnt'].mean())
max_rental = df_filtered['cnt'].max()

col1, col2, col3 = st.columns(3)
col1.metric("📈 Total Penyewaan", f"{total_rentals:,}")
col2.metric("📊 Rata-rata Penyewaan", f"{avg_rentals:,}")
col3.metric("🏆 Sewa Tertinggi", f"{max_rental:,}")


st.subheader("📈 Tren Penyewaan Sepeda (2011-2012)")
yearly_trend = df_filtered.groupby("yr")["cnt"].sum().reset_index()
yearly_trend["yr"] = yearly_trend["yr"].map({0: "2011", 1: "2012"})

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="yr", y="cnt", data=yearly_trend, color="royalblue", ax=ax)
ax.set_xlabel("Tahun")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Sepeda per Tahun")
st.pyplot(fig)


st.subheader("📅 Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
workday_trend = df_filtered.groupby("day_type")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="day_type", y="cnt", data=workday_trend, color="royalblue", ax=ax)
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
st.pyplot(fig)


st.markdown("📌 **Kesimpulan:**")
st.markdown("- 🚴 Penyewaan meningkat dari 2011 ke 2012.")
st.markdown("- 📅 Hari kerja memiliki jumlah penyewaan lebih tinggi dibanding akhir pekan.")
