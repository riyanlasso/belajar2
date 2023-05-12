import c3d
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

with open('446447.c3d', 'rb') as handle:
    reader = c3d.Reader(handle)
    
    frames = []
#1
    # for i, points, analog in reader.read_frames():
    #     print(f'Frame {i}:')
    #     for j, marker in enumerate(markers):
    #         x = np.array(points[j])
    #         sumbuX = np.array(points[:, 0])
    #         #print(marker,x)

#2
# points_data = []
# markers_data = []
# # for item in enumerate(markers):
# #     markers_data.append(item)
# for item2 in enumerate(points):
#     points_data.append(item2)

#df = pd.DataFrame(points_data,columns=['1','2'])
#print(df)

#3
    markers = reader.point_labels 
    
    x_data, y_data, z_data = [], [], [], 
    
    frame_no_list = []
    
    scoring_x,scoring_y,scoring_z, = [], [], []
    
    markers_to_show = []

    # marker_indices = [i for i, label in enumerate(reader.point_labels) if label in markers_to_show]
    # markers_list = []

    # for frame_no, points, analog in reader.read_frames():
    #     frame_no_list.append(frame_no)
    #     x_data.append(points[:,0])
    #     y_data.append(points[:,1])
    #     z_data.append(points[:,2])

    markers_to_show.append(markers) # memasukkan nilai dari markers ke variabel markers_to_show
    # print(markers_to_show)
    #menghilangkan spasi
    markers_list = (markers_to_show[0])
    markers_list[0] = markers_list[0].replace(" ", "")
    markers_list[1]= markers_list[1].replace(" ", "")
    markers_list[49]= markers_list[49].replace(" ", "")
    markers_list[38]= markers_list[38].replace(" ", "")
    markers_list[39]= markers_list[39].replace(" ", "")
    markers_list[48]= markers_list[48].replace(" ", "")
    markers_list[40]= markers_list[40].replace(" ", "")
    markers_list[47]= markers_list[47].replace(" ", "")
    markers_list[39]= markers_list[39].replace(" ", "")
    markers_list[48]= markers_list[48].replace(" ", "")
    markers_list[41]= markers_list[41].replace(" ", "")
    markers_list[42]= markers_list[42].replace(" ", "")
    markers_list[43]= markers_list[43].replace(" ", "")
    markers_list[46]= markers_list[46].replace(" ", "")
    markers_list[45]= markers_list[45].replace(" ", "")
    markers_list[44]= markers_list[44].replace(" ", "")
    
    # nama marker
    markers_fix = [markers_list[0],markers_list[1],
                   markers_list[49],markers_list[38],
                   markers_list[39],markers_list[48],
                   markers_list[40],markers_list[47],
                   markers_list[39],markers_list[48],
                   markers_list[41],markers_list[42],
                   markers_list[43],markers_list[46],
                   markers_list[45],markers_list[44],] 
    # print(markers_fix)
    markers_fix2 = []
    #points
    points_data = []
    for frame_no, points, analog in reader.read_frames():
        frame_no_list.append(frame_no)
        # points_data.append(points[:, 0])
        # print(points_data)
        for i, label in enumerate(markers_fix):
            # markers_fix2.append(label)
            # print(label)
            if label in markers_fix:
                x_data.append(points[i, 0])
                y_data.append(points[i, 1])
                z_data.append(points[i, 2])
                
                # for i in [0, 2]:
                #     label = markers_fix[i]
                #     x_data.append(points[i, 0])
                #     y_data.append(points[i, 1])
                #     z_data.append(points[i, 2])
    # print(x_data)            
    # print(markers_fix2)                    
    # print(points) 
    # print(x_data)       
    # print('')
    # print(y_data)        
    # print('')
    # print(z_data)
    
    
    df = pd.DataFrame({
                'Frame': frame_no_list * len(markers_fix),
                'Marker': np.repeat(markers_fix, len(frame_no_list)),
                'X': np.array(x_data).flatten(),
                'Y': np.array(y_data).flatten(),
                'Z': np.array(z_data).flatten(),
                })
    print(df)
    

# data_arr = np.array(points) 
# data_1d = data_arr.flatten()
# # df1 = pd.DataFrame(i,frames, columns=points)      

# min_length = min(len(frame_no_list), len(markers_list), len(x_data), len(y_data), len(z_data))
    # frame_no_list = frame_no_list[:min_length]
    # markers_list = markers_list[:min_length]
    # x_data = x_data[:min_length]
    # y_data = y_data[:min_length]
    # z_data = z_data[:min_length]

#print
# wb = Workbook()
# ws = wb.active
# for r in dataframe_to_rows(df, index=True, header=True):
#     ws.append(r)  
# wb.save('cobabaru3.xlsx')

# notes
# harus memecah variabel X,Y,Z
# convert ke xlsx
# membandingkan nilai koordinat X dengan X yang lain untuk scoring
# hasil XYZ masih salah, harus ada kondisi atau perulangan sekali lagi
# array_pertama = [1, 2, 3, 4, 5]
# array_kedua = [4, 5, 6, 7, 8]

# for angka in array_pertama:
#     if angka in array_kedua:
#         print(f'angka {angka} ada di keduanya')
            
import c3d
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

with open('currentFrame447.c3d', 'rb') as handle:
    reader = c3d.Reader(handle)
    markers = reader.point_labels
    print(markers)
    frames = []
    markers_to_show = []
    markers_to_show.append(markers)
    #menghilangkan spasi
    markers_list = (markers_to_show[0])
    markers_list[0] = markers_list[0].replace(" ", "")
    markers_list[1]= markers_list[1].replace(" ", "")
    markers_list[49]= markers_list[49].replace(" ", "")
    markers_list[38]= markers_list[38].replace(" ", "")
    markers_list[39]= markers_list[39].replace(" ", "")
    markers_list[48]= markers_list[48].replace(" ", "")
    markers_list[40]= markers_list[40].replace(" ", "")
    markers_list[47]= markers_list[47].replace(" ", "")
    markers_list[39]= markers_list[39].replace(" ", "")
    markers_list[48]= markers_list[48].replace(" ", "")
    markers_list[41]= markers_list[41].replace(" ", "")
    markers_list[42]= markers_list[42].replace(" ", "")
    markers_list[43]= markers_list[43].replace(" ", "")
    markers_list[46]= markers_list[46].replace(" ", "")
    markers_list[45]= markers_list[45].replace(" ", "")
    markers_list[44]= markers_list[44].replace(" ", "")
    
    # nama marker
    markers_fix = [markers_list[0],markers_list[1],
                   markers_list[44],markers_list[49],
                   markers_list[38],
                   markers_list[39],markers_list[48],
                   markers_list[40],markers_list[47],
                   markers_list[39],markers_list[48],
                   markers_list[41],markers_list[42],
                   markers_list[43],markers_list[46],
                   markers_list[45],]
    # print(markers_fix)

    x_data, y_data, z_data = [], [], [],

    for i, points, analog in reader.read_frames():

        for j, marker in enumerate(markers):
            # x = np.array(points[j])
            # KONDISI untuk cek nilainya apakah milik marker tersebut     
            if marker == markers_fix[0]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])

                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
                # print(x_data,y_data,z_data)

            elif marker == markers_fix[1]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[2]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[3]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[4]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[5]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[6]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[7]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[8]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[9]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[10]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[11]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[12]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[13]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[14]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[15]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            else : 
                continue
            
    # df = pd.DataFrame({
    #             'Frame': i * len(markers_fix),
    #             'Marker': np.repeat(markers_fix, len(i)),
    #             'X': np.array(x_data).flatten(),
    #             'Y': np.array(y_data).flatten(),
    #             'Z': np.array(z_data).flatten(),
    #             })
    # print(df)
    
    #dibalik

    # for j, marker in enumerate(markers):
    #     # print(marker)
    #     for i, points, analog in reader.read_frames():
            
    #         x = np.array(points[j])
    #         sumbuX = np.array(points[j, 0])
    #         sumbuY = np.array(points[j, 1])
    #         sumbuZ = np.array(points[j, 2])
    #         # print(f'Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
    #         # print(x)

# markers = {
#     'X': (1, 2, 3),
#     'O': (4, 5, 6),
#     'Y': (7, 8, 9)
# }

# for marker_name in markers:
#     # marker = markers[marker_name]
#     # x, y, z = marker
#     print(markers)
#     # if marker_name == 'X':
#     #     print(f"Marker {marker_name} berada di koordinat ({x}, {y}, {z})")
#     # elif marker_name == 'O':
#     #     print(f"Marker {marker_name} berada di koordinat ({x}, {y}, {z})")
#     # elif marker_name == 'Y':
#     #     print(f"Marker {marker_name} berada di koordinat ({x}, {y}, {z})")
#     # else:
#     #     print(f"Tidak ada marker dengan nama yang cocok")

