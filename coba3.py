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
    # print(markers_to_show)
    # menghilangkan spasi
    markers_list = (markers_to_show[0])
    markers_list[0] = markers_list[0].replace(" ", "")
    markers_list[1] = markers_list[1].replace(" ", "")
    markers_list[49] = markers_list[49].replace(" ", "")
    markers_list[38] = markers_list[38].replace(" ", "")
    markers_list[39] = markers_list[39].replace(" ", "")
    markers_list[48] = markers_list[48].replace(" ", "")
    markers_list[40] = markers_list[40].replace(" ", "")
    markers_list[47] = markers_list[47].replace(" ", "")
    markers_list[50] = markers_list[50].replace(" ", "")
    markers_list[51] = markers_list[51].replace(" ", "")
    markers_list[41] = markers_list[41].replace(" ", "")
    markers_list[42] = markers_list[42].replace(" ", "")
    markers_list[43] = markers_list[43].replace(" ", "")
    markers_list[46] = markers_list[46].replace(" ", "")
    markers_list[45] = markers_list[45].replace(" ", "")
    markers_list[44] = markers_list[44].replace(" ", "")

    # nama marker
    markers_fix = [markers_list[0], markers_list[1], markers_list[38], markers_list[39], markers_list[40],
                   markers_list[41], markers_list[42], markers_list[43], markers_list[44], markers_list[45],
                   markers_list[46], markers_list[47], markers_list[48], markers_list[49], markers_list[50],
                   markers_list[51]]
    # print(markers_fix)

    x_data, y_data, z_data = [], [], [],

    scoringXdata, scoringYdata, scoringZdata = [], [], [],

    frame_no_list = []
    # pisahkan data
    # start
    frame_data = []
    for q, points, analog in reader.read_frames():
        # print(q)
        frame_no_list.append(q)
    # print(frame_no_list)

    # indexArray = []
    # for c in range(len(frame_no_list)):
    #     indexArray.append(c)
    # print(indexArray)
    data_dict = {}
    prev_x_data = None
    prev_y_data = None
    prev_z_data = None
    for i, points, analog in reader.read_frames():
        # frame_no_list.append(i)
        # print(i)
        # count += (0 * i) + 1
        # print(frame_no_list)
        if i in frame_no_list:
            # print(f'Frame {i}:')
            # perulangan sejumlah banyak markers
            # yang ditampilkan yang di if saja, jika tidak ada di kondisi maka continue
            # urutan perulangan masih sama dengan markers
            for j, marker in enumerate(markers):
                # x = np.array(points[j])
                # KONDISI untuk cek nilainya apakah milik marker tersebut berdasarkan frame
                if marker in markers_fix:
                    # baca marker
                    namaMarker = marker
                    sumbuX = np.array(points[j, 0])
                    sumbuY = np.array(points[j, 1])
                    sumbuZ = np.array(points[j, 2])

                    # masukkan data ke array
                    x_data.append(points[j, 0])
                    y_data.append(points[j, 1])
                    z_data.append(points[j, 2])
                    frame_data.append(i)

                    print(
                        f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    
                    
                    # if prev_x_data is not None :
                    #     diffX = sumbuX - prev_x_data[j]
                    #     diffY = sumbuY - prev_y_data[j]
                    #     diffZ = sumbuZ - prev_z_data[j]
                    #     print(f'Frame {i} : {namaMarker} Scoring X : {diffX} Scoring Y : {diffY} Scoring Z : {diffZ}')
                    # prev_x_data = np.copy(points[:, 0])
                    # prev_y_data = np.copy(points[:, 1])
                    # prev_z_data = np.copy(points[:, 2])
                    
                # Skoring
    
    # print(x_data)

    for x in range(len(x_data)):
        if x < len(x_data)-1:
            # print(x_data[x])
            if x_data[x] < x_data[x+1]:
                skorX = x_data[x+1] - x_data[x]
                scoringXdata.append(skorX)
            elif x_data[x] > x_data[x+1] :
                skorX = x_data[x+1] - x_data[x]
                scoringXdata.append(skorX)
        else:
            skorX = 0
            scoringXdata.append(skorX)
    # print(scoringXdata)

    # skoring

    #  if x_data[i] < x_data[i-1]:
    #       print('Lebih kecil')

    # end

    # new_x,new_y,new_z = [],[],[]
    # new_x.append(x_data)
    # new_y.append(y_data)
    # new_z.append(z_data)

    # df = pd.DataFrame({'x_data': new_x, 'y_data': new_y, 'z_data': new_z})
    # print(markers_fix)

    # print(fusion)

    # df = pd.DataFrame({
    #             'Frame ': frame_no_list *len(markers_fix),
    #             'Marker': markers_fix * len(frame_no_list),
    #             'X': np.array(x_data).flatten(),
    #             'Y': np.array(y_data).flatten(),
    #             'Z': np.array(z_data).flatten(),
    #             })
    print(scoringXdata)
    # df = pd.DataFrame({
    #     'Frame': frame_data,
    #     'Marker': markers_fix * len(frame_no_list),
    #     'X': np.array(x_data).flatten(),
    #     'Y': np.array(y_data).flatten(),
    #     'Z': np.array(z_data).flatten(),
    #     'Scoring X': scoringXdata,
    #     'Scoring Y': scoringYdata,
    #     'Scoring Z': scoringZdata,
    # })
    
    # print(df)

    # print
    # wb = Workbook()
    # ws = wb.active
    # for r in dataframe_to_rows(df, index=True, header=True):
    #     ws.append(r)
    # wb.save('cobaFixBanged2.xlsx')

    # dibalik

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
    
    # print(f'frame {i} marker {namaMarker} sumbuX{LPSIX[x]} sumbuY{LPSIY[x]} sumbuZ{LPSIZ[x]} Pengurangan X {penguranganLPSIX} Pengurangan Y {penguranganLPSIY} Pengurangan Z {penguranganLPSIZ} Hasil Skoring X {hasilSkorLPSIX} Hasil Skoring X {hasilSkorLPSIX}')