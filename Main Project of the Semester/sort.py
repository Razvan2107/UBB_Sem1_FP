from entities import Carte

def insertionSort(n,key):
    for i in range(1, len(n)):
        x=n[i]
        j=i-1     
        while j>=0 and x<n[j]:
            n[j + 1]=n[j]
            j=j-1
        n[j+1]=x
    return n


def sort1(list,key=lambda x: x):
    list_length=len(list)

    if list_length<=1:
        return list

    return insertionSort(list,key)


def combSort(n):
    indice=1.3
    j=len(n)
    ok=True
    i=0
    while j>1 or ok:
        j=int(float(j)/indice)
        ok=False
        i=0
        while j+i<len(n):
            if n[i]>n[i+j]:
                n[i],n[i+j]=n[i+j],n[i]
                ok=True
            i+=1
    return n
