import tkinter as tk
from tkhtmlview import HTMLLabel

# Crear la ventana principal
root = tk.Tk()
root.title("Hello World Web View")

# Definir el tamaño de la ventana
root.geometry("300x200")

# Crear un HTMLLabel para mostrar contenido HTML
html_label = HTMLLabel(root, html="<h1>Hello World</h1>")
html_label.pack(expand=True, fill="both")

# Iniciar el loop de la ventana
root.mainloop()
