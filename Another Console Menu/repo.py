from domain import get_parte_imaginara, get_parte_reala
import math

def generate_numbers():
    """
    Genereaza o list predefinita (un dictionar predefinit)
    :return: un dictionar de numere complexe
    :rtype: dict
    """
#    return [{'parte.reala':5,'parte.imaginara':2},
#            {'parte.reala':1,'parte.imaginara':2},
#            {'parte.reala':2,'parte.imaginara':1},
#            {'parte.reala':5,'parte.imaginara':2},
#            {'parte.reala':8,'parte.imaginara':6},
#            {'parte.reala':3,'parte.imaginara':2},
#            {'parte.reala':3,'parte.imaginara':3},
#            {'parte.reala':1,'parte.imaginara':9},
#            {'parte.reala':0,'parte.imaginara':10},
#            {'parte.reala':5,'parte.imaginara':2}
#            ]
    return [create_number(5,2),
            create_number(1,2),
            create_number(2,1),
            create_number(5,2),
            create_number(8,6),
            create_number(3,2),
            create_number(3,3),
            create_number(2,1),
            create_number(1,9),
            create_number(0,10),
            create_number(5,2)
            ]

def add_number_to_list(number_list, number):
    """
    Adauga un numar complex la sfarsitul listei
    :param number_list: lista de numere
    :type number_list: list
    :param number: numarul care trebuie adaugat
    :type number: dict
    :return: -; lista de numere se modifica prin adaugarea numarului dat
    :rtype: -;
    """
    number_list.append(number)
    return number_list

def create_number(parte_reala, parte_imaginara ):
    """
    Creeaza numar complex
    :param parte.reala: partea reala a numarului
    :type parte.reala: int
    :param parte.imaginara: partea imaginara a numarului
    :type parte.imaginara: int
    :return: numar creat
    :rtype: dict(chei: parte.reala, parte.imaginara)
    """
#    return {'parte.reala': parte_reala, 'parte.imaginara': parte_imaginara}
    return [parte_reala,parte_imaginara]

def adauga_numar1(number_list,poz,number):
    """
    Adauga un numar complex (partea reala + partea imaginara) la sfarsitul dictionarului de numere complexe
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :param poz: pozitia pe care se va insera un element nou
    :type poz: int
    :param number: numarul ce va fi inserat in lista
    :type number: dict
    :return: lista de numere dupa ce s-a adaugat un numar pe o pozitie data
    :rtype: list (of dicts)
    """
    #number_list.slice(poz+1)
    left = number_list[:poz]
    right = number_list[poz:]
    number_list = left + [number] + right
    return number_list

def remove_number_from_list(number_list, pozitie):
    """
    Elimina din lista, numarul de pe o pozitie data
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :param pozitie: pozitia numarului care va fi sters
    :type pozitie: int
    :return: lista numerelor fara numarul de pe pozitia data
    :rtype: list (of dicts)
    """
    new_list=[number_list[i] for i in range(0, len(number_list)) if i!=pozitie]
    return new_list

def sterge_interval_pozitii_parte_reala(number_list,poz1,poz2):
    """"
    Sterge partile reale ale elementelor de pe un interval de pozitii
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista partilor reale rezultata dupa stergerea elementelor de pe un interval de pozitii
    :rtype: list
    """
    sol=[]
    for i in range(0,len(number_list)):
        if i<poz1 or i>poz2:
            sol.append(get_parte_reala(number_list[i]))
    return sol

def sterge_interval_pozitii_parte_imaginara(number_list,poz1,poz2):
    """
    Sterge partile imaginare ale elementelor de pe un interval de pozitii
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista partilor imaginare rezultata dupa stergerea elementelor de pe un interval de pozitii
    :rtype: list
    """
    sol=[]
    for i in range(0,len(number_list)):
        if i<poz1 or i>poz2:
            sol.append(get_parte_imaginara(number_list[i]))
    return sol

def inlocuieste_numar1(number_list,pr1,pi1,pr2,pi2):
    """
    Inlocuieste toate aparitiile unui numar complex cu un alt numar complex
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :param pr1: partea reala a numarului care va fi inlocuit
    :type pr1: int
    :param pi1: partea imaginara a numarului care va fi inlocuit
    :type pi1: int
    :param pr2: partea reala a numarului introdus
    :type pr2: int
    :param pi2: partea imaginara a numarului introdus
    :type pi2: int
    """
    number1=create_number(pr2,pi2)
    for i in range(0,len(number_list)):
        if get_parte_reala(number_list[i])==pr1 and get_parte_imaginara(number_list[i])==pi1:
            number_list[i]=number1
    return number_list

def interval_pozitii1(number_list,poz1,poz2):
    """
    Creeaza o noua lista cu partile imaginare a numerelor complexe aflate intre cele doua pozitii
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :param poz1: pozitia de inceput
    :type poz1: int
    :param poz2: pozitia de sfarsit
    :type poz2: int
    :return: lista cu partile imaginare
    :rtype: list
    """
    sol=[]
    for i in range(0, len(number_list)):
        if i>=poz1 and i<=poz2:
            sol.append(get_parte_imaginara(number_list[i]))
    return sol

def modul(number):
    """
    Returneaza modulul unui numar complex
    :param number: numarul complex
    :type number: dict
    :retun: modulul
    :rtype: int
    """
    return int(math.sqrt(get_parte_reala(number)**2+get_parte_imaginara(number)**2))

def modul_mai_mic_decat_10_parte_reala(number_list):
    """
    Returneaza lista partilor reale a numerelor complexe al caror modul este mai mic decat 10
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista partilor reale
    :rtype: list
    """
    sol=[]
    for number in number_list:
        if modul(number)<10:
            sol.append(get_parte_reala(number))
    return sol

def modul_mai_mic_decat_10_parte_imaginara(number_list):
    """
    Returneaza lista partilor imaginare a numerelor complexe al caror modul este mai mic decat 10
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista partilor imaginare
    :rtype: list
    """
    sol=[]
    for number in number_list:
        if modul(number)<10:
            sol.append(get_parte_imaginara(number))
    return sol

def modul_egal_10_parte_reala(number_list):
    """
    Returneaza lista partilor reale a numerelor complexe al caror modul este egal cu 10
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista partilor reale
    :rtype: list
    """
    sol=[]
    for number in number_list:
        if modul(number)==10:
            sol.append(get_parte_reala(number))
    return sol

def modul_egal_10_parte_imaginara(number_list):
    """
    Returneaza lista partilor imaginare a numerelor complexe al caror modul este egal cu 10
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista partilor imaginare
    :rtype: list
    """
    sol=[]
    for number in number_list:
        if modul(number)==10:
            sol.append(get_parte_imaginara(number))
    return sol

def suma(number_list,poz1,poz2):
    """
    Suma numerelor dintr-o subsecventa data (se da pozitia de inceput si cea de sfarsit)
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :param poz1: pozitia de inceput
    :type poz1: int
    :param poz2: pozitia de sfarsit
    :type poz2: int
    :return: suma partilor reale (a) si imaginare (b) a numerelor aflate in subsecventa
    :rtype: a-int; b-int
    """
    a=0
    b=0
    for i in range(0,len(number_list)):
        if i>=poz1 and i<=poz2:
            a=a+get_parte_reala(number_list[i])
            b=b+get_parte_imaginara(number_list[i])
    return a,b

def produs(number_list,poz1,poz2):
    """
    Produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :param poz1: pozitia de inceput
    :type poz1: int
    :param poz2: pozitia de sfarsit
    :type poz2: int
    :return: produsul numerelor complexe aflate in aceasta subsecventa data, respectiv partile reale si imaginare a produsului final
    :rtype: a-int; b-int
    """
    a=1
    b=1
    for i in range(0,len(number_list)):
        if i>=poz1 and i<=poz2:
            ca=a
            cb=b
            a=ca*get_parte_reala(number_list[i])-cb*get_parte_imaginara(number_list[i])
            b=ca*get_parte_imaginara(number_list[i])+cb*get_parte_reala(number_list[i])
    return a,b

def sortare_list(number_list):
    """
    Returneaza lista sortată descrescător după partea imaginara
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista sortata descrescator in functie de partea imaginara
    :rtype: list (of dicts) 
    """
    return sorted(number_list, reverse=True, key=get_parte_imaginara)

def prim(x):
    """
    Verifica daca un numar este un numar prim
    :param x: numarul care vrem sa vedem daca e prim
    :type x: int
    :return: adevarat/fals in functie de numar
    :rtype: bool
    """
    if x<2:
        return False
    elif x==2:
        return True
    elif x%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(x)),2):
            if x%i==0:
                return False
    return True

def filtrare_parte_reala_prim(number_list):
    """
    Filtrare parte reala prim -elimină din listă numerele complexe la care partea reala este prim
    :param number_list: lista de numere complexe
    :type number_list: list (of dicts)
    :return: lista cu numerele a caror parte reala nu este prima
    :rtype: list
    """
    sol=[]
    for number in number_list:
        if prim(get_parte_reala(number))==False:
            sol.append(number)
    return sol

def filtrare_modul(number_list,x,opt):
    """
    Filtrare modul -elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista rezultata dupa ce se face operatia ceruta
    :rtype: list (of dicts)
    """
    sol=[]
    if opt==1:
        for number in number_list:
            if modul(number)>=x:
                sol.append(number)
        return sol
    elif opt==2:
        for number in number_list:
            if modul(number)!=x:
                sol.append(number)
        return sol
    elif opt==3:
        for number in number_list:
            if modul(number)<=x:
                sol.append(number)
        return sol

def setup_show_manager(add_predefined):
    """
    Initializeaza un obiect de tip show manager
    :param add_predefined: indicator pentru adaugarea serialelor predefinite in lista curenta de seriale
            daca add_predefined==True se incepe cu o lista populata de seriale predefinite, altfel cu o lista
            goala de seriale
    :type add_predefined: bool
    :return: o lista cu 2 pozitii care reprezinta show_manager-ul, show_manager[0] - lista curenta de seriale
                    show_manager[1] = undo_list
    :rtype: list
    """
    if add_predefined:
        crt_show_list = generate_numbers()
    else:
        crt_show_list = []

    undo_list = []
    return [crt_show_list, undo_list]








