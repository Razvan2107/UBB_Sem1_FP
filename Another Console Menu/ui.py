from service import *
from repo import *
from tests import *
from domain import *
from termcolor import colored

def print_menu():
    """
    Se printeaza meniul principal al aplicatiei
    """
    print("1. Adaugă număr complex la sfârșitul listei")
    print("2. Inserare număr complex pe o poziție dată")
    print("3. Șterge element de pe o poziție dată")
    print("4. Șterge elementele de pe un interval de poziții")
    print("5. Înlocuiește toate aparițiile unui număr complex cu un alt număr complex")
    print("6. Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența)")
    print("7. Tipărește toate numerele complexe care au modulul mai mic decât 10")
    print("8. Tipărește toate numerele complexe care au modulul egal cu 10")
    print("9. Suma numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)")
    print("10. Produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)")
    print("11. Tipărește lista sortată descrescător după partea imaginara")
    print("12. Filtrare parte reala prim -elimină din listă numerele complexe la care partea reala este prim")
    print("13. Filtrare modul -elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat")
    print("14. Reface ultima operație (lista de numere revine la numerele ce existau înainte de ultima operație care a modificat lista) -Nu folosiți funcția deepCopy")

def print_menu2():
    """
    Se printeaza meniul principal al aplicatiei
    """
    print("Optiunile disponibile sunt: add, delete, print, filter, exit")


def delete_numbe_ui(number_list):
    """
    Tipareste lista rezultata dupa stergerea unui element de pe o pozitie citita de la tastatura
    :param number_list: lista de numere
    :typr number_list: list (of dicts)
    """
    for number in range(0,len(delete_number(number_list))):
        print(get_parte_reala(number),'+',get_parte_imaginara(number),'i')

def sterge_interval_pozitii_ui(number_list):
    """
    Șterge elementele de pe un interval de poziții
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    """
    try:
        poz1=int(input('Pozitia de inceput este:'))
        poz2=int(input('Pozitia de sfarsit este:'))
        if poz1<=poz2 and poz2<len(number_list):
            for i in range(0,len(number_list)):
                if i<poz1 or i>poz2:
                    print(get_parte_reala(number_list[i]),"+",get_parte_imaginara(number_list[i]),"i")
            print(colored("Elementele de pe pozitiile date s-au sters cu succes!",'green'))
        else:
            print(colored("Pozitiile trebuie sa fie mai mici decat lungimea sirului.",'red'))
    except ValueError:
        print(colored("Pozitia de inceput cat si cea de sfarsit a secventei trebuie sa fie un numar real.",'red'))

def inlocuieste_numar_ui(number_list):
    """
    Printeaza lista de numere complexe dupa ce toate aparitiile unui numar complex au fost inlocuite cu un alt numar complex
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    """
    try:
        ok=0
        parte_reala1=int(input("Partea reala a numarului care va fi inlocuit este:"))
        parte_imaginara1=int(input("Partea imaginara a numarului care va fi inlocuit este:"))
        parte_reala2=int(input("Partea reala a numarului introdus este:"))
        parte_imaginara2=int(input("Partea imaginara a numarului introdus este:"))
        for i in range(0,len(number_list)):
            if get_parte_reala(number_list[i])==parte_reala1 and get_parte_imaginara(number_list[i])==parte_imaginara1:
                print(parte_reala2,"+",parte_imaginara2,"i")
                ok=1
            else:
                print(get_parte_reala(number_list[i]),"+",get_parte_imaginara(number_list[i]),"i")
        if ok==1:
            print(colored("Inlocuirea numarului s-a realizat cu succes!",'green'))
        else:
            print(colored("Nu exista numar complex in lista care sa aiba aceasta parte reala si imaginara!",'red'))
    except ValueError:
        print(colored("Partile reale si imaginare ale numerelor trebuie sa fie numere reale.",'red'))
    
def interval_pozitii_ui(number_list):
    """
    Tipărește partea imaginara pentru numerele din listă
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    """
    try:
        poz1=int(input('Pozitia de inceput este:'))
        poz2=int(input('Pozitia de sfarsit este:'))
        if poz1<=poz2 and poz2<len(number_list):
            for i in range(0,len(number_list)):
                if i>=poz1 and i<=poz2:
                    print(get_parte_imaginara(number_list[i]))
            print(colored("Tiparirea partilor imaginare dintr-o secventa data s-a sters cu succes!",'green'))
        else:
            print(colored("Pozitiile trebuie sa fie mai mici decat lungimea sirului.",'red'))
    except ValueError:
        print(colored("Pozitia de inceput cat si cea de sfarsit a secventei trebuie sa fie un numar real.",'red'))

def modul_mai_mic_decat_10_ui(number_list):
    """
    Tipareste toate numerele complexe care au modul mai mic decat 10
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    """
    ok=0
    for number in number_list:
        if modul(number)<10:
            if ok==0:
                print(colored("Numerele care au modulul mai mic decat 10 sunt:",'green'))
            print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")
            ok=1
    if ok==0:
        print(colored("Nu exista numere care au modulul mai mic decat 10!",'red'))

def modul_egal_10_ui(number_list):
    """
    Tipareste toate numerele complexxe care au modulul egal cu 10
    :param number_list: lista de numere complexe
    :type numebr_list: list (of dicts)
    """
    ok=0
    for number in number_list:
        if modul(number)==10:
            if ok==0:
                print(colored("Numerele care au modulul egal cu 10 sunt:",'green'))
            print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")
            ok=1
    if ok==0:
        print(colored("Nu exista numere care au modulul egal cu 10!",'red'))

def suma_ui(number_list):
    """
    Printeaza suma numerelor dintr-o subsecventa data
    :param number_list: lista de numere complexe
    :type numnber_list: list (of dicts)
    """
    try:
        a=0
        b=0
        poz1=int(input('Pozitia de inceput este:'))
        poz2=int(input('Pozitia de sfarsit este:'))
        if poz1<poz2 and poz2<len(number_list):
            for i in range(0,len(number_list)):
                if i>=poz1 and i<=poz2:
                    a=a+get_parte_reala(number_list[i])
                    b=b+get_parte_imaginara(number_list[i])
            print(colored("Suma partilor reale din subsecventa data este:",'green'),a)
            print(colored("Suma partilor imaginare din subsecventa data este:",'green'),b)
        else:
            print(colored("Pozitiile trebuie sa fie mai mici decat lungimea sirului.",'red'))
    except ValueError:
        print(colored("Pozitia de inceput cat si cea de sfarsit a secventei trebuie sa fie un numar real.",'red'))

def produs_ui(number_list):
    """
    Printeaza produsul numerelor dintr-o subsecventa data
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    """
    try:
        poz1=int(input('Pozitia de inceput este:'))
        poz2=int(input('Pozitia de sfarsit este:'))
        if poz1<poz2 and poz2<len(number_list):
            a=get_parte_reala(number_list[poz1])
            b=get_parte_imaginara(number_list[poz1])
            for i in range(0,len(number_list)):
                if i>poz1 and i<=poz2:
                    ca=a
                    cb=b
                    a=ca*get_parte_reala(number_list[i])-cb*get_parte_imaginara(number_list[i])
                    b=ca*get_parte_imaginara(number_list[i])+cb*get_parte_reala(number_list[i])
            print(colored("Partea reala a produsului elementelor din subsecventa data este:",'green'),a)
            print(colored("Partea imaginara a produsului elementelor din subsecventa data este:",'green'),b)
        else:
            print(colored("Pozitiile trebuie sa fie mai mici decat lungimea sirului.",'red'))
    except ValueError:
        print(colored("Pozitia de inceput cat si cea de sfarsit a secventei trebuie sa fie un numar real.",'red'))

def sortare_lista_ui(number_list):
    """
    Tipărește lista sortată descrescător după partea imaginara
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    """
    v=sortare_list(number_list)
    print(colored("Lista sortata descrescator dupa partea imaginara este:",'green'))
    for i in range(0,len(v)):
        print(get_parte_reala(v[i]),"+",get_parte_imaginara(v[i]),"i")

def filtrare_parte_reala_prim_ui(number_list):
    """
    Printeaza lista filtrata prin partea reala prima -elimină din listă numerele complexe la care partea reala este prim
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    """
    v=filtrare_parte_reala_prim(number_list)
    if len(v)==0:
        print(colored("Nu exista numere complexe a caror parte reala sa fie prima",'red'))
    else:
        print(colored("Lista rezultata dupa eliminarea numerelor complexe a caror parte reala este un numar prim este:",'green'))
        for i in range(0,len(v)):
            print(get_parte_reala(v[i]),"+",get_parte_imaginara(v[i]),"i")

def filtrare_modul_ui(number_list):
    """
    Filtrare modul -elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista rezultata dupa ce se face operatia ceruta
    :rtype: list (of dicts)
    """
    try:
        print("1.Modulul sa fie mai mic decat un numar citit\n2.Modulul sa fie egal cu un numar citit\n3.Modulul sa fie mai mare decat un numar citit")
        x=int(input("Numarul citit este: "))
        opt=int(input("Optiunea dumneavoastra este: "))
        sol=[]
        if opt==1:
            for number in number_list:
                if modul(number)<x:
                    sol.append(number)
            print(colored("Lista rezultata dupa eliminarea numerelor complexe a caror modul este mai < decât un număr dat este:",'green'))
            for number in sol:
                print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")
        elif opt==2:
            for number in number_list:
                if modul(number)!=x:
                    sol.append(number)
            print(colored("Lista rezultata dupa eliminarea numerelor complexe a caror modul este = decât un număr dat este:",'green'))
            for number in sol:
                print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")
        elif opt==3:
            for number in number_list:
                if modul(number)>x:
                    sol.append(number)
            print(colored("Lista rezultata dupa eliminarea numerelor complexe a caror modul este mai > decât un număr dat este:",'green'))
            for number in sol:
                print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")
        else:
            print(colored("Optiune invalida!",'red'))
    except ValueError:
        print(colored("Variabilele trebuie sa fie numere reale!",'red'))

def printare(number_list):
    for number in number_list:
        print(get_parte_reala(number),"+",get_parte_imaginara(number),"i")





