"""wxPython Hello World - TreeView demo with toolbar."""

import argparse
import os
import threading
import wx

from words import random_label


def run_smoke_test(app, frame):
    app.SetTopWindow(frame)
    frame.Show()
    app.ProcessPendingEvents()

    errors = []

    # 1. Verify frame basics
    if not frame.GetTitle():
        errors.append("frame has no title")
    if not frame.GetStatusBar():
        errors.append("status bar missing")
    if not frame.GetToolBar():
        errors.append("toolbar missing")

    # 2. Verify tree was seeded (constructor adds 3 items)
    count = frame._count_items()
    if count < 3:
        errors.append("expected >=3 seed items, got {}".format(count))

    # 3. Add a random top-level item
    prev = count
    frame._add_random_item()
    app.ProcessPendingEvents()
    count = frame._count_items()
    if count != prev + 1:
        errors.append("add_random_item: expected {} items, got {}".format(prev + 1, count))

    # 4. Select an item and add a child
    root_child, _ = frame.tree.GetFirstChild(frame.root)
    if root_child.IsOk():
        frame.tree.SelectItem(root_child)
        app.ProcessPendingEvents()
        prev = count
        child = frame.tree.AppendItem(root_child, "Smoke Child")
        frame.tree.Expand(root_child)
        frame._update_status()
        app.ProcessPendingEvents()
        count = frame._count_items()
        if count != prev + 1:
            errors.append("add child: expected {} items, got {}".format(prev + 1, count))

    # 5. Clear the tree
    frame.tree.DeleteChildren(frame.root)
    frame._update_status()
    app.ProcessPendingEvents()
    count = frame._count_items()
    if count != 0:
        errors.append("clear: expected 0 items, got {}".format(count))

    # 6. Verify status bar updates
    status_text = frame.GetStatusBar().GetStatusText()
    if "0" not in status_text:
        errors.append("status bar should show 0 after clear, got: {}".format(status_text))

    # 7. Verify random_label works
    from words import random_label
    label = random_label()
    if not label or len(label.split()) != 2:
        errors.append("random_label() returned bad value: {}".format(label))

    frame.Destroy()
    app.ProcessPendingEvents()

    if errors:
        for e in errors:
            print("SMOKE FAIL: {}".format(e), flush=True)
        os._exit(1)

    print("SMOKE OK: all checks passed", flush=True)
    os._exit(0)


class MainFrame(wx.Frame):
    """Main application window."""

    def __init__(self):
        super().__init__(None, title="wxPython Hello World", size=(600, 400))

        # --- Toolbar ---
        toolbar = self.CreateToolBar(style=wx.TB_TEXT)

        add_tool = toolbar.AddTool(
            wx.ID_ANY, "Add Random",
            wx.ArtProvider.GetBitmap(wx.ART_PLUS, wx.ART_TOOLBAR, (16, 16)),
            shortHelp="Add a random item to the tree",
        )
        add_child_tool = toolbar.AddTool(
            wx.ID_ANY, "Add Child",
            wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_TOOLBAR, (16, 16)),
            shortHelp="Add a random child under the selected item",
        )
        clear_tool = toolbar.AddTool(
            wx.ID_ANY, "Clear Tree",
            wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_TOOLBAR, (16, 16)),
            shortHelp="Remove all items from the tree",
        )
        toolbar.Realize()

        # --- Status bar ---
        self.CreateStatusBar()

        # --- TreeCtrl ---
        self.tree = wx.TreeCtrl(self, style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT)
        self.root = self.tree.AddRoot("Hidden Root")

        # Seed a few items so the tree isn't empty on start
        for _ in range(3):
            self._add_random_item()

        # --- Event bindings ---
        self.Bind(wx.EVT_TOOL, self._on_add_random, add_tool)
        self.Bind(wx.EVT_TOOL, self._on_add_child, add_child_tool)
        self.Bind(wx.EVT_TOOL, self._on_clear, clear_tool)
        self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self._on_selection)

        self.Centre()

    # ---- helpers --------------------------------------------------------

    def _add_random_item(self):
        """Append a random top-level item and return it."""
        item = self.tree.AppendItem(self.root, random_label())
        self.tree.EnsureVisible(item)
        self._update_status()
        return item

    def _count_items(self, parent=None):
        """Recursively count all items in the tree."""
        if parent is None:
            parent = self.root
        count = 0
        child, cookie = self.tree.GetFirstChild(parent)
        while child.IsOk():
            count += 1
            count += self._count_items(child)
            child, cookie = self.tree.GetNextChild(parent, cookie)
        return count

    def _update_status(self):
        self.SetStatusText("Items: {}".format(self._count_items()))

    # ---- event handlers -------------------------------------------------

    def _on_add_random(self, _event):
        self._add_random_item()

    def _on_add_child(self, _event):
        selected = self.tree.GetSelection()
        if not selected.IsOk() or selected == self.root:
            # Nothing selected — fall back to top-level
            self._add_random_item()
            return
        child = self.tree.AppendItem(selected, random_label())
        self.tree.Expand(selected)
        self.tree.EnsureVisible(child)
        self._update_status()

    def _on_clear(self, _event):
        self.tree.DeleteChildren(self.root)
        self._update_status()

    def _on_selection(self, event):
        item = event.GetItem()
        if item.IsOk():
            self.SetStatusText("Selected: {}".format(self.tree.GetItemText(item)))


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke-test", action="store_true")
    args = parser.parse_args(argv)

    if args.smoke_test:
        threading.Timer(10.0, lambda: os._exit(1)).start()

    app = wx.App()
    frame = MainFrame()
    if args.smoke_test:
        run_smoke_test(app, frame)
    app.SetTopWindow(frame)
    frame.Show()
    app.MainLoop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
