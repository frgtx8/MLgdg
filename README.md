# Proyek Analisis Data: Bike Sharing Analysis

## Deskripsi
Proyek ini melakukan analisis data end-to-end pada dataset Bike Sharing untuk memahami pola penyewaan sepeda berdasarkan musim dan tren tahunan. Proyek ini juga mengimplementasikan Machine Learning sederhana (Linear Regression) untuk prediksi.

## Dataset
Bike Sharing Dataset

## Teknologi yang Digunakan
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- Jupyter Notebook
- Streamlit (Dashboard)

## Cara Menjalankan Dashboard
1. Pastikan library terinstall:
   ```bash
   pip install -r requirements.txt
2. Jalankan streamlit
   ```bash
   streamlit run dashboard.py
   
## Ringkasan Insight Hasil Analisis

Berdasarkan seluruh tahapan analisis (dari Data Wrangling, EDA, hingga Visualisasi), berikut adalah temuan-temuan utama:
1.  Pengaruh Musim (Seasonality):
    Analisis menunjukkan bahwa musim memiliki dampak besar terhadap perilaku penyewaan sepeda. Musim Gugur (Fall) konsisten menjadi periode dengan rata-rata penyewaan tertinggi. Sebaliknya, Musim Semi (Spring) memiliki jumlah penyewaan terendah. Hal ini memberikan insight bahwa pengguna lebih suka bersepeda saat cuaca mulai stabil dan sejuk, bukan saat transisi musim dingin ke semi yang mungkin masih terlalu dingin atau basah.
2.  Tren Pertumbuhan Bisnis (Yearly Trend):
    Terdapat peningkatan performa bisnis yang signifikan dari tahun 2011 ke 2012. Rata-rata penyewaan harian di tahun 2012 jauh lebih tinggi dibandingkan tahun sebelumnya. Ini menandakan strategi bisnis berjalan baik dan popularitas layanan *bike sharing* ini sedang meningkat (growing).
3.  Faktor Cuaca (Weather Impact):
    Suhu (Temperature) adalah faktor lingkungan yang paling berkorelasi positif dengan jumlah penyewaan. Semakin hangat suhu (hingga batas wajar), semakin banyak orang yang menyewa sepeda. Sebaliknya, kelembaban tinggi dan angin kencang cenderung menurunkan minat penyewaan, meskipun pengaruhnya tidak sekuat suhu.
