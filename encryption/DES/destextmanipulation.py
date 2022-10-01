def to_8bit(text):
    input=[]
    for i in range(int(len(text)/8)):
        j=i*8
        input.append(text[j:j+8])
    return input

def to_string(bin):
    return "".join([chr(int(binary, 2)) for binary in bin.split(" ")])

def tolist(key):
    x=[i for a,i in enumerate(key)]
    return x

def tostr(text):
    c=''
    for i in text:
        c+=i
    return c

def numberedlist(n):
    l=[]
    for i in range(1,n+1):
        l.append(i)
    return l

