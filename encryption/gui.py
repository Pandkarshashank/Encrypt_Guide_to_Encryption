from tkinter import *

def play():
    import playfair

def col():
    import columnar

def cc():
    import caesarcipher

def vig():
    import vignere

def rf():
    import railfence

def mono():
    import monoalphabetic

window=Tk()

window.title("Encrypt")

label=Label(window,text="Welcome to Encrypt!!",font=(30,30),pady=10)
label.pack(padx=30,pady=30)

label=Label(window,text="Guide to Encryption",font=(20,20))
label.pack(padx=30,pady=30)

frame=LabelFrame(window,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

playfair=Button(frame,text="Playfair",font=(15,15),padx=15,pady=15,command=play)
playfair.grid(row=1,column=1)

columnar=Button(frame,text="Columnar",font=(15,15),padx=15,pady=15,command=col)
columnar.grid(row=1,column=2)

caesar=Button(frame,text="Caesar Cipher",font=(15,15),padx=15,pady=15,command=cc)
caesar.grid(row=1,column=3)

vignere=Button(frame,text="Vignere",font=(15,15),padx=15,pady=15,command=vig)
vignere.grid(row=1,column=4)

railfence=Button(frame,text="Rail Fence",font=(15,15),padx=15,pady=15,command=rf)
railfence.grid(row=1,column=5)

monoalphabetic=Button(frame,text="Monoalphabetic",font=(15,15),padx=15,pady=15,command=mono)
monoalphabetic.grid(row=1,column=6)


window.mainloop()