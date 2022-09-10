import random as rd
from tkinter import *

def remove(string):
    return string.replace(" ","")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vig=[[]]
def genkey():
    text='vig'
    n=len(entry.get())
    for i in range(26):
        m=[]
        for j in range(26):
            key=rd.sample(range(0,26),26)
            for i in range(0,26):
                k=key[i]
                m.append(alphabets[k])
        vig.append(m)
    key=[]
    if n%3==0:
        for i in range(int(n/3)):
            for j in range(3):
                key.append(text[j])
    else:
        for i in range(int(n/3)):
            for j in range(3):
                key.append(text[j])
        k=n%3
        for i in range(k):
            key.append(text[i])
    return key,vig


def indexfind(text):
    return alphabets.index(text)

def changeplain(row,col,matrix):
    return matrix[row][col]

def encryption():
    mseg=entry.get()
    msg=remove(mseg)
    key,vig=genkey()
    cipher=[]
    for i in range(len(msg)):
       r=indexfind(msg[i])
       c=indexfind(key[i])
       cipher.append(changeplain(r-1,c-i,vig))
    ciphertext=''
    for i in cipher:
        ciphertext+=i
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=cipher,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)

vignere=Tk()

label1=Label(vignere,text="Vignere Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(vignere,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)


label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)


button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)


vignere.mainloop()