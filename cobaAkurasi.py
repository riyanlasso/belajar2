import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from math import sqrt
import numpy as np

class KNNWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('K-Nearest Neighbors')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.features_layout = QHBoxLayout()
        self.layout.addLayout(self.features_layout)
        self.feature1_label = QLabel('Feature 1:')
        self.feature1_input = QLineEdit()
        self.features_layout.addWidget(self.feature1_label)
        self.features_layout.addWidget(self.feature1_input)
        
        self.feature2_label = QLabel('Feature 2:')
        self.feature2_input = QLineEdit()
        self.features_layout.addWidget(self.feature2_label)
        self.features_layout.addWidget(self.feature2_input)
        
        self.predict_button = QPushButton('Predict')
        self.predict_button.clicked.connect(self.predict)
        self.layout.addWidget(self.predict_button)
        
    def euclidean_distance(self, p1, p2):
        # Menghitung jarak Euclidean antara dua titik p1 dan p2
        print(f'{p1[0]} dan {p2[0]} dengan {p1[1]} dan {p2[1]}')
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def predict(self):
        # Mengambil input fitur dari pengguna
        feature1 = float(self.feature1_input.text())
        feature2 = float(self.feature2_input.text())
        
        
        X_train = [[1.0, 2.0], [2.0, 1.0], [2.0, 3.0], [3.0, 2.0]]
        y_train = ['A', 'B', 'C', 'D']
        
        
        k = 1  
        distances = []
        for i in range(len(X_train)):
            distance = self.euclidean_distance([feature1, feature2], X_train[i])
            distances.append((distance, y_train[i]))
            
            print(distance)
            # print((distance, y_train[i]))
        
        distances.sort()  # Mengurutkan berdasarkan jarak terkecil
        neighbors = [distances[i][1] for i in range(k)]  # Memilih k tetangga terdekat
        print(neighbors)
        predicted_class = max(set(neighbors), key=neighbors.count)  # Memilih kelas yang paling sering muncul
        print(predicted_class)
        
        accuracy = sum([1 for i in range(len(X_train)) if y_train[i] == predicted_class]) / len(X_train)
                
        unclassified = {}
        for c in set(y_train):
            unclassified[c] = sum([1 for i in range(len(X_train)) if y_train[i] != c]) / len(X_train)
                
        classes = sorted(set(y_train))
        confusion_matrix = np.zeros((len(classes), len(classes)), dtype=int)
        for i in range(len(X_train)):
            true_class_index = classes.index(y_train[i])
            predicted_class_index = classes.index(predicted_class)
            confusion_matrix[true_class_index][predicted_class_index] += 1
        
        
        message = f'Predicted class: {predicted_class}\nAccuracy: {accuracy*100:.2f}%\n'
        for c, perc in unclassified.items():
            message += f'Unclassified ({c}): {perc*100:.2f}%\n'
        message += '\nConfusion Matrix:\n'
        message += '    ' + ' '.join(classes) + '\n'
        for i in range(len(classes)):
            message += classes[i] + '   ' + ' '.join(str(confusion_matrix[i][j]) for j in range(len(classes))) + '\n'
        QMessageBox.information(self, 'Prediction Result', message)


app = QApplication(sys.argv)
window = KNNWidget()
window.show()
sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QMessageBox
# from PyQt5.QtCore import Qt
# from math import sqrt
# import numpy as np

# class KNNWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle('K-Nearest Neighbors')
#         self.layout = QVBoxLayout()
#         self.setLayout(self.layout)
        
#         self.features_layout = QHBoxLayout()
#         self.layout.addLayout(self.features_layout)
#         self.feature1_label = QLabel('Feature 1:')
#         self.feature1_input = QLineEdit()
#         self.features_layout.addWidget(self.feature1_label)
#         self.features_layout.addWidget(self.feature1_input)
        
#         self.feature2_label = QLabel('Feature 2:')
#         self.feature2_input = QLineEdit()
#         self.features_layout.addWidget(self.feature2_label)
#         self.features_layout.addWidget(self.feature2_input)
        
#         self.predict_button = QPushButton('Predict')
#         self.predict_button.clicked.connect(self.predict)
#         self.layout.addWidget(self.predict_button)
        
#     def euclidean_distance(self, p1, p2):
#         # Menghitung jarak Euclidean antara dua titik p1 dan p2
#         return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
#     def predict(self):
#         # Mengambil input fitur dari pengguna
#         feature1 = float(self.feature1_input.text())
#         feature2 = float(self.feature2_input.text())
        
#         # Menentukan dataset latih
#         X_train = [[1.0, 2.0], [2.0, 1.0], [2.0, 3.0], [3.0, 2.0]]
#         y_train = ['A', 'A', 'B', 'B']
        
#         # Memprediksi kelas target
#         k = 3  # Jumlah tetangga terdekat yang akan dipertimbangkan
#         distances = []
#         for i in range(len(X_train)):
#             distance = self.euclidean_distance([feature1, feature2], X_train[i])
#             distances.append((distance, y_train[i]))
        
#         distances.sort()  
#         neighbors = [distances[i][1] for i in range(k)]  
#         predicted_class = max(set(neighbors), key=neighbors.count)  
        
#         accuracy = sum([1 for i in range(len(X_train)) if y_train[i] == predicted_class]) / len(X_train)
    
#         unclassified = {}
        
#         for c in set(y_train):
#             unclassified[c] = sum([1 for i in range(len(X_train)) if y_train[i] != c]) / len(X_train)
        
        
#         classes = sorted(set(y_train))
#         confusion_matrix = np.zeros((len(classes), len(classes)), dtype=int)
#         for i in range(len(X_train)):
#             true_class_index = classes.index(y_train[i])
#             predicted_class_index = classes.index(predicted_class)
#             confusion_matrix[true_class_index][predicted_class_index] += 1
        
        
#         message = f'Predicted class: {predicted_class}\nAccuracy: {accuracy*100:.2f}%\n'
#         for c, perc in unclassified.items():
#             message += f'Unclassified ({c}): {perc*100:.2f}%\n'
#         message += '\nConfusion Matrix:\n'
#         message += '    ' + ' '.join(classes) + '\n'
#         for i in range(len(classes)):
#             message += classes[i] + '   ' + ' '.join(str(confusion_matrix[i][j]) for j in range(len(classes))) + '\n'
#         QMessageBox.information(self, 'Prediction Result', message)

# # Membuat aplikasi PyQt
# app = QApplication(sys.argv)
# window = KNNWidget()
# window.show()
# sys.exit(app.exec_())
