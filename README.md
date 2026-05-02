# House Prices Prediction API

Proyek ini menyediakan API sederhana untuk memprediksi harga jual rumah berdasarkan berbagai fitur properti menggunakan dataset *Ames Housing*. API ini dibangun menggunakan framework **FastAPI** dan model machine learning **Gradient Boosting Regressor**.

## Deskripsi Proyek

Proyek ini dikembangkan berdasarkan materi dari **course Dicoding**. Tujuan utamanya adalah untuk mendemonstrasikan bagaimana model machine learning yang telah dilatih dapat di-*deploy* sebagai layanan web (API). Pengguna dapat mengirimkan data spesifikasi rumah dalam format JSON, dan API akan mengembalikan estimasi harga jual (`SalePrice`).

### Fitur Utama:
- **FastAPI**: Digunakan untuk membangun endpoint RESTful yang cepat dan efisien.
- **Pydantic**: Digunakan untuk validasi skema data input.
- **Scikit-learn**: Model prediksi menggunakan algoritma `GradientBoostingRegressor`.
- **Joblib**: Digunakan untuk memuat model yang telah dilatih secara serial.

## Teknologi yang Digunakan
- Python 3.x
- FastAPI
- Uvicorn (ASGI Server)
- Scikit-learn
- Pandas
- Joblib

## Cara Menjalankan

1.  **Install Dependensi:**
    Pastikan Anda telah menginstal semua pustaka yang diperlukan:
    ```bash
    pip install fastapi uvicorn pandas scikit-learn joblib
    ```

2.  **Siapkan Model:**
    Pastikan file model `gbr_model.joblib` berada di direktori yang sama dengan `main.py`.

3.  **Jalankan Server:**
    ```bash
    python main.py
    ```
    API akan berjalan secara default di `http://127.0.0.1:8000`.

4.  **Akses Dokumentasi API:**
    Buka browser dan navigasikan ke `http://127.0.0.1:8000/docs` untuk mencoba API melalui antarmuka Swagger UI.

## Struktur Endpoint
- `POST /predict`: Mengirimkan parameter rumah untuk mendapatkan prediksi harga.

---

## ⚠️ Disclaimer

Proyek ini dibuat untuk tujuan pembelajaran dan dokumentasi **alur kerja (workflow) Machine Learning** dasar, mulai dari pemuatan model hingga penyajian (serving) melalui API. 

Harap dicatat bahwa:
- Implementasi ini **tidak ditujukan** untuk penggunaan produksi berskala besar.
- Proses *feature engineering*, penanganan *missing values*, dan optimasi hyperparameter dalam kode ini mungkin belum mencapai tahap yang paling optimal atau kompleks.
- Fokus utama adalah pada integrasi sistem daripada performa absolut dari model prediksinya.
---
