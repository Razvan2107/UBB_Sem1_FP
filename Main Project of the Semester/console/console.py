from termcolor import colored
from exceptions.exceptions import ValidationException,DuplicateIDException,ClientNotFoundException,BookNotFoundException,Inchiriere_ReturnareAlreadyAssignedException
#from sort import myFunc

class Console:
   
    def __init__(self,srv_books,srv_customers,srv_hires_returns):
        """
        Initializeaza consola
        :type srv_books: CarteService
        :type srv_customers: ClientService
        :type srv_hires_returns: Inchirieri_ReturnariService
        """
        self.__srv_books=srv_books
        self.__srv_customers=srv_customers
        self.__srv_hires_returns=srv_hires_returns
    
    #Book
    def __print_all_books(self):
        """
        Afiseaza toate cartile disponibile
        """
        book_list=self.__srv_books.get_all_books()
        if len(book_list)==0:
            print(colored('Nu exista carti in lista!','red'))
        else:
            print('Lista de carti este:')
            for book in book_list:
                print('Id carte: ',colored(book.getId(),'cyan'),';- Titlu carte: ',colored(book.getTitlu(),'cyan'),';- Descriere: ',colored(book.getDescriere(),'cyan'),';- Autor: ',colored(book.getAutor(),'cyan'),';- Status: ',colored(book.getStatus(),'cyan'),';- Numar: ',colored(book.getNumar(),'cyan'))

    def __add_book(self):
        """
        Adauga o carte cu datele citite de la tastatura
        """
        try:
            id=int(input("Id-ul cartii este: "))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre!", 'red'))
        try:
            titlu=input("Titlul cartii: ")
            descriere=input("Descrierea cartii este: ")
            autor=input("Autorul cartii este: ")
            status=0
            numar=0
            added_book=self.__srv_books.add_book(id,titlu,descriere,autor,status,numar)
            print(colored('Cartea ','green')+colored(added_book.getTitlu(),'cyan')+colored(' (','green')+colored(added_book.getAutor(),'cyan')+colored(') a fost adaugata cu succes!','green'))
        except ValidationException as ve:
            print(colored(str(ve),'red'))
        except DuplicateIDException as e:
            print(colored(str(e),'red'))

    def __delete_book(self):
        """
        Sterge o carte dupa id-ul citit de la tastatura
        """
        try:
            id=int(input('Id-ul cartii care se va sterge: '))
            deleted_book=self.__srv_books.delete_book(id)
            print(colored('Cartea ','green')+colored(deleted_book.getTitlu(),'cyan')+colored(' (','green')+colored(deleted_book.getAutor(),'cyan')+colored(') a fost stearsa cu succes (Id=','green')+colored(deleted_book.getId(),'cyan')+colored(')!','green'))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre!",'red'))            
        except BookNotFoundException as ve:
            print(colored(str(ve),'red'))

    def __find_book_id(self):
        """
        Cauta o carte dupa id-ul citit de la tastatura
        """
        try:
            id=int(input('Id-ul cartii cautate este: '))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre!",'red'))
            return
        
        try:
            found_book=self.__srv_books.find_book(id)
            print(colored('Cartea ','green')+colored(found_book.getTitlu(),'cyan')+colored(' (','green')+colored(found_book.getAutor(),'cyan')+colored(') a fost gasita cu succes (Id=','green')+colored(found_book.getId(),'cyan')+colored(')!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __update_book(self):
        try:
            id=int(input('Id-ul cartii care va fi modificate: '))
            titlu=input("Titlul cartii: ")
            descriere=input("Descrierea cartii: ")
            autor=input("Autorul cartii: ")
            status=0
            numar=0
            modified_book=self.__srv_books.update_book(id,titlu,descriere,autor,status,numar)
            print(colored('Cartea ','green')+colored(modified_book.getTitlu(),'cyan')+colored(' (','green')+colored(modified_book.getAutor(),'cyan')+colored(') a fost modificat cu succes!','green'))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre!",'red'))
        except ValidationException as ve:
            print(colored(str(ve), 'red'))
        except BookNotFoundException as e:
            print(colored(str(e),'red'))

    def __random_book(self):
        try:
            x=int(input("Numarul de generari random este: "))
        except ValueError:
            print(colored('Numarul trebuie sa fie un numar natural!','red'))

        book_list=self.__srv_books.generate_random_books_service(x)
        print('Lista de carti este:')
        for book in book_list:
            print('Id carte: ',colored(book.getId(),'cyan'),'- Titlu carte: ',colored(book.getTitlu(),'cyan'),'- Descriere: ',colored(book.getDescriere(),'cyan'),'- Autor: ',colored(book.getAutor(),'cyan'))

    #Customer
    def __print_all_customers(self):
        """
        Afiseaza toti clientii
        """
        customer_list=self.__srv_customers.get_all_customers()
        if len(customer_list)==0:
            print(colored('Nu exista clienti in lista!','red'))
        else:
            print('Lista de clienti este:')
            for customer in customer_list:
                print('Id client: ',colored(customer.getId(),'cyan'),';- Nume client: ',colored(customer.getNume(),'cyan'),';- Cnp client: ',colored(customer.getCnp(),'cyan'))
    
    def __add_customer(self):
        """
        Adauga un client cu datele citite de la tastatura
        """
        try:
            id=int(input("Id-ul clientului este: "))
        except ValueError:
            print(colored('Id-ul clientului trebuie sa fie un numar care are minim 3 cifre.','red'))
            return
        
        nume=input("Numele clientului este: ")
        
        try:
            cnp=int(input("Cnp-ul clientului este: "))
        except ValueError:
            print(colored("Cnp-ul clientului trebuie sa fie un numar care are exact 13 cifre.",'red'))

        try:
            added_customer=self.__srv_customers.add_customer(id,nume,cnp)
            print(colored('Clinetul ','green')+colored(added_customer.getNume(),'cyan')+colored(' (','green')+colored(added_customer.getCnp(),'cyan')+colored(') a fost adaugat cu succes.','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))
    
    def __delete_customer(self):
        """
        Sterge un client dupa id-ul citit de la tastatura
        """
        try:
            id=int(input('Id-ul clientului care se va sterge: '))
        except ValueError:
            print(colored("Id-ul clientului trebuie sa fie un numar care are minim 3 cifre!",'red'))
            return
            
        try:
            deleted_customer=self.__srv_customers.delete_customer(id)
            print(colored('Clientul ','green')+colored(deleted_customer.getNume(),'cyan')+colored(' (','green')+colored(deleted_customer.getCnp(),'cyan')+colored(') a fost sters cu succes (Id=','green')+colored(deleted_customer.getId(),'cyan')+colored(')!','green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __find_customer_id(self):
        """
        Cauta un client dupa id-ul citit de la tastatura
        """
        try:
            id=int(input('Id-ul clientului cautat este: '))
        except ValueError:
            print(colored("Id-ul clientului trebuie sa fie un numar care are minim 3 cifre!",'red'))
            return
        
        try:
            found_customer=self.__srv_customers.find_customer(id)
            print(colored('Clientul ','green')+colored(found_customer.getNume(),'cyan')+colored(' (','green')+colored(found_customer.getCnp(),'cyan')+colored(') a fost gasit cu succes (Id=','green')+colored(found_customer.getId(),'cyan')+colored(')!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __update_customer(self):
        try:
            id=int(input('Id-ul clientului care va fi modificat: '))
        except ValueError:
            print(colored("Id-ul clientului trebuie sa fie un numar care are minim 3 cifre!",'red'))
            return

        nume=input("Numele clientului: ")
        try:
            cnp=int(input("Cnp-ul clientului: "))
        except ValueError:
            print(colored("Cnp-ul trebuie sa fie un numar care are exact 13 cifre!",'red'))

        try:
            modified_customer=self.__srv_customers.update_customer(id,nume,cnp)
            print(colored('CLientul ','green')+colored(modified_customer.getNume(),'cyan')+colored(' (','green')+colored(modified_customer.getCnp(),'cyan')+colored(') a fost modificat cu succes!','green'))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __random_customer(self):
        try:
            x=int(input("Numarul de generari random este: "))
        except ValueError:
            print(colored('Numarul trebuie sa fie un numar natural!','red'))

        customer_list=self.__srv_customers.generate_random_customers_service(x)
        print('Lista de carti este:')
        for customer in customer_list:
            print('Id client: ',colored(customer.getId(),'cyan'),'- Nume client: ',colored(customer.getNume(),'cyan'),'- Cnp: ',colored(customer.getCnp(),'cyan'))

    #Hire/Return
    def __print_hires(self):
        """
        Afiseaza o lista de inchirieri
        """
        hire_list=self.__srv_hires_returns.get_all_hires()
        if len(hire_list)==0:
            print(colored('Nu exista inchirieri/returnari in lista!','red'))
        else:
            print('Lista de inchirieri este:')
            for hire in hire_list:
                #print(hire)
                if hire.getInchiriere_Returnare()==True:
                    print('Carte: [',colored(hire.getCarte().getTitlu(),'cyan'),'; ',colored(hire.getCarte().getAutor(),'cyan'),'] '
                          'Client: [',colored(hire.getClient().getNume(),'cyan'),'; ',colored(hire.getClient().getCnp(),'cyan'),'] '
                          'Inchiriere: ',colored(hire.getInchiriere_Returnare(),'magenta'))

    def __print_returns(self):
        """
        Afiseaza o lista de inchirieri
        """
        returns_list=self.__srv_hires_returns.get_all_returns()
        if len(returns_list)==0:
            print(colored('Nu exista inchirieri/returnari in lista.','red'))
        else:
            print('Lista de inchirieri este:')
            for returns in returns_list:
                # print(return)
                if returns.getInchiriere_Returnare()==False:
                    print('Carte: [',colored(returns.getCarte().getTitlu(),'cyan'),'; ',colored(returns.getCarte().getAutor(),'cyan'),'] '
                          'Client: [',colored(returns.getClient().getNume(),'cyan'),'; ',colored(returns.getClient().getNume(),'cyan'),'] '
                          'Returnare: ',colored(returns.getInchiriere_Returnare(),'magenta'))

    def __hire(self):
        """
        Adauga o inchiriere la lista de inchirieri
        """
        try:
            id_book=int(input("Id-ul cartii care se va inchiria este: "))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre.",'red'))
            return

        ok=0
        book_list=self.__srv_books.get_all_books()
        if len(book_list)==0:
            raise ValueError('Nu exista carti in lista!')
        else:
            for book in book_list:
                if book.getId()==id_book:
                    ok=1
                    carte=book
        if ok==0:
            raise ValueError('Nu exista carte cu acest id!')
        #elif carte.getStatus()==0:
        elif carte.getStatus()==1:
            raise ValueError('Momentan aceasta carte nu este disponibila si nu poate fi inchiriata!')
        carte.setStatus(1)
        carte.setNumar(int(carte.getNumar())+1)

        try:
            id_customer=int(input("Id-ul clientului care va inchiria cartea: "))
        except ValueError:
            print(colored("Id-ul clientului trebuie sa fie un numar care are minim 3 cifre.",'red'))
        
        ok=0
        customer_list=self.__srv_customers.get_all_customers()
        if len(customer_list)==0:
            raise ValueError('Nu exista clienti in lista!')
        else:
            for customer in customer_list:
                if customer.getId()==id_customer:
                    client=customer
                    ok=1
        if ok==0:
            raise ValueError('Nu exista client cu acest id!')

        try:
            added_hire=self.__srv_hires_returns.hire_book(carte,client,True)
            print(colored('Cartea ','green')+colored(added_hire.getCarte().getTitlu(),'cyan')+colored(' (','green')+colored(added_hire.getCarte().getAutor(),'cyan')+colored(') a fost inchiriata cu succes de catre clientul ','green')+colored(added_hire.getClient().getNume(),'cyan')+colored('!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __return(self):
        """
        Adauga o returnare la lista de returnari
        """
        try:
            id_book=int(input("Id-ul cartii care se va returna este: "))
        except ValueError:
            print(colored("Id-ul cartii trebuie sa fie un numar care are minim 3 cifre.",'red'))
            return

        ok=0
        book_list=self.__srv_books.get_all_books()
        for book in book_list:
            if book.getId()==id_book:
                carte=book
                ok=1
        if ok==0:
            raise ValueError('Nu exista carte cu acest id!')
        elif book.getStatus()==0:
            raise ValueError('Momentan aceasta carte este disponibila si nu poate fi returnata!')
        carte.setStatus(0)

        hire_list=self.__srv_hires_returns.get_all_hires()
        for hire in hire_list:
            if hire.getCarte()==carte:
                inchiriere=hire

        try:
            added_return=self.__srv_hires_returns.return_book(inchiriere.getCarte(),inchiriere.getClient(),False)
            print(colored('Cartea ','green')+colored(added_return.getCarte().getTitlu(),'cyan')+colored(' (','green')+colored(added_return.getCarte().getAutor(),'cyan')+colored(') a fost returnata cu succes de catre clientul ','green')+colored(added_return.getClient().getNume(),'cyan')+colored('!','green'))
        except ValueError as ve:
            print(colored(str(ve),'red'))

    def __raport1(self):
        """
        Afiseaza cele mai inchiriate 10 carti din lista de carti
        """
        books_list=self.__srv_books.get_all_books()

        for i in range(0,len(books_list)-1):
            for j in range(i+1,len(books_list)):
                if books_list[j].getNumar()>books_list[i].getNumar():
                    aux=books_list[i]
                    books_list[i]=books_list[j]
                    books_list[j]=aux

        if len(books_list)>=10:
            for i in range (0,10) and books_list[i].getNumar()!=0:
                print('ID Carte: ',colored(books_list[i].getId(),'cyan'),';- Titlu carte: ',colored(books_list[i].getTitlu(),'cyan'),';- Descriere: ',colored(books_list[i].getDescriere(),'cyan'),';- Autor: ',colored(books_list[i].getAutor(),'cyan'),';- Status: ',colored(books_list[i].getStatus(),'cyan'),';- Numar: ',colored(books_list[i].getNumar(),'cyan'))
        elif len(books_list)==0:
            raise ValueError('Nu exista carti inchiriate!')
        elif len(books_list)>0 and len(books_list)<10:
            for book in books_list: 
                if book.getNumar()!=0:
                    print('Id carte: ',colored(book.getId(),'cyan'),';- Titlu carte: ',colored(book.getTitlu(),'cyan'),';- Descriere: ',colored(book.getDescriere(),'cyan'),';- Autor: ',colored(book.getAutor(),'cyan'),';- Status: ',colored(book.getStatus(),'cyan'),';- Numar: ',colored(book.getNumar(),'cyan'))

    #UI
    def ui(self):
        while True:
            print('Comenzi disponibile:'+'\n'+
                  '1.add_book'+'\n'+ 
                  '2.delete_book'+'\n'+
                  '3.update_book'+'\n'+
                  '4.find_book'+'\n'+ 
                  '5.random_book'+'\n'+ 
                  '6.show_all_books'+'\n'+ 
                  '7.add_customer'+'\n'+ 
                  '8.delete_customer'+'\n'+ 
                  '9.find_customer'+'\n'+ 
                  '10.random_customer'+'\n'+ 
                  '11.update_customer'+'\n'+ 
                  '12.show_all_customers'+'\n'+ 
                  '13.hire_book_by_customer'+'\n'+ 
                  '14.show_all_hires'+'\n'+ 
                  '15.return_book'+'\n'+ 
                  '16.show_all_returns'+'\n'+ 
                  '17.the_most10_rented'+'\n'+ 
                  '18.exit')

            cmd=input('Comanda este: ')
            cmd=cmd.lower().strip()
            if cmd=='add_book':
                self.__add_book()
            elif cmd=='delete_book':
                self.__delete_book()
            elif cmd=='update_book':
                self.__update_book()
            elif cmd=='find_book':
                self.__find_book_id()
            elif cmd=='random_book':
                self.__random_book()
            elif cmd=='show_all_books':
                self.__print_all_books()

            elif cmd=='add_customer':
                self.__add_customer()
            elif cmd=='delete_customer':
                self.__delete_customer()
            elif cmd=='update_customer':
                self.__update_customer()
            elif cmd=='find_customer':
                self.__find_customer_id()
            elif cmd=='random_customer':
                self.__random_customer()
            elif cmd=='show_all_customers':
                self.__print_all_customers()
            
            elif cmd=='hire_book_by_customer':
                self.__hire()
            elif cmd=='show_all_hires':
                self.__print_hires()

            elif cmd=='return_book':
                self.__return()
            elif cmd=='show_all_returns':
                self.__print_returns()

            elif cmd=='the_most10_rented':
                self.__raport1()
            

            elif cmd=='exit':
                print(colored("Goodbye!",'green'))
                return
            
            else:
                print(colored('Comanda invalida!', 'red'))

