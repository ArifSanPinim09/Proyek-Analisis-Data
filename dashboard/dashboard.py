import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


file_path = "main_data.csv"  

if os.path.exists(file_path):
    st.success(f"✅ File ditemukan: {file_path}")
else:
    st.error("❌ File tidak ditemukan! Pastikan file sudah diunggah ke GitHub dan berada di direktori yang benar.")

# Jika file ditemukan, load data
if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    st.write(df.head())
else:
    st.stop()  # Hentikan Streamlit jika file tidak ditemukan


st.sidebar.header("Filter Data")
year_filter = st.sidebar.multiselect("Pilih Tahun:", df['yr'].unique(), format_func=lambda x: "2011" if x == 0 else "2012")
season_filter = st.sidebar.multiselect("Pilih Musim:", df['season'].unique(), format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1])

df_filtered = df.copy()
if year_filter:
    df_filtered = df_filtered[df_filtered['yr'].isin(year_filter)]
if season_filter:
    df_filtered = df_filtered[df_filtered['season'].isin(season_filter)]


st.title("📊 Dashboard Penyewaan Sepeda")
st.markdown("""
**Analisis Penyewaan Sepeda Tahun 2011-2012**
- **Apakah ada tren peningkatan jumlah penyewaan sepeda dari 2011 ke 2012?**
- **Bagaimana perbedaan jumlah penyewaan antara hari kerja dan akhir pekan?**
""")

# Grafik Tren Penyewaan Sepeda
st.subheader("📈 Tren Penyewaan Sepeda (2011-2012)")
yearly_trend = df_filtered.groupby("yr")["cnt"].sum().reset_index()
yearly_trend["yr"] = yearly_trend["yr"].map({0: "2011", 1: "2012"})
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="yr", y="cnt", data=yearly_trend, palette="coolwarm", ax=ax)
ax.set_xlabel("Tahun")
ax.set_ylabel("Total Penyewaan")
ax.set_title("Total Penyewaan Sepeda per Tahun")
st.pyplot(fig)

# Grafik Hari Kerja vs Akhir Pekan
st.subheader("📅 Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
df_filtered["day_type"] = df_filtered["workingday"].map({0: "Akhir Pekan", 1: "Hari Kerja"})
workday_trend = df_filtered.groupby("day_type")["cnt"].mean().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="day_type", y="cnt", data=workday_trend, palette="viridis", ax=ax)
ax.set_xlabel("Jenis Hari")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_title("Rata-rata Penyewaan Sepeda: Hari Kerja vs Akhir Pekan")
st.pyplot(fig)

st.markdown("📌 **Kesimpulan:**\n")
st.markdown("- Jumlah penyewaan meningkat dari 2011 ke 2012.\n")
st.markdown("- Hari kerja memiliki jumlah penyewaan lebih tinggi dibanding akhir pekan.")