from tkinter import *

def remove(string):
    return string.replace(" ","")

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def encryption():
    msg=entry.get()
    key=int(keyy.get())
    cipher=[]
    for i in range(key):
        c=''
        c=msg[i::key]
        cipher.append(c)
    ciphertext=''
    for i in cipher:
        ciphertext+=i
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=ciphertext,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)
    return cipher


def decryption():
    msg=encryption()
    key=int(keyy.get())
    plaintext=''
    plain=[]
    for i in range(key):
        c=''
        c=msg[i::key]
        plain.append(c)
    print(plain)
    for i in plain:
        plaintext=''.join(str(e) for e in plain)
    label=Label(frame,text="Decryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=0)
    label=Label(frame,text=plaintext,font=(20,20) ,padx=10,pady=10)
    label.grid(row=4,column=1)


railfence=Tk()

label1=Label(railfence,text="Railfence Cipher",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(railfence,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

label=Label(frame,text="Enter integer key",font=(20,20) ,padx=10,pady=10)
label.grid(row=2,column=0)

keyy=Entry(frame,font=(20,20))
keyy.grid(row=2,column=1)

button=Button(frame,text="Encrypt",command=encryption)
button.grid(row=1,column=2)

button=Button(frame,text="Decrypt",command=decryption)
button.grid(row=1,column=3)

railfence.mainloop()