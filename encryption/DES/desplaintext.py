import random as rd
alphabets=['0','1']

def remove(string):
    return string.replace(" ","")

def to_binary(text):
    return ''.join(format(ord(i),'08b')for i in text)


def add_dummy(text,add):
    for i in range(0,add):
        dummy=''.join(rd.choices(alphabets,k=1))
        text=text+dummy
    return text

def genplain(message):
    mesg=remove(str(message))
    msg=to_binary(mesg)
    i=0
    n=len(msg)
    if n<64:
        plaintext=add_dummy(msg,(64-n))
        return plaintext
    elif n==64*i:
            plaintext=msg[0:64*i]
            i+=1
            return plaintext
    elif n==64:
        plaintext=msg
        return plaintext
    elif n>64:
        add=n%64
        div=int(n/64)
        plain=msg[0:((64*div)+add)]
        addon=add_dummy(plain,((64*div)-add))
        plaintext=addon
        return plaintext
    else:
        msg=input("Enter another message")
        plaintext=genplain(msg)
        return plaintext

def genblocks(message):
    plain=genplain(message)
    input=[]
    for i in range(int(len(plain)/64)):
        j=i*64
        input.append(plain[j:j+64])
    return input