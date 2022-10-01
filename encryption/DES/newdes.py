import random as rd
import desgenkey as deskey
import desplaintext as desplain
import destextmanipulation as dtm
import dessbox as dsbox
import desfistelcipher as fistel
from tkinter import *
#permutation of ip

cipher=[[]]

def permute(block,permutation):
    clist=[]
    num=dtm.numberedlist(len(block))
    print(num)
    for i in range(len(block)):
        value=num.index(permutation[i])
        clist.append(block[value])
    return clist


IntialP=[58,50,42,34,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]
InverseP=[40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

def encryption(message):
    blocks=desplain.genblocks(message)
    print(dtm.tostr(blocks))
    for i in range(len(blocks)):
        l=permute(dtm.tostr(blocks[i]),IntialP)
        cipher.append(permute(fistel.fistel_cipher(dtm.tostr(l)),InverseP))
    return (dtm.tostr(dsbox.mattolist(cipher)))


def actual():
    message=entry.get()     
    str=''
    ciphertext=(dtm.to_8bit(encryption(message)))
    for i in range(len(ciphertext)):
        str+=(dtm.to_string(ciphertext[i]))
    label=Label(frame,text="Encryption:",font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=0)
    label=Label(frame,text=str,font=(20,20) ,padx=10,pady=10)
    label.grid(row=3,column=1)
    return str




caesarci=Tk()

label1=Label(caesarci,text="DES",font=(30,30) ,padx=10,pady=10)
label1.pack(padx=30,pady=30)

frame=LabelFrame(caesarci,text="",padx=60,pady=60)
frame.pack(padx=30,pady=30)

label=Label(frame,text="Enter message",font=(20,20) ,padx=10,pady=10)
label.grid(row=1,column=0)

entry=Entry(frame,font=(20,20))
entry.grid(row=1,column=1)

button=Button(frame,text="Encrypt",command=actual)
button.grid(row=1,column=2)


caesarci.mainloop()