import webview
import os
os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--no-sandbox"

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

def start():
  window = webview.create_window('Hello World!', html, width=800, height=600)
  webview.start()

if __name__ == "__main__":
  start()
