def listmaker():
    n=int(input("How many elements do you want in your list? : "))
    k=0
    l1=[]
    for k in range(n):
        k+=1
        b=str(k)
        if k==1:
            f='st'
        elif k==2:
            f='nd'
        elif k==3:
            f='rd'
        else:
            f='th'
        ele=input("Enter the "+b+f+" element to add to the list: ")
        l1.append(ele)
    return l1

def dictionarymaker(ch):
    Dictionary={}
    n=int(input("How many entries do you want in your dictionary (key-value pairs)?:  "))
    k=0
    for k in range(n):
        key=input("Create key:")
        val=input("Enter value to be assigned to the key: ")
        Dictionary[key]=val
    print(Dictionary)
    keys=Dictionary.keys()
    values=Dictionary.values()
    if ch =='keys':
        return keys
    elif ch=='values':
        return values
    elif ch=='dict':
        return Dictionary
    else:
        return null


def tuplemaker():
    n=int(input("How many elements do you want in your tuple? : "))
    k=0
    t1=()
    for k in range(n):
        k+=1
        b=str(k)
        if k==1:
            f='st'
        elif k==2:
            f='nd'
        elif k==3:
            f='rd'
        else:
            f='th'
        ele=input("Enter the "+b+f+" element to add to the list: ")
        t1=t1+(ele,)
    return t1
