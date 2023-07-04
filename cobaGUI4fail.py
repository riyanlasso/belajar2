import importlib
import sys
from PyQt5.QtWidgets import QScrollArea, QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QFileDialog
from PyQt5.QtGui import QScreen, QGuiApplication
from PyQt5.QtGui import QFont
import pyqtgraph as pg
import numpy as np
import pandas as pd
import c3d
import mysql.connector
import pymysql



class MainWindow(QMainWindow):
    # koneksikan ke database
    def databaseConnection(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlasso')
        cursor = connection.cursor()
        # cek tabel yang ada
        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata4']
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        return tables, cursor

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh GUI PyQtGraph")
        self.setGeometry(200, 200, 2000, 980)
        self.move(0,0)
        
        # screen = QGuiApplication.primaryScreen()
        # screen_geometry = screen.availableGeometry()
        # self.setGeometry(screen_geometry)
        

        # Buat input teks untuk nama, umur, dan tinggi badan
        self.name_input_training = QLineEdit()
        self.age_input_training = QLineEdit()
        self.height_input_training = QLineEdit()
        self.weight_input_training = QLineEdit()
        # grafik
        self.plot_widget_training_x = pg.PlotWidget()
        self.plot_widget_training_y = pg.PlotWidget()
        self.plot_widget_training_z = pg.PlotWidget()
        # x
        self.plot_widget_training_x.setWindowTitle("ALL TRAINING DATA")
        label_font = QFont("Arial", 12, QFont.Bold)
        self.plot_widget_training_x.getAxis(
            'left').setStyle(tickFont=label_font)
        self.plot_widget_training_x.getAxis(
            'bottom').setStyle(tickFont=label_font)
        # Memberikan label pada sumbu
        self.plot_widget_training_x.setLabel('left', text='FRAME')
        self.plot_widget_training_x.setLabel(
            'bottom', text='X - AXIS _ CORDINATES')
        # y
        self.plot_widget_training_y.setWindowTitle("ALL TRAINING DATA")
        label_font = QFont("Arial", 12, QFont.Bold)
        self.plot_widget_training_y.getAxis(
            'left').setStyle(tickFont=label_font)
        self.plot_widget_training_y.getAxis(
            'bottom').setStyle(tickFont=label_font)
        # Memberikan label pada sumbu
        self.plot_widget_training_y.setLabel('left', text='FRAME')
        self.plot_widget_training_y.setLabel(
            'bottom', text='Y - AXIS _ CORDINATES')
        # z
        self.plot_widget_training_z.setWindowTitle("ALL TRAINING DATA")
        label_font = QFont("Arial", 12, QFont.Bold)
        self.plot_widget_training_z.getAxis(
            'left').setStyle(tickFont=label_font)
        self.plot_widget_training_z.getAxis(
            'bottom').setStyle(tickFont=label_font)
        # Memberikan label pada sumbu
        self.plot_widget_training_z.setLabel('left', text='FRAME')
        self.plot_widget_training_z.setLabel(
            'bottom', text='Z - AXIS _ CORDINATES')
        # show training data button
        self.input_button_training = QPushButton("coba hitung variabel knn training")
        self.input_button_training.clicked.connect(self.hitungKNN)
        
        self.plot_input_training_data = QPushButton("Input Data Training")
        self.plot_input_training_data.clicked.connect(self.input_data_training)
        
        self.plot_button_training = QPushButton("Show Data Training")
        self.plot_button_training.clicked.connect(self.show_data_training)

        # Buat input teks testing data untuk nama, umur, dan tinggi badan
        self.name_input = QLineEdit()
        self.age_input = QLineEdit()
        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setWindowTitle("TESTING DATA")
        label_font2 = QFont("Arial", 12, QFont.Bold)
        self.plot_widget.getAxis('left').setStyle(tickFont=label_font2)
        self.plot_widget.getAxis('bottom').setStyle(tickFont=label_font2)
        # Memberikan label pada sumbu
        self.plot_widget.setLabel('left', text='FRAME')
        self.plot_widget.setLabel('bottom', text='X - AXIS _ CORDINATES')
        self.plot_button = QPushButton("Input Testing Data")
        self.plot_button.clicked.connect(self.plot_data)
        self.input_button_testing = QPushButton("coba hitung variabel knn testing")
        self.input_button_testing.clicked.connect(self.cobaInputKnnTesting3)

        namaTabel, cursor2 = self.databaseConnection()

        layout = QVBoxLayout()
        layout2 = QHBoxLayout()
        layout.addWidget(QLabel(f"Tabel yang ada di database : {namaTabel}"))
        # layout training
        layout.addWidget(QLabel("Nama:"))
        layout.addWidget(self.name_input_training)
        layout.addWidget(QLabel("Umur:"))
        layout.addWidget(self.age_input_training)
        layout.addWidget(QLabel("Tinggi Badan:"))
        layout.addWidget(self.height_input_training)
        layout.addWidget(QLabel("Berat Badan:"))
        layout.addWidget(self.weight_input_training)

        layout.addWidget(self.plot_widget_training_x)
        layout.addWidget(self.plot_widget_training_y)
        layout.addWidget(self.plot_widget_training_z)
        #coba KNN
        layout.addWidget(self.input_button_training)
        #input .c3d training
        layout.addWidget(self.plot_input_training_data)
        #show graphic
        layout.addWidget(self.plot_button_training)

        # layout testing
        layout.addWidget(QLabel("Nama:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Umur:"))
        layout.addWidget(self.age_input)
        layout.addWidget(QLabel("Tinggi Badan:"))
        layout.addWidget(self.height_input)
        layout.addWidget(QLabel("Berat Badan:"))
        layout.addWidget(self.weight_input)
        # layout.addWidget(import_button)
        layout.addWidget(self.input_button_testing)
        layout.addWidget(self.plot_button)
        layout.addWidget(self.plot_widget)

        # Buat widget utama dan atur layout utama
        main_widget = QWidget()
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        # Atur widget utama sebagai widget pusat dalam jendela utama

    def import_file(self):
        # Menggunakan dialog file untuk memilih file yang akan diimpor
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Pilih File")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_():
            # Mendapatkan path file yang dipilih
            file_path = file_dialog.selectedFiles()[0]
            print("File yang dipilih:", file_path)
        return file_path

    # input testing plot_data
    def plot_data(self):
        # panggil fungsi koneksi database

        # Mendapatkan nilai dari input teks
        name = self.name_input.text()
        age = self.age_input.text()
        height = self.height_input.text()
        weight = self.weight_input.text()

        path = self.import_file()
        # read c3d file
        with open(f'{path}', 'rb') as handle:
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

            # nama marker
            # markers_fix = [markers_list[0], markers_list[1], markers_list[38], markers_list[39], markers_list[40],
            #                markers_list[41], markers_list[42], markers_list[43], markers_list[44], markers_list[45],
            #                markers_list[46], markers_list[47], markers_list[48], markers_list[49], markers_list[50],
            #                markers_list[51]]
            pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                           'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
            markers_fix = []
            for marker in hilangkanSpasi:
                if marker in pilihMarker:
                    markers_fix.append(marker)
            print(markers_fix)

            # markers_fix2 = [LPSI,RPSI,RTOE,LHEE,LKNE,LTIB,RTIB,LANK,RTHI,LTHI,RANK,RKNE,RHEE,LTOE,RASI,LASI]
            # var = [X,Y,Z]

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
                            if marker == pilihMarker[0]:
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

                            elif marker == pilihMarker[1]:
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

                            elif marker == pilihMarker[2]:
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

                            elif marker == pilihMarker[3]:
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
                            elif marker == pilihMarker[4]:
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
                            elif marker == pilihMarker[5]:
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
                            elif marker == pilihMarker[6]:
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
                            elif marker == pilihMarker[7]:
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
                            elif marker == pilihMarker[8]:
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
                            elif marker == pilihMarker[9]:
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
                            elif marker == pilihMarker[10]:
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
                            elif marker == pilihMarker[11]:
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
                            elif marker == pilihMarker[12]:
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
                            elif marker == pilihMarker[13]:
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
                            elif marker == pilihMarker[14]:
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
                            elif marker == pilihMarker[15]:
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
                        else:
                            print(
                                f'Frame {i} Marker : {marker} Tidak ditunjukkan')
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
            # print(penguranganLPSIX)
            # print(hasilSkorLPSIX)
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
            # print(penguranganLPSIY)
            # print(hasilSkorLPSIY)
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
            # print(penguranganLPSIZ)
            # print(hasilSkorLPSIZ)
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
                        skorRPSIX = 1
                        hasilSkorRPSIX.append(skorRPSIX)
            except IndexError:
                skorRPSIX = 1
                penguranganRPSIX.append(0)
                hasilSkorRPSIX.append(skorRPSIX)
            # print(RPSIX)
            # print(penguranganRPSIX)
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
            # print(RPSIY)
            # print(penguranganRPSIY)
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
                        hasilSkorRPSIZ.append(skorRPSIZ)
            except IndexError:
                skorRPSIZ = 1
                penguranganRPSIZ.append(0)
                hasilSkorRPSIZ.append(skorRPSIZ)
            # print(RPSIZ)
            # print(penguranganRPSIZ)
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
            # print(RTOEX)
            # print(penguranganRTOEX)
            # print(hasilSkorRTOEX)

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
            # print(RTOEY)
            # print(penguranganRTOEY)
            # print(hasilSkorRTOEY)

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
            # print(RTOEZ)
            # print(penguranganRTOEZ)
            # print(hasilSkorRTOEZ)

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
            # print(LHEEX)
            # print(penguranganLHEEX)
            # print(hasilSkorLHEEX)

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
            # print(LHEEY)
            # print(penguranganLHEEY)
            # print(hasilSkorLHEEY)

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
            # print(LHEEZ)
            # print(penguranganLHEEZ)
            # print(hasilSkorLHEEZ)

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
            # print(LKNEX)
            # print(penguranganLKNEX)
            # print(hasilSkorLKNEX)

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
            # print(LKNEY)
            # print(penguranganLKNEY)
            # print(hasilSkorLKNEY)

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
            # print(LKNEZ)
            # print(penguranganLKNEZ)
            # print(hasilSkorLKNEZ)

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
            # print(LTIBX)
            # print(penguranganLTIBX)
            # print(hasilSkorLTIBX)

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
            # print(LTIBY)
            # print(penguranganLTIBY)
            # print(hasilSkorLTIBY)

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
            # print(LTIBZ)
            # print(penguranganLTIBZ)
            # print(hasilSkorLTIBZ)
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
            # print(RTIBX)
            # print(penguranganRTIBX)
            # print(hasilSkorRTIBX)

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
            # print(RTIBY)
            # print(penguranganRTIBY)
            # print(hasilSkorRTIBY)

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
            # print(RTIBZ)
            # print(penguranganRTIBZ)
            # print(hasilSkorRTIBZ)

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
            # print(LANKX)
            # print(penguranganLANKX)
            # print(hasilSkorLANKX)

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
            # print(LANKY)
            # print(penguranganLANKY)
            # print(hasilSkorLANKY)

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
            # print(LANKZ)
            # print(penguranganLANKZ)
            # print(hasilSkorLANKZ)

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
            # print(RTHIX)
            # print(penguranganRTHIX)
            # print(hasilSkorRTHIX)

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
            # print(RTHIY)
            # print(penguranganRTHIY)
            # print(hasilSkorRTHIY)

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
            # print(RTHIZ)
            # print(penguranganRTHIZ)
            # print(hasilSkorRTHIZ)

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
            # print(LTHIX)
            # print(penguranganLTHIX)
            # print(hasilSkorLTHIX)

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
            # print(LTHIY)
            # print(penguranganLTHIY)
            # print(hasilSkorLTHIY)

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
            # print(LTHIZ)
            # print(penguranganLTHIZ)
            # print(hasilSkorLTHIZ)

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
            # print(RANKX)
            # print(penguranganRANKX)
            # print(hasilSkorRANKX)

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
            # print(RANKY)
            # print(penguranganRANKY)
            # print(hasilSkorRANKY)

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
            # print(RANKZ)
            # print(penguranganRANKZ)
            # print(hasilSkorRANKZ)

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
            # print(RKNEX)
            # print(penguranganRKNEX)
            # print(hasilSkorRKNEX)

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
            # print(RKNEY)
            # print(penguranganRKNEY)
            # print(hasilSkorRKNEY)

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
            # print(RKNEZ)
            # print(penguranganRKNEZ)
            # print(hasilSkorRKNEZ)

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
            # print(RHEEX)
            # print(penguranganRHEEX)
            # print(hasilSkorRHEEX)

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
            # print(RHEEY)
            # print(penguranganRHEEY)
            # print(hasilSkorRHEEY)

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
            # print(RHEEZ)
            # print(penguranganRHEEZ)
            # print(hasilSkorRHEEZ)

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
            # print(LTOEX)
            # print(penguranganLTOEX)
            # print(hasilSkorLTOEX)

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
            # print(LTOEY)
            # print(penguranganLTOEY)
            # print(hasilSkorLTOEY)

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
            # print(LTOEZ)
            # print(penguranganLTOEZ)
            # print(hasilSkorLTOEZ)

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
            # print(RASIX)
            # print(penguranganRASIX)
            # print(hasilSkorRASIX)

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
            # print(RASIY)
            # print(penguranganRASIY)
            # print(hasilSkorRASIY)

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
            # print(RASIZ)
            # print(penguranganRASIZ)
            # print(hasilSkorRASIZ)

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
            # print(LASIX)
            # print(penguranganLASIX)
            # print(hasilSkorLASIX)

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
            # print(LASIY)
            # print(penguranganLASIY)
            # print(hasilSkorLASIY)

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

            # print(LASIZ)
            # print(penguranganLASIZ)
            # print(hasilSkorLASIZ)

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
            # print(df)
            result = pd.concat([df, df3, df2], axis=1)
            # print(result)
            # print(len(frame_data))
            # print(len(markers_fix * len(frame_no_list)))
            marker = markers_fix * len(frame_no_list)
            # print ke csv
            # wb = Workbook()
            # ws = wb.active
            # for r in dataframe_to_rows(result, index=False, header=True):
            #     ws.append(r)
            # wb.save('cobaSampaiScoring3Cara2.xlsx')

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlassotesting')
        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata','knndata2','knndata3','knndata4',]
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        # print(tables)
        # # nama pemilik marker
        namaPemilikData = name.strip()
        umur = age
        tinggiBadan = height
        beratBadan = weight
        namaPemilikData = namaPemilikData.lower()

        if namaPemilikData not in tables:
            print(f"tabel {namaPemilikData} belum ada")
            # tables.append(namaPemilikData)
            table_query = f"""
            CREATE TABLE IF NOT EXISTS {namaPemilikData} (
            id INTEGER PRIMARY KEY,
            Name VARCHAR(255),
            Age INTEGER,
            Height INTEGER,
            Weight INTEGER,
            Frame INTEGER,
            Marker VARCHAR(255),
            X_Cordinates DOUBLE,
            X_Scoring INTEGER,
            Y_Cordinates DOUBLE,
            Y_Scoring INTEGER,
            Z_Cordinates DOUBLE,
            Z_Scoring INTEGER
            )
            """
            cursor.execute(table_query)
            print('Berhasil membuat tabel baru')

            # ambil nilai data berdasarkan file .c3d yang terbaca
            for i in range(len(frame_data)):
                with connection.cursor() as cursor:
                    # Query SQL untuk memasukkan data
                    sql = f"INSERT INTO {namaPemilikData} (id,Name,Age,Height,Weight,Frame, Marker, X_Cordinates, X_Scoring, Y_Cordinates, Y_Scoring, Z_Cordinates, Z_Scoring) VALUES ({i},'{namaPemilikData}',{umur},{tinggiBadan},{beratBadan}, {frame_data[i]}, '{marker[i]}', {x_data[i]}, {gabungkanx_data[i]}, {y_data[i]}, {gabungkany_data[i]}, {z_data[i]}, {gabungkanz_data[i]})"
                    cursor.execute(sql)
                # Commit perubahan ke database
                connection.commit()
            print(f"Data {namaPemilikData} berhasil ditambahkan")
        else:
            for cekTabel in tables:
                if cekTabel in tables:
                    print(f"tabel {cekTabel} sudah ada")
                    if cekTabel == namaPemilikData:
                        for i in range(len(frame_data)):
                            with connection.cursor() as cursor:
                                sql = f"UPDATE {cekTabel} SET Name = '{namaPemilikData}', Age = {umur}, Height = {tinggiBadan}, Weight = {beratBadan},Frame = {frame_data[i]}, Marker = '{marker[i]}', X_Cordinates = {x_data[i]}, X_Scoring = {gabungkanx_data[i]}, Y_Cordinates = {y_data[i]}, Y_Scoring = {gabungkany_data[i]}, Z_Cordinates = {z_data[i]}, Z_Scoring = {gabungkanz_data[i]} WHERE id = {i}"
                                cursor.execute(sql)
                            connection.commit()
                        print(f"Data {cekTabel} berhasil diupdate")
                else:
                    print(f"tabel {cekTabel} belum ada")
        print('')
        # print('')
        # print('')
        # print(frame_data)
        self.plot_widget.plot(frame_no_list, LPSIX,
                              pen='g', symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RPSIX,
                              pen='g', symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RTOEX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, LHEEX,
                              pen=None, symbol='o', symbolSize=10)

        self.plot_widget.plot(frame_no_list, LKNEX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, LTIBX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RTIBX,
                              pen=None, symbol='o', symbolSize=10)

        self.plot_widget.plot(frame_no_list, LANKX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RTHIX,
                              pen=None, symbol='o', symbolSize=10)

        self.plot_widget.plot(frame_no_list, LTHIX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RANKX,
                              pen=None, symbol='o', symbolSize=10)

        self.plot_widget.plot(frame_no_list, RKNEX,
                              pen=None, symbol='x', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RHEEX,
                              pen=None, symbol='o', symbolSize=10)

        self.plot_widget.plot(frame_no_list, LTOEX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, RASIX,
                              pen=None, symbol='o', symbolSize=10)
        self.plot_widget.plot(frame_no_list, LASIX,
                              pen=None, symbol='o', symbolSize=10)

        # Lakukan plot data sesuai dengan kebutuhan Anda

    # input training plot_data

    def input_data_training(self):
        # panggil fungsi koneksi database

        # Mendapatkan nilai dari input teks
        name = self.name_input_training.text()
        age = self.age_input_training.text()
        height = self.height_input_training.text()
        weight = self.weight_input_training.text()

        path = self.import_file()
        # read c3d file
        averages = {}
        with open(f'{path}', 'rb') as handle:
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

            # nama marker
            # markers_fix = [markers_list[0], markers_list[1], markers_list[38], markers_list[39], markers_list[40],
            #                markers_list[41], markers_list[42], markers_list[43], markers_list[44], markers_list[45],
            #                markers_list[46], markers_list[47], markers_list[48], markers_list[49], markers_list[50],
            #                markers_list[51]]
            pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                           'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
            markers_fix = []
            for marker in hilangkanSpasi:
                if marker in pilihMarker:
                    markers_fix.append(marker)
            print(markers_fix)

            # markers_fix2 = [LPSI,RPSI,RTOE,LHEE,LKNE,LTIB,RTIB,LANK,RTHI,LTHI,RANK,RKNE,RHEE,LTOE,RASI,LASI]
            # var = [X,Y,Z]

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
                            if marker == pilihMarker[0]:
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

                            elif marker == pilihMarker[1]:
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

                            elif marker == pilihMarker[2]:
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

                            elif marker == pilihMarker[3]:
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
                            elif marker == pilihMarker[4]:
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
                            elif marker == pilihMarker[5]:
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
                            elif marker == pilihMarker[6]:
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
                            elif marker == pilihMarker[7]:
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
                            elif marker == pilihMarker[8]:
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
                            elif marker == pilihMarker[9]:
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
                            elif marker == pilihMarker[10]:
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
                            elif marker == pilihMarker[11]:
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
                            elif marker == pilihMarker[12]:
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
                            elif marker == pilihMarker[13]:
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
                            elif marker == pilihMarker[14]:
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
                            elif marker == pilihMarker[15]:
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
                        else:
                            print(
                                f'Frame {i} Marker : {marker} Tidak ditunjukkan')
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
            # print(penguranganLPSIX)
            # print(hasilSkorLPSIX)
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
            # print(penguranganLPSIY)
            # print(hasilSkorLPSIY)
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
            # print(penguranganLPSIZ)
            # print(hasilSkorLPSIZ)
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
            # print(RPSIX)
            # print(penguranganRPSIX)
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
            # print(RPSIY)
            # print(penguranganRPSIY)
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
                        hasilSkorRPSIZ.append(skorRPSIZ)
            except IndexError:
                skorRPSIZ = 1
                penguranganRPSIZ.append(0)
                hasilSkorRPSIZ.append(skorRPSIZ)
            # print(RPSIZ)
            # print(penguranganRPSIZ)
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
            # print(RTOEX)
            # print(penguranganRTOEX)
            # print(hasilSkorRTOEX)

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
            # print(RTOEY)
            # print(penguranganRTOEY)
            # print(hasilSkorRTOEY)

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
            # print(RTOEZ)
            # print(penguranganRTOEZ)
            # print(hasilSkorRTOEZ)

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
            # print(LHEEX)
            # print(penguranganLHEEX)
            # print(hasilSkorLHEEX)

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
            # print(LHEEY)
            # print(penguranganLHEEY)
            # print(hasilSkorLHEEY)

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
            # print(LHEEZ)
            # print(penguranganLHEEZ)
            # print(hasilSkorLHEEZ)

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
            # print(LKNEX)
            # print(penguranganLKNEX)
            # print(hasilSkorLKNEX)

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
            # print(LKNEY)
            # print(penguranganLKNEY)
            # print(hasilSkorLKNEY)

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
            # print(LKNEZ)
            # print(penguranganLKNEZ)
            # print(hasilSkorLKNEZ)

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
            # print(LTIBX)
            # print(penguranganLTIBX)
            # print(hasilSkorLTIBX)

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
            # print(LTIBY)
            # print(penguranganLTIBY)
            # print(hasilSkorLTIBY)

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
            # print(LTIBZ)
            # print(penguranganLTIBZ)
            # print(hasilSkorLTIBZ)
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
            # print(RTIBX)
            # print(penguranganRTIBX)
            # print(hasilSkorRTIBX)

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
            # print(RTIBY)
            # print(penguranganRTIBY)
            # print(hasilSkorRTIBY)

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
            # print(RTIBZ)
            # print(penguranganRTIBZ)
            # print(hasilSkorRTIBZ)

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
            # print(LANKX)
            # print(penguranganLANKX)
            # print(hasilSkorLANKX)

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
            # print(LANKY)
            # print(penguranganLANKY)
            # print(hasilSkorLANKY)

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
            # print(LANKZ)
            # print(penguranganLANKZ)
            # print(hasilSkorLANKZ)

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
            # print(RTHIX)
            # print(penguranganRTHIX)
            # print(hasilSkorRTHIX)

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
            # print(RTHIY)
            # print(penguranganRTHIY)
            # print(hasilSkorRTHIY)

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
            # print(RTHIZ)
            # print(penguranganRTHIZ)
            # print(hasilSkorRTHIZ)

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
            # print(LTHIX)
            # print(penguranganLTHIX)
            # print(hasilSkorLTHIX)

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
            # print(LTHIY)
            # print(penguranganLTHIY)
            # print(hasilSkorLTHIY)

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
            # print(LTHIZ)
            # print(penguranganLTHIZ)
            # print(hasilSkorLTHIZ)

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
            # print(RANKX)
            # print(penguranganRANKX)
            # print(hasilSkorRANKX)

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
            # print(RANKY)
            # print(penguranganRANKY)
            # print(hasilSkorRANKY)

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
            # print(RANKZ)
            # print(penguranganRANKZ)
            # print(hasilSkorRANKZ)

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
            # print(RKNEX)
            # print(penguranganRKNEX)
            # print(hasilSkorRKNEX)

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
            # print(RKNEY)
            # print(penguranganRKNEY)
            # print(hasilSkorRKNEY)

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
            # print(RKNEZ)
            # print(penguranganRKNEZ)
            # print(hasilSkorRKNEZ)

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
            # print(RHEEX)
            # print(penguranganRHEEX)
            # print(hasilSkorRHEEX)

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
            # print(RHEEY)
            # print(penguranganRHEEY)
            # print(hasilSkorRHEEY)

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
            # print(RHEEZ)
            # print(penguranganRHEEZ)
            # print(hasilSkorRHEEZ)

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
            # print(LTOEX)
            # print(penguranganLTOEX)
            # print(hasilSkorLTOEX)

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
            # print(LTOEY)
            # print(penguranganLTOEY)
            # print(hasilSkorLTOEY)

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
            # print(LTOEZ)
            # print(penguranganLTOEZ)
            # print(hasilSkorLTOEZ)

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
            # print(RASIX)
            # print(penguranganRASIX)
            # print(hasilSkorRASIX)

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
            # print(RASIY)
            # print(penguranganRASIY)
            # print(hasilSkorRASIY)

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
            # print(RASIZ)
            # print(penguranganRASIZ)
            # print(hasilSkorRASIZ)

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
            # print(LASIX)
            # print(penguranganLASIX)
            # print(hasilSkorLASIX)

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
            # print(LASIY)
            # print(penguranganLASIY)
            # print(hasilSkorLASIY)

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

            # print(LASIZ)
            # print(penguranganLASIZ)
            # print(hasilSkorLASIZ)

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
            # print(df)
            result = pd.concat([df, df3, df2], axis=1)
            # print(result)
            # print(len(frame_data))
            # print(len(markers_fix * len(frame_no_list)))
            marker = markers_fix * len(frame_no_list)
            # print ke csv
            # wb = Workbook()
            # ws = wb.active
            # for r in dataframe_to_rows(result, index=False, header=True):
            #     ws.append(r)
            # wb.save('cobaSampaiScoring3Cara2.xlsx')

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlasso')
        cursor = connection.cursor()

        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata4','knntrainingdata']
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        # print(tables)
        # # nama pemilik marker
        
        namaPemilikData = name.strip()
        umur = age
        tinggiBadan = height
        beratBadan = weight
        namaPemilikData = namaPemilikData.lower()
        
        if namaPemilikData not in tables:
            print(f"tabel {namaPemilikData} belum ada")
            # tables.append(namaPemilikData)
            table_query = f"""
            CREATE TABLE IF NOT EXISTS {namaPemilikData} (
            id INTEGER PRIMARY KEY,
            Name VARCHAR(255),
            Age INTEGER,
            Height INTEGER,
            Weight INTEGER,
            Frame INTEGER,
            Marker VARCHAR(255),
            X_Cordinates DOUBLE,
            X_Scoring INTEGER,
            Y_Cordinates DOUBLE,
            Y_Scoring INTEGER,
            Z_Cordinates DOUBLE,
            Z_Scoring INTEGER
            )
            """
            cursor.execute(table_query)
            print('Berhasil membuat tabel baru')

            # ambil nilai data berdasarkan file .c3d yang terbaca
            for i in range(len(frame_data)):
                with connection.cursor() as cursor:
                    # Query SQL untuk memasukkan data
                    sql = f"INSERT INTO {namaPemilikData} (id,Name,Age,Height,Weight,Frame, Marker, X_Cordinates, X_Scoring, Y_Cordinates, Y_Scoring, Z_Cordinates, Z_Scoring) VALUES ({i},'{namaPemilikData}',{umur},{tinggiBadan},{beratBadan}, {frame_data[i]}, '{marker[i]}', {x_data[i]}, {gabungkanx_data[i]}, {y_data[i]}, {gabungkany_data[i]}, {z_data[i]}, {gabungkanz_data[i]})"
                    cursor.execute(sql)
                # Commit perubahan ke database
                connection.commit()
            print(f"Data {namaPemilikData} berhasil ditambahkan")

        else:
            for cekTabel in tables:
                if cekTabel in tables:
                    print(f"tabel {cekTabel} sudah ada")
                    if cekTabel == namaPemilikData:
                        delete_sql = f"DELETE FROM {namaPemilikData}"
                        cursor.execute(delete_sql)
                        for i in range(len(frame_data)):
                            with connection.cursor() as cursor:
                                # sql = f"UPDATE {cekTabel} SET Name = '{namaPemilikData}', Age = {umur}, Height = {tinggiBadan}, Weight = {beratBadan},Frame = {frame_data[i]}, Marker = '{marker[i]}', X_Cordinates = {x_data[i]}, X_Scoring = {gabungkanx_data[i]}, Y_Cordinates = {y_data[i]}, Y_Scoring = {gabungkany_data[i]}, Z_Cordinates = {z_data[i]}, Z_Scoring = {gabungkanz_data[i]} WHERE id = {i}"
                                sql = f"INSERT INTO {namaPemilikData} (id,Name,Age,Height,Weight,Frame, Marker, X_Cordinates, X_Scoring, Y_Cordinates, Y_Scoring, Z_Cordinates, Z_Scoring) VALUES ({i},'{namaPemilikData}',{umur},{tinggiBadan},{beratBadan}, {frame_data[i]}, '{marker[i]}', {x_data[i]}, {gabungkanx_data[i]}, {y_data[i]}, {gabungkany_data[i]}, {z_data[i]}, {gabungkanz_data[i]})"
                                cursor.execute(sql)
                            connection.commit()
                        print(f"Data {cekTabel} berhasil diupdate")
                else:
                    print(f"tabel {cekTabel} belum ada")
        
        # self.plot_widget.plot(frame_no_list, LPSIX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RPSIX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RTOEX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, LHEEX,
        #                       pen='g', symbol='o', symbolSize=10)

        # self.plot_widget.plot(frame_no_list, LKNEX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, LTIBX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RTIBX,
        #                       pen='g', symbol='o', symbolSize=10)

        # self.plot_widget.plot(frame_no_list, LANKX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RTHIX,
        #                       pen='g', symbol='o', symbolSize=10)

        # self.plot_widget.plot(frame_no_list, LTHIX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RANKX,
        #                       pen='g', symbol='o', symbolSize=10)

        # self.plot_widget.plot(frame_no_list, RKNEX,
        #                       pen='g', symbol='x', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RHEEX,
        #                       pen='g', symbol='o', symbolSize=10)

        # self.plot_widget.plot(frame_no_list, LTOEX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, RASIX,
        #                       pen='g', symbol='o', symbolSize=10)
        # self.plot_widget.plot(frame_no_list, LASIX,
        #                       pen='g', symbol='o', symbolSize=10)

        # Lakukan plot data sesuai dengan kebutuhan Anda
        
    # show training plot_data
    def show_data_training(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlasso')
        
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata4','knntrainingdata']
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        
        connection2 = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='trainingknnvariables')
        cursor2 = connection2.cursor()
        cursor2.execute("SHOW TABLES")
        tables2 = [table2[0] for table2 in cursor2.fetchall()]
        
        pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                       'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
        LPSIX, RPSIX, RTOEX, LHEEX, LKNEX, LTIBX, RTIBX, LANKX, RTHIX, LTHIX, RANKX, RKNEX, RHEEX, LTOEX, RASIX, LASIX = [
        ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
        LPSIY, RPSIY, RTOEY, LHEEY, LKNEY, LTIBY, RTIBY, LANKY, RTHIY, LTHIY, RANKY, RKNEY, RHEEY, LTOEY, RASIY, LASIY = [
        ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
        LPSIZ, RPSIZ, RTOEZ, LHEEZ, LKNEZ, LTIBZ, RTIBZ, LANKZ, RTHIZ, LTHIZ, RANKZ, RKNEZ, RHEEZ, LTOEZ, RASIZ, LASIZ = [
        ], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
        
        penjumlahanLPSI = []
        penjumlahanRPSI = []
        penjumlahanRTOE = []
        penjumlahanLHEE = []
        penjumlahanLKNE = []
        penjumlahanLTIB = []
        penjumlahanRTIB = []
        penjumlahanLANK = []
        penjumlahanRTHI = []
        penjumlahanLTHI = []
        penjumlahanRANK = []
        penjumlahanRKNE = []
        penjumlahanRHEE = []
        penjumlahanLTOE = []
        penjumlahanRASI = []
        penjumlahanLASI = []
        
        frame_no_list = []

        all_marker_x = []
        
        all_marker_y = []
        
        all_marker_z = []

        self.plot_widget_training_x.clear()
        self.plot_widget_training_y.clear()
        self.plot_widget_training_z.clear()

        # tables=['orang1,orang2']
        for cekTabel in tables:
            print(cekTabel)
            namaOrang = [cekTabel]
            # namaOrang.append(cekTabel)
            with connection.cursor() as cursor:
                for i in range(len(pilihMarker)):
                    sql = f"SELECT {cekTabel}.Frame,{cekTabel}.Name,{cekTabel}.Age,{cekTabel}.Height,{cekTabel}.Weight,{cekTabel}.Marker, {cekTabel}.X_Cordinates, {cekTabel}.X_Scoring, {cekTabel}.Y_Cordinates, {cekTabel}.Y_Scoring, {cekTabel}.Z_Cordinates, {cekTabel}.Z_Scoring FROM {cekTabel} where {cekTabel}.Marker = '{pilihMarker[i]}'"
                    # sql = f"SELECT {cekTabel}.Marker, {cekTabel}.X_Cordinates, {cekTabel}.X_Scoring, {cekTabel}.Y_Cordinates, {cekTabel}.Y_Scoring, {cekTabel}.Z_Cordinates, {cekTabel}.Z_Scoring FROM {cekTabel} where {cekTabel}.Marker = '{pilihMarker[i]}'"
                    cursor.execute(sql)
                    result = cursor.fetchall()
                    for row in result:
                        with connection2.cursor() as cursor2:
                            frame = row[0]
                            frame_no_list.append(frame)
                            name = row[1]
                            age = row[2]
                            height = row[3]
                            weight = row[4]
                            for z in range(len(namaOrang)):
                                if name == namaOrang[z]:
                                    marker = row[5]
                                    if marker == pilihMarker[0]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LPSIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LPSIY.append(x_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LPSIZ.append(x_scoring)
                                          
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)
                                        
                                    elif marker == pilihMarker[1]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RPSIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RPSIY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RPSIZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[2]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RTOEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RTOEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RTOEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[3]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LHEEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LHEEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LHEEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    # Lanjutkan untuk setiap elemen dalam pilihMarker

                                    elif marker == pilihMarker[4]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LKNEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LKNEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LKNEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[5]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LTIBX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LTIBY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LTIBZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)
                                    elif marker == pilihMarker[6]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RTIBX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RTIBY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RTIBZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[7]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LANKX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LANKY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LANKZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[8]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RTHIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RTHIY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RTHIZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[9]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LTHIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LTHIY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LTHIZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[10]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RANKX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RANKY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RANKZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[11]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RKNEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RKNEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RKNEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)
                                    elif marker == pilihMarker[12]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RHEEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RHEEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RHEEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[13]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LTOEX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LTOEY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LTOEZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[14]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        RASIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        RASIY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        RASIZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)

                                    elif marker == pilihMarker[15]:
                                        x = row[6]
                                        all_marker_x.append(x)
                                        x_scoring = row[7]
                                        LASIX.append(x_scoring)
                                        y = row[8]
                                        all_marker_y.append(y)
                                        y_scoring = row[9]
                                        LASIY.append(y_scoring)
                                        z = row[10]
                                        all_marker_z.append(z)
                                        z_scoring = row[11]
                                        LASIZ.append(z_scoring)
                                        # print(frame, name,age,height,weight, marker, x, x_scoring,y, y_scoring,z, z_scoring)
                            
                            # sql2 = f"INSERT INTO knndata (Name,Age,Height,Weight,LPSI) VALUES {tables[1],age,height,weight,sum(LPSIX+LPSIY+LPSIZ)/3}"
                            # cursor2.execute(sql2)
                            # connection2.commit()        
            # berikan warna yang berbeda setiap orang            

            self.plot_widget_training_x.plot(all_marker_x,frame_no_list,pen=None, symbol='x', symbolSize=15,symbolBrush='r')
            self.plot_widget_training_y.plot(all_marker_y,frame_no_list,pen=None, symbol='o', symbolSize=15,symbolBrush='y')
            self.plot_widget_training_z.plot(all_marker_z,frame_no_list,pen=None, symbol='o', symbolSize=15,symbolBrush='b')
            

    # def cobaInputKnn(self) :

    #     connection = pymysql.connect(host='localhost',
    #                                  user='root',
    #                                  password='Iamironman123',
    #                                  db='riyanlasso')
        
    #     cursor = connection.cursor()
    #     cursor.execute("SHOW TABLES")
    #     tables_to_exclude = ['knndata4']
    #     tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]

    #     connection2 = pymysql.connect(host='localhost',
    #                                  user='root',
    #                                  password='Iamironman123',
    #                                  db='riyanlasso2')
        
    #     cursor2 = connection2.cursor()
    #     cursor2.execute("SHOW TABLES")
    #     table2 = [table2[0] for table2 in cursor2.fetchall()]
             
    #     pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
    #                    'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
    #     averages = {}

    #     for cekTabel in range(len(tables)):
    #         for i in range(len(pilihMarker)):
    #             nama = tables[cekTabel]
    #             marker = pilihMarker[i]

    #             sql = f"SELECT {tables[cekTabel]}.Frame, {tables[cekTabel]}.Name, {tables[cekTabel]}.Age, {tables[cekTabel]}.Height, {tables[cekTabel]}.Weight, {tables[cekTabel]}.Marker, {tables[cekTabel]}.X_Cordinates, {tables[cekTabel]}.X_Scoring, {tables[cekTabel]}.Y_Cordinates, {tables[cekTabel]}.Y_Scoring, {tables[cekTabel]}.Z_Cordinates, {tables[cekTabel]}.Z_Scoring FROM {tables[cekTabel]} WHERE {tables[cekTabel]}.Name = '{nama}' AND {tables[cekTabel]}.Marker = '{marker}'"
    #             cursor.execute(sql)
    #             result = cursor.fetchall()
             
    #             for row in result:
    #                 age = row[2]
    #                 height = row[3]
    #                 weight = row[4]
    #                 x_scoring = row[7]
    #                 y_scoring = row[9]
    #                 z_scoring = row[11]

    #                 key = (nama, marker)
                    
    #                 # print(key)
    #                 if key in averages:
    #                     averages[key][0].append(age)
    #                     averages[key][1].append(height)
    #                     averages[key][2].append(weight)
    #                     averages[key][3].append(x_scoring)
    #                     averages[key][4].append(y_scoring)
    #                     averages[key][5].append(z_scoring)
    #                 else:
    #                     averages[key] = [[age], [height], [weight], [x_scoring], [y_scoring], [z_scoring]]
            
    #         # print(tables[cekTabel],averages[key])
    #     # # Memasukkan hasil perhitungan ke dalam database
        
    #     for key, values in averages.items():
    #         nama, marker = key
    #         age_values = values[0]
    #         height_values = values[1]
    #         weight_values = values[2]
    #         x_scores = values[3]
    #         y_scores = values[4]
    #         z_scores = values[5]

    #         average_age = sum(age_values) / len(age_values)
    #         average_height = sum(height_values) / len(height_values)
    #         average_weight = sum(weight_values) / len(weight_values)
    #         average_x = sum(x_scores) / len(x_scores)
    #         average_y = sum(y_scores) / len(y_scores)
    #         average_z = sum(z_scores) / len(z_scores)

    #         insert_sql = f"INSERT INTO knndata2 (Name, Marker, Average_Age, Average_Height, Average_Weight, Average_X_Scoring, Average_Y_Scoring, Average_Z_Scoring) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {average_x}, {average_y}, {average_z})"
    #         cursor2.execute(insert_sql)
    #         connection2.commit()
            
    #     connection2.commit()
                
    # def cobaInputKnn2(self) :

    #     connection = pymysql.connect(host='localhost',
    #                                  user='root',
    #                                  password='Iamironman123',
    #                                  db='riyanlasso')
        
    #     cursor = connection.cursor()
    #     cursor.execute("SHOW TABLES")
    #     tables_to_exclude = ['knndata4']
    #     tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]

    #     connection2 = pymysql.connect(host='localhost',
    #                                  user='root',
    #                                  password='Iamironman123',
    #                                  db='riyanlasso2')
        
    #     cursor2 = connection2.cursor()
    #     cursor2.execute("SHOW TABLES")
    #     tables2 = [tables2[0] for tables2 in cursor2.fetchall()]
        
        

            
        
    #     # print(table2)     
    #     pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
    #                    'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
    #     averages = {}

    #     for cekTabel in range(len(tables)):
            
    #         if tables[cekTabel] not in tables2:
    #             # print(f'{tables[cekTabel]} tidak ada di database 2')
    #             create_sql1 = f"CREATE TABLE {tables[cekTabel]} ( `Name` varchar(255) DEFAULT NULL, `Marker` varchar(255) DEFAULT NULL, `Average_Age` int DEFAULT NULL, `Average_Height` int DEFAULT NULL, `Average_Weight` int DEFAULT NULL, `AverageMarker` double DEFAULT NULL )"
    #             cursor2.execute(create_sql1)
    #             connection2.commit()
    #             # print(f"berhasil membuat tabel {tables[cekTabel]}")
            
    #         for i in range(len(pilihMarker)):
    #             nama = tables[cekTabel]
    #             marker = pilihMarker[i]
                
    #             sql = f"SELECT {tables[cekTabel]}.Frame, {tables[cekTabel]}.Name, {tables[cekTabel]}.Age, {tables[cekTabel]}.Height, {tables[cekTabel]}.Weight, {tables[cekTabel]}.Marker, {tables[cekTabel]}.X_Cordinates, {tables[cekTabel]}.X_Scoring, {tables[cekTabel]}.Y_Cordinates, {tables[cekTabel]}.Y_Scoring, {tables[cekTabel]}.Z_Cordinates, {tables[cekTabel]}.Z_Scoring FROM {tables[cekTabel]} WHERE {tables[cekTabel]}.Name = '{nama}' AND {tables[cekTabel]}.Marker = '{marker}'"
    #             cursor.execute(sql)
    #             result = cursor.fetchall()
             
    #             for row in result:
    #                 age = row[2]
    #                 height = row[3]
    #                 weight = row[4]
    #                 x_scoring = row[7]
    #                 y_scoring = row[9]
    #                 z_scoring = row[11]

    #                 key = (nama, marker)
                    
    #                 # print(key)
    #                 if key in averages:
    #                     averages[key][0].append(age)
    #                     averages[key][1].append(height)
    #                     averages[key][2].append(weight)
    #                     averages[key][3].append(x_scoring)
    #                     averages[key][4].append(y_scoring)
    #                     averages[key][5].append(z_scoring)
    #                 else:
    #                     averages[key] = [[age], [height], [weight], [x_scoring], [y_scoring], [z_scoring]]
            
    #         # print(tables[cekTabel],averages[key])
    #     # # Memasukkan hasil perhitungan ke dalam database
        
    #     for key, values in averages.items():
            
    #         nama, marker = key
    #         age_values = values[0]
    #         height_values = values[1]
    #         weight_values = values[2]
    #         x_scores = values[3]
    #         y_scores = values[4]
    #         z_scores = values[5]

    #         average_age = sum(age_values) / len(age_values)
    #         average_height = sum(height_values) / len(height_values)
    #         average_weight = sum(weight_values) / len(weight_values)
    #         average_x = sum(x_scores) / len(x_scores)
    #         average_y = sum(y_scores) / len(y_scores)
    #         average_z = sum(z_scores) / len(z_scores)
    #         averageTotal = average_x + average_y + average_z
            
            
    #         # insert_sql = f"INSERT INTO {nama} (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
    #         # cursor2.execute(insert_sql)
    #         # connection2.commit()
    #         # print('data sudah masuk database2')
            
            
    #         # sql = f"UPDATE {nama} SET Name = '{nama}', Marker = '{marker}', Average_Age = {average_age}, Average_Height = {average_height}, Average_Weight = {average_weight}, AverageMarker = {averageTotal} WHERE"
            
    #         # if nama in tables:
    #         #     print(f'{nama} ada di database 1')
    #         #     if nama in table2:
    #         #         print(f'{nama} ada di database 2')
    #         #         cursor2.execute(f"SELECT COUNT(*) FROM {nama}")
    #         #         result = cursor2.fetchone()
    #         #         if result[0] > 0:
    #         #             print("Tabel berisi data.")
    #         #             sql_update = f"UPDATE {nama} SET Name='{nama}', Average_Age={average_age}, Average_Height={average_height}, Average_Weight={average_weight}, AverageMarker={averageTotal} WHERE Name='{nama}'"
    #         #             cursor2.execute(sql_update)
    #         #             connection2.commit()
    #         #             print(f"Tabel {nama} sudah ada. Data untuk Marker: {marker} telah diperbarui.")
    #         #         else:
    #         #             print("Tabel kosong.")
    #         #             insert_sql = f"INSERT INTO {nama} (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
    #         #             cursor2.execute(insert_sql)
    #         #             connection2.commit()
    #         #     else:
    #         #         print(f'{nama} tidak ada di database 2')
    #         #         create_sql1 = f"CREATE TABLE {nama} ( `Name` varchar(255) DEFAULT NULL, `Marker` varchar(255) DEFAULT NULL, `Average_Age` int DEFAULT NULL, `Average_Height` int DEFAULT NULL, `Average_Weight` int DEFAULT NULL, `AverageMarker` double DEFAULT NULL )"
    #         #         cursor2.execute(create_sql1)
    #         #         connection2.commit()
    #         # else:
    #         #     print(f'{nama} tidak ada di database 1')
        
    def cobaInputKnnTraining3(self) :

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlasso')
        
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata4','knntrainingdata']
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        
        connection2 = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='trainingknnvariables')
        
        cursor2 = connection2.cursor()
        cursor2.execute("SHOW TABLES")
        tables_to_exclude2 = ['trainingknnvariables','fusiontrainingknnvariables']
        tables2 = [tables2[0] for tables2 in cursor2.fetchall()if tables2[0] not in tables_to_exclude2]
            
        # print(table2)     
        pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                       'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
        averages = {}

        for cekTabel in range(len(tables)):
            
            if tables[cekTabel] not in tables2:
                # print(f'{tables[cekTabel]} tidak ada di database 2')
                create_sql1 = f"CREATE TABLE {tables[cekTabel]} ( `Name` varchar(255) DEFAULT NULL, `Marker` varchar(255) DEFAULT NULL, `Average_Age` int DEFAULT NULL, `Average_Height` int DEFAULT NULL, `Average_Weight` int DEFAULT NULL, `AverageMarker` double DEFAULT NULL )"
                cursor2.execute(create_sql1)
                connection2.commit()
                # print(f"berhasil membuat tabel {tables[cekTabel]}")
            
            for i in range(len(pilihMarker)):
                nama = tables[cekTabel]
                marker = pilihMarker[i]
                
                sql = f"SELECT {tables[cekTabel]}.Frame, {tables[cekTabel]}.Name, {tables[cekTabel]}.Age, {tables[cekTabel]}.Height, {tables[cekTabel]}.Weight, {tables[cekTabel]}.Marker, {tables[cekTabel]}.X_Cordinates, {tables[cekTabel]}.X_Scoring, {tables[cekTabel]}.Y_Cordinates, {tables[cekTabel]}.Y_Scoring, {tables[cekTabel]}.Z_Cordinates, {tables[cekTabel]}.Z_Scoring FROM {tables[cekTabel]} WHERE {tables[cekTabel]}.Name = '{nama}' AND {tables[cekTabel]}.Marker = '{marker}'"
                cursor.execute(sql)
                result = cursor.fetchall()
             
                for row in result:
                    age = row[2]
                    height = row[3]
                    weight = row[4]
                    x_scoring = row[7]
                    y_scoring = row[9]
                    z_scoring = row[11]

                    key = (nama, marker)
                    
                    # print(key)
                    if key in averages:
                        averages[key][0].append(age)
                        averages[key][1].append(height)
                        averages[key][2].append(weight)
                        averages[key][3].append(x_scoring)
                        averages[key][4].append(y_scoring)
                        averages[key][5].append(z_scoring)
                    else:
                        averages[key] = [[age], [height], [weight], [x_scoring], [y_scoring], [z_scoring]]
            delete_sql = f"DELETE FROM {nama}"
            cursor2.execute(delete_sql)
            delete_sql2 = f"DELETE FROM trainingknnvariables"
            cursor2.execute(delete_sql2)
            print(nama)
            # print(tables[cekTabel],averages[key])
        # # Memasukkan hasil perhitungan ke dalam database
        for key, values in averages.items():
            
            nama, marker = key
            age_values = values[0]
            height_values = values[1]
            weight_values = values[2]
            x_scores = values[3]
            print(x_scores)
            y_scores = values[4]
            z_scores = values[5]

            average_age = sum(age_values) / len(age_values)
            average_height = sum(height_values) / len(height_values)
            average_weight = sum(weight_values) / len(weight_values)
            # average_x = sum(x_scores) / len(x_scores)
            # average_y = sum(y_scores) / len(y_scores)
            # average_z = sum(z_scores) / len(z_scores)
            average_x = sum(x_scores) / 3
            average_y = sum(y_scores) / 3
            average_z = sum(z_scores) / 3
            averageTotal = average_x + average_y + average_z
            
            insert_sql = f"INSERT INTO {nama} (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
            cursor2.execute(insert_sql)
            insert_sql2 = f"INSERT INTO trainingknnvariables (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
            cursor2.execute(insert_sql2)
            connection2.commit()
            print(f'data {key} sudah masuk database trainingknnvariables')

        #jadikan marker sebagai row bukan column
    def cobaInputKnnTesting3(self) :

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='riyanlassotesting')
        
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['knndata4','knntrainingdata']
        tables = [table[0] for table in cursor.fetchall() if table[0] not in tables_to_exclude]
        
        connection2 = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='testingknnvariables')
        
        cursor2 = connection2.cursor()
        cursor2.execute("SHOW TABLES")
        tables_to_exclude2 = ['testingknnvariables']
        tables2 = [tables2[0] for tables2 in cursor2.fetchall()if tables2[0] not in tables_to_exclude2]
            
        # print(table2)     
        pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                       'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
        averages = {}

        for cekTabel in range(len(tables)):
            
            if tables[cekTabel] not in tables2:
                # print(f'{tables[cekTabel]} tidak ada di database 2')
                create_sql1 = f"CREATE TABLE {tables[cekTabel]} ( `Name` varchar(255) DEFAULT NULL, `Marker` varchar(255) DEFAULT NULL, `Average_Age` int DEFAULT NULL, `Average_Height` int DEFAULT NULL, `Average_Weight` int DEFAULT NULL, `AverageMarker` double DEFAULT NULL )"
                cursor2.execute(create_sql1)
                connection2.commit()
                # print(f"berhasil membuat tabel {tables[cekTabel]}")
            
            for i in range(len(pilihMarker)):
                nama = tables[cekTabel]
                marker = pilihMarker[i]
                
                sql = f"SELECT {tables[cekTabel]}.Frame, {tables[cekTabel]}.Name, {tables[cekTabel]}.Age, {tables[cekTabel]}.Height, {tables[cekTabel]}.Weight, {tables[cekTabel]}.Marker, {tables[cekTabel]}.X_Cordinates, {tables[cekTabel]}.X_Scoring, {tables[cekTabel]}.Y_Cordinates, {tables[cekTabel]}.Y_Scoring, {tables[cekTabel]}.Z_Cordinates, {tables[cekTabel]}.Z_Scoring FROM {tables[cekTabel]} WHERE {tables[cekTabel]}.Name = '{nama}' AND {tables[cekTabel]}.Marker = '{marker}'"
                cursor.execute(sql)
                result = cursor.fetchall()
             
                for row in result:
                    age = row[2]
                    height = row[3]
                    weight = row[4]
                    x_scoring = row[7]
                    y_scoring = row[9]
                    z_scoring = row[11]

                    key = (nama, marker)
                    
                    # print(key)
                    if key in averages:
                        averages[key][0].append(age)
                        averages[key][1].append(height)
                        averages[key][2].append(weight)
                        averages[key][3].append(x_scoring)
                        averages[key][4].append(y_scoring)
                        averages[key][5].append(z_scoring)
                    else:
                        averages[key] = [[age], [height], [weight], [x_scoring], [y_scoring], [z_scoring]]
            delete_sql = f"DELETE FROM {nama}"
            cursor2.execute(delete_sql)
            delete_sql2 = f"DELETE FROM testingknnvariables"
            cursor2.execute(delete_sql2)
            print(nama)
            # print(tables[cekTabel],averages[key])
        # Memasukkan hasil perhitungan ke dalam database
        for key, values in averages.items():
            
            nama, marker = key
            age_values = values[0]
            height_values = values[1]
            weight_values = values[2]
            x_scores = values[3]
            # print(x_scores)
            y_scores = values[4]
            z_scores = values[5]

            average_age = sum(age_values) / len(age_values)
            average_height = sum(height_values) / len(height_values)
            average_weight = sum(weight_values) / len(weight_values)
            
            average_x = sum(x_scores) / 3
            average_y = sum(y_scores) / 3
            average_z = sum(z_scores) / 3
            averageTotal = average_x + average_y + average_z
            
            insert_sql = f"INSERT INTO {nama} (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
            cursor2.execute(insert_sql)
            insert_sql2 = f"INSERT INTO testingknnvariables (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
            cursor2.execute(insert_sql2)
            connection2.commit()
            print(f'data {key} sudah masuk database trainingknnvariables')

        #jadikan marker sebagai row bukan column

    def hitungKNN(self) :

        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='trainingknnvariables')
        
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES")
        tables_to_exclude = ['trainingknnvariables']
        tables = [table[0] for table in cursor.fetchall() if table[0] in tables_to_exclude]
        
        sqlname = f"SELECT trainingknnvariables.name from trainingknnvariables.trainingknnvariables"
        cursor.execute(sqlname)
        resultname = cursor.fetchall()
        name_list_fix = [row[0] for row in resultname]
        # print(name_list_fix)
        

        connection2 = pymysql.connect(host='localhost',
                                     user='root',
                                     password='Iamironman123',
                                     db='testingknnvariables')
        
        cursor2 = connection2.cursor()
        cursor2.execute("SHOW TABLES")
        tables2_to_exclude2 = ['testingknnvariables']
        tables2 = [tables2[0] for tables2 in cursor2.fetchall() if tables2[0] in tables2_to_exclude2]     
        
        sqltesting = f"SELECT testingknnvariables.name from testingknnvariables.testingknnvariables"
        cursor2.execute(sqltesting)
        resultnametesting = cursor2.fetchall()
        name_list_fix_testing = [row2[0] for row2 in resultnametesting]
        # print(name_list_fix_testing)
        
        pilihMarker = ['LPSI', 'RPSI', 'RTOE', 'LHEE', 'LKNE', 'LTIB', 'RTIB',
                       'LANK', 'RTHI', 'LTHI', 'RANK', 'RKNE', 'RHEE', 'LTOE', 'RASI', 'LASI']
        
        averages = {}
        averages2 = {}

        euclidean_distances = {}
        namaTraining = []
        namaTesting = []
        # Loop melalui tabel orang
        for cekTabel in range(len(name_list_fix)):
            # Inisialisasi total_distance untuk orang saat ini
            # print(name_list_fix[cekTabel])
            total_distance = 0
            # Loop melalui data marker
            for i in range(len(pilihMarker)):
                nama = name_list_fix[cekTabel]
                namaTraining.append(nama)
                nama2 = name_list_fix_testing
                namaTesting.append(nama2)
                marker = pilihMarker[i]
                
                # Query untuk mendapatkan data dari tabel trainingknnvariables
                sql1 = f"SELECT trainingknnvariables.Name, trainingknnvariables.Average_Age, trainingknnvariables.Average_Height, trainingknnvariables.Average_Weight, trainingknnvariables.AverageMarker FROM trainingknnvariables.trainingknnvariables"
                cursor.execute(sql1)
                result1 = cursor.fetchall()
                
                # Query untuk mendapatkan data dari tabel testingknnvariables
                sql2 = f"SELECT testingknnvariables.Name, testingknnvariables.Average_Age, testingknnvariables.Average_Height, testingknnvariables.Average_Weight, testingknnvariables.AverageMarker FROM testingknnvariables.testingknnvariables"
                cursor2.execute(sql2)
                result2 = cursor2.fetchall()

        #training
        for row in result1:
            age = row[1]
            height = row[2]
            weight = row[3]
            averagemarker = row[4]

            key = (namaTraining[len(row)], pilihMarker[len(row)])
                    
                # print(key)
            if key in averages:
                averages[key][0].append(age)
                averages[key][1].append(height)
                averages[key][2].append(weight)
                averages[key][3].append(averagemarker)
                        
            else:
                averages[key] = [[age], [height], [weight], [averagemarker]]
        print(averages[key])
        
        # for key, values in averages.items():
        #     print(key)
        
                # # Mendapatkan nilai rata-rata dari tabel trainingknnvariables
                # n1, x1, y1, z1, m1 = result1[0]
                # # print(result1[0])
                # # Mendapatkan nilai rata-rata dari tabel testingknnvariables
                # n2, x2, y2, z2, m2 = result2[0]

                # Menghitung Euclidean distance secara manual
                # distance = ((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2) + ((m1 - m2) ** 2)
                # distance = ((x1 - x2) ** 2) + ((y1 - y2) ** 2) + ((z1 - z2) ** 2) + ((m1 - m2) ** 2)
                # distance = ((x1 - x2) ** 2)
        
            #     # Tambahkan hasil Euclidean distance ke total_distance
            #     total_distance += distance

            # # Simpan hasil total_distance untuk orang saat ini ke dalam dictionary
            # euclidean_distances[name_list_fix[cekTabel]] = total_distance
        
        # print("training")
        # for row1 in result1 :
        #     print(row1[0], row1[1], row1[2], row1[3], row1[4])
            
        # print("testing")
        # for row2 in result2 :
        #         print(row2[0], row2[1], row2[2], row2[3], row2[4])
        
        for orang, distance in euclidean_distances.items():
            print(f"Orang: {orang}, Distance: {distance}")
        
        # for cekTabel in range(len(tables)):
            
        #     if tables[cekTabel] not in tables2:
        #         # print(f'{tables[cekTabel]} tidak ada di database 2')
        #         create_sql1 = f"CREATE TABLE {tables[cekTabel]} ( `Name` varchar(255) DEFAULT NULL, `Marker` varchar(255) DEFAULT NULL, `Average_Age` int DEFAULT NULL, `Average_Height` int DEFAULT NULL, `Average_Weight` int DEFAULT NULL, `AverageMarker` double DEFAULT NULL )"
        #         cursor2.execute(create_sql1)
        #         connection2.commit()
        #         # print(f"berhasil membuat tabel {tables[cekTabel]}")
            
        #     for i in range(len(pilihMarker)):
        #         nama = tables[cekTabel]
        #         marker = pilihMarker[i]
                
        #         sql = f"SELECT {tables[cekTabel]}.Frame, {tables[cekTabel]}.Name, {tables[cekTabel]}.Age, {tables[cekTabel]}.Height, {tables[cekTabel]}.Weight, {tables[cekTabel]}.Marker, {tables[cekTabel]}.X_Cordinates, {tables[cekTabel]}.X_Scoring, {tables[cekTabel]}.Y_Cordinates, {tables[cekTabel]}.Y_Scoring, {tables[cekTabel]}.Z_Cordinates, {tables[cekTabel]}.Z_Scoring FROM {tables[cekTabel]} WHERE {tables[cekTabel]}.Name = '{nama}' AND {tables[cekTabel]}.Marker = '{marker}'"
        #         cursor.execute(sql)
        #         result = cursor.fetchall()
             
        #         for row in result:
        #             age = row[2]
        #             height = row[3]
        #             weight = row[4]
        #             x_scoring = row[7]
        #             y_scoring = row[9]
        #             z_scoring = row[11]

        #             key = (nama, marker)
                    
        #             # print(key)
        #             if key in averages:
        #                 averages[key][0].append(age)
        #                 averages[key][1].append(height)
        #                 averages[key][2].append(weight)
        #                 averages[key][3].append(x_scoring)
        #                 averages[key][4].append(y_scoring)
        #                 averages[key][5].append(z_scoring)
        #             else:
        #                 averages[key] = [[age], [height], [weight], [x_scoring], [y_scoring], [z_scoring]]
        #     delete_sql = f"DELETE FROM {nama}"
        #     cursor2.execute(delete_sql)
        #     delete_sql2 = f"DELETE FROM testingknnvariables"
        #     cursor2.execute(delete_sql2)
        #     # print(nama)
        #     # print(tables[cekTabel],averages[key])
        # # Memasukkan hasil perhitungan ke dalam database
        # # for key, values in averages.items():
            
        # #     nama, marker = key
        # #     age_values = values[0]
        # #     height_values = values[1]
        # #     weight_values = values[2]
        # #     x_scores = values[3]
        # #     # print(x_scores)
        # #     y_scores = values[4]
        # #     z_scores = values[5]

        # #     average_age = sum(age_values) / len(age_values)
        # #     average_height = sum(height_values) / len(height_values)
        # #     average_weight = sum(weight_values) / len(weight_values)
            
        # #     average_x = sum(x_scores) / 3
        # #     average_y = sum(y_scores) / 3
        # #     average_z = sum(z_scores) / 3
        # #     averageTotal = average_x + average_y + average_z
            
        # #     insert_sql = f"INSERT INTO {nama} (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
        # #     cursor2.execute(insert_sql)
        # #     insert_sql2 = f"INSERT INTO testingknnvariables (Name, Marker, Average_Age, Average_Height, Average_Weight, AverageMarker) VALUES ('{nama}', '{marker}', {average_age}, {average_height}, {average_weight}, {averageTotal})"
        # #     cursor2.execute(insert_sql2)
        # #     connection2.commit()
        # #     print(f'data {key} sudah masuk database trainingknnvariables')
        
        # for key, values in averages.items():
        #     nama, marker = key
            
        #     # Ambil data dari tabel trainingknnvariables
        #     sql_training = f"SELECT Average_Age, Average_Height, Average_Weight, AverageMarker FROM trainingknnvariables WHERE Name = '{nama}' AND Marker = '{marker}'"
        #     cursor2.execute(sql_training)
        #     result_training = cursor2.fetchone()
        #     training_age = result_training[0]
        #     training_height = result_training[1]
        #     training_weight = result_training[2]
        #     training_marker = result_training[3]

        #     # Ambil data dari tabel testingknnvariables
        #     sql_testing = f"SELECT Average_Age, Average_Height, Average_Weight, AverageMarker FROM testingknnvariables WHERE Name = '{nama}' AND Marker = '{marker}'"
        #     cursor2.execute(sql_testing)
        #     result_testing = cursor2.fetchone()
        #     testing_age = result_testing[0]
        #     testing_height = result_testing[1]
        #     testing_weight = result_testing[2]
        #     testing_marker = result_testing[3]

        #     # Hitung Euclidean distance antara data training dan testing
        #     age_distance = abs(training_age - testing_age)
        #     height_distance = abs(training_height - testing_height)
        #     weight_distance = abs(training_weight - testing_weight)
        #     marker_distance = abs(training_marker - testing_marker)

        #     # Print hasil perhitungan
        #     print(f"Marker {marker} - Age Distance: {age_distance}")
        #     print(f"Marker {marker} - Height Distance: {height_distance}")
        #     print(f"Marker {marker} - Weight Distance: {weight_distance}")
        #     print(f"Marker {marker} - Marker Distance: {marker_distance}")

        # # jadikan marker sebagai row bukan column

            
    
                        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
