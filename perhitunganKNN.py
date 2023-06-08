# Ambil data dari database
# contoh KNN
# dataset = [18,162,skoring RTOE - LASI]
import pymysql
connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='Iamironman123',
                                 db='riyanlasso')
cursor = connection.cursor()

# buat query untuk 
dataset = [[2, 4, 0], [4, 2, 1], [4, 4, 0], [4, 6, 1], [6, 4, 1], [6, 6, 1], [8, 4, 0], [8, 6, 0]]
dataset = []    
new_data = [6, 2]
k = 3

distances = []
# rumus eucledian distance
for data in dataset:
    dist = ((data[0] - new_data[0])**2 + (data[1] - new_data[1])**2)**0.5 
    distances.append([dist, data[2]])
print()
distances.sort()
neighbors = distances[:k]
votes = [0, 0]
for neighbor in neighbors:
    if neighbor[1] == 0:
        votes[0] += 1
    else:
        votes[1] += 1

if votes[0] > votes[1]:
    print("Data baru termasuk ke kelas 0")
else:
    print("Data baru termasuk ke kelas 1")

# pada website
# 1. bisa inputkan data training : kondisi jika tidak ada data training maka tidak bisa excecute
# 2. bisa input data testing dengan file .c3d
# 3. memunculkan grafik perbedaan data antar personal
# 4. memunculkan akurasi terdeteksi sebagai orang ini