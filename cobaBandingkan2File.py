import c3d
import numpy as np

# Load the first c3d file
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
    frame_data = []
    for q, points, analog in reader.read_frames():
        frame_no_list.append(q)

    my_marker = []

    for i, points, analog in reader.read_frames():
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
#cek frame
cekFrame1 = []

for i in frame_no_list : 
    # print(i)
    cekFrame1.append(i)
print(cekFrame1)

cekMarker = []
for i in markers_fix : 
    # print(i)
    cekMarker.append(i)
print(cekMarker)
# Load the second c3d file
# training
with open('446447.c3d', 'rb') as handle:
    reader = c3d.Reader(handle)
    markers = reader.point_labels
    # print(markers)
    frames = []
    markers_to_show = []
    markers_to_show.append(markers)
    frame_no_list = []
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

cekFrame2 = []
for j in frame_no_list :
     cekFrame2.append(j)
print(cekFrame2)

cekMarker2 = []
for j in markers_fix :
     cekMarker2.append(j)
print(cekMarker2)
# Compare the two files
print('membandingkan 2 File dari datanya')
if np.array_equal(cekFrame1, cekFrame2):
    print("kedua data sama")
else:
    print("kedua data berbeda")
    print(f'data pertama memiliki frame {cekFrame1} , sedangkan data kedua memiliki frame{cekFrame2}')
    if len(markers_fix) == len(cekMarker) and len(markers_fix) == len(cekMarker2):
        print("marker sama")
    
