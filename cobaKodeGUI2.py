import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QScrollArea
import pyqtgraph as pg

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrollable PlotWidget Example")
        
        # Membuat widget utama
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Membuat layout horizontal
        self.layout = QHBoxLayout(self.central_widget)

        # Membuat QScrollArea
        self.scroll_area = QScrollArea()
        self.layout.addWidget(self.scroll_area)

        # Membuat widget konten di dalam QScrollArea
        self.scroll_content = QWidget()
        self.scroll_area.setWidget(self.scroll_content)

        # Membuat layout konten di dalam QScrollArea
        self.scroll_layout = QHBoxLayout(self.scroll_content)
        self.scroll_layout2 = QHBoxLayout(self.scroll_content)

        # Membuat PlotWidgets
        self.plot_widget_training_x = pg.PlotWidget()
        self.plot_widget_training_y = pg.PlotWidget()
        self.plot_widget_training_z = pg.PlotWidget()

        self.plot_widget_training_x2 = pg.PlotWidget()
        self.plot_widget_training_y2 = pg.PlotWidget()
        self.plot_widget_training_z2 = pg.PlotWidget()

        # Menambahkan PlotWidgets ke dalam layout konten
        self.scroll_layout.addWidget(self.plot_widget_training_x)
        self.scroll_layout.addWidget(self.plot_widget_training_y)
        self.scroll_layout.addWidget(self.plot_widget_training_z)

        self.scroll_layout2.addWidget(self.plot_widget_training_x2)
        self.scroll_layout2.addWidget(self.plot_widget_training_y2)
        self.scroll_layout2.addWidget(self.plot_widget_training_z2)

        # Mengatur ukuran kotak untuk setiap PlotWidget
        self.plot_widget_training_x.setMaximumHeight(200)
        self.plot_widget_training_y.setMaximumHeight(200)
        self.plot_widget_training_z.setMaximumHeight(200)

        self.plot_widget_training_x2.setMaximumHeight(200)
        self.plot_widget_training_y2.setMaximumHeight(200)
        self.plot_widget_training_z2.setMaximumHeight(200)

        # Mengaktifkan penyesuaian ukuran widget dalam QScrollArea
        self.scroll_area.setWidgetResizable(True)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
