import pandas as pd
import pyarrow.parquet as pq
from datetime import datetime
import os

def main():
    # Konfigurasi File
    input_file = 'yellow_tripdata_2026-03.parquet'  # Ganti jika nama file beda
    output_file = 'hasil_analytic.csv'

    print(f"\n--- Mulai ETL pada {datetime.now().strftime('%H:%M:%S')} ---")

    # Cek apakah file input ada
    if not os.path.exists(input_file):
        print(f"❌ ERROR: File '{input_file}' tidak ditemukan di folder ini.")
        print("Pastikan file Parquet ada di folder yang sama dengan script ini.")
        return

    try:
        # 1. EXTRACT: Baca file Parquet
        print(f"📂 Membaca {input_file}...")
        df = pd.read_parquet(input_file)
        print(f"   ✅ Berhasil membaca {len(df):,} baris data.")
        print(f"   Kolom yang ditemukan: {list(df.columns)}")

        # 2. TRANSFORM: Bersihkan & Hitung
        print("\n⚙️  Melakukan Transformasi...")
        
        # A. Bersihkan data: Hapus baris dengan nilai kosong (jika ada)
        df = df.dropna()

        print(f"   ✅ Transformasi selesai. Total baris akhir: {len(df):,}")

        # 3. LOAD: Simpan ke CSV (Siap untuk Dashboard)
        print(f"\n💾 Menyimpan hasil ke '{output_file}'...")
        encoding='utf-8-sig' # penting agar Excel/Looker Studio membaca karakter Indonesia dengan benar
        df.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"   ✅ File '{output_file}' berhasil dibuat!")

        # Tampilkan 5 baris pertama sebagai preview
        print("\n📊 Preview 5 Baris Pertama:")
        print(df.head().to_string())

        print("\n🎉 ETL Selesai! Silakan buka file CSV untuk dashboard.")

    except Exception as e:
        print(f"\n❌ Terjadi ERROR: {e}")
        print("Cek apakah tipe data di Parquet sesuai atau library sudah terinstall.")

if __name__ == "__main__":
    main()