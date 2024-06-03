import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)

# Crear la ventana principal
window = QWidget()
window.setWindowTitle('Hello World Web View')
window.setGeometry(100, 100, 300, 200)

# Crear un layout y un label
layout = QVBoxLayout()
label = QLabel('<button>aprietame sin miedo</button><h1>Hello World</h1>')
label.setAlignment(Qt.AlignCenter)

# Añadir el label al layout
layout.addWidget(label)
window.setLayout(layout)

# Mostrar la ventana
window.show()

# Ejecutar el loop de la aplicación
sys.exit(app.exec_())
