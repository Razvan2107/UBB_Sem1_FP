from repo import *
from domain import *
from tests import *
from termcolor import colored

def add_number1(number_list):
    """
    Adauga un numar complex (parte reala + parte imaginara) la sfarsitul dictionarul de numere complexe
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista de numere dupa adaugarea elementului
    :rtype: list (of dicts)
    """
    try:
        parte_reala=int(input("Partea reala a numarului:"))
        parte_imaginara=int(input("Partea imaginara a numarului:"))
        number=create_number(parte_reala,parte_imaginara)
        add_number_to_list(number_list, number)
        print_list(number_list)
        print(colored("Numarul s-a adaugat cu succes!",'green'))
    except ValueError:
        print(colored("Partea reala si imaginara trebuie sa fie un numar real.",'red'))

def adauga_numar(number_list):
    """
    Adauga un numar complex (partea reala + partea imaginara) la sfarsitul dictionarului de numere complexe
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista de numere dupa ce s-a adaugat un numar pe o pozitie data
    :rtype: list (of dicts)
    """
    try:
        parte_reala=int(input("Partea reala a numarului:"))
        parte_imaginara=int(input("Partea imaginara a numarului:"))
        number=create_number(parte_reala,parte_imaginara)
        poz=int(input("Pozitia pe care o va ocupa numarul complex este:"))
        for i in range(len(number_list)+1,poz+1):
            number_list[i]=number_list[i-1]
        number_list[poz]=number
        print_list(number_list)
        print(colored("Numarul s-a adaugat cu succes!",'green'))
    except ValueError:
        print(colored("Partea reala si imaginara trebuie sa fie un numar real, iar pozitia pe care se va adauga elementul sa fie naturala si sa fie mai mica decat numarul de elemente al listei de numere complexe.",'red'))

def delete_number(number_list):
    """
    Sterge un element de pe o pozitie citita la tastatura
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista numerelor rezultata dupa stergerea unui element de pe pozitia data
    :rtype: list (of dicts)
    """
    try:
        pozitie=int(input('Pozitia numarului care va fi sters:'))
        number_list=remove_number_from_list(number_list,pozitie)
        print_list(number_list)
        print(colored("Numarul s-a sters cu succes!",'green'))
    except ValueError:
        print(colored("Poztia numarului care va fi sters trebuie sa fie un numar natural si sa fie mai mica decat numarul de elemente al listei de numere complexe.",'red'))
        
def interval_pozitii(number_list):
    """
    Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența)
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista partilor imaginare din intervalul specificat
    :rtype: list
    """
    poz1=int(input('Pozitia de inceput este:'))
    poz2=int(input('Pozitia de sfarsit este:'))
    pozitii_list=interval_pozitii1(number_list,poz1,poz2)
    return pozitii_list

def filtrare_modul_ui(number_list):
    """
    Filtrare modul -elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat
    :param number_list: lista de numere
    :type number_list: list (of dicts)
    :return: lista rezultata dupa ce se face operatia ceruta
    :rtype: list (of dicts)
    """
    print("1. Modulul sa fie mai mic decat un numar citit\n 2. Modulul sa fie egal cu un numar citit\n 3. Modulul sa fie mai mare decat un numar citit")
    x=int(input("Numarul citit este: "))
    opt=int(input("Optiunea dumneavoastra este: "))
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
    else:
        print(colored("Optiune invalida!",'red'))

def print_list(number_list):
    """
    Printeaza lista de numere complexe
    :param number_list: lista numerelor complexe
    :type number_list: list (of dicts)
    """
    for i in range(0,len(number_list)):
        print(get_parte_reala(number_list[i]),'+',get_parte_imaginara(number_list[i]),'i')

def get_undo_list(number):
    return number[1]

def undo(number_list):
    """
    Face undo la ultima operatie de adaugare sau stergere
     :param number_list: obiect de tip show manager
    :type number_list: list (len(number_list)=2, number_list[0] = lista crt de show-uri, number_list[1] = lista de undo
    :return: lista curenta de show-uri revine la starea de dinainte de ultima operatie
    :rtype: -;
    """
    undo_list = get_undo_list(number_list)

    if len(undo_list) == 0:
        raise ValueError("Nu se mai poate face undo.")
    else:
        previous_list = undo_list[-1]

        set_number_list(number_list, previous_list)
        set_undo_list(number_list, undo_list[:-1])

def undo_ui(number_list):
    try:
        undo(number_list)
        print(number_list)
        print(colored("Undo realizat cu succes.", 'green'))
        print_list(number_list)
    except ValueError as ve:
        print(colored(ve, 'red'))


