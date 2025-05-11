import tkinter as tk


class HelpWindow:
    def __init__(self, parent):
        self.top = tk.Toplevel(parent)
        self.top.title("How to Use PixView")
        self.top.geometry("400x250")

        tk.Label(self.top, text="PixView Instructions", font=("Helvetica", 16)).pack(pady=10)

        instructions = (
            "1. Click 'Load Folder' to choose a folder with images.\n"
            "2. Use 'Next' and 'Previous' to browse through them.\n"
            "3. Click 'Exit' to close the app.\n\n"
            "Only image files (.jpg, .png, etc.) will be shown."
        )

        tk.Label(self.top, text=instructions, justify="left").pack(padx=10, pady=10)

        tk.Button(self.top, text="Close", command=self.top.destroy).pack(pady=10)