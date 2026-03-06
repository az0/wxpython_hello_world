"""wxPython Hello World - TreeView demo with toolbar."""

import wx

from words import random_label


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

        # --- TreeCtrl ---
        self.tree = wx.TreeCtrl(self, style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT)
        self.root = self.tree.AddRoot("Hidden Root")

        # Seed a few items so the tree isn't empty on start
        for _ in range(3):
            self._add_random_item()

        # --- Status bar ---
        self.CreateStatusBar()
        self._update_status()

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


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()


if __name__ == "__main__":
    main()
