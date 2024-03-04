"""
Se cere dezvoltarea unei aplicatii care prelucreaza numere complexe. Programul gestioneaza o lista de numere complexe si permite efectuarea repetata a mai multor actiuni.

Aplicatia are interfata de tip consola, si ofera urmatoarele functionalitati:

1. Adaugă număr complex la sfârșitul listei
2. Inserare număr complex pe o poziție dată
3. Șterge element de pe o poziție dată
4. Șterge elementele de pe un interval de poziții
5. Înlocuiește toate aparițiile unui număr complex cu un alt număr complex
6. Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența)
7. Tipărește toate numerele complexe care au modulul mai mic decât 10
8. Tipărește toate numerele complexe care au modulul egal cu 10
9. Suma numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)
10. Produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)
11. Tipărește lista sortată descrescător după partea imaginara
12. Filtrare parte reala prim -elimină din listă numerele complexe la care partea reala este prim
13. Filtrare modul -elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat
14. Reface ultima operație (lista de numere revine la numerele ce existau înainte de ultima operație care a modificat lista) -Nu folosiți funcția deepCopy

Se va adauga o optiune pentru printarea listei curente (sau se va printa dupa fiecare operatie).
Se cere folosirea procesului de dezvoltare incrementala bazata pe functionalitati si dezvoltarea dirijata de teste.
"""
from service import *
from repo import *
from ui import *
from domain import *
from tests import *
from termcolor import colored

# Meniul principal
def start():
    crt_number_list=generate_numbers()
    finished=False
    while not finished:
        print_menu()
        option=int(input("Optiunea dumneavoastra este: "))
        if option==1:
            add_number1(crt_number_list)
        elif option==2:
            adauga_numar(crt_number_list)
        elif option==3:
            delete_number(crt_number_list)
        elif option==4:
            sterge_interval_pozitii_ui(crt_number_list)
        elif option==5:
            inlocuieste_numar_ui(crt_number_list)
        elif option==6:
            interval_pozitii_ui(crt_number_list)     
        elif option==7:
            modul_mai_mic_decat_10_ui(crt_number_list)
        elif option==8:
            modul_egal_10_ui(crt_number_list)
        elif option==9:
            suma_ui(crt_number_list)    
        elif option==10:
            produs_ui(crt_number_list)       
        elif option==11:
            sortare_lista_ui(crt_number_list)        
        elif option==12:
            filtrare_parte_reala_prim_ui(crt_number_list)   
        elif option==13:
            filtrare_modul_ui(crt_number_list)       
        elif option==14:
            undo_ui(crt_number_list)
            #for i in range(0,len(crt_number_list)):
            #    print(get_parte_reala(crt_number_list[i]),'+',get_parte_imaginara(crt_number_list[i]),'i')

        else:
            print(colored("Optiunea introdusa este invalida.",'red'))

testall()

start()

def run_menu():
    print(colored("Optiunile care pot fi alese sunt: add, delete, filter, print",'magenta'))
    s=input("Optiunile dumneavostra sunt: ")
    commands=s.split(";")
    for command in commands:
        crt_number_list=generate_numbers()
        splits=command.strip().split(" ")
        name=splits[0].upper().strip()
        args=splits[1:]
        for arg in args:
            arg=arg.strip()
        if name=="ADD":
            try:
                parte_reala=int(args[0])
                parte_imaginara=int(args[1])
            except ValueError:
                print(colored("Partea reala cat si partea imaginara trebuie sa fie un numar real!",'red'))
            number=create_number(parte_reala,parte_imaginara)
            add_number_to_list(crt_number_list,number)
            print_list(crt_number_list)
            print(colored("Numarul s-a adaugat cu succes!",'green'))
        elif name=='DELETE':
            try:
                pozitie=int(args[0])
            except ValueError:
                print(colored("Pozitia numarului trebuie sa fie un numar real!",'red'))
            crt_number_list=remove_number_from_list(crt_number_list,pozitie)
            print_list(crt_number_list)
            print(colored("Numarul s-a sters cu succes!",'green'))
        elif name=='FILTER':
            filtrare_parte_reala_prim_ui(crt_number_list)
        elif name=='PRINT':
            sortare_lista_ui(crt_number_list)

#run_menu()



