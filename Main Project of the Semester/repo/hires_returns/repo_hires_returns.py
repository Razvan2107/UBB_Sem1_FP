from entities.entities import Carte,Client,Inchiriere_Returnare
from exceptions.exceptions import DuplicateIDException,BookNotFoundException,ClientNotFoundException,CorruptedFileException


class InMemoryRepositoryHires_Returns():
    
    def __init__(self):
        #hiers-multimea de inchirieri/returnari pe care o gestionam
        self.__hires=[]
        self.__returns=[]

    def find_book_id(self,id):
        """
        Cauta cartea cu id dat
        :param id: id dat
        :type id: str
        :return: cartea cu id dat, None daca nu exista
        :rtype: Carte
        """
        for book in self.__hires:
            if book.getCarte().getId()==id:
                return book
        return None
    
    def find_customer_id(self,id):
        """
        Cauta clientul cu id dat
        :param id: id dat
        :type id: str
        :return: client cu id dat, None daca nu exista
        :rtype: Client
        """
        for customer in self.__hires:
            if customer.getClient().getId()==id:
                return customer
        return None

    def store_hires(self,hire):
        """
        Adauga o inchiriere in lista
        :param hier: inchirierea care se adauga
        :type hier: Inchiriere_Returnare
        :return: -; lista de inchirieri se modifica prin adaugarea inchirierii date
        """
        if (self.find_book_id(hire.getCarte().getId()) is not None) and (self.find_customer_id(hire.getClient().getId()) is not None):
            if hire.getInchiriere_Returnare()==True:
                raise ValueError('Acest client a inchiriat aceasta carte deja!')
        self.__hires.append(hire)

    def store_returns(self,returnare):
        """
        Adauga o returnare in lista
        :param returnare: returnarea care se adauga
        :type returnare: Inchiriere_Returnare
        :return: -; lista de returnari se modifica prin adaugarea returnarii date
        """
        self.__returns.append(returnare)

    def get_all_hires(self):
        """
        Returneaza o lista cu toate inchirierile existente
        :rtype: list of objects de tip Inchiriere_Returnare
        """
        return self.__hires

    def get_all_returns(self):
        """
        Returneaza o lista cu toate returnarile existente
        :rtype: list of objects de tip Inchiriere-Returnare
        """
        return self.__returns


class Hires_ReturnsFileRepo():

    def __init__(self,filename_hires,filename_returns):
        self.__filename_hires=filename_hires
        self.__filename_returns=filename_returns

    def __load_from_file_hires(self):
        """
        Incarca datele din fisier
        :return: lista cu inchirierile din fisier
        :rtype: list of hires
        """
        try:
            f=open(self.__filename_hires,'r')
        except IOError:
            raise CorruptedFileException()

        hires=[]
        lines=f.readlines()
        for line in lines:
            hire_carte,hire_client,hire_inchiriere_returnare=[token.strip() for token in line.split(';')]
            a=Inchiriere_Returnare(hire_carte,hire_client,hire_inchiriere_returnare)
            hires.append(a)
        f.close()
        return hires
    
    def __load_from_file_returns(self):
        """
        Incarca datele din fisier
        :return: lista cu returnarile din fisier
        :rtype: list of returns
        """
        try:
            f=open(self.__filename,'r')
        except IOError:
            raise CorruptedFileException()

        returnss=[]
        lines=f.readlines()
        for line in lines:
            returns_carte,returns_client,returns_inchiriere_returnare=[token.strip() for token in line.split(';')]
            a=Inchiriere_Returnare(returns_carte,returns_client,returns_inchiriere_returnare)
            returnss.append(a)
        f.close()
        return returnss

    def __save_to_file_hires(self,hires):
        """
        Salveaza in fisier inchirierile date
        :param customer_list: lista de inchirieri
        :type customer_list: list of Inchiriare_Returnare
        :return:-;
        :rtype:-;
        """
        with open(self.__filename_hires,'w') as f:
            for hire in hires:
                hire_string=str(hire.getCarte().getTitlu())+';'+str(hire.getClient().getgetNume())+';'+str(hire.getInchiriare_Returnare())+'\n'
                f.write(hire_string)

    def __save_to_file_returns(self,returnss):
        """
        Salveaza in fisier returnarile date
        :param customer_list: lista de inchirieri
        :type customer_list: list of Inchiriare_Returnare
        :return:-;
        :rtype:-;
        """
        with open(self.__filename,'w') as f:
            for returns in returnss:
                returns_string=str(returns.getCarte().getTitlu())+';'+str(returns.getClient().getgetNume())+';'+str(returns.getInchiriare_Returnare())+'\n'
                f.write(returns_string)
    
    def get_all_hires(self):
        """
        Returneaza o lista cu toate inchirierile existente din multime
        :return: lista cu toate inchirierile existente
        :rtype: list of objects de tip Inchiriere_Returnare
        """
        return self.__load_from_file_hires()

    def get_all_returns(self):
        """
        Returneaza o lista cu toate returnarile existente din multime
        :return: lista cu toate returnarile existente
        :rtype: list of objects de tip Inchiriere_Returnare
        """
        return self.__load_from_file_returns()

    def store_hires(self,hire):
        """
        Adauga inchiriere in lista
        :param hire: inchirierea care va fi adaugata
        :type hire: Inchiriere_Returnare
        :return:-; lista de inchirierei se modifica prin adaugarea inchirierii
        :rtype:-; inchirierea este adaugata
        :raises: DuplicateIDException daca exista deja inchirierea
        """
        hires=self.__load_from_file_hires()
        if hire in hires:
            raise DuplicateIDException()
        hires.append(hire)
        self.__save_to_file_hires(hires)

    def store_returns(self,returns):
        """
        Adauga returnarea in lista
        :param returns: returnarea care va fi adaugata
        :type returns: returnarea
        :return:-; lista de returnari se modifica prin adaugarea returnarii
        :rtype:-; returnarea este adaugata
        :raises: DuplicateIDException daca exista deja returnarea
        """
        returnss=self.__load_from_file_returns()
        if returns in returnss:
            raise DuplicateIDException()
        returns.append(returns)
        self.__save_to_file_returns(returnss)

