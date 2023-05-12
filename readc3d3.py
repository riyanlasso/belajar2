# import c3d

# # membuka file c3d
# with open('currentFrame447.c3d', 'rb') as handle:
#     reader = c3d.Reader(handle)

#     # membaca header file c3d
    

#     # menampilkan nama-nama marker
#     markers = reader.point_labels
#     print(markers)

#     # menampilkan koordinat marker tertentu
#     marker_name = 'RPSI'  # ganti dengan nama marker yang ingin ditampilkan
#     marker_index = None
#     for i, name in enumerate(markers):
#         if name == marker_name:
#             marker_index = i
#             break
#     if marker_index is not None:
#         for frame_no, points, analog in reader.read_frames():
#             x, y, z = points[marker_index]
#             print(f"Frame {frame_no}: {marker_name} = ({x}, {y}, {z})")
#     else:
#         print(f"Marker {marker_name} not found in file.")
arr = ["apple", "banana", "cherry","Mangga"] * 20

# mengambil nilai pada indeks ke-10 dan ke-50 dengan satu variabel
nilai = (arr[10],arr[19],arr[31],arr[22], arr[50])

# menampilkan nilai
print(nilai)