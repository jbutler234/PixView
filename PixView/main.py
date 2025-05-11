import os
from tkinter import filedialog, Label, Button, Frame
from PIL import Image, ImageTk


class ImageViewerWindow:
    def __init__(self, root):
        self.root = root
        self.image_files = []
        self.current_index = 0

        # UI layout
        self.title_label = Label(root, text="Welcome to PixView!", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        self.image_label = Label(root, text="Image not available", width=70, height=20)
        self.image_label.pack()

        self.info_label = Label(root, text="", font=("Helvetica", 12))
        self.info_label.pack()

        # Navigation
        nav_frame = Frame(root)
        nav_frame.pack(pady=10)

        self.prev_button = Button(nav_frame, text="<< Previous", command=self.show_prev)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = Button(nav_frame, text="Next >>", command=self.show_next)
        self.next_button.grid(row=0, column=1, padx=5)

        self.load_button = Button(root, text="Load Folder", command=self.load_images)
        self.load_button.pack(pady=5)

        self.exit_button = Button(root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def load_images(self):
        folder = filedialog.askdirectory()
        if not folder:
            self.info_label.config(text="No folder selected.")
            return

        extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
        self.image_files = [
            os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(extensions)
        ]
        self.image_files.sort()
        self.current_index = 0

        if not self.image_files:
            self.image_label.config(text="No images found in folder.")
            self.info_label.config(text="")
        else:
            self.show_image()

    def show_image(self):
        try:
            image_path = self.image_files[self.current_index]
            image = Image.open(image_path)
            image = image.resize((700, 500))
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.info_label.config(
                text=f"Image {self.current_index + 1} of {len(self.image_files)}"
            )
        except Exception:
            self.image_label.config(text="Image failed to load.")
            self.image_label.image = None
            self.info_label.config(text="")

    def show_next(self):
        if self.image_files and self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.show_image()

    def show_prev(self):
        if self.image_files and self.current_index > 0:
            self.current_index -= 1
            self.show_image()