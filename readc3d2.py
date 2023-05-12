import c3d
import pandas as pd

# membuka file c3d
with open('currentFrame447.c3d', 'rb') as handle:
    reader = c3d.Reader(handle)

    # membaca header file c3d
    # header = reader.get_header()

    # mengambil data lintasan sumbu X, Y, dan Z dari marker yang dipilih
    markers_to_show = ['LPSI', 'RPSI', 'LTOE', 'RTOE', 'LHEE', 'RHEE', 'LKNE', 'RKNE', 'LTIB', 'RTIB', 'LANK', 'RANK', 'LTHI', 'RTHI', 'LASI', 'RASI']
    marker_indices = [i for i, label in enumerate(reader.point_labels) if label in markers_to_show]
    x_data, y_data, z_data = [], [], []
    for i, (frame_no, points, analog) in enumerate(reader.read_frames()):
        x_data.append(points[marker_indices, 0])
        y_data.append(points[marker_indices, 1])
        z_data.append(points[marker_indices, 2])

    # membuat DataFrame dari data lintasan sumbu X, Y, dan Z
    df = pd.DataFrame()
    for i, label in enumerate(markers_to_show):
        df[label + '_X'] = [x[i] for x in x_data]
        df[label + '_Y'] = [y[i] for y in y_data]
        df[label + '_Z'] = [z[i] for z in z_data]
    df.index = range(1, len(df) + 1)  # mengatur index menjadi nomor frame

    # menampilkan DataFrame
    print(df)
