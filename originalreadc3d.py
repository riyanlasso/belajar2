# import c3d
# import numpy as np
# import pandas as pd

# # membaca file C3D
# with open('currentFrame447.c3d', 'rb') as handle:
#     reader = c3d.Reader(handle)
#     markers = reader.point_labels

#     x_data, y_data, z_data = [], [], []
#     frame_no_list = []
#     for frame_no, points, analog in reader.read_frames():
#         frame_no_list.append(frame_no)
#         x_data.append(points[:, 0])
#         y_data.append(points[:, 1])
#         z_data.append(points[:, 2])


#     df = pd.DataFrame({'Frame': frame_no_list * len(markers),
#                        'Marker': np.repeat(markers, len(frame_no_list)),
#                        'X': np.array(x_data).flatten(),
#                        'Y': np.array(y_data).flatten(),
#                        'Z': np.array(z_data).flatten()})
#     print(df)

#     x_data, y_data, z_data = [], [], [], 
    
#     frame_no_list = []
    
#     markers_to_show = []
    
#     markers_to_show.append(markers) 
    
#     markers_list = (markers_to_show[0])
    
#     markers_fix = [markers_list[0],markers_list[1],
#                    markers_list[49],markers_list[38],
#                    markers_list[39],markers_list[48],
#                    markers_list[40],markers_list[47],
#                    markers_list[39],markers_list[48],
#                    markers_list[41],markers_list[42],
#                    markers_list[43],markers_list[46],
#                    markers_list[45],markers_list[44],] 

#     for frame_no, points, analog in reader.read_frames():
#             frame_no_list.append(frame_no)
#             for i, label in enumerate(markers_fix):
#                 if label in markers_fix:
#                     x_data.append(points[i, 0])
#                     y_data.append(points[i, 1])
#                     z_data.append(points[i, 2])
# markers_list[0],
#                    markers_list[1],
#                    markers_list[49],
#                    markers_list[38],
#                    markers_list[39],
#                    markers_list[48],
#                    markers_list[40],
#                    markers_list[47],
#                    markers_list[39],
#                    markers_list[48],
#                    markers_list[41],
#                    markers_list[42],
#                    markers_list[43],
#                    markers_list[46],
#                    markers_list[45],
#                    markers_list[44]
