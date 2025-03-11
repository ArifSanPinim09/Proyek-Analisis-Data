# 📊 Proyek Analisis Data: Penyewaan Sepeda

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis tren penyewaan sepeda berdasarkan berbagai faktor seperti tahun, hari kerja, dan cuaca. Analisis dilakukan menggunakan Python, dan hasilnya divisualisasikan melalui dashboard interaktif dengan Streamlit.

## 💂‍️ Struktur Folder
```
submission
├───dashboard
│   ├───main_data.csv
│   └───dashboard.py
├───data
│   ├───day.csv
│   └───hour.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## 🚀 Cara Menjalankan Proyek
### 1️⃣ Menjalankan Notebook
Buka dan jalankan `notebook.ipynb` untuk melihat analisis data secara menyeluruh.

### 2️⃣ Menjalankan Dashboard
1. Pastikan semua dependensi telah terinstal dengan menjalankan:
   ```sh
   pip install -r requirements.txt
   ```
2. Jalankan Streamlit dengan perintah:
   ```sh
   streamlit run dashboard.py
   ```
3. Buka link yang muncul di terminal untuk mengakses dashboard interaktif.

## 📊 Fitur Dashboard
Dashboard ini memiliki beberapa fitur analisis yang dapat dieksplorasi secara interaktif:
- 📅 **Tren Penyewaan Sepeda**: Visualisasi jumlah penyewaan sepeda dari tahun 2011 ke 2012.
- 🏢 **Penyewaan Sepeda per Hari**: Perbandingan penyewaan sepeda antara hari kerja dan akhir pekan.
- ⛅ **Pengaruh Cuaca**: Analisis dampak kondisi cuaca terhadap jumlah penyewaan sepeda.
- 🔍 **Filter Interaktif**: Memungkinkan pengguna untuk melakukan eksplorasi data berdasarkan musim dan kondisi cuaca.

## 📃 Dependensi
Pastikan Anda memiliki dependensi berikut:
- Python 3.x
- Streamlit
- Pandas
- Seaborn
- Matplotlib

Semua dependensi dapat diinstal dengan:
```sh
pip install -r requirements.txt
```

## 📚 Sumber Data
Dataset yang digunakan dalam proyek ini berasal dari **Penyewaan Sepeda**, yang mencakup data penyewaan berdasarkan faktor-faktor cuaca, hari kerja, dan tahun.

## 👥 Kontributor
- Arifsan Pinim

## 📚 Lisensi
Proyek ini berlisensi MIT. Anda bebas untuk menggunakan dan memodifikasinya sesuai kebutuhan.