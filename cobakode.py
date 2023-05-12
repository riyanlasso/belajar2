# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
# list4 = [10, 11, 12]

# merged_list = []

# for i in range(len(list1)):
#     merged_list.append(list1[i])
#     merged_list.append(list2[i])
#     merged_list.append(list3[i])
#     merged_list.append(list4[i])

# print(merged_list)

# import pandas as pd

# # Membuat dataframe pertama
# df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
#                     'B': ['B0', 'B1', 'B2', 'B3'],
#                     'C': ['C0', 'C1', 'C2', 'C3'],
#                     'D': ['D0', 'D1', 'D2', 'D3']})

# # Membuat dataframe kedua dengan jumlah indeks yang berbeda
# df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6'],
#                     'B': ['B4', 'B5', 'B6'],
#                     'C': ['C4', 'C5', 'C6'],
#                     'D': ['D4', 'D5', 'D6']},
#                     index=[4, 5, 6])  # indeks pada df2 berbeda dengan df1

# # Menggabungkan kedua dataframe berdasarkan kolom A dan B
# merged_df = pd.merge(df1, df2, on=['A', 'B'])

# # Menyimpan hasil gabungan ke dalam file Excel
# merged_df.to_excel('hasil_gabungan.xlsx', index=False)

# import numpy as np
# from sklearn.neighbors import KNeighborsClassifier

# # Menentukan data latih
# X_train = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
# y_train = np.array([0, 0, 1, 1, 1]) # kelas untuk masing-masing data latih

# # Membuat model KNN dengan 3 tetangga terdekat
# knn = KNeighborsClassifier(n_neighbors=3)

# # Melatih model dengan data latih
# knn.fit(X_train, y_train)

# # Memprediksi kelas untuk data uji
# X_test = np.array([[4, 5], [8, 9]])
# y_pred = knn.predict(X_test)

# # Menampilkan hasil prediksi
# print("Hasil prediksi:", y_pred)

import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Iamironman123',
                             db='riyanlasso')


nama = ['John', 'Doe', 'Jane', 'riyan','doni']
umur = [25, 30, 27, 26,17]

# menghapus seluruh data tabel tanpa kehilangan struktur tabel (kolom)

cursor = connection.cursor()
truncate_query = "TRUNCATE TABLE coba"
cursor.execute(truncate_query)

# Looping untuk memasukkan data ke database

for i in range(len(nama)):

    with connection.cursor() as cursor:
        #     # Query SQL untuk memasukkan data
        sql = "INSERT INTO coba (id,nama,umur) VALUES (%s,%s, %s)"
        cursor.execute(sql, (i, nama[i], umur[i]))

    # # Commit perubahan ke database
    connection.commit()

# # Tutup koneksi ke database
connection.close()
