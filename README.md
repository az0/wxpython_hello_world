# wxPython Hello World

A minimal wxPython application to evaluate wxWidgets as a cross-platform GUI
toolkit — specifically targeting a small, native-looking Windows `.exe`.

## Features

- **TreeView** with a hidden root
- **Toolbar** with buttons to add random items, add children, and clear the tree
- Starts with a few seed items so the UI isn't blank
- Status bar shows item count / selection

## Goals

| Goal | Notes |
|------|-------|
| Evaluate wxWidgets for Windows + other platforms | Native look & feel is a known strength |
| Easy to build a basic app | Single-file `app.py`, ~100 lines |
| Easy to make a portable app | PyInstaller `--onefile` produces a single `.exe` |
| Small installer / binary | Target < 15 MB compressed |
| Reliable, native UI | wxWidgets wraps native controls |

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

## Comparison context

This project is one leg of a three-way comparison:

| Toolkit | Project |
|---------|---------|
| **wxPython** (this repo) | wxWidgets via Python bindings |
| PyQt | Qt via Python bindings |
| PyGTK 3 | GTK 3 via Python bindings |

The comparison evaluates ease of development, binary size, native appearance,
and cross-platform reliability.
