import c3d
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

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
    print(frame_no_list)
    cobaArray = []
    for i, points, analog in reader.read_frames():
        for j, marker in enumerate(markers_fix):
            if marker in markers_fix:
                # frame_data.append(i)
                if marker == markers_fix[0]:
                    namaMarker = marker
                    sumbuX = np.array(points[j, 0])
                    sumbuY = np.array(points[j, 1])
                    sumbuZ = np.array(points[j, 2])

                    x_data.append(points[j, 0])
                    y_data.append(points[j, 1])
                    z_data.append(points[j, 2])

                    # LPSIX.append(points[j, 0])
                    # LPSIY.append(points[j, 1])
                    # LPSIZ.append(points[j, 2])
                    # cobaArray.append([i, namaMarker, sumbuX, sumbuY, sumbuZ])
                    print(
                        f'Frame : {i} Marker : {namaMarker} Sumbu X : {sumbuX} Sumbu Y : {sumbuY} Sumbu Z : {sumbuZ} ')
    
    # print(cobaArray)
    # print('cobaArray')
    # for j in cobaArray :
    #     print(j)
