import random as rd
from tkinter import *

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dummy=[]
n=len(alphabets)
def createdummy():
    key=rd.sample(range(0,n),n)
    for i in range(0,n):
        k=key[i]
        dummy.append(alphabets[k])
    return dummy
def remove(string):
    return string.replace(" ","")

def encryption():
    msg=entry.get()
    dummy=createdummy()
    cipher=''
    for i in msg:
        c=alphabets.index(i)
        cipher=cipher+dummy[c]
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)
    return cipher,dummy

def decryption():
    msg,dummy=encryption()
    cipher=''
    for i in msg:
        c=dummy.index(i)
        cipher=cipher+alphabets[c]
    label=Label(frame,text="Decryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=1)
    return cipher

mono=Tk()

label1=Label(mono,text="Monoalphabetic Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(mono,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)

button=Button(frame,text="Decrypt",command=decryption)
button.grid(row=1,column=3)

mono.mainloop()