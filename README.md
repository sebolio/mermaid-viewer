# Visualizador de Mermaid en Python 3

### Usar Virtual Env como buena práctica
VENV en Linux o Mac
```
python3 -m venv venv
source venv/bin/activate
```

VENV en Windows
```
python3 -m venv venv
venv/scripts/activate.bat
venv/scripts/activate.ps1
```

### Instalar dependencias
```
pip3 install PyQt5 PyQtWebEngine
sudo apt install libqt5x11extras5 #linux
```

### Correr
Puede recibir codigo o un archivo como parametro, o abre el selector
```
python3 mermaid.py
python3 mermaid.py 'string'
python3 mermaid.py ejemplo.txt
```

### Crear binario:
Si quieres generar un binario portátil del visualizador:

```
pyinstaller -F --noconsole mermaid.py
```
