import random as rd
import desgenkey as deskey
import desplaintext as desplain
import destextmanipulation as dtm
import dessbox as dsbox

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','I','J','K','G','H','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']
Expand=[32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

siz=8
ikey=''.join(rd.choices(alpha,k=siz))


def resize(block,permutation):
    clist=[]
    num=dtm.numberedlist(48)
    for i in range(48):
        value=(num.index((permutation[i])))
        clist.append(block[value])
    return clist

def xor(temp,key):
    res=[]
    for i in range(len(key)):
        if temp[i]==key[i]:
            res.append('0')
        else:
            res.append('1')    
    return res

def swap(left,right):
    return right,left

def fun(text,key,i):
    print("text",text,len(text),len(key))
    temp=resize((text),Expand)
    print("temp",temp,len(temp))
    result=xor(temp,key)
    print("result",result,len(result))
    imper=dsbox.mattolist(dsbox.shrink(result,i))
    print("imper",imper,len(imper))
    return imper   

def fistel_cipher(text):
    left=text[:32]
    right=text[32:]
    print("l",left,"\nr",right)
    cipher=''
    keys=deskey.sendlist()
    for i in range(16):
        print("keys",keys[i],len(keys[i]),"\nround",i)
        key=keys[i]
        temp=right
        right=xor(left,fun(right,key,i))
        print("left",left,"\nfun right",fun(right,key,i),"\nxored right",right)
        left=temp
    l=dtm.tostr(left)
    r=dtm.tostr(right)
    l,r=swap(l,r)
    cipher=l+r   
    return cipher 
