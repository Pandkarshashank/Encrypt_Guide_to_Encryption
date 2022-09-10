from cmath import sqrt
import math
import random as rd
import string
import numpy as np
from tkinter import *

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def remove(string):
    return string.replace(" ","")

def add_dummy(text):
    n=len(text)
    sr=math.floor(math.sqrt(n))
    add=(sr+1)*(sr+1)
    for i in range(n,add):
        dummy=''.join(rd.choices(alphabets,k=1))
        text=text+dummy
    z=sqrt(add)
    return text,int(z.real)

def inputkey(msg):
    keyvalue={}
    txt,siz=add_dummy(msg)
    l=rd.sample(range(0,siz),siz)
    for i in range(siz):
        keyvalue.update({i:l[i]})
    return keyvalue

def colform(text,size):
    col=[]
    col=np.reshape(text,(size,size))
    return col

def encryption():
    text=entry.get()
    key=inputkey(entry.get())
    plain,size=add_dummy(text)
    plaintext=list(plain)
    col=colform(plaintext,size)
    cipher=[]
    print(col,key)
    l=[]
    for i in range(size):
        l.append(key.get(i))
    for i in l:
        cipher.append(col[:,l[i]])
    c=''
    for i in cipher:
        for j in i:
            c=c+j
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=c,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)


columnar=Tk()

label1=Label(columnar,text="Columnar Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(columnar,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)


columnar.mainloop()






