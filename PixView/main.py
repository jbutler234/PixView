import tkinter as tk
from viewer import ImageViewerWindow
from help_window import HelpWindow


class PixViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PixView")
        self.root.geometry("800x600")

        # Create main viewer window
        self.viewer_window = ImageViewerWindow(self.root)

        # Add Help/About menu
        menubar = tk.Menu(self.root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="How to Use", command=self.open_help_window)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

    def open_help_window(self):
        HelpWindow(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = PixViewApp(root)
    root.mainloop()