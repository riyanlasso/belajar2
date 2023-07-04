# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QPlainTextEdit
# from PyQt5.QtCore import QThread, pyqtSignal, QTimer

# class DataThread(QThread):
#     data_updated = pyqtSignal(str)

#     def __init__(self):
#         super().__init__()

#     def run(self):
#         counter = 0
#         while True:
#             data = f"Data: {counter}"
#             self.data_updated.emit(data)
#             counter += 1
#             self.msleep(1000)  # Delay 1 detik


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Contoh Real-Time Data PyQt5")
#         self.setGeometry(200, 200, 400, 300)

#         # Membuat layout utama menggunakan QVBoxLayout
#         main_layout = QVBoxLayout()

#         # Membuat tombol untuk memulai/menghentikan pembaruan data
#         self.start_button = QPushButton("Start")
#         self.start_button.clicked.connect(self.start_data_thread)
#         self.stop_button = QPushButton("Stop")
#         self.stop_button.clicked.connect(self.stop_data_thread)

#         # Membuat wadah untuk menampilkan data
#         self.data_display = QPlainTextEdit()

#         # Menambahkan tombol dan wadah ke dalam layout utama
#         main_layout.addWidget(self.start_button)
#         main_layout.addWidget(self.stop_button)
#         main_layout.addWidget(self.data_display)

#         # Mengatur layout utama ke dalam window
#         self.setLayout(main_layout)

#         # Inisialisasi thread pembaruan data
#         self.data_thread = DataThread()
#         self.data_thread.data_updated.connect(self.update_data_display)

#     def start_data_thread(self):
#         self.data_thread.start()
#         self.start_button.setEnabled(False)
#         self.stop_button.setEnabled(True)

#     def stop_data_thread(self):
#         self.data_thread.terminate()
#         self.start_button.setEnabled(True)
#         self.stop_button.setEnabled(False)

#     def update_data_display(self, data):
#         self.data_display.appendPlainText(data)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
# from io import StringIO

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Contoh GUI dengan PyQt5")
#         self.setGeometry(300, 200, 400, 300)

#         # Membuat tata letak utama dan widget
#         layout = QVBoxLayout()
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)

#         # Membuat label dan tombol
#         self.label = QLabel("Hasil Output", self)
#         layout.addWidget(self.label)
#         button_output = QPushButton("Klik untuk Output", self)
#         layout.addWidget(button_output)
#         button_refresh = QPushButton("Refresh", self)
#         layout.addWidget(button_refresh)

#         # Menghubungkan tombol dengan metode onClicked
#         button_output.clicked.connect(self.onOutputClicked)
#         button_refresh.clicked.connect(self.onRefreshClicked)

#         # Membuat objek StringIO untuk menangkap output
#         self.output_stream = StringIO()

#     def onOutputClicked(self):
#         # Mengarahkan output ke objek StringIO
#         print("Ini adalah output yang ditampilkan di konsol.")
#         sys.stdout = self.output_stream
#         # Mengubah teks label ketika tombol Output diklik
#         self.label.setText("Output telah ditampilkan di konsol.")
#         # Menampilkan output ke konsol
        

#     def onRefreshClicked(self):
#         # Mengembalikan teks label ke nilai semula
#         self.label.setText("Hasil Output")

#         # Membersihkan konsol dengan mengosongkan objek StringIO
#         self.output_stream.truncate(0)
#         self.output_stream.seek(0)

#         # Mengarahkan output kembali ke sys.stdout
#         sys.stdout = sys.__stdout__

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# Menghitung akar pangkat dua (akar kuadrat)
# angka = 16
# akar = angka ** 0.5
# print(akar)  # Output: 4.0

# # Menghitung akar pangkat tiga (akar kubik)
# angka = 27
# akar = angka ** (1/3)
# print(akar)  # Output: 3.0


# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Contoh GUI Responsif")
#         self.setGeometry(200, 200, 600, 400)

#         # Widget utama
#         main_widget = QWidget(self)
#         self.setCentralWidget(main_widget)
#         main_layout = QVBoxLayout(main_widget)

#         # Widget responsif
#         label = QLabel("Ini adalah Label Responsif")
#         button = QPushButton("Ini adalah Tombol Responsif")

#         # Set kebijakan ukuran widget
#         label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#         button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

#         # Menambahkan widget ke dalam layout
#         main_layout.addWidget(label)
#         main_layout.addWidget(button)

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contoh GridLayout")
        self.setGeometry(200, 200, 400, 200)

        # Widget utama
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QGridLayout(main_widget)

        # Widget di dalam GridLayout
        label1 = QLabel("Nama:")
        label2 = QLabel("Umur:")
        label3 = QLabel("Tinggi Badan:")
        label4 = QLabel("Berat Badan:")

        line_edit1 = QLineEdit()
        line_edit2 = QLineEdit()
        line_edit3 = QLineEdit()
        line_edit4 = QLineEdit()

        button = QPushButton("Simpan")

        # Menambahkan widget ke dalam GridLayout
        main_layout.addWidget(label1, 0, 0)
        main_layout.addWidget(line_edit1, 0, 1)
        main_layout.addWidget(label2, 1, 0)
        main_layout.addWidget(line_edit2, 1, 1)
        main_layout.addWidget(label3, 2, 0)
        main_layout.addWidget(line_edit3, 2, 1)
        main_layout.addWidget(label4, 3, 0)
        main_layout.addWidget(line_edit4, 3, 1)
        main_layout.addWidget(button, 4, 0, 1, 2)  # Menggunakan rowSpan dan columnSpan

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



