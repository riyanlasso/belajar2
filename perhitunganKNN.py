# Ambil data dari database
# contoh KNN
# dataset = [18,162,skoring RTOE - LASI]
dataset = []    
new_data = [6, 2]
k = 3

distances = []
# rumus eucledian distance
for data in dataset:
    dist = ((data[0] - new_data[0])**2 + (data[1] - new_data[1])**2)**0.5 
    distances.append([dist, data[2]])
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
