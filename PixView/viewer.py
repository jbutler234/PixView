import os
from tkinter import filedialog, Label, Button, Frame
from PIL import Image, ImageTk

# Main image viewer window
class ImageViewerWindow:
    def __init__(self, root):
        self.root = root
        self.image_files = []       # List of image file paths
        self.current_index = 0      # Track current image index

        # --- Title Label ---
        self.title_label = Label(root, text="Welcome to PixView!", font=("Helvetica", 20))
        self.title_label.pack(pady=10)

        # --- Image Display Area ---
        self.image_label = Label(root)
        self.image_label.pack(expand=True)

        # --- Info Label (e.g. "Image 2 of 5") ---
        self.info_label = Label(root, text="", font=("Helvetica", 12))
        self.info_label.pack(pady=5)

        # --- Navigation Buttons ---
        nav_frame = Frame(root)
        nav_frame.pack(pady=10)

        self.prev_button = Button(nav_frame, text="<< Previous", command=self.show_prev)
        self.prev_button.grid(row=0, column=0, padx=5)

        self.next_button = Button(nav_frame, text="Next >>", command=self.show_next)
        self.next_button.grid(row=0, column=1, padx=5)

        # --- Load Folder Button ---
        self.load_button = Button(root, text="Load Folder", command=self.load_images)
        self.load_button.pack(pady=5)

        # --- Exit Button ---
        self.exit_button = Button(root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    # Let user select a folder and load image paths
    def load_images(self):
        folder = filedialog.askdirectory()
        if not folder:
            self.info_label.config(text="No folder selected.")
            return

        # Filter image files by extension
        extensions = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
        self.image_files = [
            os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(extensions)
        ]
        self.image_files.sort()
        self.current_index = 0

        # Show first image if available
        if not self.image_files:
            self.image_label.config(text="No images found in folder.")
            self.image_label.image = None
            self.info_label.config(text="")
        else:
            self.show_image()

    # Display the current image
    def show_image(self):
        try:
            image_path = self.image_files[self.current_index]
            image = Image.open(image_path)
            image = image.resize((1000, 700))  # Resize image larger
            photo = ImageTk.PhotoImage(image)

            self.image_label.config(image=photo)
            self.image_label.image = photo  # Prevent garbage collection
            self.info_label.config(
                text=f"Image {self.current_index + 1} of {len(self.image_files)}"
            )
        except Exception:
            self.image_label.config(text="Image failed to load.")
            self.image_label.image = None
            self.info_label.config(text="")

    # Show next image
    def show_next(self):
        if self.image_files and self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.show_image()

    # Show previous image
    def show_prev(self):
        if self.image_files and self.current_index > 0:
            self.current_index -= 1
            self.show_image()