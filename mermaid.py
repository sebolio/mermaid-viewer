# Visualizador de Mermaid - por Seb Findling
# Se puede enviar un archivo o codigo como parmetro, o nada para seleccionar visualmente:

# python3 mermaid.py 'codigo mermaid'
# python3 mermaid.py <archivo>
# python3 mermaid.py


import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class MermaidViewer(QMainWindow):
    def __init__(self, mermaid_code=None, file_path=None):
        super().__init__()
        self.setWindowTitle('Mermaid Viewer')
        #self.setGeometry(100, 100, 800, 600)
        
        self.web_view = QWebEngineView()
        self.setCentralWidget(self.web_view)

        if mermaid_code:
            self.display_mermaid(mermaid_code)

        else:
          if file_path:
            with open(file_path, 'r') as file:
                mermaid_code = file.read()
            self.display_mermaid(mermaid_code)

          else:
            self.open_file_dialog()

    def display_mermaid(self, mermaid_code):
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script type="module">
                import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.0.2/dist/mermaid.esm.min.mjs';
            </script>
        </head>
        <body>
            <div class="mermaid" style="color:white">
                {mermaid_code}
            </div>
        </body>
        </html>
        """
        self.web_view.setHtml(html_content)

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Abrir archivo Mermaid", "", "Archivos de texto (*.txt);;Todos los archivos (*)")
        if file_path:
            with open(file_path, 'r') as file:
                mermaid_code = file.read()
            self.display_mermaid(mermaid_code)
        else:
            sys.exit()

def main():
    app = QApplication(sys.argv + ['--no-sandbox'])
    print("argv")
    print(sys.argv)

    mermaid_code = None
    file_path = None

    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            file_path = sys.argv[1]
        else:
            mermaid_code = sys.argv[1]

    viewer = MermaidViewer(mermaid_code, file_path)
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
