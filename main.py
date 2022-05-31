import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image, UnidentifiedImageError


class AlatooApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Ala-Too app')
        self._frame = None
        self.switch_frame(StartPage)
        self.resizable(False, False)
        self.center_window()

    def center_window(self):
        w = 400
        h = 600

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #   ------------    'switch_frames' from Stackoverflow   ------------
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


#   /-------------------------------------/      START - PAGE       /----------------------------/
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Photo editor").pack(side="top", fill="x", pady=(10, 0))
        self.logo = Image.open('./img/ala-too_logo.jpeg')
        self.logo = ImageTk.PhotoImage(image=self.logo)
        tk.Label(self, image=self.logo).pack(pady=(20, 10))
        tk.Button(self, text="Crop image",
                  command=lambda: master.switch_frame(Crop)).pack()
        tk.Button(self, text="Black & White filter",
                  command=lambda: master.switch_frame(BlackWhite)).pack(pady=10)
        tk.Button(self, text="About & Copyright",
                  command=lambda: master.switch_frame(AboutCopy)).pack()


#   /-------------------------------------/      CROP - PAGE       /----------------------------/
class Crop(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.new = None
        self.cropped = None
        self.fln = None
        self.img = None
        self.canvas = Canvas(self, width=350, height=350)
        tk.Label(self, text="Crop Image").pack(side="top", pady=10)
        self.config()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=(10, 20))

    #   ------------    'config' and 'show_image' from YouTube chanel "Python world"   ------------
    def config(self):
        self.canvas.pack()

        tk.Button(self, text="Open Image", command=self.show_image).pack()

        tk.Button(self, text="Crop Image", command=self.crop_image).pack(pady=10)

        # tk.Button(self, text="Download Image", command=self.download_image).pack()

    def show_image(self):
        self.fln = filedialog.askopenfilename()
        try:
            self.img = Image.open(self.fln)
            self.img.thumbnail((350, 350))
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(0, 1, image=self.img, anchor='nw')
        except UnidentifiedImageError:
            messagebox.showerror(
                "Error", "Image not defined"
            )

    #   ------------    function 'crop' from github.com/Emazov  ------------
    def crop_image(self):
        self.cropped = Image.open(self.fln)

        w = self.cropped.width
        h = self.cropped.height
        new_width = 1080
        new_height = 1080

        left = (w - new_width) / 2
        top = (h - new_height) / 2
        right = (w + new_width) / 2
        bottom = (h + new_height) / 2

        self.cropped = self.cropped.crop((left, top, right, bottom))
        self.cropped.thumbnail((350, 350))
        self.cropped = ImageTk.PhotoImage(self.cropped)
        self.canvas.create_image(1, 1, image=self.cropped, anchor='nw')


#   /-------------------------------------/      BLACK & WIGHT - PAGE       /----------------------------/
class BlackWhite(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.new = None
        self.fln = None
        self.img = None
        self.canvas = Canvas(self, width=350, height=350)
        tk.Label(self, text="Black and White filter").pack(side="top", pady=10)
        self.config()
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=10)

    #   ------------    'show_image' and 'config' from YouTube chanel "Python world"   ------------
    def config(self):
        self.canvas.pack()

        tk.Button(self, text="Open Image", command=self.show_image).pack()

        tk.Button(self, text="Use filter", command=self.filter_image).pack(pady=10)

        # tk.Button(self, text="Download Image", command=self.download_image).pack()

    def show_image(self):
        self.fln = filedialog.askopenfilename()
        self.img = Image.open(self.fln)
        self.img.thumbnail((350, 350))
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(0, 1, image=self.img, anchor='nw')

    def filter_image(self):
        self.new = Image.open(self.fln)
        self.new = self.new.convert(mode='L')
        self.new.thumbnail((350, 350))
        self.new = ImageTk.PhotoImage(self.new)
        self.canvas.create_image(0, 1, image=self.new, anchor='nw')


#   /-------------------------------------/      ABOUT-COPYRIGHT - PAGE       /----------------------------/
class AboutCopy(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Copyright").pack(side="top", pady=10)

        text_box = Text(self, height=15, width=45)
        text_box.pack(expand=True)
        text_box.insert("end", self.copyright)

        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=10)

    @property
    def copyright(self):
        copyright_symbol = "\u00A9"

        return f"""

    This work is the intellectual property of the author. 

    Permission is granted for this material 
to be shared for non-commercial, educational 
purposes, provided that this copyright 
statement appears on the reproduced materials
and notice is given hat the copying is by 
permission of the author. 
        
                  {copyright_symbol} Emazov"""


if __name__ == "__main__":
    app = AlatooApp()
    app.mainloop()
