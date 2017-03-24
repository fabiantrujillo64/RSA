from Tkinter import *
import tkMessageBox
from PIL import Image, ImageTk
from datetime import datetime
from threading import *
import sys
reload(sys)
sys.setdefaultencoding('utf8')

LUT_encryption = dict()
LUT_decryption = dict()

def encrypt_message():
    n =int(entry1.get())
    e =int(entry2.get())
    msg= Text1.get(1.0, END)
    encrypted_msg = ""
    for i in msg:
        if i in LUT_encryption:
          encrypted_msg += LUT_encryption[i]
        else:  
            numerize = ord(i)
            encrypt = pow(numerize, e, n)
            LUT_encryption[i] = unichr(encrypt)
            encrypted_msg += unichr(encrypt)
        Text1.delete(1.0, END)
        Text1.insert(END, encrypted_msg)
    tkMessageBox.showinfo("Message Status", "Encryption Successful")
    
def decrypt_message():
    d = 503
    n =int(entry1.get())
    msg = Text2.get(1.0, END)
    decrypted_msg = ""
    for i in msg:
        if i in LUT_decryption:
            decrypted_msg += LUT_decryption[i]
        else:
            numerize = ord(i)
            decrypt = pow(numerize, d, n)
            LUT_decryption[i] = unichr(decrypt)
            decrypted_msg += unichr(decrypt)
        Text2.delete(1.0, END)
        Text2.insert(END, decrypted_msg)
    tkMessageBox.showinfo("Message Status", "Decryption Successful")

def savefileW():
    n_2 = entry1.get()
    e_2 = entry2.get()
    e_msg = Text1.get(1.0, END)
    f = n_2 + e_2 + ".txt"
    doc =  open(f,"w")
    doc.write(e_msg)
    doc.close()
    
def savefileW2():
    e_msg = Text2.get(1.0, END)
    doc =  open("Decryption.txt","w")
    doc.write(e_msg)
    doc.close()
    
    
def openfileR():
    n_22 = entry1.get()
    e_22 = entry2.get()
    f_2 = n_22 + e_22 + ".txt"
    docu =  open(f_2,"r")
    for line in docu:
        Text1.insert(END, line)
    docu.close()
    
def openfileR2():
    docu =  open("Decryption.txt","r")
    for line in docu:
        Text2.insert(END, line)
    docu.close()
    
    

root = Tk() #gives us a blank canvas object to work with
root.title("RSA Project")
root.config(width = 500, height=500, )

label1 = Label(root, text="n=", anchor=W,)
label1.grid(row=0, column=0)

entry1 = Entry(root)
entry1.grid(row=0, column=1)
entry1.config(width = 40)

button1 = Button(root, text="Encrypt", command = encrypt_message)
button1.grid(row=1, column=0, sticky = N)

label2 = Label(root, text="e=", anchor=W , )
label2.grid(row=0, column=3)

entry2 = Entry(root)
entry2.grid(row=0, column=4)
entry2.config(width = 40)

button2 = Button(root, text="Decrypt", command = decrypt_message)
button2.grid(row=1, column=3, sticky = N)

scrollbar = Scrollbar(root, orient=VERTICAL)
Text1 = Text(root, yscrollcommand=scrollbar.set)
scrollbar.config(command= Text1.yview)
scrollbar.grid(row=1, column=2, rowspan=10, sticky=NS)
Text1.grid(row=1, column=1)
Text1.config(width = 30, height=10)

scrollbar = Scrollbar(root, orient=VERTICAL)
Text2 = Text(root, yscrollcommand=scrollbar.set)
scrollbar.config(command= Text2.yview)
scrollbar.grid(row=1, column=5, rowspan=10, sticky=NS)
Text2.grid(row=1, column=4, sticky= S)
Text2.config(width = 30, height=10)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR)
filemenu.add_separator()
filemenu.add_command(label="Save", command=savefileW)

menubar.add_cascade(label="Encryption", menu=filemenu)

menubar1 = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfileR2)
filemenu.add_separator()
filemenu.add_command(label="Save", command=savefileW2)

menubar.add_cascade(label="Decryption", menu=filemenu)

root.config(menu=menubar)





mainloop()