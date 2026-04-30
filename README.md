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

## Building the .exe locally on Windows

```bash
pip install -r requirements.txt

# One-file build (single .exe)
pyinstaller --onefile --windowed --name wxHelloWorld --strip --noupx app.py
# output: dist/wxHelloWorld.exe

# One-directory build (folder with .exe and dependencies)
pyinstaller --windowed --name wxHelloWorld --strip --noupx app.py
# output: dist/wxHelloWorld/wxHelloWorld.exe
```

## Building the .app / DMG locally on macOS

```bash
pip install -r requirements.txt

# Build the .app bundle
pyinstaller --windowed --name wxHelloWorld --strip --noupx app.py
# output: dist/wxHelloWorld.app

# Create a DMG installer (requires create-dmg: brew install create-dmg)
create-dmg \
  --volname "wxHelloWorld" \
  --window-pos 200 120 \
  --window-size 600 400 \
  --icon-size 100 \
  --icon "wxHelloWorld.app" 150 190 \
  --app-drop-link 450 190 \
  --no-internet-enable \
  "dist/wxHelloWorld.dmg" \
  "dist/wxHelloWorld.app"
# output: dist/wxHelloWorld.dmg
```

## CI / CD

The GitHub Actions workflow (`.github/workflows/build.yml`) builds the Windows
`.exe` and macOS `.dmg` on every push to `main` and uploads them as artifacts.

Helpful commands

```terminal
# list recent runs (non-inactive)
gh run list

# interactively view summary of workflow run
gh run view

# non-interactively view fail log for latest run
RUN_ID=$(gh run list --limit 1 --json databaseId --jq '.[0].databaseId') && gh run view $RUN_ID --log-failed
```

## Comparison

Compare this project to:

* [Python QT6 using PySide6](https://github.com/az0/qt_windows_hello_world)
* [Python 2.7 with GTK3](https://github.com/az0/frozen_pygtk3): outdated
