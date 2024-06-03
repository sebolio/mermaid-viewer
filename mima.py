import tkinter as tk
from ttkwebview import webview

window = tk.Tk()
window.title("Hello World!")

# Create webview widget
my_webview = webview(window)
my_webview.pack(fill=tk.BOTH, expand=True)

# Load HTML content with "Hello World!" heading
html = """
<!DOCTYPE html>
<html>
<head>
  <title>Hello World!</title>
</head>
<body>
  <h1>Hello World!</h1>
</body>
</html>
"""

my_webview.set_text(html)  # Set HTML content instead of loading URL

window.mainloop()
