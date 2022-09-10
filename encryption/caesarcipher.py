from cProfile import label
from distutils.text_file import TextFile
from turtle import color
import numpy as np
from tkinter import *

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caesar=np.roll(alphabets,3)
key=caesar.tolist()


def remove(string):
    return string.replace(" ","")

def encryption():
    txt=(entry.get())
    text=remove(txt)
    cipher=''
    for i in range(len(text)):
        index=alphabets.index(text[i])
        cipher=cipher+caesar[index]
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)
    return cipher


def decryption():
    text=encryption()
    plaintext=''
    for i in range(len(text)):
        index=key.index(text[i])
        plaintext=plaintext+alphabets[index]
    label=Label(frame,text="Decryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=0)
    label=Label(frame,text=plaintext,font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=1)

caesarci=Tk()

result=StringVar

label1=Label(caesarci,text="Caesar Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(caesarci,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)

button=Button(frame,text="Decrypt",command=decryption)
button.grid(row=1,column=3)

caesarci.mainloop()


