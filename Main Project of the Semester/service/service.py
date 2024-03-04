from entities.entities import Carte,Client,Inchiriere_Returnare
from validators.validators import CarteValidator,ClientValidator,Inchiriere_ReturnareValidator
from repo.hires_returns.repo_hires_returns import InMemoryRepositoryHires_Returns,Hires_ReturnsFileRepo
from repo.books.repo_books import InMemoryRepositoryBooks,BookFileRepo
from repo.customers.repo_customers import InMemoryRepositoryCustomers,CustomerFileRepo
from randomorg import generate_random_books,generate_random_customers

class CarteService:

    def __init__(self,repo,validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de carti
        :type repo: InMemoryRepositoryBooks
        :param validator: validator pentru verificarea cartilor
        :type validator: CarteValidator
        """
        self.__repo=repo
        self.__validator=validator

    def add_book(self,id,titlu,descriere,autor,status,numar):
        """
        Adauga carte
        :param id: id-ul cartii
        :type id: int
        :param titlu: titlul cartii
        :type titlu: str
        :param descriere: descrierea cartii
        :type descriere: str
        :param autor: autorul cartii
        :type autor: str
        :param status: statusul cartii daca este disponibila pentru a fi inchiriata(0) sau daca este deja inchiriata(1)
        :type status: bool(1/0)
        :param numar: de cate ori a fost inchiriata cartea respectiva
        :type numar:c 
        :return: obiectul de tip Carte creat
        :rtype:-; cartea s-a adaugat in lista
        :raises: ValueError daca cartea are date invalide
        """
        s=Carte(id,titlu,descriere,autor,status,numar)
        self.__validator.validate(s)
        self.__repo.store_books(s)
        return s

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile disponibile
        :return: lista de carti disponibile
        :rtype: list of objects de tip Carte
        """
        return self.__repo.get_all_books()

    def delete_book(self,id):
        """
        Sterge cartea cu id dat din lista
        :param id: id-ul dat
        :type id: int
        :return: cartea stearsa
        :rtype: Carte
        :raises: ValueError daca nu exista carte cu id-ul dat
        """
        return self.__repo.delete_by_id_book(id)

    def update_book(self,id,titlu,descriere,autor,status,numar):
        """
        Modifica datele cartii cu id dat
        :param id: id-ul cartii de modificat
        :type id: int
        :param titlu: noul titlu al cartii
        :type titlu: str
        :param descriere: noua descriere a cartii
        :type descriere: str
        :param autor: noul autor al cartii
        :type autor: str
        :param status: noul status al cartii care va fi 0 ulterior
        :type status: bool(0/1)
        :param numar: noul numar de inchirieri a cartii care va fi 0 ulterior
        :type numar: int
        :return: cartea modificata
        :rtype: Carte
        :raises: ValueError daca noile date nu sunt valide, sau nu exista carte cu id dat
        """
        s=Carte(id,titlu,descriere,autor,status,numar)
        self.__validator.validate(s)
        return self.__repo.update_book(id,s)
    
    def generate_random_books_service(self,x):
        """
        Genreaza random x carti
        :param x: cate obiecte de tip Carte se vor genera random
        :type x: int
        :return: lista de obiecte de tip Carte generate random
        :rtype: list (of objects type Carte)
        """
        return generate_random_books(x)


def test_add_book_service():
    repo= InMemoryRepositoryBooks()
    validator=CarteValidator()
    test_srv=CarteService(repo,validator)

    added_book=test_srv.add_book(123,"Moara cu noroc","Nuvela psihologica","Ioan Slavici",0,0)
    assert (added_book.getId()==123)
    assert (added_book.getTitlu()=="Moara cu noroc")
    assert (added_book.getDescriere()=="Nuvela psihologica")
    assert (added_book.getAutor()=="Ioan Slavici")
    assert (added_book.getStatus()==0)
    assert (added_book.getNumar()==0)

    assert (len(test_srv.get_all_books())==1)

    try:
        added_book=test_srv.add_book(2,"Moara cu noroc","Nuvela psihologica","Ioan Slavici",0,0)
        assert False
    except ValueError:
        assert True

def test_delete_book_service():
    repo=InMemoryRepositoryBooks()
    validator=CarteValidator()
    test_srv=CarteService(repo, validator)

    test_srv.add_book(323,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    deleted_book=test_srv.delete_book(323)

    assert (len(test_srv.get_all_books())==0)
    assert (deleted_book.getTitlu()=='Moara cu noroc')
    assert (deleted_book.getDescriere()=='Nuvela psihologica')
    assert (deleted_book.getAutor()=='Ioan Slavici')
    assert (deleted_book.getStatus()==0)
    assert (deleted_book.getNumar()==0)

    try:
        test_srv.delete_book(223)
        assert False
    except ValueError:
        assert True

def test_get_all_books_service():
    repo=InMemoryRepositoryBooks()
    validator=CarteValidator()
    test_srv=CarteService(repo,validator)

    test_srv.add_book(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    test_srv.add_book(223,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)
    assert (type(test_srv.get_all_books())==list)
    assert (len(test_srv.get_all_books())==2)

def test_update_book_service():
    repo=InMemoryRepositoryBooks()
    validator=CarteValidator()
    test_srv=CarteService(repo, validator)

    test_srv.add_book(123,'Moara','Nuvela psihologica','Ioan Slavici',0,0)
    updated_book=test_srv.update_book(123,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)

    assert (updated_book.getTitlu()=='O scrisoare pierduta')
    assert (updated_book.getDescriere()=='Comedie')
    assert (updated_book.getAutor()=='Ion Luca Caragiale')
    assert (updated_book.getStatus()==0)
    assert (updated_book.getNumar()==0)

    try:
        test_srv.update_book(2,'See','Comedie','Ion Luca Caragiale',0,0)
        assert False
    except ValueError:
        assert True

def test_all_books_service():
    test_add_book_service()
    test_delete_book_service()
    test_get_all_books_service()
    test_update_book_service()


class ClientService:

    def __init__(self,repo,validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de seriale
        :type repo: InMemoryRepositoryCustomers
        :param validator: validator pentru verificarea serialelor
        :type validator: ClientValidator
        """
        self.__repo=repo
        self.__validator=validator
    
    def add_customer(self,id,nume,cnp):
        """
        Adauga client
        :param id: id-ul clientului
        :type id: int
        :param nume: numele clientului
        :type nume: str
        :param cnp: cnp-ul clientului
        :type cnp: int
        :return: obiectul de tip Client creat
        :rtype:-; clientul s-a adaugat in lista
        :raises: ValueError daca clientul are date invalide
        """
        s=Client(id,nume,cnp)
        self.__validator.validate(s)
        self.__repo.store_customers(s)
        return s
    
    def get_all_customers(self):
        """
        Returneaza o lista cu toti clienti disponibili
        :return: lista de clienti disponibili
        :rtype: list of objects de tip Client
        """
        return self.__repo.get_all_customers()

    def delete_customer(self,id):
        """
        Sterge clientul cu id dat din lista
        :param id: id-ul dat
        :type id: str
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca nu exista client cu id-ul dat
        """
        return self.__repo.delete_by_id_customer(id)

    def update_customer(self,id,nume,cnp):
        """
        Modifica datele clientului cu id dat
        :param id: id-ul clientului de modificat
        :type id: int
        :param nume: noul nume al clientului
        :type nume: str
        :param an_aparitie: noul cnp a clientului
        :type an_aparitie: int
        :return: clientul modificat
        :rtype: Client
        :raises: ValueError daca noile date nu sunt valide, sau nu exista client cu id dat
        """
        s=Client(id,nume,cnp)
        self.__validator.validate(s)
        return self.__repo.update_customer(id,s)

    def generate_random_customers_service(self,x):
        """
        Genereaza random x clienti
        :param x: cate obiecte de tip Client se vor genera random
        :type x: int
        :return: lista de obiecte de tip Client generate random
        :rtype: list (of objects type Client)
        """
        return generate_random_customers(x)


def test_add_customer_service():
    repo=InMemoryRepositoryCustomers()
    validator=ClientValidator()
    test_srv=ClientService(repo,validator)

    added_customer=test_srv.add_customer(123,"Huiban Alexandru",'5030723046222')
    assert (added_customer.getId()==123)
    assert (added_customer.getNume()=="Huiban Alexandru")
    assert (added_customer.getCnp()=='5030723046222')

    assert (len(test_srv.get_all_customers())==1)

    try:
        added_customer=test_srv.add_customer(1,"Huiban Alexandru",'530723046222')
        assert False
    except ValueError:
        assert True

def test_delete_customer_service():
    repo=InMemoryRepositoryCustomers()
    validator=ClientValidator()
    test_srv=ClientService(repo, validator)

    test_srv.add_customer(323,'Popa Rares','1234567890123')
    deleted_customer=test_srv.delete_customer(323)

    assert (len(test_srv.get_all_customers())==0)
    assert (deleted_customer.getNume()=='Popa Rares')
    assert (deleted_customer.getCnp()=='1234567890123')

    try:
        test_srv.delete_customer(223)
        assert False
    except ValueError:
        assert True

def test_get_all_customers_service():
    repo=InMemoryRepositoryCustomers()
    validator=ClientValidator()
    test_srv=ClientService(repo,validator)

    test_srv.add_customer(123,'Popa Rares','1234567890123')
    test_srv.add_customer(223,'Huiban Alexandru','1234567890123')
    assert (type(test_srv.get_all_customers())==list)
    assert (len(test_srv.get_all_customers())==2)

def test_update_customer_service():
    repo=InMemoryRepositoryCustomers()
    validator=ClientValidator()
    test_srv=ClientService(repo, validator)

    test_srv.add_customer(123,'Popa Rares','1234567890123')
    updated_customer=test_srv.update_customer(123,'Huiban Alexandru','1234567890123')

    assert (updated_customer.getNume()=='Huiban Alexandru')
    assert (updated_customer.getCnp()=='1234567890123')

    try:
        test_srv.update_customer(2,'See','1234567890123')
        assert False
    except ValueError:
        assert True

def test_all_customers_service():
    test_add_customer_service()
    test_delete_customer_service
    test_get_all_customers_service()
    test_update_customer_service()


class Inchirieri_ReturnariService:

    def __init__(self,repo,validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de inchirieri
        :type repo: InMemoryRepositoryHiers
        :param validator: validator pentru verificarea inchirierilor
        :type validator: InchiriereValidator
        """
        self.__repo=repo
        self.__validator=validator

    def hire_book(self,book,customer,inchiriere):
        """
        Inchiriaza carte de catre un client
        :param book: cartea inchiriata
        :type book: Carte
        :param customer: clientul care inchiriaza
        :type customer: Client
        :param inchiriere: inchiriere
        :type inchiriere: bool
        """
        s=Inchiriere_Returnare(book,customer,inchiriere)
        self.__validator.validate(s)
        self.__repo.store_hires(s)
        return s

    def return_book(self,book,customer,returnare):
        """
        Returneaza carte de catre un client
        :param book: carte returnata
        :type book: Carte
        :param customer: clientul care returneaza
        :type customer: Client
        :param returnare: returnare
        :type returnare: bool
        """
        s=Inchiriere_Returnare(book,customer,returnare)
        self.__validator.validate(s)
        self.__repo.store_returns(s)
        return s

    def get_all_hires(self):
        """
        Returneaza o lista cu toate inchirierile existente
        :return: lista de inchirieri existente
        :rtype: list of objects de tip Inchiriere_Returnare
        """
        return self.__repo.get_all_hires()

    def get_all_returns(self):
        """
        Returneaza o lista cu toate returnarile existente
        :return: lista de returnari existente
        :rtype: list of objects de tip Inchiriere_Returnare
        """
        return self.__repo.get_all_returns()









