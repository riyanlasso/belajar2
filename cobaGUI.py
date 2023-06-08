import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QLineEdit,QPushButton
import pyqtgraph as pg
import numpy as np
import c3d


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh GUI PyQtGraph untuk File C3D")
        self.setGeometry(100, 100, 800, 600)

        # Buat widget untuk menampung grafik
        self.plot_widget = pg.PlotWidget()
        # input keyboard
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.height_input = QLineEdit()
        # Tampilkan data dari file C3D
        # self.show_c3d_data()
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.show_c3d_data())
        # Atur layout utama
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)

        # Buat widget utama dan atur layout utama
        main_widget = QWidget()
        main_widget.setLayout(layout)

        # Atur widget utama sebagai widget pusat dalam jendela utama
        self.setCentralWidget(main_widget)

    def show_c3d_data(self):
        with open('446448.c3d', 'rb') as handle:
            reader = c3d.Reader(handle)
            markers = reader.point_labels
            frames = []
            markers_to_show = []
            markers_to_show.append(markers)
            # menghilangkan spasi
            hilangkanSpasi = []
            for marker in markers:
                marker = marker.strip()
                hilangkanSpasi.append(marker)
            pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB','LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
            markers_fix = []
            for marker in hilangkanSpasi:
                if marker in pilihMarker:
                    markers_fix.append(marker)
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

                    for j, marker in enumerate(hilangkanSpasi):

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
        pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB','LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        self.plot_widget.plot(LPSIX,LPSIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        self.plot_widget.plot(RPSIX,RPSIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        self.plot_widget.plot(RTOEX,RTOEY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LHEEX,LHEEY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LKNEX,LKNEY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LTIBX,LTIBY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(RTIBX,RTIBX, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LANKX,LANKY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(RTHIX,RTHIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LTHIX,LTHIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(RANKX,RANKY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(RKNEX,RKNEY, pen=None, symbol='x', symbolSize=10,name='agneska')

        # self.plot_widget.plot(RHEEX,RHEEY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LTOEX,LTOEY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(RASIX,RASIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        # self.plot_widget.plot(LASIX,LASIY, pen=None, symbol='o', symbolSize=10,name='agneska')
        
        # self.plot_widget.plot(y_data, pen=None, symbol='o', symbolSize=5)
        # self.plot_widget.plot(z_data, pen=None, symbol='o', symbolSize=5)
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
