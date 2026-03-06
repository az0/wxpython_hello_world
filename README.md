# wxPython Hello World

A minimal wxPython application to evaluate wxWidgets as a cross-platform GUI
toolkit.

## Features

- **TreeView** with a hidden root
- **Toolbar** with buttons to add random items, add children, and clear the tree
- Starts with a few seed items so the UI isn't blank
- Status bar shows item count / selection

## Running locally

```bash
pip install -r requirements.txt
python app.py
```

## Building the .exe (locally on Windows)

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --name wxHelloWorld --strip --noupx app.py
# output: dist/wxHelloWorld.exe
```

## CI / CD

The GitHub Actions workflow (`.github/workflows/build.yml`) builds the `.exe`
on every push to `main` and uploads it as an artifact.

## Comparison

Compare this project to:

* [Python QT6 using PySide6](https://github.com/az0/qt_windows_hello_world)
* [Python 2.7 with GTK3](https://github.com/az0/frozen_pygtk3): outdated
