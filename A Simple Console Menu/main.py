def print_menu():
    print("Meniu \n 1.Citirea unei liste de numere intregi \n 2.Gasirea secventei de lungime maxima a oricaror doua elemente consecutive difera printr-un numar prim \n 3. Gasirea secventei de lungime maxima a elementelor ce apartin intervalului [0,10] \n 4. Iesire din aplicatie")
 
crt_list=[]

def read_list():
    nr=int(input("Numarul de numere intregi: "))
    elems = input().split(" ")
    for elem in elems:
        crt_list.append(int(elem))

def prim(n):
    if n<2:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,n//2,2):
            if n%i==0:
                return False
    return True

def prop_1(lst):
    x=0
    maxi=0
    list=[]
    sol=[]
    list.append(lst[0])
    for i in range(1,len(lst)):
        if prim(abs(lst[i]-lst[i-1]))==True:
            x+=1
            list.append(lst[i])
            if x>maxi:
                maxi=x
                sol = list.copy()
        else:
            x=0
            list.clear()
            list.append(lst[i])        
    return sol
      
def zece(lst):
    x=-1
    maxi=0
    list=[]
    sol=[]
    for i in range(0,len(lst)):
        if lst[i] in range(0,11):
            x+=1
            list.append(lst[i])
            if x>maxi:
                maxi=x
                sol = list.copy()
        else:
            x=0
            list.clear()        
    return sol

def prop_3(lst):
    lista=[]
    sol=[]
    a=lst[0]
    b=0
    c=0
    lista.append(a)
    for i in range(1,len(lst)):
        if a!=lst[i] and b==0:
            b=lst[i]
            lista.append(b)
        elif a!=lst[i] and b!=lst[i] and c==0:
            c=lst[i]
            lista.append(c)
        elif lst[i]!=a and lst[i]!=b and lst[i]!=c:
            if len(lista)>len(sol):
                sol = lista.copy()
            lista.clear()
            lista.append(b)
            lista.append(c)
            a=b
            b=c
        else:
            lista.append(lst[i])
    return sol


def test_prop_3():
    assert prop_3([12, 13, 14, 15]) == [12, 13, 14]
    assert prop_3([11, 11, 14, 16, 23]) ==  [11, 11, 14, 16]
    

def run():
    while True:
        print_menu()
        opt=int(input("Optiunea selectata este: "))
        if opt==1:
            # citire lista
            read_list()
        elif opt==2:
            # gasirea secventei de lungime maxima a oricaror doua elemente consecutive difera printr-un numar prim
            if len(prop_1(crt_list)) == 0:
                print("Nu exista elemente consecutive care respecta aceasta proprietate")
            else:
                print(prop_1(crt_list))
        elif opt==3:
            # gasirea secventei de lungime maxima a elementelor ce apartin intervalului [0,10]
            if  len(zece(crt_list)) == 0:
                print("Nu exista elemente ce apartin intervalului [0,10]")
            else:
                print(zece(crt_list))
        elif opt==4:
            # iesire din meniul principal
            return

test_prop_3()

#run()
