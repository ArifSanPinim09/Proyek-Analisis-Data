import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Dapatkan lokasi file dengan pendekatan yang lebih aman
current_dir = os.path.dirname(os.path.abspath(__file__))  # Direktori tempat script ini berada
file_path = os.path.join(current_dir, "dashboard", "main_data.csv")

# Cek apakah file ada
if not os.path.exists(file_path):
    st.error("❌ File `main_data.csv` tidak ditemukan! Harap pastikan file berada di folder `dashboard`.")
    uploaded_file = st.file_uploader("Atau unggah file CSV secara manual:", type=["csv"])
    if uploaded_file is not None:
        day_df = pd.read_csv(uploaded_file)
        st.success("✅ File berhasil diunggah dan dimuat!")
    else:
        st.stop()  # Menghentikan eksekusi Streamlit jika file belum ada
else:
    day_df = pd.read_csv(file_path)
    st.success(f"✅ File ditemukan di {file_path}")

# Konversi tanggal
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Sidebar filter
st.sidebar.header("Filter Data")
year_filter = st.sidebar.multiselect("Pilih Tahun:", day_df['yr'].unique(), format_func=lambda x: "2011" if x == 0 else "2012")
season_filter = st.sidebar.multiselect("Pilih Musim:", day_df['season'].unique(), format_func=lambda x: ["Spring", "Summer", "Fall", "Winter"][x-1])

# Terapkan filter
df_filtered = day_df.copy()
if year_filter:
    df_filtered = df_filtered[df_filtered['yr'].isin(year_filter)]
if season_filter:
    df_filtered = df_filtered[df_filtered['season'].isin(season_filter)]

# Tampilan dashboard
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
