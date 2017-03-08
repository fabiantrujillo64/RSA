from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *

root = Tk() #gives us a blank canvas object to work with
root.title("RSA Project")
root.config(width = 500, height=500)

label1 = Label(root, text="n=", anchor=W)
label1.grid(row=0, column=0)

entry1 = Entry(root)
entry1.grid(row=0, column=1)

button1 = Button(root, text="Decrypt")
button1.grid(row=1, column=0)

label2 = Label(root, text="e=", anchor=W)
label2.grid(row=0, column=2)

entry2 = Entry(root)
entry2.grid(row=0, column=3)

button2 = Button(root, text="Decrypt")
button2.grid(row=1, column=2)

mainloop()