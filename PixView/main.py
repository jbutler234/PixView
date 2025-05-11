import tkinter as tk
from viewer import ImageViewerWindow
from help_window import HelpWindow

# Main application class for PixView
class PixViewApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PixView")
        self.root.geometry("1100x850")  # Set larger window size

        # Create the main image viewer window
        self.viewer_window = ImageViewerWindow(self.root)

        # Create a menu bar with a Help menu
        menubar = tk.Menu(self.root)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="How to Use", command=self.open_help_window)
        menubar.add_cascade(label="Help", menu=help_menu)
        self.root.config(menu=menubar)

    # Opens the secondary Help window
    def open_help_window(self):
        HelpWindow(self.root)

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PixViewApp(root)
    root.mainloop()