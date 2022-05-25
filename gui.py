from tkinter import *
from PIL import ImageTk, Image

tk = Tk()
tk.title('alatoo-app')
tk.geometry('300x300')

img = ImageTk.PhotoImage(file='img/ala-too_logo.jpeg')

label = Label(tk, image=img)
label.pack(pady=20)

tk.mainloop()



