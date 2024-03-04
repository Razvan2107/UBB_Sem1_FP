from entities import Client
from exceptions import DuplicateIDException,ClientNotFoundException,CorruptedFileException

class InMemoryRepositoryCustomers():

    def __init__(self):
        #customers-multimea de clienti pe care o gestionam
        self.__customers=[]
    
    def find_customer(self,id):
        """
        Cauta clientul cu id dat
        :param id: id dat
        :type id: str
        :return: client cu id dat, None daca nu exista
        :rtype: Client
        """
        for customer in self.__customers:
            if customer.getId()==id:
                return customer
        return None
    
    def store_customers(self,customer):
        """
        Adauga o client in lista
        :param customer: clientul care se adauga
        :type customer: Client
        :return: -; lista de clienti se modifica prin adaugarea clientului dat
        :rtype:
        """

        #verificare id duplicat

        if self.find_customer(customer.getId()) is not None:
            raise ValueError('Exista deja client cu acest id!')
        self.__customers.append(customer)

    def get_all_customers(self):
        """
        Returneaza o lista cu toti clienti existenti
        :rtype: list of objects de tip Client
        """
        return self.__customers

    def size_customer(self):
        """
        Returneaza numarul de clienti din multime
        :return: numar clienti existenti
        :rtype:int
        """
        return len(self.__customers)

    def delete_by_id_customer(self,id):
        """
        Sterge client dupa id
        :param id: id-ul dat
        :type id: str
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca id-ul nu exista
        """

        #varianta remove by value

        customer=self.find_customer(id)
        if customer is None:
            raise ClientNotFoundException()
            #raise ValueError('Nu exista client cu acest id!')

        self.__customers.remove(customer)
        return customer

    def update_customer(self,id,modified_customer):
        """
        Modifica datele clientului cu id dat
        :param id: id dat
        :type id: str
        :param modified_customer: customer-ul cu datele noi
        :type modified_customer: Client
        :return: customer-ul modificat
        :rtype: Client
        """

        # self.delete_by_id(id)
        # self.store_customers(modified_customer)
        # return modified_customer

        customer=self.find_customer(id)
        if customer is None:
            raise ValueError('Nu exista carte cu acest id.')

        customer.setNume(modified_customer.getNume())
        customer.setCnp(modified_customer.getCnp())
        return customer

    def delete_all(self):
        """
        Sterge toate elementele din lista de clienti
        """
        self.__customers=[]

def setup_test_repo_customers_repo():
    client1=Client('1111','Popa Rares','1234567890123')
    client2=Client('1112','Huiban Alexandru','1234567890123')
    client3=Client('1113','Nanu Alexandra','1234567890123')
    client4=Client('1114','Bratu Luca','1234567890123')
    client5=Client('1115','Rotaru Stefan','1234567890123')
    client6=Client('1116','Lichi Tudor','1234567890123')
    client7=Client('1117','Patrut Stefan','1234567890123')
    client8=Client('1118','Lungu Mihai','1234567890123')
    client9=Client('1119','Vlad Teodora','1234567890123')
    client10=Client('1110','Mancas Teodor','1234567890123')

    test_repo=InMemoryRepositoryCustomers()
    test_repo.store_customers(client1)
    test_repo.store_customers(client2)
    test_repo.store_customers(client3)
    test_repo.store_customers(client4)
    test_repo.store_customers(client5)
    test_repo.store_customers(client6)
    test_repo.store_customers(client7)
    test_repo.store_customers(client8)
    test_repo.store_customers(client9)
    test_repo.store_customers(client10)
    return test_repo

def test_find_customer_repo():
    test_repo=setup_test_repo_customers_repo()

    p=test_repo.find_customer('1119')
    assert (p.getNume()=='Vlad Teodora')
    assert (p.getCnp()=='1234567890123')

    p1=test_repo.find_customer('1101')
    assert (p1 is None)

def test_size_customer_repo():
    test_repo1=setup_test_repo_customers_repo()
    assert (test_repo1.size_customer()==10)
    test_repo1.delete_by_id_customer('1119')
    test_repo1.delete_by_id_customer('1118')

    assert (test_repo1.size_customer()==8)

    test_repo1.store_customers(Client('1011','Popa Rares','1234567890123'))
    assert (test_repo1.size_customer()==9)
    test_repo1.update_customer('1011', Client('1011','Huiban Alexandru','1234567890123'))
    assert (test_repo1.size_customer()==9)

def test_get_all_customers_repo():
    test_repo1=setup_test_repo_customers_repo()
    crt_customers=test_repo1.get_all_customers()
    assert (type(crt_customers)==list)
    assert (len(crt_customers)==10)

    test_repo1.delete_by_id_customer('1112')
    test_repo1.delete_by_id_customer('1113')

    crt_customers=test_repo1.get_all_customers()
    assert (len(crt_customers)==8)

    test_repo1.store_customers(Client('1102','Huiban Alexandru','1234567890123'))
    assert (test_repo1.size_customer()==9)

    # not a good test if we don't know if the customer is stored on the last position or not
    assert (test_repo1.get_all_customers()[-1].getNume()=='Huiban Alexandru')
    assert (test_repo1.get_all_customers()[-1].getCnp()=='1234567890123')

    test_repo1.update_customer('1102', Client('1102','Huiban Alexandru','1234567890123'))

    # is it always the case that the updated customer keeps its position?
    # e.g. implement update as delete(old_customer)+insert(new_customer)
    assert (test_repo1.get_all_customers()[-1].getNume()=='Huiban Alexandru')
    assert (test_repo1.get_all_customers()[-1].getCnp()=='1234567890123')
    assert (test_repo1.size_customer()==9)

def test_store_customers_repo():
    test_repo=InMemoryRepositoryCustomers()
    
    customer1=Client('1111','Popa Rares','1234567890123')
    test_repo.store_customers(customer1)
    assert (test_repo.size_customer()==1)

    customer2=Client('1102','Huiban Alexandru','1234567890123')
    test_repo.store_customers(customer2)
    assert (test_repo.size_customer()==2)

    try:
        #duplicate id
        test_repo.store_customers(customer2)
        assert False
    except ValueError:
        assert True

def test_delete_customer_repo():
    test_repo=InMemoryRepositoryCustomers()
    customer1=Client('1111','Popa Rares','1234567890123')
    test_repo.store_customers(customer1)
    customer2=Client('112','Huiban Alexandru','1234567890123')
    test_repo.store_customers(customer2)

    deleted_customer=test_repo.delete_by_id_customer('112')
    assert (deleted_customer.getNume()=='Huiban Alexandru')
    assert (test_repo.size_customer()==1)

    customer_left=test_repo.find_customer('1111')
    assert (customer_left.getNume()=='Popa Rares')

    try:
        test_repo.delete_by_id_customer('wrongid')
        assert False
    except ValueError:
        assert True

def test_update_customer_repo():
    test_repo=InMemoryRepositoryCustomers()
    customer1=Client('1111','Popa Rares','1234567890123')
    test_repo.store_customers(customer1)
    customer2=Client('1141','Huiban Alexandru','1234567890123')
    test_repo.store_customers(customer2)
    customer3=Client('1141','Bratu Luca','1234567890123')

    modified_customer=test_repo.update_customer('1141',customer3)
    assert (modified_customer.getNume()=='Bratu Luca')
    assert (modified_customer.getCnp()=='1234567890123')

    try:
        test_repo.update_customer('243545',Client('1141','Bratu Luca','1234567890123'))
        assert False
    except ValueError:
        assert True

def test_all_customers_repo():
    test_find_customer_repo()
    test_size_customer_repo()
    test_get_all_customers_repo()
    test_store_customers_repo()
    test_delete_customer_repo()
    test_update_customer_repo()


class CustomerFileRepo:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista cu clientii din fisier
        :rtype: list of customers
        """
        try:
            f=open(self.__filename,'r')
        except IOError:
            raise CorruptedFileException()

        customers=[]
        lines=f.readlines()
        for line in lines:
            customer_id,customer_nume,customer_cnp=[token.strip() for token in line.split(';')]
            a=Client(customer_id,customer_nume,customer_cnp)
            customers.append(a)
        f.close()
        return customers

    def __save_to_file(self,customers):
        """
        Salveaza in fisier clientii dati
        :param customer_list: lista de clienti
        :type customer_list: list of Client
        :return:-;
        :rtype:-;
        """
        with open(self.__filename,'w') as f:
            for customer in customers:
                customer_string=str(customer.getId())+';'+str(customer.getNume())+';'+str(customer.getCnp())+'\n'
                f.write(customer_string)

    def find_customer(self,id):
        """
        Cauta clientul dupa id dat
        :param id: id dat
        :type id: int
        :return: clientul cu id dat, None daca nu exista client cu id dat
        :rtype: Client
        """
        customers=self.__load_from_file()
        for customer in customers:
            if customer.getId()==id:
                return customer
        return None

    def store_customers(self,customer):
        """
        Adauga client in lista
        :param customer: clientul care va fi adaugat
        :type customer: Client
        :return:-; lista de clienti se modifica prin adaugarea clientului
        :rtype:-; clientul este adaugat
        :raises: DuplicateIDException daca exista deja clientul
        """
        customers=self.__load_from_file()
        if customer in customers:
            raise DuplicateIDException()
        customers.append(customer)
        self.__save_to_file(customers)

    def get_all_customers(self):
        """
        Returneaza o lista cu toti clientii existenti din multime
        :return: lista cu toti clientii existenti
        :rtype: list of objects de tip Client
        """
        return self.__load_from_file()

    def size_customer(self):
        """
        Returneaza numarul de clienti din multime
        :return: numar de clienti existenti
        :rtype: int
        """
        return len(self.__load_from_file())

    def __find_index(self,customers,id):
        """
        Gaseste pozitia in lista customers a clientului cu id dat
        :param customers: lista de clienti
        :type customers: list of Client
        :param id: id-ul dat
        :type id: int
        :return: pozitia clientului cu id in lista de data, -1 daca nu exista
        :rtype: int, >0, <len(customers)
        """
        index=-1
        for i in range(len(customers)):
            if customers[i].getId()==id:
                index=i
                break
        return index

    def delete_customer_by_id(self,id):
        """
        Sterge client dupa id
        :param id: id-ul dat
        :type id: int
        :return: clientul sters
        :rtype: Client
        :raises: ClientNotFoundException daca id-ul nu exista
        """
        customers=self.__load_from_file()
        index=self.__find_index(customers,id)
        if index==-1:
            raise ClientNotFoundException()

        deleted_customer=customers.pop(index)
        self.__save_to_file(customers)
        return deleted_customer

    def update_customer(self,id,modified_customer):
        """
        Modifica datele clientului cu id dat
        :param id: id dat
        :type id: int
        :param modified_customer: clientul cu datele noi
        :type modified_customer: Client
        :return: clientul modificat
        :rtype: Client
        :raises: ClientNotFoundException daca nu exista client cu id dat
        """
        customers=self.__load_from_file()
        index=self.__find_index(customers,id)
        if index==-1:
            raise ClientNotFoundException()

        customers[index]=modified_customer
        self.__save_to_file(customers)

        return modified_customer

    def delete_all_customers(self):
        """
        Sterge toti clienti din fisier
        :return:-;
        :rtype:-;
        """
        self.__save_to_file([])


def test_store_file_customers():
    test_repo = CustomerFileRepo('test_customers_repo.txt')
    test_repo.delete_all()
    test_repo.store(Client(123,'Huiban Alexandru',5030721123456))
    assert (test_repo.size()==1)

    try:
        test_repo.store(Client(123,'Huiban Alexandru',5030721123456))
        assert False
    except DuplicateIDException():
        assert True

def test_update_file_customers():
    pass

def test_delete_file_customers():
    pass

def test_find_file_customers():
    pass

def test_all_customers_repo_file_customers():
    test_store_file_customers()
    test_update_file_customers()
    test_delete_file_customers()
    test_find_file_customers()


class ClientFileRepoInheritance(InMemoryRepositoryCustomers):
    def __init__(self,filename):
        InMemoryRepositoryCustomers.__init__(self)
        self.__filename=filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista cu clientii din fisier
        :rtype: list of customers
        """
        try:
            f=open(self.__filename,'r')
        except IOError:
            raise CorruptedFileException()

        lines=f.readlines()
        for line in lines:
            customer_id,customer_nume,customer_cnp=[token.strip() for token in line.split(';')]
            a=Client(customer_id,customer_nume,customer_cnp)
            InMemoryRepositoryCustomers.store_customers(self,a)
        f.close()
    
    def __save_to_file(self):
        """
        Salveaza in fisier clientii dati
        :param customer_list: lista de clienti
        :type customer_list: list of Client
        :return:-;
        :rtype:-;
        """
        customers=InMemoryRepositoryCustomers.get_all_customers(self)
        with open(self.__filename,'w') as f:
            for customer in customers:
                customer_string=str(customer.getId())+';'+str(customer.getNume())+';'+str(customer.getCnp())+'\n'
                f.write(customer_string)

    def store(self,customer):
        """
        Adauga client in lista
        :param customer: clientul care va fi adaugat
        :type customer: Client
        :return:-; lista de clienti se modifica prin adaugarea clientului
        :rtype:-; clientul este adaugat
        :raises: DuplicateIDException daca exista deja clientul
        """
        InMemoryRepositoryCustomers.store_customers(self,customer)
        self.__save_to_file()

    def update(self,id,modified_customer):
        """
        Modifica datele clientului cu id dat
        :param id: id dat
        :type id: int
        :param modified_customer: clientul cu datele noi
        :type modified_customer: Client
        :return: clientul modificat
        :rtype: Client
        :raises: ClientNotFoundException daca nu exista client cu id dat
        """
        updated_client=InMemoryRepositoryCustomers.update_customer(self,id,modified_customer)
        self.__save_to_file()
        return updated_client

    def delete(self,id):
        """
        Sterge client dupa id
        :param id: id-ul dat
        :type id: int
        :return: clientul sters
        :rtype: Client
        :raises: ClientNotFoundException daca id-ul nu exista
        """
        deleted_client=InMemoryRepositoryCustomers.delete_by_id_customer(self,id)
        self.__save_to_file()
        return deleted_client

    def get_all(self):
        """
        Returneaza o lista cu toti clientii existenti din multime
        :return: lista cu toti clientii existenti
        :rtype: list of objects de tip Client
        """
        return InMemoryRepositoryCustomers.get_all_customers(self)

    def size(self):
        """
        Returneaza numarul de clienti din multime
        :return: numar de clienti existenti
        :rtype: int
        """
        return InMemoryRepositoryCustomers.size_customer(self)

    def delete_all(self):
        """
        Sterge toti clienti din fisier
        :return:-;
        :rtype:-;
        """
        InMemoryRepositoryCustomers.delete_all(self)
        self.__save_to_file()

    def find(self,id):
        """
        Cauta clientul dupa id dat
        :param id: id dat
        :type id: int
        :return: clientul cu id dat, None daca nu exista client cu id dat
        :rtype: Client
        """
        return InMemoryRepositoryCustomers.find_customer(self,id)

    
