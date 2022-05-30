import tkinter as tk
from tkinter import Text, Label
from PIL import ImageTk, Image


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
        h = 500

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #   ------------    switch_frames from https://stackoverflow.com/   ------------
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
        tk.Label(self, text="Photo editor").pack(side="top", fill="x", pady=20)
        self.logo = Image.open('./logo/ala-too_logo.jpeg')
        self.logo = ImageTk.PhotoImage(image=self.logo)
        tk.Label(self, image=self.logo).pack(pady=(0, 10))
        tk.Button(self, text="Crop image",
                  command=lambda: master.switch_frame(Crop)).pack()
        tk.Button(self, text="Black & White filter",
                  command=lambda: master.switch_frame(BlackWhite)).pack()
        tk.Button(self, text="About & Copyright",
                  command=lambda: master.switch_frame(AboutCopy)).pack()


#   /-------------------------------------/      CROP - PAGE       /----------------------------/
class Crop(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Crop").pack(side="top", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=10)


#   /-------------------------------------/      BLACK & WIGHT - PAGE       /----------------------------/
class BlackWhite(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="BlackWhite").pack(side="top", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=10)


#   /-------------------------------------/      ABOUT-COPYRIGHT - PAGE       /----------------------------/
class AboutCopy(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Copyright").pack(side="top", pady=10)

        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack(side=tk.BOTTOM, pady=10)


if __name__ == "__main__":
    app = AlatooApp()
    app.mainloop()
