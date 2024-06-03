import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

# HTML content with a button
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World Web View</title>
</head>
<body>
    <h1>Holiwi</h1>
    <button onclick="alert('Button Pressed!')">Press Me</button>
</body>
</html>
"""

app = QApplication(sys.argv + ['--no-sandbox'])

# Crear la ventana principal
window = QWidget()
window.setWindowTitle('Hello World Web View')
#window.setGeometry(100, 100, 400, 300)

# Crear el layout
layout = QVBoxLayout()

# Crear el componente QWebEngineView
webview = QWebEngineView()
webview.setHtml(html_content)

# Añadir el componente al layout
layout.addWidget(webview)
window.setLayout(layout)

# Mostrar la ventana
window.show()

# Ejecutar el loop de la aplicación
sys.exit(app.exec_())
