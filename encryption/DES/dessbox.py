import random as rd
import desgenkey as key
import desplaintext as dpt
import destextmanipulation as dtm

sboxes=[]

def mattolist(mat):
    l=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            l.append(mat[i][j])
    return l

def bintodec(bin):
    return int(bin,2)

def dectobin(dec):
    d=bin(dec).replace("0b","")
    if len(d)==2:
        return ('00'+d)
    elif len(d)==1:
        return ('000'+d)
    elif len(d)==23:
        return ('0'+d)
    else:
        return d

def gensbox():
    l=rd.sample(range(0,16),16)
    matrix=[[]]
    for row in range(4):
        matrix.append(l)
    return matrix   


def inputforsbox(text):
    l=[]
    for i in range(0,len(text),6):
        l.append(text[i:i+6])
    return l

def shrink(txt,i):
    for i in range(8):
        sboxes.append(gensbox())
    ans=[[]]
    text=dtm.tolist(inputforsbox(txt))
    print("text",text,len(text))
    for i in range(len(text)):
        sbox=sboxes[i]
        print("sbox1",sbox)
        bits=text[i]
        row=bits[0]+bits[-1]
        col=''.join(bits[1:5])
        r,c=bintodec(row),bintodec(col)
        res=sbox[r+1][c]
        print("r",r+1,"\nc",c)
        print("res",res)
        add=dectobin(res)
        if len(add)<4:
            add='0'+add
        print("add",add)
        l=[]
        for i in range(len(add)):
            l.append(add[i])
        ans.append(l)
    return (ans)



