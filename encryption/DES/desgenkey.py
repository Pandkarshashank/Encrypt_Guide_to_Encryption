import random as rd
import desplaintext as dpt
import destextmanipulation as dtm

alphabets=['0','1']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','I','J','K','G','H','L','M','N','O','P','Q','R','S','T','U','W','X','Y','Z']


def tolist(key):
    x=[i for a,i in enumerate(key)]
    return x

def numberedlist(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)
    return l

def permutestr(block,permutation,num):
    clist=[]
    for i in range(len(block)):
        value=(num.index((permutation[i])))
        clist.append(block[value])
    return clist

def resize(block,permutation,num):
    clist=[]
    for i in range(48):
        value=(num.index((permutation[i])))
        clist.append(block[value])
    return clist

def strto56(key):
    key56=''
    key64=[key[i:i+8]for i in range(0,len(key),8)]
    for i in range(len(key64)):
        key56+=key64[i][:-1]
    return key56

def listto56(key):
    key56=[]
    for i in range(1,len(key)//8+1):
        key.remove(key[i*7])
    for i in key:
        key56.append(i)
    return key56 

PC=[57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,13,5,28,20,12,4]
PC2=[14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

def leftrotate(key,d):
    return key[d:]+key[:d]

def scheduleleftshift(key,index):
    scleftshift=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    keyl=leftrotate(key,scleftshift[index])
    return keyl

def forpc2():
    remove=[]
    numof56=numberedlist(56)
    for i in range(1,len(numof56)):
        if i not in PC2:
            remove.append(i)
    for i in numof56:
        if i in remove:
            numof56.remove(i)
    return numof56

def genkey(key,index):
    num56=listto56(numberedlist(64))
    numof56=forpc2()
    pckey=permutestr(key,PC,num56)
    sckey=scheduleleftshift(pckey,index)
    pc2key=resize(sckey,PC2,numof56)
    return pc2key

def sendlist():
    keys=[]
    siz=64
    ikey=''.join(rd.choices(alphabets,k=siz))
    num=numberedlist(64)
    key56=listto56(tolist(ikey))
    keys.append(genkey(tolist(key56),1))
    for i in range(16):
        key=key56
        keys.append(genkey(key,i))
        key56=key
    return keys







