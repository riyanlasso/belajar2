import c3d
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pymysql

# ceknama = 'AGNESKA     sasasasas'
# nama = ceknama.replace(" ", "")
# print(nama)
# training
with open('446448.c3d', 'rb') as handle:
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
    LPSIX, RPSIX, RTOEX, LHEEX, LKNEX, LTIBX, RTIBX, LANKX, RTHIX, LTHIX, RANKX, RKNEX, RHEEX, LTOEX, RASIX, LASIX = [
    ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    LPSIY, RPSIY, RTOEY, LHEEY, LKNEY, LTIBY, RTIBY, LANKY, RTHIY, LTHIY, RANKY, RKNEY, RHEEY, LTOEY, RASIY, LASIY = [
    ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
    LPSIZ, RPSIZ, RTOEZ, LHEEZ, LKNEZ, LTIBZ, RTIBZ, LANKZ, RTHIZ, LTHIZ, RANKZ, RKNEZ, RHEEZ, LTOEZ, RASIZ, LASIZ = [
    ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],

    frame_no_list = []
    # pisahkan data
    # start
    frame_data = []
    for q, points, analog in reader.read_frames():
        frame_no_list.append(q)

    my_marker = []

    for i, points, analog in reader.read_frames():
        # print(points)
        if i in frame_no_list:

            for j, marker in enumerate(markers_fix):

                if marker in markers_fix:
                    if marker == markers_fix[0]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])

                        LPSIX.append(points[j, 0])
                        LPSIY.append(points[j, 1])
                        LPSIZ.append(points[j, 2])

                        frame_data.append(i)
                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')

                    elif marker == markers_fix[1]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RPSIX.append(points[j, 0])
                        RPSIY.append(points[j, 1])
                        RPSIZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')

                    elif marker == markers_fix[2]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RTOEX.append(points[j, 0])
                        RTOEY.append(points[j, 1])
                        RTOEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')

                    elif marker == markers_fix[3]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LHEEX.append(points[j, 0])
                        LHEEY.append(points[j, 1])
                        LHEEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[4]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LKNEX.append(points[j, 0])
                        LKNEY.append(points[j, 1])
                        LKNEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[5]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LTIBX.append(points[j, 0])
                        LTIBY.append(points[j, 1])
                        LTIBZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[6]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RTIBX.append(points[j, 0])
                        RTIBY.append(points[j, 1])
                        RTIBZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[7]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LANKX.append(points[j, 0])
                        LANKY.append(points[j, 1])
                        LANKZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[8]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RTHIX.append(points[j, 0])
                        RTHIY.append(points[j, 1])
                        RTHIZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[9]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LTHIX.append(points[j, 0])
                        LTHIY.append(points[j, 1])
                        LTHIZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[10]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RANKX.append(points[j, 0])
                        RANKY.append(points[j, 1])
                        RANKZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[11]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RKNEX.append(points[j, 0])
                        RKNEY.append(points[j, 1])
                        RKNEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[12]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RHEEX.append(points[j, 0])
                        RHEEY.append(points[j, 1])
                        RHEEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[13]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        LTOEX.append(points[j, 0])
                        LTOEY.append(points[j, 1])
                        LTOEZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[14]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])
                        RASIX.append(points[j, 0])
                        RASIY.append(points[j, 1])
                        RASIZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')
                    elif marker == markers_fix[15]:
                        namaMarker = marker
                        sumbuX = np.array(points[j, 0])
                        sumbuY = np.array(points[j, 1])
                        sumbuZ = np.array(points[j, 2])

                        x_data.append(points[j, 0])
                        y_data.append(points[j, 1])
                        z_data.append(points[j, 2])

                        LASIX.append(points[j, 0])
                        LASIY.append(points[j, 1])
                        LASIZ.append(points[j, 2])

                        frame_data.append(i)

                        print(
                            f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ}')

    # print(LPSIX)
    # print(LPSIY)
    # print(LPSIZ)
    # print(x_data)

    # cara1
    # mengurangi dengan urut sesuai index x_data,y_data_z_data
    # datapenguranganX, datapenguranganY, datapenguranganZ = [], [], []
    # penguranganX, penguranganY, penguranganZ = [], [], []
    # hasilSkorX, hasilSkorY, hasilSkorZ = [], [], []
    # print('CARA 1')
    # try:
    #     print('scoring X')
    #     for x in range(len(x_data)):
    #         if x_data[x] < x_data[x+16] :
    #             penguranganX = x_data[x] - x_data[x+16]
    #             datapenguranganX.append(penguranganX)
    #             if penguranganX > 0 :
    #                 skorX = 2
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX < 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX == 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             print(f"hasil pengurangan {x_data[x]} dengan {x_data[x+16]} adalah {penguranganX} scoring = {skorX}")

    #         elif x_data[x] > x_data[x+16]:
    #             scoringX = x_data[x] - x_data[x+16]
    #             datapenguranganX.append(penguranganX)
    #             if penguranganX > 0 :
    #                 skorX = 2
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX < 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX == 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             print(f"hasil pengurangan {x_data[x]} dengan {x_data[x+16]} adalah {penguranganX} scoring = {skorX}")

    #         elif x_data[x] == x_data[x+16]:
    #             scoringX = x_data[x] - x_data[x+16]
    #             datapenguranganX.append(penguranganX)
    #             if penguranganX > 0 :
    #                 skorX = 2
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX < 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             elif penguranganX == 0 :
    #                 skorX = 1
    #                 hasilSkorX.append(skorX)
    #             print(f"hasil pengurangan {x_data[x]} dengan {x_data[x+16]} adalah {penguranganX} scoring = {skorX}")

    # except IndexError:
    #     for _ in range(16):
    #         datapenguranganX.append(0)
    #         hasilSkorX.append(0)
    # print(hasilSkorX)

    # try:
    #     print('scoring Y')
    #     for y in range(len(y_data)):
    #         if y_data[y] < y_data[y+16] :
    #             scoringY = y_data[y] - y_data[y+16]
    #             penguranganY.append(scoringY)
    #             skorY = 1
    #             hasilSkorY.append(skorY)
    #             print(f"{y_data[y]} lebih kecil dari {y_data[y+16]} scoring = {skorY}")

    #         if y_data[y] > y_data[y+16] :
    #             scoringY = y_data[y] - y_data[y+16]
    #             penguranganY.append(scoringY)
    #             skorY = 2
    #             hasilSkorY.append(skorY)
    #             print(f"{y_data[y]} lebih besar dari {y_data[y+16]} scoring = {skorY}")

    #         if y_data[y] == y_data[y+16] :
    #             scoringY = y_data[y] - y_data[y+16]
    #             penguranganY.append(scoringY)
    #             skorY = 1
    #             hasilSkorY.append(skorY)
    #             print(f"{y_data[y]} sama dengan {y_data[y+16]} scoring = {skorY}")
    # except IndexError:
    #     for _ in range(16):
    #         penguranganY.append(0)
    #         hasilSkorY.append(0)
    # print(hasilSkorY)

    # try :
    #     print('scoring Z')
    #     for z in range(len(z_data)):
    #                 if z_data[z] < z_data[z+16] :
    #                     scoringZ = z_data[z] - z_data[z+16]
    #                     penguranganZ.append(scoringZ)
    #                     skorZ = 1
    #                     hasilSkorZ.append(skorZ)
    #                     print(f"{z_data[z]} lebih kecil dari {z_data[z+16]} scoring = {skorZ}")

    #                 if z_data[z] > z_data[z+16] :
    #                     scoringZ = z_data[z] - z_data[z+16]
    #                     penguranganZ.append(scoringZ)
    #                     skorZ = 2
    #                     hasilSkorZ.append(skorZ)
    #                     print(f"{z_data[z]} lebih besar dari {z_data[z+16]} scoring = {skorZ}")

    #                 if z_data[z] == z_data[z+16] :
    #                     scoringZ = z_data[z] - z_data[z+16]
    #                     penguranganZ.append(scoringZ)
    #                     skorZ = 1
    #                     hasilSkorZ.append(skorZ)
    #                     print(f"{z_data[z]} sama dengan {z_data[z+16]} scoring = {skorZ}")
    # except IndexError:
    #     for _ in range(16):
    #         penguranganZ.append(0)
    #         hasilSkorZ.append(0)S

    # print(hasilSkorZ)

    # cara3
    # datapenguranganX, datapenguranganY, datapenguranganZ = [], [], []
    # penguranganX, penguranganY, penguranganZ = [], [], []
    # hasilSkorX, hasilSkorY, hasilSkorZ = [], [], []
    # print('CARA 3')
    # print('scoring X')
    # try:
    #     for x in range(len(x_data)):
    #         penguranganX = x_data[x+16] - x_data[x]
    #         datapenguranganX.append(penguranganX)

    #         if penguranganX > 0:
    #             skorX = 2
    #             hasilSkorX.append(skorX)
    #             # print(f"hasil pengurangan {x_data[x+16]} dengan {x_data[x]} adalah {penguranganX} scoring = {skorX}")
    #         elif penguranganX < 0:
    #             skorX = 1
    #             hasilSkorX.append(skorX)
    #             # print(f"hasil pengurangan {x_data[x+16]} dengan {x_data[x]} adalah {penguranganX} scoring = {skorX}")
    #         elif penguranganX == 0:
    #             skorX = 1
    #             hasilSkorX.append(skorX)
    #             # print(f"hasil pengurangan {x_data[x+16]} dengan {x_data[x]} adalah {penguranganX} scoring = {skorX}")
    # except IndexError:
    #     for _ in range(16):
    #         datapenguranganX.append(0)
    #         skorX = 1
    #         hasilSkorX.append(skorX)

    # print(hasilSkorX)

    # print('scoring Y')
    # try:
    #     for y in range(len(y_data)):
    #         penguranganY = y_data[y+16] - y_data[y]
    #         datapenguranganY.append(penguranganY)
    #         if penguranganY > 0:
    #             skorY = 2
    #             hasilSkorY.append(skorY)
    #             # print(f"hasil pengurangan {y_data[y+16]} dengan {y_data[y]} adalah {penguranganY} scoring = {skorY}")
    #         elif penguranganY < 0:
    #             skorY = 1
    #             hasilSkorY.append(skorY)
    #             # print(f"hasil pengurangan {y_data[y+16]} dengan {y_data[y]} adalah {penguranganY} scoring = {skorY}")
    #         elif penguranganY == 0:
    #             skorY = 1
    #             hasilSkorY.append(skorY)
    #             # print(f"hasil pengurangan {y_data[y+16]} dengan {y_data[y]} adalah {penguranganY} scoring = {skorY}")
    # except IndexError:
    #     for _ in range(16):
    #         datapenguranganY.append(0)
    #         skorY = 1
    #         hasilSkorY.append(skorY)
    # print(hasilSkorY)

    # print('scoring Z')
    # try:
    #     for z in range(len(z_data)):
    #         penguranganZ = z_data[z+16] - z_data[z]
    #         datapenguranganZ.append(penguranganZ)
    #         if penguranganZ > 0:
    #             skorZ = 2
    #             hasilSkorZ.append(skorZ)
    #             # print(f"hasil pengurangan {z_data[z+16]} dengan {z_data[z]} adalah {penguranganZ} scoring = {skorZ}")
    #         elif penguranganZ < 0:
    #             skorZ = 1
    #             hasilSkorZ.append(skorZ)
    #             # print(f"hasil pengurangan {z_data[z+16]} dengan {z_data[z]} adalah {penguranganZ} scoring = {skorZ}")
    #         elif penguranganZ == 0:
    #             skorZ = 1
    #             hasilSkorZ.append(skorZ)
    #             # print(f"hasil pengurangan {z_data[z+16]} dengan {z_data[z]} adalah {penguranganZ} scoring = {skorZ}")
    # except IndexError:
    #     for _ in range(16):
    #         datapenguranganZ.append(0)
    #         skorZ = 1
    #         hasilSkorZ.append(skorZ)
    # print(hasilSkorZ)

    # cara2
    # simpan datanya ke variabel marker dengan nilai array kosong di setiap frame
    # pengurangannya di setiap masing - masing sumbuX, Y dan Z setiap marker
    # (setiap sumbu punya array kosong sendiri sesuai dengan markernya)
    # hasil skoring berdasarkan hasil pengurangannya dari setiap marker

    print('CARA 2')
    penguranganLPSIX, penguranganLPSIY, penguranganLPSIZ = [], [], []
    hasilSkorLPSIX, hasilSkorLPSIY, hasilSkorLPSIZ = [], [], []

    penguranganRPSIX, penguranganRPSIY, penguranganRPSIZ = [], [], []
    hasilSkorRPSIX, hasilSkorRPSIY, hasilSkorRPSIZ = [], [], []

    penguranganRTOEX, penguranganRTOEY, penguranganRTOEZ = [], [], []
    hasilSkorRTOEX, hasilSkorRTOEY, hasilSkorRTOEZ = [], [], []
    #
    penguranganLHEEX, penguranganLHEEY, penguranganLHEEZ = [], [], []
    hasilSkorLHEEX, hasilSkorLHEEY, hasilSkorLHEEZ = [], [], []

    penguranganLKNEX, penguranganLKNEY, penguranganLKNEZ = [], [], []
    hasilSkorLKNEX, hasilSkorLKNEY, hasilSkorLKNEZ = [], [], []

    penguranganLTIBX, penguranganLTIBY, penguranganLTIBZ = [], [], []
    hasilSkorLTIBX, hasilSkorLTIBY, hasilSkorLTIBZ = [], [], []
    #
    penguranganRTIBX, penguranganRTIBY, penguranganRTIBZ = [], [], []
    hasilSkorRTIBX, hasilSkorRTIBY, hasilSkorRTIBZ = [], [], []

    penguranganLANKX, penguranganLANKY, penguranganLANKZ = [], [], []
    hasilSkorLANKX, hasilSkorLANKY, hasilSkorLANKZ = [], [], []

    penguranganRTHIX, penguranganRTHIY, penguranganRTHIZ = [], [], []
    hasilSkorRTHIX, hasilSkorRTHIY, hasilSkorRTHIZ = [], [], []

    penguranganLTHIX, penguranganLTHIY, penguranganLTHIZ = [], [], []
    hasilSkorLTHIX, hasilSkorLTHIY, hasilSkorLTHIZ = [], [], []

    penguranganRANKX, penguranganRANKY, penguranganRANKZ = [], [], []
    hasilSkorRANKX, hasilSkorRANKY, hasilSkorRANKZ = [], [], []

    penguranganRKNEX, penguranganRKNEY, penguranganRKNEZ = [], [], []
    hasilSkorRKNEX, hasilSkorRKNEY, hasilSkorRKNEZ = [], [], []

    penguranganRHEEX, penguranganRHEEY, penguranganRHEEZ = [], [], []
    hasilSkorRHEEX, hasilSkorRHEEY, hasilSkorRHEEZ = [], [], []
    #
    penguranganLTOEX, penguranganLTOEY, penguranganLTOEZ = [], [], []
    hasilSkorLTOEX, hasilSkorLTOEY, hasilSkorLTOEZ = [], [], []

    penguranganRASIX, penguranganRASIY, penguranganRASIZ = [], [], []
    hasilSkorRASIX, hasilSkorRASIY, hasilSkorRASIZ = [], [], []

    penguranganLASIX, penguranganLASIY, penguranganLASIZ = [], [], []
    hasilSkorLASIX, hasilSkorLASIY, hasilSkorLASIZ = [], [], []

    # hasilSkorLASIX, hasilSkorLASIY, hasilSkorLASIZ = [], [], []
    # hasilSkorLPSIX, hasilSkorLPSIY, hasilSkorLPSIZ = [], [], []
    # hasilSkorRPSIX, hasilSkorRPSIY, hasilSkorRPSIZ = [], [], []
    # hasilSkorRTOEX, hasilSkorRTOEY, hasilSkorRTOEZ = [], [], []
    # hasilSkorLHEEX, hasilSkorLHEEY, hasilSkorLHEEZ = [], [], []
    # hasilSkorLKNEX, hasilSkorLKNEY, hasilSkorLKNEZ = [], [], []
    # hasilSkorRTIBX, hasilSkorRTIBY, hasilSkorRTIBZ = [], [], []
    # hasilSkorLANKX, hasilSkorLANKY, hasilSkorLANKZ = [], [], []
    # hasilSkorRTHIX, hasilSkorRTHIY, hasilSkorRTHIZ = [], [], []
    # hasilSkorLTHIX, hasilSkorLTHIY, hasilSkorLTHIZ = [], [], []
    # hasilSkorRANKX, hasilSkorRANKY, hasilSkorRANKZ = [], [], []
    # hasilSkorRKNEX, hasilSkorRKNEY, hasilSkorRKNEZ = [], [], []
    # hasilSkorRHEEX, hasilSkorRHEEY, hasilSkorRHEEZ = [], [], []
    # hasilSkorLTOEX, hasilSkorLTOEY, hasilSkorLTOEZ = [], [], []
    # hasilSkorRASIX, hasilSkorRASIY, hasilSkorRASIZ = [], [], []
    # hasilSkorLASIX, hasilSkorLASIY, hasilSkorLASIZ = [], [], []

    hasilSkorLASIX, hasilSkorLASIY, hasilSkorLASIZ = [], [], []
    penjumlahanLPSIX, penjumlahanLPSIY, penjumlahanLPSIZ = [], [], []
    penjumlahanRPSIX, penjumlahanRPSIY, penjumlahanRPSIZ = [], [], []
    penjumlahanRTOEX, penjumlahanRTOEY, penjumlahanRTOEZ = [], [], []
    penjumlahanLHEEX, penjumlahanLHEEY, penjumlahanLHEEZ = [], [], []
    penjumlahanLKNEX, penjumlahanLKNEY, penjumlahanLKNEZ = [], [], []
    penjumlahanLTIBX, penjumlahanLTIBY, penjumlahanLTIBZ = [], [], []
    penjumlahanRTIBX, penjumlahanRTIBY, penjumlahanRTIBZ = [], [], []
    penjumlahanLANKX, penjumlahanLANKY, penjumlahanLANKZ = [], [], []
    penjumlahanRTHIX, penjumlahanRTHIY, penjumlahanRTHIZ = [], [], []
    penjumlahanLTHIX, penjumlahanLTHIY, penjumlahanLTHIZ = [], [], []
    penjumlahanRANKX, penjumlahanRANKY, penjumlahanRANKZ = [], [], []
    penjumlahanRKNEX, penjumlahanRKNEY, penjumlahanRKNEZ = [], [], []
    penjumlahanRHEEX, penjumlahanRHEEY, penjumlahanRHEEZ = [], [], []
    penjumlahanLTOEX, penjumlahanLTOEY, penjumlahanLTOEZ = [], [], []
    penjumlahanRASIX, penjumlahanRASIY, penjumlahanRASIZ = [], [], []
    penjumlahanLASIX, penjumlahanLASIY, penjumlahanLASIZ = [], [], []

    # # LPSI START
    try:
        print('scoring LPSIX')
        for x in range(len(LPSIX)):
            pengurangan = LPSIX[x+1] - LPSIX[x]
            penguranganLPSIX.append(pengurangan)
            if pengurangan > 0:
                skorLPSIX = 2
                hasilSkorLPSIX.append(skorLPSIX)
            elif pengurangan < 0:
                skorLPSIX = 1
                hasilSkorLPSIX.append(skorLPSIX)
            elif pengurangan == 0:
                skorLPSIX = 1
                hasilSkorLPSIX.append(skorLPSIX)
    except IndexError:
        skorLPSIX = 1
        penguranganLPSIX.append(0)
        hasilSkorLPSIX.append(skorLPSIX)

    # print(LPSIX)
    print(penguranganLPSIX)
    print(hasilSkorLPSIX)
    # penjumlahanLPSIX.append(sum(hasilSkorLPSIX))
    # print(penjumlahanLPSIX)
    try:
        print('scoring LPSIY')
        for x in range(len(LPSIY)):
            pengurangan = LPSIY[x+1] - LPSIY[x]
            penguranganLPSIY.append(pengurangan)
            if pengurangan > 0:
                skorLPSIY = 2
                hasilSkorLPSIY.append(skorLPSIY)
            elif pengurangan < 0:
                skorLPSIY = 1
                hasilSkorLPSIY.append(skorLPSIY)
            elif pengurangan == 0:
                skorLPSIY = 1
                hasilSkorLPSIY.append(skorLPSIY)
    except IndexError:
        skorLPSIY = 1
        penguranganLPSIY.append(0)
        hasilSkorLPSIY.append(skorLPSIY)
    print(penguranganLPSIY)
    print(hasilSkorLPSIY)
    try:
        print('scoring LPSIZ')
        for x in range(len(LPSIZ)):
            pengurangan = LPSIZ[x+1] - LPSIZ[x]
            penguranganLPSIZ.append(pengurangan)
            if pengurangan > 0:
                skorLPSIZ = 2
                hasilSkorLPSIZ.append(skorLPSIZ)
            elif pengurangan < 0:
                skorLPSIZ = 1
                hasilSkorLPSIZ.append(skorLPSIZ)
            elif pengurangan == 0:
                skorLPSIZ = 1
                hasilSkorLPSIZ.append(skorLPSIZ)
    except IndexError:
        skorLPSIZ = 1
        penguranganLPSIZ.append(0)
        hasilSkorLPSIZ.append(skorLPSIZ)
    print(penguranganLPSIZ)
    print(hasilSkorLPSIZ)
    # # LPSI END

    # # RPSI START
    try:
        print('scoring RPSIX')
        for x in range(len(RPSIX)):
            pengurangan = RPSIX[x+1] - RPSIX[x]
            penguranganRPSIX.append(pengurangan)
            if pengurangan > 0:
                skorRPSIX = 2
                hasilSkorRPSIX.append(skorRPSIX)
            elif pengurangan < 0:
                skorRPSIX = 1
                hasilSkorRPSIX.append(skorRPSIX)
            elif pengurangan == 0:
                skorRPSIZ = 1
                hasilSkorRPSIX.append(skorRPSIX)
    except IndexError:
        skorRPSIX = 1
        penguranganRPSIX.append(0)
        hasilSkorRPSIX.append(skorRPSIX)
    print(RPSIX)
    print(penguranganRPSIX)
    print(hasilSkorRPSIX)

    try:
        print('scoring RPSIY')
        for x in range(len(RPSIY)):
            pengurangan = RPSIY[x+1] - RPSIY[x]
            penguranganRPSIY.append(pengurangan)
            if pengurangan > 0:
                skorRPSIY = 2
                hasilSkorRPSIY.append(skorRPSIY)
            elif pengurangan < 0:
                skorRPSIY = 1
                hasilSkorRPSIY.append(skorRPSIY)
            elif pengurangan == 0:
                skorRPSIY = 1
                hasilSkorRPSIY.append(skorRPSIY)
    except IndexError:
        skorRPSIY = 1
        penguranganRPSIY.append(0)
        hasilSkorRPSIY.append(skorRPSIY)
    print(RPSIY)
    print(penguranganRPSIY)
    print(hasilSkorRPSIY)

    try:
        print('scoring RPSIZ')
        for x in range(len(RPSIZ)):
            pengurangan = RPSIZ[x+1] - RPSIZ[x]
            penguranganRPSIZ.append(pengurangan)
            if pengurangan > 0:
                skorRPSIZ = 2
                hasilSkorRPSIZ.append(skorRPSIZ)
            elif pengurangan < 0:
                skorRPSIZ = 1
                hasilSkorRPSIZ.append(skorRPSIZ)
            elif pengurangan == 0:
                skorRPSIZ = 1
                hasilSkorRPSIY.append(skorRPSIY)
    except IndexError:
        skorRPSIZ = 1
        penguranganRPSIZ.append(0)
        hasilSkorRPSIZ.append(skorRPSIZ)
    print(RPSIZ)
    print(penguranganRPSIZ)
    print(hasilSkorRPSIZ)
    # # RPSI END

    # # RTOE START
    try:
        print('scoring RTOEX')
        for x in range(len(RTOEX)):
            pengurangan = RTOEX[x+1] - RTOEX[x]
            penguranganRTOEX.append(pengurangan)
            if pengurangan > 0:
                skorRTOEX = 2
                hasilSkorRTOEX.append(skorRTOEX)
            elif pengurangan < 0:
                skorRTOEX = 1
                hasilSkorRTOEX.append(skorRTOEX)
            elif pengurangan == 0:
                skorRTOEX = 1
                hasilSkorRTOEX.append(skorRTOEX)
    except IndexError:
        skorRTOEX = 1
        penguranganRTOEX.append(0)
        hasilSkorRTOEX.append(skorRTOEX)
    print(RTOEX)
    print(penguranganRTOEX)
    print(hasilSkorRTOEX)

    try:
        print('scoring RTOEY')
        for x in range(len(RTOEY)):
            pengurangan = RTOEY[x+1] - RTOEY[x]
            penguranganRTOEY.append(pengurangan)
            if pengurangan > 0:
                skorRTOEY = 2
                hasilSkorRTOEY.append(skorRTOEY)
            elif pengurangan < 0:
                skorRTOEY = 1
                hasilSkorRTOEY.append(skorRTOEY)
            elif pengurangan == 0:
                skorRTOEY = 1
                hasilSkorRTOEY.append(skorRTOEY)
    except IndexError:
        skorRTOEY = 1
        penguranganRTOEY.append(0)
        hasilSkorRTOEY.append(skorRTOEY)
    print(RTOEY)
    print(penguranganRTOEY)
    print(hasilSkorRTOEY)

    try:
        print('scoring RTOEZ')
        for x in range(len(RTOEZ)):
            pengurangan = RTOEZ[x+1] - RTOEZ[x]
            penguranganRTOEZ.append(pengurangan)
            if pengurangan > 0:
                skorRTOEZ = 2
                hasilSkorRTOEZ.append(skorRTOEZ)
            elif pengurangan < 0:
                skorRTOEZ = 1
                hasilSkorRTOEZ.append(skorRTOEZ)
            elif pengurangan == 0:
                skorRTOEZ = 1
                hasilSkorRTOEZ.append(skorRTOEZ)
    except IndexError:
        skorRTOEZ = 1
        penguranganRTOEZ.append(0)
        hasilSkorRTOEZ.append(skorRTOEZ)
    print(RTOEZ)
    print(penguranganRTOEZ)
    print(hasilSkorRTOEZ)

    # # RTOE END

    # # LHEE START
    try:
        print('scoring LHEEX')
        for x in range(len(LHEEX)):
            pengurangan = LHEEX[x+1] - LHEEX[x]
            penguranganLHEEX.append(pengurangan)
            if pengurangan > 0:
                skorLHEEX = 2
                hasilSkorLHEEX.append(skorLHEEX)
            elif pengurangan < 0:
                skorLHEEX = 1
                hasilSkorLHEEX.append(skorLHEEX)
            elif pengurangan == 0:
                skorLHEEX = 1
                hasilSkorLHEEX.append(skorLHEEX)
    except IndexError:
        skorLHEEX = 1
        penguranganLHEEX.append(0)
        hasilSkorLHEEX.append(skorLHEEX)
    print(LHEEX)
    print(penguranganLHEEX)
    print(hasilSkorLHEEX)

    try:
        print('scoring LHEEY')
        for x in range(len(LHEEY)):
            pengurangan = LHEEY[x+1] - LHEEY[x]
            penguranganLHEEY.append(pengurangan)
            if pengurangan > 0:
                skorLHEEY = 2
                hasilSkorLHEEY.append(skorLHEEY)
            elif pengurangan < 0:
                skorLHEEY = 1
                hasilSkorLHEEY.append(skorLHEEY)
            elif pengurangan == 0:
                skorLHEEY = 1
                hasilSkorLHEEY.append(skorLHEEY)
    except IndexError:
        skorLHEEY = 1
        penguranganLHEEY.append(0)
        hasilSkorLHEEY.append(skorLHEEY)
    print(LHEEY)
    print(penguranganLHEEY)
    print(hasilSkorLHEEY)

    try:
        print('scoring LHEEZ')
        for x in range(len(LHEEZ)):
            pengurangan = LHEEZ[x+1] - LHEEZ[x]
            penguranganLHEEZ.append(pengurangan)
            if pengurangan > 0:
                skorLHEEZ = 2
                hasilSkorLHEEZ.append(skorLHEEZ)
            elif pengurangan < 0:
                skorLHEEZ = 1
                hasilSkorLHEEZ.append(skorLHEEZ)
            elif pengurangan == 0:
                skorLHEEZ = 1
                hasilSkorLHEEZ.append(skorLHEEZ)
    except IndexError:
        skorLHEEZ = 1
        penguranganLHEEZ.append(0)
        hasilSkorLHEEZ.append(skorLHEEZ)
    print(LHEEZ)
    print(penguranganLHEEZ)
    print(hasilSkorLHEEZ)

    # # LHEE END

    # # LKNE START
    try:
        print('scoring LKNEX')
        for x in range(len(LKNEX)):
            pengurangan = LKNEX[x+1] - LKNEX[x]
            penguranganLKNEX.append(pengurangan)
            if pengurangan > 0:
                skorLKNEX = 2
                hasilSkorLKNEX.append(skorLKNEX)
            elif pengurangan < 0:
                skorLKNEX = 1
                hasilSkorLKNEX.append(skorLKNEX)
            elif pengurangan == 0:
                skorLKNEX = 1
                hasilSkorLKNEX.append(skorLKNEX)
    except IndexError:
        skorLKNEX = 1
        penguranganLKNEX.append(0)
        hasilSkorLKNEX.append(skorLKNEX)
    print(LKNEX)
    print(penguranganLKNEX)
    print(hasilSkorLKNEX)

    try:
        print('scoring LKNEY')
        for x in range(len(LKNEY)):
            pengurangan = LKNEY[x+1] - LKNEY[x]
            penguranganLKNEY.append(pengurangan)
            if pengurangan > 0:
                skorLKNEY = 2
                hasilSkorLKNEY.append(skorLKNEY)
            elif pengurangan < 0:
                skorLKNEY = 1
                hasilSkorLKNEY.append(skorLKNEY)
            elif pengurangan == 0:
                skorLKNEY = 1
                hasilSkorLKNEY.append(skorLKNEY)
    except IndexError:
        skorLKNEY = 1
        penguranganLKNEY.append(0)
        hasilSkorLKNEY.append(skorLKNEY)
    print(LKNEY)
    print(penguranganLKNEY)
    print(hasilSkorLKNEY)

    try:
        print('scoring LKNEZ')
        for x in range(len(LKNEZ)):
            pengurangan = LKNEZ[x+1] - LKNEZ[x]
            penguranganLKNEZ.append(pengurangan)
            if pengurangan > 0:
                skorLKNEZ = 2
                hasilSkorLKNEZ.append(skorLKNEZ)
            elif pengurangan < 0:
                skorLKNEZ = 1
                hasilSkorLKNEZ.append(skorLKNEZ)
            elif pengurangan == 0:
                skorLKNEZ = 1
                hasilSkorLKNEZ.append(skorLKNEZ)
    except IndexError:
        skorLKNEZ = 1
        penguranganLKNEZ.append(0)
        hasilSkorLKNEZ.append(skorLKNEZ)
    print(LKNEZ)
    print(penguranganLKNEZ)
    print(hasilSkorLKNEZ)

    # # LKNE END

    # # LTIB
    try:
        print('scoring LTIBX')
        for x in range(len(LTIBX)):
            pengurangan = LTIBX[x+1] - LTIBX[x]
            penguranganLTIBX.append(pengurangan)
            if pengurangan > 0:
                skorLTIBX = 2
                hasilSkorLTIBX.append(skorLTIBX)
            elif pengurangan < 0:
                skorLTIBX = 1
                hasilSkorLTIBX.append(skorLTIBX)
            elif pengurangan == 0:
                skorLTIBX = 1
                hasilSkorLTIBX.append(skorLTIBX)
    except IndexError:
        skorLTIBX = 1
        penguranganLTIBX.append(0)
        hasilSkorLTIBX.append(skorLTIBX)
    print(LTIBX)
    print(penguranganLTIBX)
    print(hasilSkorLTIBX)

    try:
        print('scoring LTIBY')
        for x in range(len(LTIBY)):
            pengurangan = LTIBY[x+1] - LTIBY[x]
            penguranganLTIBY.append(pengurangan)
            if pengurangan > 0:
                skorLTIBY = 2
                hasilSkorLTIBY.append(skorLTIBY)
            elif pengurangan < 0:
                skorLTIBY = 1
                hasilSkorLTIBY.append(skorLTIBY)
            elif pengurangan == 0:
                skorLTIBY = 1
                hasilSkorLTIBY.append(skorLTIBY)
    except IndexError:
        skorLTIBY = 1
        penguranganLTIBY.append(0)
        hasilSkorLTIBY.append(skorLTIBY)
    print(LTIBY)
    print(penguranganLTIBY)
    print(hasilSkorLTIBY)

    try:
        print('scoring LTIBZ')
        for x in range(len(LTIBZ)):
            pengurangan = LTIBZ[x+1] - LTIBZ[x]
            penguranganLTIBZ.append(pengurangan)
            if pengurangan > 0:
                skorLTIBZ = 2
                hasilSkorLTIBZ.append(skorLTIBZ)
            elif pengurangan < 0:
                skorLTIBZ = 1
                hasilSkorLTIBZ.append(skorLTIBZ)
            elif pengurangan == 0:
                skorLTIBZ = 1
                hasilSkorLTIBZ.append(skorLTIBZ)
    except IndexError:
        skorLTIBZ = 1
        penguranganLTIBZ.append(0)
        hasilSkorLTIBZ.append(skorLTIBZ)
    print(LTIBZ)
    print(penguranganLTIBZ)
    print(hasilSkorLTIBZ)
    # # LTIB END

    # # RTIB START
    try:
        print('scoring RTIBX')
        for x in range(len(RTIBX)):
            pengurangan = RTIBX[x+1] - RTIBX[x]
            penguranganRTIBX.append(pengurangan)
            if pengurangan > 0:
                skorRTIBX = 2
                hasilSkorRTIBX.append(skorRTIBX)
            elif pengurangan < 0:
                skorRTIBX = 1
                hasilSkorRTIBX.append(skorRTIBX)
            elif pengurangan == 0:
                skorRTIBX = 1
                hasilSkorRTIBX.append(skorRTIBX)
    except IndexError:
        skorRTIBX = 1
        penguranganRTIBX.append(0)
        hasilSkorRTIBX.append(skorRTIBX)
    print(RTIBX)
    print(penguranganRTIBX)
    print(hasilSkorRTIBX)

    try:
        print('scoring RTIBY')
        for x in range(len(RTIBY)):
            pengurangan = RTIBY[x+1] - RTIBY[x]
            penguranganRTIBY.append(pengurangan)
            if pengurangan > 0:
                skorRTIBY = 2
                hasilSkorRTIBY.append(skorRTIBY)
            elif pengurangan < 0:
                skorRTIBY = 1
                hasilSkorRTIBY.append(skorRTIBY)
            elif pengurangan == 0:
                skorRTIBY = 1
                hasilSkorRTIBY.append(skorRTIBY)
    except IndexError:
        skorRTIBY = 1
        penguranganRTIBY.append(0)
        hasilSkorRTIBY.append(skorRTIBY)
    print(RTIBY)
    print(penguranganRTIBY)
    print(hasilSkorRTIBY)

    try:
        print('scoring RTIBZ')
        for x in range(len(RTIBZ)):
            pengurangan = RTIBZ[x+1] - RTIBZ[x]
            penguranganRTIBZ.append(pengurangan)
            if pengurangan > 0:
                skorRTIBZ = 2
                hasilSkorRTIBZ.append(skorRTIBZ)
            elif pengurangan < 0:
                skorRTIBZ = 1
                hasilSkorRTIBZ.append(skorRTIBZ)
            elif pengurangan == 0:
                skorRTIBZ = 1
                hasilSkorRTIBZ.append(skorRTIBZ)
    except IndexError:
        skorRTIBZ = 1
        penguranganRTIBZ.append(0)
        hasilSkorRTIBZ.append(skorRTIBZ)
    print(RTIBZ)
    print(penguranganRTIBZ)
    print(hasilSkorRTIBZ)

    # # RTIB END

    # # LANK START
    try:
        print('scoring LANKX')
        for x in range(len(LANKX)):
            pengurangan = LANKX[x+1] - LANKX[x]
            penguranganLANKX.append(pengurangan)
            if pengurangan > 0:
                skorLANKX = 2
                hasilSkorLANKX.append(skorLANKX)
            elif pengurangan < 0:
                skorLANKX = 1
                hasilSkorLANKX.append(skorLANKX)
            elif pengurangan == 0:
                skorLANKX = 1
                hasilSkorLANKX.append(skorLANKX)
    except IndexError:
        skorLANKX = 1
        penguranganLANKX.append(0)
        hasilSkorLANKX.append(skorLANKX)
    print(LANKX)
    print(penguranganLANKX)
    print(hasilSkorLANKX)

    try:
        print('scoring LANKY')
        for x in range(len(LANKY)):
            pengurangan = LANKY[x+1] - LANKY[x]
            penguranganLANKY.append(pengurangan)
            if pengurangan > 0:
                skorLANKY = 2
                hasilSkorLANKY.append(skorLANKY)
            elif pengurangan < 0:
                skorLANKY = 1
                hasilSkorLANKY.append(skorLANKY)
            elif pengurangan == 0:
                skorLANKY = 1
                hasilSkorLANKY.append(skorLANKY)
    except IndexError:
        skorLANKY = 1
        penguranganLANKY.append(0)
        hasilSkorLANKY.append(skorLANKY)
    print(LANKY)
    print(penguranganLANKY)
    print(hasilSkorLANKY)

    try:
        print('scoring LANKZ')
        for x in range(len(LANKZ)):
            pengurangan = LANKZ[x+1] - LANKZ[x]
            penguranganLANKZ.append(pengurangan)
            if pengurangan > 0:
                skorLANKZ = 2
                hasilSkorLANKZ.append(skorLANKZ)
            elif pengurangan < 0:
                skorLANKZ = 1
                hasilSkorLANKZ.append(skorLANKZ)
            elif pengurangan == 0:
                skorLANKZ = 1
                hasilSkorLANKZ.append(skorLANKZ)
    except IndexError:
        skorLANKZ = 1
        penguranganLANKZ.append(0)
        hasilSkorLANKZ.append(skorLANKZ)
    print(LANKZ)
    print(penguranganLANKZ)
    print(hasilSkorLANKZ)

    # # LANK END

    # # RTHI START
    try:
        print('scoring RTHIX')
        for x in range(len(RTHIX)):
            pengurangan = RTHIX[x+1] - RTHIX[x]
            penguranganRTHIX.append(pengurangan)
            if pengurangan > 0:
                skorRTHIX = 2
                hasilSkorRTHIX.append(skorRTHIX)
            elif pengurangan < 0:
                skorRTHIX = 1
                hasilSkorRTHIX.append(skorRTHIX)
            elif pengurangan == 0:
                skorRTHIX = 1
                hasilSkorRTHIX.append(skorRTHIX)
    except IndexError:
        skorRTHIX = 1
        penguranganRTHIX.append(0)
        hasilSkorRTHIX.append(skorRTHIX)
    print(RTHIX)
    print(penguranganRTHIX)
    print(hasilSkorRTHIX)

    try:
        print('scoring RTHIY')
        for x in range(len(RTHIY)):
            pengurangan = RTHIY[x+1] - RTHIY[x]
            penguranganRTHIY.append(pengurangan)
            if pengurangan > 0:
                skorRTHIY = 2
                hasilSkorRTHIY.append(skorRTHIY)
            elif pengurangan < 0:
                skorRTHIY = 1
                hasilSkorRTHIY.append(skorRTHIY)
            elif pengurangan == 0:
                skorRTHIY = 1
                hasilSkorRTHIY.append(skorRTHIY)
    except IndexError:
        skorRTHIY = 1
        penguranganRTHIY.append(0)
        hasilSkorRTHIY.append(skorRTHIY)
    print(RTHIY)
    print(penguranganRTHIY)
    print(hasilSkorRTHIY)

    try:
        print('scoring RTHIZ')
        for x in range(len(RTHIZ)):
            pengurangan = RTHIZ[x+1] - RTHIZ[x]
            penguranganRTHIZ.append(pengurangan)
            if pengurangan > 0:
                skorRTHIZ = 2
                hasilSkorRTHIZ.append(skorRTHIZ)
            elif pengurangan < 0:
                skorRTHIZ = 1
                hasilSkorRTHIZ.append(skorRTHIZ)
            elif pengurangan == 0:
                skorRTHIZ = 1
                hasilSkorRTHIZ.append(skorRTHIZ)
    except IndexError:
        skorRTHIZ = 1
        penguranganRTHIZ.append(0)
        hasilSkorRTHIZ.append(skorRTHIZ)
    print(RTHIZ)
    print(penguranganRTHIZ)
    print(hasilSkorRTHIZ)

    # # RTHI END

    # # LTHI START
    try:
        print('scoring LTHIX')
        for x in range(len(LTHIX)):
            pengurangan = LTHIX[x+1] - LTHIX[x]
            penguranganLTHIX.append(pengurangan)
            if pengurangan > 0:
                skorLTHIX = 2
                hasilSkorLTHIX.append(skorLTHIX)
            elif pengurangan < 0:
                skorLTHIX = 1
                hasilSkorLTHIX.append(skorLTHIX)
            elif pengurangan == 0:
                skorLTHIX = 1
                hasilSkorLTHIX.append(skorLTHIX)
    except IndexError:
        skorLTHIX = 1
        penguranganLTHIX.append(0)
        hasilSkorLTHIX.append(skorLTHIX)
    print(LTHIX)
    print(penguranganLTHIX)
    print(hasilSkorLTHIX)

    try:
        print('scoring LTHIY')
        for x in range(len(LTHIY)):
            pengurangan = LTHIY[x+1] - LTHIY[x]
            penguranganLTHIY.append(pengurangan)
            if pengurangan > 0:
                skorLTHIY = 2
                hasilSkorLTHIY.append(skorLTHIY)
            elif pengurangan < 0:
                skorLTHIY = 1
                hasilSkorLTHIY.append(skorLTHIY)
            elif pengurangan == 0:
                skorLTHIY = 1
                hasilSkorLTHIY.append(skorLTHIY)
    except IndexError:
        skorLTHIY = 1
        penguranganLTHIY.append(0)
        hasilSkorLTHIY.append(skorLTHIY)
    print(LTHIY)
    print(penguranganLTHIY)
    print(hasilSkorLTHIY)

    try:
        print('scoring LTHIZ')
        for x in range(len(LTHIZ)):
            pengurangan = LTHIZ[x+1] - LTHIZ[x]
            penguranganLTHIZ.append(pengurangan)
            if pengurangan > 0:
                skorLTHIZ = 2
                hasilSkorLTHIZ.append(skorLTHIZ)
            elif pengurangan < 0:
                skorLTHIZ = 1
                hasilSkorLTHIZ.append(skorLTHIZ)
            elif pengurangan == 0:
                skorLTHIZ = 1
                hasilSkorLTHIZ.append(skorLTHIZ)
    except IndexError:
        skorLTHIZ = 1
        penguranganLTHIZ.append(0)
        hasilSkorLTHIZ.append(skorLTHIZ)
    print(LTHIZ)
    print(penguranganLTHIZ)
    print(hasilSkorLTHIZ)

    # # LTHI END

    # # RANK START
    try:
        print('scoring RANKX')
        for x in range(len(RANKX)):
            pengurangan = RANKX[x+1] - RANKX[x]
            penguranganRANKX.append(pengurangan)
            if pengurangan > 0:
                skorRANKX = 2
                hasilSkorRANKX.append(skorRANKX)
            elif pengurangan < 0:
                skorRANKX = 1
                hasilSkorRANKX.append(skorRANKX)
            elif pengurangan == 0:
                skorRANKX = 1
                hasilSkorRANKX.append(skorRANKX)
    except IndexError:
        skorRANKX = 1
        penguranganRANKX.append(0)
        hasilSkorRANKX.append(skorRANKX)
    print(RANKX)
    print(penguranganRANKX)
    print(hasilSkorRANKX)

    try:
        print('scoring RANKY')
        for x in range(len(RANKY)):
            pengurangan = RANKY[x+1] - RANKY[x]
            penguranganRANKY.append(pengurangan)
            if pengurangan > 0:
                skorRANKY = 2
                hasilSkorRANKY.append(skorRANKY)
            elif pengurangan < 0:
                skorRANKY = 1
                hasilSkorRANKY.append(skorRANKY)
            elif pengurangan == 0:
                skorRANKY = 1
                hasilSkorRANKY.append(skorRANKY)
    except IndexError:
        skorRANKY = 1
        penguranganRANKY.append(0)
        hasilSkorRANKY.append(skorRANKY)
    print(RANKY)
    print(penguranganRANKY)
    print(hasilSkorRANKY)

    try:
        print('scoring RANKZ')
        for x in range(len(RANKZ)):
            pengurangan = RANKZ[x+1] - RANKZ[x]
            penguranganRANKZ.append(pengurangan)
            if pengurangan > 0:
                skorRANKZ = 2
                hasilSkorRANKZ.append(skorRANKZ)
            elif pengurangan < 0:
                skorRANKZ = 1
                hasilSkorRANKZ.append(skorRANKZ)
            elif pengurangan == 0:
                skorRANKZ = 1
                hasilSkorRANKZ.append(skorRANKZ)
    except IndexError:
        skorRANKZ = 1
        penguranganRANKZ.append(0)
        hasilSkorRANKZ.append(skorRANKZ)
    print(RANKZ)
    print(penguranganRANKZ)
    print(hasilSkorRANKZ)

    # # RANK END

    # # RKNE START
    try:
        print('scoring RKNEX')
        for x in range(len(RKNEX)):
            pengurangan = RKNEX[x+1] - RKNEX[x]
            penguranganRKNEX.append(pengurangan)
            if pengurangan > 0:
                skorRKNEX = 2
                hasilSkorRKNEX.append(skorRKNEX)
            elif pengurangan < 0:
                skorRKNEX = 1
                hasilSkorRKNEX.append(skorRKNEX)
            elif pengurangan == 0:
                skorRKNEX = 1
                hasilSkorRKNEX.append(skorRKNEX)
    except IndexError:
        skorRKNEX = 1
        penguranganRKNEX.append(0)
        hasilSkorRKNEX.append(skorRKNEX)
    print(RKNEX)
    print(penguranganRKNEX)
    print(hasilSkorRKNEX)

    try:
        print('scoring RKNEY')
        for x in range(len(RKNEY)):
            pengurangan = RKNEY[x+1] - RKNEY[x]
            penguranganRKNEY.append(pengurangan)
            if pengurangan > 0:
                skorRKNEY = 2
                hasilSkorRKNEY.append(skorRKNEY)
            elif pengurangan < 0:
                skorRKNEY = 1
                hasilSkorRKNEY.append(skorRKNEY)
            elif pengurangan == 0:
                skorRKNEY = 1
                hasilSkorRKNEY.append(skorRKNEY)
    except IndexError:
        skorRKNEY = 1
        penguranganRKNEY.append(0)
        hasilSkorRKNEY.append(skorRKNEY)
    print(RKNEY)
    print(penguranganRKNEY)
    print(hasilSkorRKNEY)

    try:
        print('scoring RKNEZ')
        for x in range(len(RKNEZ)):
            pengurangan = RKNEZ[x+1] - RKNEZ[x]
            penguranganRKNEZ.append(pengurangan)
            if pengurangan > 0:
                skorRKNEZ = 2
                hasilSkorRKNEZ.append(skorRKNEZ)
            elif pengurangan < 0:
                skorRKNEZ = 1
                hasilSkorRKNEZ.append(skorRKNEZ)
            elif pengurangan == 0:
                skorRKNEZ = 1
                hasilSkorRKNEZ.append(skorRKNEZ)
    except IndexError:
        skorRKNEZ = 1
        penguranganRKNEZ.append(0)
        hasilSkorRKNEZ.append(skorRKNEZ)
    print(RKNEZ)
    print(penguranganRKNEZ)
    print(hasilSkorRKNEZ)

    # # RHEE START
    try:
        print('scoring RHEEX')
        for x in range(len(RHEEX)):
            pengurangan = RHEEX[x+1] - RHEEX[x]
            penguranganRHEEX.append(pengurangan)
            if pengurangan > 0:
                skorRHEEX = 2
                hasilSkorRHEEX.append(skorRHEEX)
            elif pengurangan < 0:
                skorRHEEX = 1
                hasilSkorRHEEX.append(skorRHEEX)
            elif pengurangan == 0:
                skorRHEEX = 1
                hasilSkorRHEEX.append(skorRHEEX)
    except IndexError:
        skorRHEEX = 1
        penguranganRHEEX.append(0)
        hasilSkorRHEEX.append(skorRHEEX)
    print(RHEEX)
    print(penguranganRHEEX)
    print(hasilSkorRHEEX)

    try:
        print('scoring RHEEY')
        for x in range(len(RHEEY)):
            pengurangan = RHEEY[x+1] - RHEEY[x]
            penguranganRHEEY.append(pengurangan)
            if pengurangan > 0:
                skorRHEEY = 2
                hasilSkorRHEEY.append(skorRHEEY)
            elif pengurangan < 0:
                skorRHEEY = 1
                hasilSkorRHEEY.append(skorRHEEY)
            elif pengurangan == 0:
                skorRHEEY = 1
                hasilSkorRHEEY.append(skorRHEEY)
    except IndexError:
        skorRHEEY = 1
        penguranganRHEEY.append(0)
        hasilSkorRHEEY.append(skorRHEEY)
    print(RHEEY)
    print(penguranganRHEEY)
    print(hasilSkorRHEEY)

    try:
        print('scoring RHEEZ')
        for x in range(len(RHEEZ)):
            pengurangan = RHEEZ[x+1] - RHEEZ[x]
            penguranganRHEEZ.append(pengurangan)
            if pengurangan > 0:
                skorRHEEZ = 2
                hasilSkorRHEEZ.append(skorRHEEZ)
            elif pengurangan < 0:
                skorRHEEZ = 1
                hasilSkorRHEEZ.append(skorRHEEZ)
            elif pengurangan == 0:
                skorRHEEZ = 1
                hasilSkorRHEEZ.append(skorRHEEZ)
    except IndexError:
        skorRHEEZ = 1
        penguranganRHEEZ.append(0)
        hasilSkorRHEEZ.append(skorRHEEZ)
    print(RHEEZ)
    print(penguranganRHEEZ)
    print(hasilSkorRHEEZ)

    # # RHEE END

    # # LTOE START
    try:
        print('scoring LTOEX')
        for x in range(len(LTOEX)):
            pengurangan = LTOEX[x+1] - LTOEX[x]
            penguranganLTOEX.append(pengurangan)
            if pengurangan > 0:
                skorLTOEX = 2
                hasilSkorLTOEX.append(skorLTOEX)
            elif pengurangan < 0:
                skorLTOEX = 1
                hasilSkorLTOEX.append(skorLTOEX)
            elif pengurangan == 0:
                skorLTOEX = 1
                hasilSkorLTOEX.append(skorLTOEX)
    except IndexError:
        skorLTOEX = 1
        penguranganLTOEX.append(0)
        hasilSkorLTOEX.append(skorLTOEX)
    print(LTOEX)
    print(penguranganLTOEX)
    print(hasilSkorLTOEX)

    try:
        print('scoring LTOEY')
        for x in range(len(LTOEY)):
            pengurangan = LTOEY[x+1] - LTOEY[x]
            penguranganLTOEY.append(pengurangan)
            if pengurangan > 0:
                skorLTOEY = 2
                hasilSkorLTOEY.append(skorLTOEY)
            elif pengurangan < 0:
                skorLTOEY = 1
                hasilSkorLTOEY.append(skorLTOEY)
            elif pengurangan == 0:
                skorLTOEY = 1
                hasilSkorLTOEY.append(skorLTOEY)
    except IndexError:
        skorLTOEY = 1
        penguranganLTOEY.append(0)
        hasilSkorLTOEY.append(skorLTOEY)
    print(LTOEY)
    print(penguranganLTOEY)
    print(hasilSkorLTOEY)

    try:
        print('scoring LTOEZ')
        for x in range(len(LTOEZ)):
            pengurangan = LTOEZ[x+1] - LTOEZ[x]
            penguranganLTOEZ.append(pengurangan)
            if pengurangan > 0:
                skorLTOEZ = 2
                hasilSkorLTOEZ.append(skorLTOEZ)
            elif pengurangan < 0:
                skorLTOEZ = 1
                hasilSkorLTOEZ.append(skorLTOEZ)
            elif pengurangan == 0:
                skorLTOEZ = 1
                hasilSkorLTOEZ.append(skorLTOEZ)
    except IndexError:
        skorLTOEZ = 1
        penguranganLTOEZ.append(0)
        hasilSkorLTOEZ.append(skorLTOEZ)
    print(LTOEZ)
    print(penguranganLTOEZ)
    print(hasilSkorLTOEZ)

    # # LTOE END

    # # RASI START
    try:
        print('scoring RASIX')
        for x in range(len(RASIX)):
            pengurangan = RASIX[x+1] - RASIX[x]
            penguranganRASIX.append(pengurangan)
            if pengurangan > 0:
                skorRASIX = 2
                hasilSkorRASIX.append(skorRASIX)
            elif pengurangan < 0:
                skorRASIX = 1
                hasilSkorRASIX.append(skorRASIX)
            elif pengurangan == 0:
                skorRASIX = 1
                hasilSkorRASIX.append(skorRASIX)
    except IndexError:
        skorRASIX = 1
        penguranganRASIX.append(0)
        hasilSkorRASIX.append(skorRASIX)
    print(RASIX)
    print(penguranganRASIX)
    print(hasilSkorRASIX)

    try:
        print('scoring RASIY')
        for x in range(len(RASIY)):
            pengurangan = RASIY[x+1] - RASIY[x]
            penguranganRASIY.append(pengurangan)
            if pengurangan > 0:
                skorRASIY = 2
                hasilSkorRASIY.append(skorRASIY)
            elif pengurangan < 0:
                skorRASIY = 1
                hasilSkorRASIY.append(skorRASIY)
            elif pengurangan == 0:
                skorRASIY = 1
                hasilSkorRASIY.append(skorRASIY)
    except IndexError:
        skorRASIY = 1
        penguranganRASIY.append(0)
        hasilSkorRASIY.append(skorRASIY)
    print(RASIY)
    print(penguranganRASIY)
    print(hasilSkorRASIY)

    try:
        print('scoring RASIZ')
        for x in range(len(RASIZ)):
            pengurangan = RASIZ[x+1] - RASIZ[x]
            penguranganRASIZ.append(pengurangan)
            if pengurangan > 0:
                skorRASIZ = 2
                hasilSkorRASIZ.append(skorRASIZ)
            elif pengurangan < 0:
                skorRASIZ = 1
                hasilSkorRASIZ.append(skorRASIZ)
            elif pengurangan == 0:
                skorRASIZ = 1
                hasilSkorRASIZ.append(skorRASIZ)
    except IndexError:
        skorRASIZ = 1
        penguranganRASIZ.append(0)
        hasilSkorRASIZ.append(skorRASIZ)
    print(RASIZ)
    print(penguranganRASIZ)
    print(hasilSkorRASIZ)

    # # LASI START
    try:
        print('scoring LASIX')
        for x in range(len(LASIX)):
            pengurangan = LASIX[x+1] - LASIX[x]
            penguranganLASIX.append(pengurangan)
            if pengurangan > 0:
                skorLASIX = 2
                hasilSkorLASIX.append(skorLASIX)
            elif pengurangan < 0:
                skorLASIX = 1
                hasilSkorLASIX.append(skorLASIX)
            elif pengurangan == 0:
                skorLASIX = 1
                hasilSkorLASIX.append(skorLASIX)
    except IndexError:
        skorLASIX = 1
        penguranganLASIX.append(0)
        hasilSkorLASIX.append(skorLASIX)
    print(LASIX)
    print(penguranganLASIX)
    print(hasilSkorLASIX)

    try:
        print('scoring LASIY')
        for x in range(len(LASIY)):
            pengurangan = LASIY[x+1] - LASIY[x]
            penguranganLASIY.append(pengurangan)
            if pengurangan > 0:
                skorLASIY = 2
                hasilSkorLASIY.append(skorLASIY)
            elif pengurangan < 0:
                skorLASIY = 1
                hasilSkorLASIY.append(skorLASIY)
            elif pengurangan == 0:
                skorLASIY = 1
                hasilSkorLASIY.append(skorLASIY)
    except IndexError:
        skorLASIY = 1
        penguranganLASIY.append(0)
        hasilSkorLASIY.append(skorLASIY)
    print(LASIY)
    print(penguranganLASIY)
    print(hasilSkorLASIY)

    try:
        print('scoring LASIZ')
        for x in range(len(LASIZ)):
            pengurangan = LASIZ[x+1] - LASIZ[x]
            penguranganLASIZ.append(pengurangan)
            if pengurangan > 0:
                skorLASIZ = 2
                hasilSkorLASIZ.append(skorLASIZ)
            elif pengurangan < 0:
                skorLASIZ = 1
                hasilSkorLASIZ.append(skorLASIZ)
            elif pengurangan == 0:
                skorLASIZ = 1
                hasilSkorLASIZ.append(skorLASIZ)
    except IndexError:
        skorLASIZ = 1
        penguranganLASIZ.append(0)
        hasilSkorLASIZ.append(skorLASIZ)

    print(LASIZ)
    print(penguranganLASIZ)
    print(hasilSkorLASIZ)

    # # LASI END
    # print('FINAL!!!')
    # # print(penguranganLPSIX)
    # # print(penguranganLPSIY)
    # # print(penguranganLPSIX)
    # # print(sum(hasilSkorLPSIX))
    # # print(frame_data)
    # # print(markers_fix)
    # # print(LPSIX)

    # # arraykosong = [[i][sumbuX][sumbuY][sumbuZ][penguranganLPSIX][penguranganLPSIY][penguranganLPSIZ][hasilSkorLPSIX][hasilSkorLPSIY][hasilSkorLPSIZ]]

    # for i, points, analog in reader.read_frames():
    #     frame = i
    #     if i in frame_no_list:
    #         for j, marker in enumerate(markers):
    #             if marker in markers_fix:
    #                 if marker == markers_fix[0]:
    #                     namaMarker = marker
    #                     sumbuX = np.array(points[j, 0])
    #                     sumbuY = np.array(points[j, 1])
    #                     sumbuZ = np.array(points[j, 2])
    #                     indeksLPSIX = list(range(len(LPSIX)))
    #                     print ('')
    #                     print(f'Frame {frame} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ} hasil skoring LPSI X : {sum(hasilSkorLPSIX)} hasil skoring LPSI Y : {sum(hasilSkorLPSIY)} hasil skoring LPSI Z : {sum(hasilSkorLPSIZ)}')
    #                     print ('')
    #                     print(f'pengurangan LPSIX {penguranganLPSIX} pengurangan LPSIY {penguranganLPSIY} pengurangan LPSIZ {penguranganLPSIZ}')
    # for k in range(len(indeksLPSIX)):
    #     print(f'Sumbu X : {sumbuX[k]}')
    # cara2 end

    # print(indeksLPSIX)
    # x_data.append(points[j, 0])
    # y_data.append(points[j, 1])
    # z_data.append(points[j, 2])

    # LPSIX.append(points[j, 0])
    # LPSIY.append(points[j, 1])
    # LPSIZ.append(points[j, 2])

    # frame_data.append(i)
    # print(f'Frame {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ} coba X: ')

    #
    # finalScoreX = (hasilSkorLPSIX + hasilSkorRPSIX + hasilSkorRTOEX + hasilSkorLHEEX +
    #                hasilSkorLKNEX + hasilSkorLTIBX + hasilSkorRTIBX + hasilSkorLANKX + hasilSkorRTHIX +
    #                hasilSkorLTHIX + hasilSkorRANKX + hasilSkorRKNEX + hasilSkorRHEEX + hasilSkorLTOEX
    #                + hasilSkorRASIX + hasilSkorLASIX)
    # print (finalScoreX)

    # print(hasilSkorLASIX)
    # print('')
    # print(hasilSkorLASIY)
    # print('')
    # print(hasilSkorLASIZ)

    # print(x_data)

    # print(hasilScoringX)
    # print(hasilScoringY)
    # print(hasilScoringZ)

    # for i in range(len(x_data)):
    #     print(i)
    # print(frame_data)
    # print(markers_fix)
    # print(frame_no_list)
    # print(np.array(x_data).flatten())

    # penjumlahan scoring LPSI X
    # print('penjumlahan scoring LPSI X')
    # panjang_array_frame = len(frame_no_list)
    # print(panjang_array_frame)
    # totalLPSIX = 0

    # for i in range(0, len(hasilSkorX), 16):
    #     totalLPSIX += hasilSkorX[i]
    # print(totalLPSIX)
    # for x in range(len(hasilSkorX)):
    #      penjumlahanLPSIX = hasilSkorX[x+16] + hasilSkorX[x]
    #      LPSIX.append(penjumlahanLPSIX)
    # print(hasilSkorX)

    gabungkanx_data = []
    gabungkany_data = []
    gabungkanz_data = []
    gabungkanPenguranganx_data = []
    gabungkanPengurangany_data = []
    gabungkanPenguranganz_data = []

    for i in range(len(LPSIX)):
        gabungkanx_data.append(hasilSkorLPSIX[i])
        gabungkanx_data.append(hasilSkorRPSIX[i])
        gabungkanx_data.append(hasilSkorRTOEX[i])
        gabungkanx_data.append(hasilSkorLHEEX[i])

        gabungkanx_data.append(hasilSkorLKNEX[i])
        gabungkanx_data.append(hasilSkorLTIBX[i])
        gabungkanx_data.append(hasilSkorRTIBX[i])
        gabungkanx_data.append(hasilSkorLANKX[i])

        gabungkanx_data.append(hasilSkorRTHIX[i])
        gabungkanx_data.append(hasilSkorLTHIX[i])
        gabungkanx_data.append(hasilSkorRANKX[i])
        gabungkanx_data.append(hasilSkorRKNEX[i])

        gabungkanx_data.append(hasilSkorRHEEX[i])
        gabungkanx_data.append(hasilSkorLTOEX[i])
        gabungkanx_data.append(hasilSkorRASIX[i])
        gabungkanx_data.append(hasilSkorLASIX[i])

        gabungkany_data.append(hasilSkorLPSIY[i])
        gabungkany_data.append(hasilSkorRPSIY[i])
        gabungkany_data.append(hasilSkorRTOEY[i])
        gabungkany_data.append(hasilSkorLHEEY[i])

        gabungkany_data.append(hasilSkorLKNEY[i])
        gabungkany_data.append(hasilSkorLTIBY[i])
        gabungkany_data.append(hasilSkorRTIBY[i])
        gabungkany_data.append(hasilSkorLANKY[i])

        gabungkany_data.append(hasilSkorRTHIY[i])
        gabungkany_data.append(hasilSkorLTHIY[i])
        gabungkany_data.append(hasilSkorRANKY[i])
        gabungkany_data.append(hasilSkorRKNEY[i])

        gabungkany_data.append(hasilSkorRHEEY[i])
        gabungkany_data.append(hasilSkorLTOEY[i])
        gabungkany_data.append(hasilSkorRASIY[i])
        gabungkany_data.append(hasilSkorLASIY[i])

        gabungkanz_data.append(hasilSkorLPSIZ[i])
        gabungkanz_data.append(hasilSkorRPSIZ[i])
        gabungkanz_data.append(hasilSkorRTOEZ[i])
        gabungkanz_data.append(hasilSkorLHEEZ[i])

        gabungkanz_data.append(hasilSkorLKNEZ[i])
        gabungkanz_data.append(hasilSkorLTIBZ[i])
        gabungkanz_data.append(hasilSkorRTIBZ[i])
        gabungkanz_data.append(hasilSkorLANKZ[i])

        gabungkanz_data.append(hasilSkorRTHIZ[i])
        gabungkanz_data.append(hasilSkorLTHIZ[i])
        gabungkanz_data.append(hasilSkorRANKZ[i])
        gabungkanz_data.append(hasilSkorRKNEX[i])

        gabungkanz_data.append(hasilSkorRHEEZ[i])
        gabungkanz_data.append(hasilSkorLTOEZ[i])
        gabungkanz_data.append(hasilSkorRASIZ[i])
        gabungkanz_data.append(hasilSkorLASIZ[i])

        gabungkanPenguranganx_data.append(penguranganLPSIX[i])
        gabungkanPenguranganx_data.append(penguranganRPSIX[i])
        gabungkanPenguranganx_data.append(penguranganRTOEX[i])
        gabungkanPenguranganx_data.append(penguranganLHEEX[i])

        gabungkanPenguranganx_data.append(penguranganLKNEX[i])
        gabungkanPenguranganx_data.append(penguranganLTIBX[i])
        gabungkanPenguranganx_data.append(penguranganRTIBX[i])
        gabungkanPenguranganx_data.append(penguranganLANKX[i])

        gabungkanPenguranganx_data.append(penguranganRTHIX[i])
        gabungkanPenguranganx_data.append(penguranganLTHIX[i])
        gabungkanPenguranganx_data.append(penguranganRANKX[i])
        gabungkanPenguranganx_data.append(penguranganRKNEX[i])

        gabungkanPenguranganx_data.append(penguranganRHEEX[i])
        gabungkanPenguranganx_data.append(penguranganLTOEX[i])
        gabungkanPenguranganx_data.append(penguranganRASIX[i])
        gabungkanPenguranganx_data.append(penguranganLASIX[i])

        gabungkanPengurangany_data.append(penguranganLPSIY[i])
        gabungkanPengurangany_data.append(penguranganRPSIY[i])
        gabungkanPengurangany_data.append(penguranganRTOEY[i])
        gabungkanPengurangany_data.append(penguranganLHEEY[i])

        gabungkanPengurangany_data.append(penguranganLKNEY[i])
        gabungkanPengurangany_data.append(penguranganLTIBY[i])
        gabungkanPengurangany_data.append(penguranganRTIBY[i])
        gabungkanPengurangany_data.append(penguranganLANKY[i])

        gabungkanPengurangany_data.append(penguranganRTHIY[i])
        gabungkanPengurangany_data.append(penguranganLTHIY[i])
        gabungkanPengurangany_data.append(penguranganRANKY[i])
        gabungkanPengurangany_data.append(penguranganRKNEY[i])

        gabungkanPengurangany_data.append(penguranganRHEEY[i])
        gabungkanPengurangany_data.append(penguranganLTOEY[i])
        gabungkanPengurangany_data.append(penguranganRASIY[i])
        gabungkanPengurangany_data.append(penguranganLASIY[i])

        gabungkanPenguranganz_data.append(penguranganLPSIZ[i])
        gabungkanPenguranganz_data.append(penguranganRPSIZ[i])
        gabungkanPenguranganz_data.append(penguranganRTOEZ[i])
        gabungkanPenguranganz_data.append(penguranganLHEEZ[i])

        gabungkanPenguranganz_data.append(penguranganLKNEZ[i])
        gabungkanPenguranganz_data.append(penguranganLTIBZ[i])
        gabungkanPenguranganz_data.append(penguranganRTIBZ[i])
        gabungkanPenguranganz_data.append(penguranganLANKZ[i])

        gabungkanPenguranganz_data.append(penguranganRTHIZ[i])
        gabungkanPenguranganz_data.append(penguranganLTHIZ[i])
        gabungkanPenguranganz_data.append(penguranganRANKZ[i])
        gabungkanPenguranganz_data.append(penguranganRKNEZ[i])

        gabungkanPenguranganz_data.append(penguranganRHEEZ[i])
        gabungkanPenguranganz_data.append(penguranganLTOEZ[i])
        gabungkanPenguranganz_data.append(penguranganRASIZ[i])
        gabungkanPenguranganz_data.append(penguranganLASIZ[i])

    # Penjumlahan Skoring
    penjumlahanLPSIX.append(sum(hasilSkorLPSIX))
    penjumlahanLPSIY.append(sum(hasilSkorLPSIY))
    penjumlahanLPSIZ.append(sum(hasilSkorLPSIZ))

    penjumlahanRPSIX.append(sum(hasilSkorRPSIX))
    penjumlahanRPSIY.append(sum(hasilSkorRPSIY))
    penjumlahanRPSIZ.append(sum(hasilSkorRPSIZ))

    penjumlahanRTOEX.append(sum(hasilSkorRTOEX))
    penjumlahanRTOEY.append(sum(hasilSkorRTOEY))
    penjumlahanRTOEZ.append(sum(hasilSkorRTOEZ))

    penjumlahanLHEEX.append(sum(hasilSkorLHEEX))
    penjumlahanLHEEY.append(sum(hasilSkorLHEEY))
    penjumlahanLHEEZ.append(sum(hasilSkorLHEEZ))

    penjumlahanLKNEX.append(sum(hasilSkorLKNEX))
    penjumlahanLKNEY.append(sum(hasilSkorLKNEY))
    penjumlahanLKNEZ.append(sum(hasilSkorLKNEZ))

    penjumlahanLTIBX.append(sum(hasilSkorLTIBX))
    penjumlahanLTIBY.append(sum(hasilSkorLTIBY))
    penjumlahanLTIBZ.append(sum(hasilSkorLTIBZ))

    penjumlahanRTIBX.append(sum(hasilSkorRTIBX))
    penjumlahanRTIBY.append(sum(hasilSkorRTIBY))
    penjumlahanRTIBZ.append(sum(hasilSkorRTIBZ))

    penjumlahanLANKX.append(sum(hasilSkorLANKX))
    penjumlahanLANKY.append(sum(hasilSkorLANKY))
    penjumlahanLANKZ.append(sum(hasilSkorLANKZ))

    penjumlahanRTHIX.append(sum(hasilSkorRTHIX))
    penjumlahanRTHIY.append(sum(hasilSkorRTHIY))
    penjumlahanRTHIZ.append(sum(hasilSkorRTHIZ))

    penjumlahanLTHIX.append(sum(hasilSkorLTHIX))
    penjumlahanLTHIY.append(sum(hasilSkorLTHIY))
    penjumlahanLTHIZ.append(sum(hasilSkorLTHIZ))

    penjumlahanRANKX.append(sum(hasilSkorRANKX))
    penjumlahanRANKY.append(sum(hasilSkorRANKY))
    penjumlahanRANKZ.append(sum(hasilSkorRANKZ))

    penjumlahanRKNEX.append(sum(hasilSkorRKNEX))
    penjumlahanRKNEY.append(sum(hasilSkorRKNEY))
    penjumlahanRKNEZ.append(sum(hasilSkorRKNEZ))

    penjumlahanRHEEX.append(sum(hasilSkorRHEEX))
    penjumlahanRHEEY.append(sum(hasilSkorRHEEY))
    penjumlahanRHEEZ.append(sum(hasilSkorRHEEZ))

    penjumlahanLTOEX.append(sum(hasilSkorLTOEX))
    penjumlahanLTOEY.append(sum(hasilSkorLTOEY))
    penjumlahanLTOEZ.append(sum(hasilSkorLTOEZ))

    penjumlahanRASIX.append(sum(hasilSkorRASIX))
    penjumlahanRASIY.append(sum(hasilSkorRASIY))
    penjumlahanRASIZ.append(sum(hasilSkorRASIZ))

    penjumlahanLASIX.append(sum(hasilSkorLASIX))
    penjumlahanLASIY.append(sum(hasilSkorLASIY))
    penjumlahanLASIZ.append(sum(hasilSkorLASIZ))

    ratarataLPSI = []
    ratarataRPSI = []
    ratarataRTOE = []
    ratarataLHEE = []
    ratarataLKNE = []
    ratarataLTIB = []
    ratarataRTIB = []
    ratarataLANK = []
    ratarataRTHI = []
    ratarataLTHI = []
    ratarataRANK = []
    ratarataRKNE = []
    ratarataRHEE = []
    ratarataLTOE = []
    ratarataRASI = []
    ratarataLASI = []

    averageLPSI = sum(penjumlahanLPSIX + penjumlahanLPSIY +
                      penjumlahanLPSIZ) / len(hasilSkorLPSIX)
    ratarataLPSI.append(averageLPSI)

    averageRPSI = sum(penjumlahanRPSIX + penjumlahanRPSIY +
                      penjumlahanRPSIZ) / len(hasilSkorRPSIX)
    ratarataRPSI.append(averageRPSI)

    averageRTOE = sum(penjumlahanRTOEX + penjumlahanRTOEY +
                      penjumlahanRTOEZ) / len(hasilSkorRTOEX)
    ratarataRTOE.append(averageRTOE)

    averageLHEE = sum(penjumlahanLHEEX + penjumlahanLHEEY +
                      penjumlahanLHEEZ) / len(hasilSkorLHEEX)
    ratarataLHEE.append(averageLHEE)

    averageLKNE = sum(penjumlahanLKNEX + penjumlahanLKNEY +
                      penjumlahanLKNEZ) / len(hasilSkorLKNEX)
    ratarataLKNE.append(averageLKNE)

    averageLTIB = sum(penjumlahanLTIBX + penjumlahanLTIBY +
                      penjumlahanLTIBZ) / len(hasilSkorLTIBX)
    ratarataLTIB.append(averageLTIB)

    averageRTIB = sum(penjumlahanRTIBX + penjumlahanRTIBY +
                      penjumlahanRTIBZ) / len(hasilSkorRTIBX)
    ratarataRTIB.append(averageRTIB)

    averageLANK = sum(penjumlahanLANKX + penjumlahanLANKY +
                      penjumlahanLANKZ) / len(hasilSkorLANKX)
    ratarataLANK.append(averageLANK)

    averageRTHI = sum(penjumlahanRTHIX + penjumlahanRTHIY +
                      penjumlahanRTHIZ) / len(hasilSkorRTHIX)
    ratarataRTHI.append(averageRTHI)

    averageLTHI = sum(penjumlahanLTHIX + penjumlahanLTHIY +
                      penjumlahanLTHIZ) / len(hasilSkorLTHIX)
    ratarataLTHI.append(averageLTHI)

    averageRANK = sum(penjumlahanRANKX + penjumlahanRANKY +
                      penjumlahanRANKZ) / len(hasilSkorRANKX)
    ratarataRANK.append(averageRANK)

    averageRKNE = sum(penjumlahanRKNEX + penjumlahanRKNEY +
                      penjumlahanRKNEZ) / len(hasilSkorRKNEX)
    ratarataRKNE.append(averageRKNE)

    averageRHEE = sum(penjumlahanRHEEX + penjumlahanRHEEY +
                      penjumlahanRHEEZ) / len(hasilSkorRHEEX)
    ratarataRHEE.append(averageRHEE)

    averageLTOE = sum(penjumlahanLTOEX + penjumlahanLTOEY +
                      penjumlahanLTOEZ) / len(hasilSkorLTOEX)
    ratarataLTOE.append(averageLTOE)

    averageRASI = sum(penjumlahanRASIX + penjumlahanRASIY +
                      penjumlahanRASIZ) / len(hasilSkorRASIX)
    ratarataRASI.append(averageRASI)

    averageLASI = sum(penjumlahanLASIX + penjumlahanLASIY +
                      penjumlahanLASIZ) / len(hasilSkorLASIX)
    ratarataLASI.append(averageLASI)

    allaverage = ratarataLPSI + ratarataRPSI + ratarataRTOE + ratarataLHEE + ratarataLKNE + ratarataLTIB + ratarataRTIB + \
        ratarataLANK + ratarataRTHI + ratarataLTHI + ratarataRANK + \
        ratarataRKNE + ratarataRHEE + ratarataLTOE + ratarataRASI + ratarataLASI
    print(allaverage)
    # print(ratarataLASI)
    # print(ratarataRPSI)
    # print(ratarataRTOE)
    # print(len(hasilSkorRTOEX))
    # # print(len(gabungkanx_data))
    # print()

    # #dataframe cara2

    df = pd.DataFrame({
        'Frame': frame_data,
        'Marker': markers_fix * len(frame_no_list),
        'X': np.array(x_data).flatten(),
        'Y': np.array(y_data).flatten(),
        'Z': np.array(z_data).flatten(),
        'Pengurangan X': gabungkanPenguranganx_data,
        ' Scoring X': gabungkanx_data,
        'Pengurangan Y': gabungkanPengurangany_data,
        ' Scoring Y': gabungkany_data,
        'Pengurangan Z': gabungkanPenguranganz_data,
        ' Scoring Z': gabungkanz_data,
    })

    df2 = pd.DataFrame({'Jumlah LPSIX': penjumlahanLPSIX,
                        'Jumlah LPSIY': penjumlahanLPSIY,
                        'Jumlah LPSIZ': penjumlahanLPSIZ,
                        'Jumlah RPSIX': penjumlahanRPSIX,
                        'Jumlah RPSIY': penjumlahanRPSIY,
                        'Jumlah RPSIZ': penjumlahanRPSIZ,
                        'Jumlah RTOEX': penjumlahanRTOEX,
                        'Jumlah RTOEY': penjumlahanRTOEY,
                        'Jumlah RTOEZ': penjumlahanRTOEZ,
                        'Jumlah LHEEX': penjumlahanLHEEX,
                        'Jumlah LHEEY': penjumlahanLHEEY,
                        'Jumlah LHEEZ': penjumlahanLHEEZ,
                        'Jumlah LKNEX': penjumlahanLKNEX,
                        'Jumlah LKNEY': penjumlahanLKNEY,
                        'Jumlah LKNEZ': penjumlahanLKNEZ,
                        'Jumlah LTIBX': penjumlahanLTIBX,
                        'Jumlah LTIBY': penjumlahanLTIBY,
                        'Jumlah LTIBZ': penjumlahanLTIBZ,
                        'Jumlah RTIBX': penjumlahanRTIBX,
                        'Jumlah RTIBY': penjumlahanRTIBY,
                        'Jumlah RTIBZ': penjumlahanRTIBZ,
                        'Jumlah LANKX': penjumlahanLANKX,
                        'Jumlah LANKY': penjumlahanLANKY,
                        'Jumlah LANKZ': penjumlahanLANKZ,
                        'Jumlah RTHIX': penjumlahanRTHIX,
                        'Jumlah RTHIY': penjumlahanRTHIY,
                        'Jumlah RTHIZ': penjumlahanRTHIZ,
                        'Jumlah LTHIX': penjumlahanLTHIX,
                        'Jumlah LTHIY': penjumlahanLTHIY,
                        'Jumlah LTHIZ': penjumlahanLTHIZ,
                        'Jumlah RANKX': penjumlahanRANKX,
                        'Jumlah RANKY': penjumlahanRANKY,
                        'Jumlah RANKZ': penjumlahanRANKZ,
                        'Jumlah RKNEZ': penjumlahanRKNEZ,
                        'Jumlah RKNEY': penjumlahanRKNEY,
                        'Jumlah RKNEX': penjumlahanRKNEX,
                        'Jumlah RHEEX': penjumlahanRHEEX,
                        'Jumlah RHEEY': penjumlahanRHEEY,
                        'Jumlah RHEEZ': penjumlahanRHEEZ,
                        'Jumlah LTOEX': penjumlahanLTOEX,
                        'Jumlah LTOEY': penjumlahanLTOEY,
                        'Jumlah LTOEZ': penjumlahanLTOEZ,
                        'Jumlah RASIX': penjumlahanRASIX,
                        'Jumlah RASIY': penjumlahanRASIY,
                        'Jumlah RASIZ': penjumlahanRASIZ,
                        'Jumlah LASIX': penjumlahanLASIX,
                        'Jumlah LASIY': penjumlahanLASIY,
                        })

    df3 = pd.DataFrame({'All Average': allaverage})
    # # df_clean = df2.dropna()

    result = pd.concat([df, df3, df2], axis=1)
    print(result)
    marker = markers_fix * len(frame_no_list)
    # print(penjumlahanLPSIX)
    # print(penjumlahanRPSIX)

    # dataframe cara 3
    # df = pd.DataFrame({
    #     'Frame': frame_data,
    #     'Marker': markers_fix * len(frame_no_list),
    #     'X': np.array(x_data).flatten(),
    #     'Y': np.array(y_data).flatten(),
    #     'Z': np.array(z_data).flatten(),
    #     'Pengurangan X': datapenguranganX,
    #     ' Scoring X': hasilSkorX,
    #     'Pengurangan Y': datapenguranganY,
    #     ' Scoring Y': hasilSkorY,
    #     'Pengurangan Z': datapenguranganZ,
    #     ' Scoring Z': hasilSkorZ,
    # })
    # print(df)

    # print
    # wb = Workbook()
    # ws = wb.active
    # for r in dataframe_to_rows(result, index=False, header=True):
    #     ws.append(r)
    # wb.save('cobaSampaiScoring4Cara2.xlsx')
# perulangan : jika marker sama maka lakukan skoring
# mendeteksi karakter L dan R untuk membedakan kaki kiri dan kanan


# koneksi ke database mysql
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Iamironman123',
                             db='riyanlasso')

cursor = connection.cursor()

# # drop_query = "DROP TABLE AGNESKA"
# # cursor.execute(drop_query)

# # table_exists = False
cursor.execute("SHOW TABLES")
tables = [table[0] for table in cursor.fetchall()]

# # print(tables)
# # tablesUpdate = []
# # tablesUpdate.append(tables)
# # print(tablesUpdate)

namaPemilikData = 'DONI'
namaPemilikData = namaPemilikData.lower()

if namaPemilikData not in tables:
    print(f"tabel {namaPemilikData} belum ada")
    # tables.append(namaPemilikData)
    table_query = f"""
    CREATE TABLE IF NOT EXISTS {namaPemilikData} (
      id INTEGER PRIMARY KEY,
      Frame FLOAT,
      Marker VARCHAR(255),
      X_Cordinates FLOAT,
      X_Scoring FLOAT,
      Y_Cordinates FLOAT,
      Y_Scoring FLOAT,
      Z_Cordinates FLOAT,
      Z_Scoring FLOAT
    )
    """
    cursor.execute(table_query)
    print('Berhasil membuat tabel baru')

    for i in range(len(frame_data)):
        with connection.cursor() as cursor:
            # Query SQL untuk memasukkan data
            sql = f"INSERT INTO {namaPemilikData} (id, Frame, Marker, X_Cordinates, X_Scoring, Y_Cordinates, Y_Scoring, Z_Cordinates, Z_Scoring) VALUES ({i}, {frame_data[i]}, '{marker[i]}', {x_data[i]}, {gabungkanx_data[i]}, {y_data[i]}, {gabungkany_data[i]}, {z_data[i]}, {gabungkanz_data[i]})"
            cursor.execute(sql)
            # print('Ambil data dari setiap tabel')
            # sql2 = f"SELECT * FROM {namaPemilikData} (id, Frame, Marker, X_Cordinates, X_Scoring, Y_Cordinates, Y_Scoring, Z_Cordinates, Z_Scoring) VALUES ({i}, {frame_data[i]}, '{marker[i]}', {x_data[i]}, {gabungkanx_data[i]}, {y_data[i]}, {gabungkany_data[i]}, {z_data[i]}, {gabungkanz_data[i]})"
            # cursor.execute(sql2)
            # print(sql2)
        # Commit perubahan ke database
        connection.commit()
    print(f"Data {namaPemilikData} berhasil ditambahkan")
else:
    for i in tables:
        if i in tables:
            print(f"tabel {i} sudah ada")
print('')

with connection.cursor() as cursor:
    # Query SQL untuk memasukkan data
    print('Ambil data dari setiap tabel')
    for i in tables : 
        sql2 = f"SELECT * FROM riyanlasso.{i}"
        cursor.execute(sql2)
        print(f"\nData dari tabel {i}:")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    

connection.close()

