def bubblesorter(List):
    n=len(List)
    print("list before bubble sorting: ",List)
    for i in range(n-1):
        for j in range(n-i-1):
            if List[j] > List[j+1]:
                List[j],List[j+1]=List[j+1],List[j]
    print("List after bubble sorting: ",List)
    return List

def insertionsorter(List):
    print("list before insertion sorting: ",List)
    for i in List:
        j=List.index(i)
        while j>0:
            if List[j-1]>List[j]:
                List[j-1],List[j]=List[j],List[j-1]
            else:
                break
            j=j-1
    print("list after insertion sorting: ",List)
    return List
