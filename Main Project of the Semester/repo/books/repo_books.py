from entities.entities import Carte,Client,Inchiriere_Returnare
from exceptions.exceptions import DuplicateIDException,BookNotFoundException,ClientNotFoundException,CorruptedFileException

class InMemoryRepositoryBooks:
    
    def __init__(self):
        #books-multimea de carti pe care o gestionam
        self.__books=[]

    def find_book(self,id):
        """
        Cauta cartea cu id dat
        :param id: id dat
        :type id: str
        :return: cartea cu id dat, None daca nu exista
        :rtype: Carte
        """
        for book in self.__books:
            if book.getId()==id:
                return book
        return None
    
    def store_books(self,book):
        """
        Adauga o carte in lista
        :param book: cartea care se adauga
        :type book: Carte
        :return: -; lista de carti se modifica prin adaugarea cartii date
        :rtype:
        """

        #verificare id duplicat

        if self.find_book(book.getId()) is not None:
            raise ValueError('Exista deja carte cu acest id!')
        self.__books.append(book)

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile existente
        :rtype: list of objects de tip Carte
        """
        return self.__books

    def size_book(self):
        """
        Returneaza numarul de carti din multime
        :return: numar carti existente
        :rtype:int
        """
        return len(self.__books)

    def delete_by_id_book(self,id):
        """
        Sterge carte dupa id
        :param id: id-ul dat
        :type id: str
        :return: cartea stearsa
        :rtype: Carte
        :raises: ValueError daca id-ul nu exista
        """

        #varianta remove by value

        book=self.find_book(id)
        if book is None:
            raise ValueError('Nu exista carte cu acest id!')

        self.__books.remove(book)
        return book
    
    def update_book(self,id,modified_book):
        """
        Modifica datele cartii cu id dat
        :param id: id dat
        :type id: str
        :param modified_book: book-ul cu datele noi
        :type modified_book: Carte
        :return: book-ul modificat
        :rtype: Carte
        """

        # self.delete_by_id_book(id)
        # self.store_books(modified_book)
        # return modified_book

        book=self.find_book(id)
        if book is None:
            raise ValueError('Nu exista carte cu acest id.')

        book.setTitlu(modified_book.getTitlu())
        book.setDescriere(modified_book.getDescriere())
        book.setAutor(modified_book.getAutor())
        book.setStatus(0)
        book.setNumar(0)
        return book


def setup_test_repo_books_repo():
    carte1=Carte('1111','1102','Huiban Alexandru','1234567890123',0,0)
    carte2=Carte('1112','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    carte3=Carte('1113','Povestea lui Harap-Alb','Basm cult','Ion Creanga',0,0)
    carte4=Carte('1114','Balatagul','Roman obiectiv de tip social','Mihail Sadoveanu',0,0)
    carte5=Carte('1115','Ion','Roman obiectiv de tip doric','Liviu Rebreanu',0,0)
    carte6=Carte('1116','Enigma Otiliei','Roman obiectiv de fractura balzaciana','George Calinescu',0,0)
    carte7=Carte('1117','Ultima nopate de dragoste, intaia nopate de razboi','Roamn subiectiv de analiza psihologica','Camil Petrescu',0,0)
    carte8=Carte('1118','Luceafarul','Romantism','Mihai Eminescu',0,0)
    carte9=Carte('1119','Plumb','Simbolism','George Bacovia',0,0)
    carte10=Carte('1110','Eu nu strivesc corola de minuni a lumii','Modernism','Lucian Blaga',0,0)

    test_repo=InMemoryRepositoryBooks()
    test_repo.store_books(carte1)
    test_repo.store_books(carte2)
    test_repo.store_books(carte3)
    test_repo.store_books(carte4)
    test_repo.store_books(carte5)
    test_repo.store_books(carte6)
    test_repo.store_books(carte7)
    test_repo.store_books(carte8)
    test_repo.store_books(carte9)
    test_repo.store_books(carte10)
    return test_repo

def test_find_book_repo():
    test_repo=setup_test_repo_books_repo()

    p=test_repo.find_book('1119')
    assert (p.getTitlu()=='Plumb')
    assert (p.getDescriere()=='Simbolism')
    assert (p.getAutor()=='George Bacovia')
    assert (p.getStatus()==0)
    assert (p.getNumar()==0)

    p1=test_repo.find_book('1101')
    assert (p1 is None)

def test_size_book_repo():
    test_repo1=setup_test_repo_books_repo()
    assert (test_repo1.size_book()==10)
    test_repo1.delete_by_id_book('1119')
    test_repo1.delete_by_id_book('1118')

    assert (test_repo1.size_book()==8)

    test_repo1.store_books(Carte('1101','Testament','Arta poetica','Tudor Arghezi',0,0))
    assert (test_repo1.size_book()==9)
    test_repo1.update_book('1101', Carte('1101','Riga Crypto si Lapona Enigel','Modernism','Ion Barbu',0,0))
    assert (test_repo1.size_book()==9)

def test_get_all_books_repo():
    test_repo1=setup_test_repo_books_repo()
    crt_books=test_repo1.get_all_books()
    assert (type(crt_books)==list)
    assert (len(crt_books)==10)

    test_repo1.delete_by_id_book('1112')
    test_repo1.delete_by_id_book('1113')

    crt_books=test_repo1.get_all_books()
    assert (len(crt_books)==8)

    test_repo1.store_books(Carte('1011','Morometii','Roman','Marin Preda',0,0))
    assert (test_repo1.size_book()==9)

    # not a good test if we don't know if the book is stored on the last position or not
    assert (test_repo1.get_all_books()[-1].getTitlu()=='Morometii')
    assert (test_repo1.get_all_books()[-1].getDescriere()=='Roman')
    assert (test_repo1.get_all_books()[-1].getAutor()=='Marin Preda')
    assert (test_repo1.get_all_books()[-1].getStatus()==0)
    assert (test_repo1.get_all_books()[-1].getNumar()==0)

    test_repo1.update_book('1011', Carte('1011','Floare albastra','Romantism','Mihai Eminescu',0,0))

    # is it always the case that the updated book keeps its position?
    # e.g. implement update as delete(old_book)+insert(new_book)
    assert (test_repo1.get_all_books()[-1].getTitlu()=='Floare albastra')
    assert (test_repo1.get_all_books()[-1].getDescriere()=='Romantism')
    assert (test_repo1.get_all_books()[-1].getAutor()=='Mihai Eminescu')
    assert (test_repo1.get_all_books()[-1].getStatus()==0)
    assert (test_repo1.get_all_books()[-1].getNumar()==0)

    assert (test_repo1.size_book()==9)

def test_store_books_repo():
    test_repo=InMemoryRepositoryBooks()
    
    book1=Carte('1111','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    test_repo.store_books(book1)
    assert (test_repo.size_book()==1)

    book2=Carte('456','O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)
    test_repo.store_books(book2)
    assert (test_repo.size_book()==2)

    try:
        #duplicate id
        test_repo.store_books(book2)
        assert False
    except ValueError:
        assert True

def test_delete_book_repo():
    test_repo=InMemoryRepositoryBooks()
    book1=Carte('113','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    test_repo.store_books(book1)
    book2=Carte('112','O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)
    test_repo.store_books(book2)

    deleted_book=test_repo.delete_by_id_book('112')
    assert (deleted_book.getTitlu()=='O scrisoare pierduta')
    assert (test_repo.size_book()==1)

    book_left=test_repo.find_book('113')
    assert (book_left.getTitlu()=='Moara cu noroc')

    try:
        test_repo.delete_by_id_book('wrongid')
        assert False
    except ValueError:
        assert True

def test_update_book_repo():
    test_repo=InMemoryRepositoryBooks()
    book1=Carte('112','Moara cu noroc','Comedie','Ion Luca Caragiale',0,0)
    test_repo.store_books(book1)
    book2=Carte('113','Balatagul','Roman','Mihail Sadoveanu',0,0)
    test_repo.store_books(book2)
    book3=Carte('113','Ion','Roman','Liviu Rebreanu',0,0)

    modified_book=test_repo.update_book('113',book3)
    assert (modified_book.getTitlu()=='Ion')
    assert (modified_book.getDescriere()=='Roman')
    assert (modified_book.getAutor()=='Liviu Rebreanu')
    assert (modified_book.getStatus()==0)
    assert (modified_book.getNumar()==0)

    try:
        test_repo.update_book('243545',Carte('113','Ion','Roman','Liviu Rebreanu',0,0))
        assert False
    except ValueError:
        assert True

def test_all_books_repo():
    test_find_book_repo()
    test_size_book_repo()
    test_get_all_books_repo()
    test_store_books_repo()
    test_delete_book_repo()
    test_update_book_repo()


class BookFileRepo:
    def __init__(self,filename):
        self.__filename=filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de carti din fisier
        :rtype: list of Carte objects
        :raises: ...
        """
        try:
            f=open(self.__filename,'r')
            #f=io.open(self.__filename, mode='r', encoding='utf-8')
        except IOError:
            return

        lines=f.readlines()
        all_books=[]
        for line in lines:
            book_id, book_nume, book_descriere, book_autor, book_status, book_numar=[token.strip() for token in line.split(';')]
            book_id=int(book_id)

            s=Carte(book_id,book_nume,book_descriere,book_autor,book_status,book_numar)
            #for book in all_books:
                #if book.getId()==book_id:
                #    raise ValueError('Cartile care se adauga in fisier vor trebui sa aiba un id diferit fata de cele aflate deja in fisier!')
            all_books.append(s)

        f.close()
        return all_books

    def __save_to_file(self,books):
        """
        Salveaza in fisier cartile date
        :param books: lista de carti
        :type books: list of Carte
        :return:-;
        :rtype:-;
        """
        with open(self.__filename,'w') as f:
            for book in books:
                book_string=str(book.getId())+';'+str(book.getTitlu())+';'+str(book.getDescriere())+';'+str(book.getAutor())+';'+str(book.getStatus())+';'+str(book.getNumar())+'\n'
                f.write(book_string)

    def find_book(self,id):
        """
        Cauta cartea cu id dat
        :param id: id dat
        :type id: str
        :return: cartea cu id dat, None daca nu exista carte cu id dat
        :rtype: Carte
        """
        all_books=self.__load_from_file()
        for book in all_books:
            if book.getId()==id:
                return book
        return None

    def store_books(self,book):
        """
        Adauga o carte in lista
        :param book: cartea care se adauga
        :type book: Carte
        :return: -; lista de carti se modifica prin adaugarea cartii date
        :rtype:
        :raises: DuplicateIDException daca cartea exista deja
        """
        all_books = self.__load_from_file()
        if book in all_books:
            raise DuplicateIDException()

        all_books.append(book)
        self.__save_to_file(all_books)

    def get_all_books(self):
        """
        Returneaza o lista cu toate cartile existente
        :rtype: list of objects de tip Carte
        """
        return self.__load_from_file()

    def size_book(self):
        """
        Returneaza numarul de carti din multime
        :return: numar carti existente
        :rtype: int
        """
        return len(self.__load_from_file())

    def __find_index(self,all_books,id):
        """
        Gaseste pozitia in lista a cartii cu id dat
        :param all_books: lista cu toate cartile
        :type all_books: list of Carte objects
        :param id: id-ul cautat
        :type id: str
        :return: pozitia in lista a cartii date, -1 daca cartea nu se regaseste in lista
        :rtype: int, >=0, <repo.size()
        """
        index=-1
        for i in range(len(all_books)):
            if all_books[i].getId() == id:
                index=i

        return index

    def delete_by_id_book(self,id):
        """
        Sterge carte dupa id
        :param id: id-ul dat
        :type id: str
        :return: cartea stearsa
        :rtype: Carte
        :raises: BookNotFoundException daca id-ul nu exista
        """
        all_books=self.__load_from_file()
        index=self.__find_index(all_books, id)
        if index==-1:
            raise BookNotFoundException()

        deleted_book=all_books.pop(index)

        self.__save_to_file(all_books)
        return deleted_book

    def update_book(self,id,modified_book):
        """
        Modifica datele cartii cu id dat
        :param id: id dat
        :type id: str
        :param modified_book: cartea cu datele noi
        :type modified_book: Carte
        :return: cartea modificata
        :rtype: Carte
        :raises: BookNotFoundException daca nu exista carte cu id dat
        """

        all_books=self.__load_from_file()
        index=self.__find_index(all_books, id)
        if index==-1:
            raise BookNotFoundException()

        all_books[index]=modified_book

        self.__save_to_file(all_books)
        return modified_book

    def delete_all_books(self):
        """
        Sterge toate cartile din fisier
        :return:-;
        :rtype:-;
        """
        self.__save_to_file([])


def test_store_file_books():
    test_repo = BookFileRepo('test_books_repo.txt')
    test_repo.delete_all()
    test_repo.store(Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0))
    assert (test_repo.size()==1)

    try:
        test_repo.store(Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0))
        assert False
    except DuplicateIDException:
        assert True

def test_update_file_books():
    pass

def test_delete_file_books():
    pass

def test_find_file_books():
    pass

def test_all_books_repo_file():
    test_store_file_books()
    test_update_file_books()
    test_delete_file_books()
    test_find_file_books()

