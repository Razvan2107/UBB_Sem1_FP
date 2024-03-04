from entities import Tractor
from repo import TractorFileRepo
from service import TractorService
from termcolor import colored

class Console:
    def __init__(self,srv_trucks):
        """
        Initializam consola
        :type srv_trucks: TractorService
        """
        self.__srv=srv_trucks

    def __store_trucks(self):
        """
        Adauga un tractor in lista de tractoare
        """
        try: 
            id=int(input("Id-ul tractorului este: "))
        except ValueError:
            print("Id-ul trebuie sa fie un numar!")

        denumire=input("Denumirea tractorului este: ")

        try:
            pret=int(input("Pretul tractorului este: "))
        except ValueError:
            print("Pretul tractorului trebuie sa fie un numar: ")

        model=input("Modelul tractorului este: ")
        data=input("Data la care expira revizia tractorului este: ")

        try:
            tractor_adaugat=self.__srv.store_trucks(id,denumire,pret,model,data)
            print(colored("Tractorul ",'green')+colored(denumire,'cyan')+colored(" a fost adaugat cu succes!",'green'))
        except ValueError:
            print(colored("Acest id sau aceasta denumire exista deja!",'red'))

    def __delete_truck(self):
        """
        Sterge un tractor din lista de tractoare
        """
        try:
            cifra=int(input("Cifra dupa care se va face stergerea este: "))
        except ValueError:
            print(colored("Cifra trebuie sa fie un numar!",'red'))

        if cifra<0 or cifra>9:
            raise ValueError(colored("Cifra nu e cifra!",'red'))

        try:
            self.__srv.delete_truck(cifra)
            print(colored("Tractorul a fost sters cu succes!",'green'))
            print(colored("Numarul de tractoare sterse: 1",'green'))
        except ValueError:
            print(colored("Nu exista tractor cu aceasta cifra in pretul acestuia!",'red'))

    def ui(self):
        while True:
            print('\n'+
                'Comenzi disponibile:'+'\n'
                '1. Adaugare tractor (add_truck)'+'\n'
                '2. Stergere tractor (delete_truck)'+'\n'
                # '3. Filter (filter)'+'\n'
                # '4. Undo la ultima operatie (undo)'+'\n'
                '5. Exit exit (exit)'+'\n'
            )

            cmd=input("Optiunea dumneavoastra este: ")
            cmd.lower().strip()

            if cmd=='add_truck':
                self.__store_trucks()

            elif cmd=='delete_truck':
                self.__delete_truck()

            # elif cmd=='filter':
            #     self.filter()

            # elif cmd=='undo':
            #     self.undo()

            elif cmd=='exit':
                print(colored('La revedere!','green'))
                return

            else:
                print(colored('Comanda invalida!','red'))


