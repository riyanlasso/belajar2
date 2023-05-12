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

with open('446447.c3d', 'rb') as handle:
    reader = c3d.Reader(handle)
    markers = reader.point_labels
    # print(markers)
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
    markers_list[50]= markers_list[50].replace(" ", "")
    markers_list[51]= markers_list[51].replace(" ", "")
    markers_list[41]= markers_list[41].replace(" ", "")
    markers_list[42]= markers_list[42].replace(" ", "")
    markers_list[43]= markers_list[43].replace(" ", "")
    markers_list[46]= markers_list[46].replace(" ", "")
    markers_list[45]= markers_list[45].replace(" ", "")
    markers_list[44]= markers_list[44].replace(" ", "")
    
    # nama marker
    markers_fix = [markers_list[0],markers_list[1],markers_list[38],markers_list[39],markers_list[40],
                   markers_list[41],markers_list[42],markers_list[43],markers_list[44],markers_list[45],
                   markers_list[46],markers_list[47],markers_list[48],markers_list[49],markers_list[50],
                   markers_list[51]]
    print(markers_fix)

    x_data, y_data, z_data = [], [], [],
    frame_no_list = []
    #pisahkan data
    #start
    fusion = []
    for i, points, analog in reader.read_frames():
        frame_no_list.append(i)
        print(f'Frame {i}:')
        # perulangan sejumlah banyak markers
        # yang ditampilkan yang di if saja, jika tidak ada di kondisi maka continue
        # urutan perulangan masih sama dengan markers
        for j, marker in enumerate(markers):
            # x = np.array(points[j])
            # KONDISI untuk cek nilainya apakah milik marker tersebut     
            if marker == markers_fix[0]:
                namaMarker = marker
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])

                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                # marker1 = np.concatenate((frame_no_list,x_data,y_data,z_data))
                # x = f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}'
                # fusion.append(x)
                
                print(f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
                # print(x)

            elif marker == markers_fix[1]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                namaMarker = marker
                x = f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}'
                # fusion.append(x)
                # print(x)
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )

            elif marker == markers_fix[2]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[3]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[4]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[5]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[6]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[7]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[8]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[9]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[10]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[11]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[12]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[13]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[14]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            elif marker == markers_fix[15]:
                sumbuX = np.array(points[j, 0])
                sumbuY = np.array(points[j, 1])
                sumbuZ = np.array(points[j, 2])
                x_data.append(points[j, 0])
                y_data.append(points[j, 1])
                z_data.append(points[j, 2])
                print(f'Frame {i} Marker : {marker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}' )
            else : 
                
                continue         
    #end
    

    # new_x,new_y,new_z = [],[],[]
    # new_x.append(x_data)
    # new_y.append(y_data)
    # new_z.append(z_data)
    
    # df = pd.DataFrame({'x_data': new_x, 'y_data': new_y, 'z_data': new_z})
    # print(markers_fix)
    
    # print(fusion)
    
    df = pd.DataFrame({
                # 'Frame ': frame_no_list * len(markers_fix),
                'Marker': markers_fix * len(frame_no_list),
                'X': np.array(x_data).flatten(),
                'Y': np.array(y_data).flatten(),
                'Z': np.array(z_data).flatten(),
                })
    print(df)
    
    

    # print
    # wb = Workbook()
    # ws = wb.active
    # for r in dataframe_to_rows(df, index=True, header=True):
    #     ws.append(r)  
    # wb.save('cobaFix2.xlsx')
    
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
