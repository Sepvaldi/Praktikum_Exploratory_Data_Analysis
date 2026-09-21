import numpy as np
import pandas as pd

#Latihan 1: Operasi Dasar Numpy Array
harga = np.array([5000, 7000, 300, 12000, 4500])
print('Rata-rata harga:', harga.mean())
print("Harga tertinggi", harga.max())
print("Harga setelah diskon 10%", harga * 0.9)
#Analisis 1 = Karena duplikasi hanya bisa dilakukan sebanyak bilangan bulat (integer), mengalikan list dengan float seperti 0.9 akan memicu error.

print('')
#Latihan 2: Membuat Series & DataFrame
data_kantin = {
        'menu': ['Nasi Goreng', 'Es Teh', 'Mie Ayam', 'Es Teh', None],
        'harga': [12000, 4000, 10000, 4000, 8000],
        'terjual': [23, 40, None, 35, 18]
}
df = pd.DataFrame(data_kantin)
#Analisis 2 - none ada di menu nomor 4, dan terjual ke 2, saat di run maka akan ada tulisan nan atau nilai tidak di ketahui
print(df)

print("")
#Latihan 3: Data Loading & Inspection
df = pd.read_csv('data_kantin.csv')
print(df.head()) # 5 baris pertama
print(df.info()) # tipe data & jumlah non-null tiap kolom
print(df.describe()) # statistik ringkas kolom numerik
print(df.shape) # jumlah (baris, kolom)

print("")
#Latihan 4: Menangani Missing Value
print(df.isnull().sum()) # jumlah data kosong tiap kolom
df['terjual'] = df['terjual'].fillna(0) # isi kekosongan dengan 0
df = df.dropna(subset=['menu']) # hapus baris jika kolom menu kosong

print('')
#Latihan 5: Menangani Duplikat dan Tipe Data
print(df.duplicated().sum()) # jumlah baris duplikat
df = df.drop_duplicates()
df['harga'] = df['harga'].astype(int) # memastikan tipe data harga adalah integer

print('')
#Latihan 6: Data Manipulation (Filtering, Sorting, Groupby)
laris = df[df['terjual'] > 20] # filtering
urut = df.sort_values(by='terjual', ascending=False) # sorting
df['total_pendapatan'] = df['harga'] * df['terjual'] # kolom turunan
ringkasan = df.groupby('menu')['total_pendapatan'].sum() # agregasi
print(ringkasan)