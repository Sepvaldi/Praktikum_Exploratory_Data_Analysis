import pandas as pd
import numpy as np

# 1. Baca data dari file CSV
df = pd.read_csv('dataset_nilai_akademik_siswa.csv')

# 2. Hapus baris data yang kembar (duplikat)
df = df.drop_duplicates()

# 3. Bersihkan kolom 'nilai' (buang teks 'poin', ganti 999 jadi kosong, ubah ke angka)
df['nilai'] = df['nilai'].astype(str).str.replace('poin', '').str.strip()
df['nilai'] = df['nilai'].replace('999', np.nan)
df['nilai'] = pd.to_numeric(df['nilai'], errors='coerce')

# 4. Isi nilai yang kosong dengan nilai rata-rata keseluruhan
df['nilai'] = df['nilai'].fillna(df['nilai'].mean()).round(2)

# 5. Ubah teks bulan 'Agustus' jadi 'August' agar tanggal bisa dibaca
df['tanggal_ujian'] = df['tanggal_ujian'].astype(str).str.replace('Agustus', 'August', case=False)
df['tanggal_ujian'] = pd.to_datetime(df['tanggal_ujian'], format='mixed', dayfirst=True)

# 6. Rapikan kolom lainnya
df['jenis_ujian'] = df['jenis_ujian'].str.upper()
df['guru_pengampu'] = df['guru_pengampu'].fillna('Belum Terdata')

# 7. Tampilkan hasil 5 baris pertama
print("=== DATA SETELAH DIBERSIHKAN ===")
print(df.head())

# Pertanyaan
# Jawaban Pertanyaan 1: Rata-rata per mata pelajaran
print("\nRata-rata Nilai per Mata Pelajaran:")
print(df.groupby('mata_pelajaran')['nilai'].mean().round(2))

# Jawaban Pertanyaan 3: Siswa remedial (< 75)
remedial_df = df[df['nilai'] < 75]
print(f"\nJumlah siswa yang butuh remedial: {remedial_df['nama'].nunique()} siswa")

# Menghitung jumlah baris duplikat yang kembar
total_duplikat = df.duplicated().sum()
print(f"Total baris duplikat: {total_duplikat} baris")