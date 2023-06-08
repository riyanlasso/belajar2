# import sys

# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget,
# )


# # Subclass QMainWindow to customize your application's main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Widgets App")

#         layout = QVBoxLayout()
#         widgets = [
#             QCheckBox,
#             QComboBox,
#             QDateEdit,
#             QDateTimeEdit,
#             QDial,
#             QDoubleSpinBox,
#             QFontComboBox,
#             QLCDNumber,
#             QLabel,
#             QLineEdit,
#             QProgressBar,
#             QPushButton,
#             QRadioButton,
#             QSlider,
#             QSpinBox,
#             QTimeEdit,
#         ]

#         for w in widgets:
#             layout.addWidget(w())

#         widget = QWidget()
#         widget.setLayout(layout)

#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(widget)


# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()

# app.exec()


import sys
from PyQt5.QtWidgets import QHBoxLayout,QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QDialog, QLabel, QLineEdit,QDesktopWidget
from PyQt5.QtGui import QScreen, QGuiApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contoh GUI PyQtGraph")
        #fullScreen mode (tidak ada exitnya)
        # self.showFullScreen()
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        self.setGeometry(screen_geometry)
        self.move(0,0)
        # Buat widget untuk menampung tombol-tombol
        button_widget = QWidget()

        # Buat tombol-tombol
        plot_button = QPushButton("Plot")
        create_button = QPushButton("Create")
        read_button = QPushButton("Read")
        update_button = QPushButton("Update")

        # Atur tata letak tombol-tombol
        layout = QHBoxLayout()
        layout.addWidget(plot_button)
        layout.addWidget(create_button)
        layout.addWidget(read_button)
        layout.addWidget(update_button)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        button_widget.setLayout(layout)

        # Atur widget tombol sebagai widget pusat dalam jendela utama
        self.setCentralWidget(button_widget)

        # Menghubungkan tombol-tombol ke metode penanganan
        plot_button.clicked.connect(self.show_plot_ui)
        create_button.clicked.connect(self.show_create_ui)
        read_button.clicked.connect(self.show_read_ui)
        update_button.clicked.connect(self.show_update_ui)


    def show_plot_ui(self):
        # Munculkan UI untuk plot
        dialog = QDialog(self)
        dialog.setWindowTitle("Plot UI")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ini adalah UI untuk Plot"))
        dialog.setLayout(layout)

        dialog.exec_()

    def show_create_ui(self):
        # Munculkan UI untuk create
        dialog = QDialog(self)
        dialog.setWindowTitle("Create UI")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ini adalah UI untuk Create"))
        dialog.setLayout(layout)

        dialog.exec_()

    def show_read_ui(self):
        # Munculkan UI untuk read
        dialog = QDialog(self)
        dialog.setWindowTitle("Read UI")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ini adalah UI untuk Read"))
        dialog.setLayout(layout)

        dialog.exec_()

    def show_update_ui(self):
        # Munculkan UI untuk update
        dialog = QDialog(self)
        dialog.setWindowTitle("Update UI")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Ini adalah UI untuk Update"))
        dialog.setLayout(layout)

        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Contoh GUI PyQtGraph")

#         # Membuat tombol untuk mengimpor file
#         import_button = QPushButton("Import File", self)
#         import_button.clicked.connect(self.import_file)

#         self.setCentralWidget(import_button)

#     def import_file(self):
#         # Menggunakan dialog file untuk memilih file yang akan diimpor
#         file_dialog = QFileDialog(self)
#         file_dialog.setWindowTitle("Pilih File")
#         file_dialog.setFileMode(QFileDialog.ExistingFile)

#         if file_dialog.exec_():
#             # Mendapatkan path file yang dipilih
#             file_path = file_dialog.selectedFiles()[0]
#             print("File yang dipilih:", file_path)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())

# import pymysql

# connection = pymysql.connect(host='localhost',
#                                      user='root',
#                                      password='Iamironman123',
#                                      db='riyanlasso')
# cursor = connection.cursor()
# cursor.execute("SHOW TABLES")
# tables = [table[0] for table in cursor.fetchall()]

# pilihMarker = ['LPSI', 'RPSI', 'RTOE','LHEE','LKNE','LTIB','RTIB','LANK','RTHI','LTHI','RANK','RKNE','RHEE','LTOE','RASI','LASI']
# frame_data = []

# for cekTabel in tables:
#     # print(cekTabel)
#     with connection.cursor() as cursor:
#         for i in range(len(pilihMarker)) : 
#             sql = f"SELECT {cekTabel}.Frame,{cekTabel}.Name, {cekTabel}.Marker, {cekTabel}.X_Cordinates X FROM {cekTabel} where {cekTabel}.Marker = '{pilihMarker[i]}'"
#             show = cursor.execute(sql)
#             result = cursor.fetchall()
#             for row in result:
#                 frame = row[0]
#                 frame_data.append(frame)
#                 name = row[1]
#                 marker = row[2]
#                 x = row[3]
#                 print(frame,name,marker,x)
# print(frame_data)
# import pyqtgraph as pg
# from PyQt5.QtWidgets import QApplication
# import numpy as np

# # Inisialisasi aplikasi Qt
# app = QApplication([])

# # Membuat window utama
# window = pg.GraphicsLayoutWidget()
# window.setWindowTitle("Tiga Plot Horizontal")

# # Membuat tiga plot secara horizontal
# plot_widget_1 = window.addPlot(row=0, col=0)
# plot_widget_2 = window.addPlot(row=0, col=1)
# plot_widget_3 = window.addPlot(row=0, col=2)

# # Menghasilkan data untuk plot
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
# y3 = np.tan(x)

# # Menampilkan data pada masing-masing plot
# plot_widget_1.plot(x, y1, pen='r')
# plot_widget_2.plot(x, y2, pen='g')
# plot_widget_3.plot(x, y3, pen='b')

# # Mengatur label sumbu
# plot_widget_1.setLabel('left', 'Nilai Y')
# plot_widget_1.setLabel('bottom', 'Nilai X')

# plot_widget_2.setLabel('left', 'Nilai Y')
# plot_widget_2.setLabel('bottom', 'Nilai X')

# plot_widget_3.setLabel('left', 'Nilai Y')
# plot_widget_3.setLabel('bottom', 'Nilai X')

# # Menampilkan window utama
# window.show()

# # Menjalankan aplikasi
# app.exec_()

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QScrollArea

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contoh Scroll Vertikal")

        # Buat widget utama
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # Tambahkan beberapa label ke dalam layout
        for i in range(50):
            label = QLabel(f"Label {i}")
            main_layout.addWidget(label)

        # Buat widget scroll area dan atur widget utama sebagai kontennya
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(main_widget)

        # Atur widget scroll area sebagai widget pusat dalam jendela utama
        self.setCentralWidget(scroll_area)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
