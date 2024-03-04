import unittest

from entities import Carte
from exceptions import DuplicateIDException, BookNotFoundException
from repo_books import InMemoryRepositoryBooks,BookFileRepo,BookRepoFileInheritance

class TestCaseCarteRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryBooks()

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

        self.__repo.store_books(carte1)
        self.__repo.store_books(carte2)
        self.__repo.store_books(carte3)
        self.__repo.store_books(carte4)
        self.__repo.store_books(carte5)
        self.__repo.store_books(carte6)
        self.__repo.store_books(carte7)
        self.__repo.store_books(carte8)
        self.__repo.store_books(carte9)
        self.__repo.store_books(carte10)

    def test_find(self):
        p=self.__repo.find_book('1119')
        self.assertTrue(p.getTitlu()=='Plumb')
        self.assertTrue(p.getDescriere()=='Simbolism')
        self.assertTrue(p.getAutor()=='George Bacovia')
        self.assertEqual(p.getStatus(),0)
        self.assertEqual(p.getNumar(),0)

        p1=self.__repo.find_book('1101')
        self.assertIs(p1,None)

    def test_size(self):
        self.assertEqual(self.__repo.size_book(),10)
        
        self.__repo.delete_by_id_book('1119')
        self.__repo.delete_by_id_book('1118')

        self.assertEqual(self.__repo.size_book(),8)

        self.__repo.store_books(Carte('1101','Testament','Arta poetica','Tudor Arghezi',0,0))
        self.assertEqual(self.__repo.size_book(),9)
        self.__repo.update_book('1101', Carte('1101','Riga Crypto si Lapona Enigel','Modernism','Ion Barbu',0,0))
        self.assertEqual(self.__repo.size_book(),9)

    def test_get_all(self):
        crt_books=self.__repo.get_all_books()
        self.assertEqual(len(crt_books),10)

        self.__repo.delete_by_id_book('1112')
        self.__repo.delete_by_id_book('1113')

        crt_books=self.__repo.get_all_books()
        self.assertEqual(len(crt_books),8)

        self.__repo.store_books(Carte('1011','Morometii','Roman','Marin Preda',0,0))
        self.assertTrue(self.__repo.size_book()==9)

        self.__repo.update_book('1011', Carte('1011','Floare albastra','Romantism','Mihai Eminescu',0,0))

        self.assertTrue(self.__repo.size_book()==9)

    def test_store(self):
        initial_size=self.__repo.size_book()
        book1=Carte('1001','Carul cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        self.__repo.store_books(book1)

        self.assertEqual(self.__repo.size_book(),initial_size+1)
        book2=Carte('456','Doua scrisori pierdute','Comedie','Ion Luca Caragiale',0,0)
        self.__repo.store_books(book2)
        self.assertEqual(self.__repo.size_book(),initial_size+2)

    def test_delete(self):
        self.__repo=InMemoryRepositoryBooks()
        book1=Carte('113','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        self.__repo.store_books(book1)
        book2=Carte('112','O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)
        self.__repo.store_books(book2)

        deleted_book=self.__repo.delete_by_id_book('112')
        self.assertTrue(deleted_book.getTitlu()=='O scrisoare pierduta')
        self.assertTrue(self.__repo.size_book()==1)

        book_left=self.__repo.find_book('113')
        self.assertEqual(book_left.getTitlu(),'Moara cu noroc')
        self.assertRaises(BookNotFoundException,self.__repo.delete_by_id_book,"Cartea nu a fost gasita.")

    def test_update(self):
        self.__repo=InMemoryRepositoryBooks()
        book1=Carte('112','Moara cu noroc','Comedie','Ion Luca Caragiale',0,0)
        self.__repo.store_books(book1)
        book2=Carte('113','Balatagul','Roman','Mihail Sadoveanu',0,0)
        self.__repo.store_books(book2)
        book3=Carte('113','Ion','Roman','Liviu Rebreanu',0,0)

        modified_book=self.__repo.update_book('113',book3)
        self.assertEqual(modified_book.getTitlu(),'Ion')
        self.assertEqual(modified_book.getDescriere(),'Roman')
        self.assertEqual(modified_book.getAutor(),'Liviu Rebreanu')
        self.assertEqual(modified_book.getStatus(),0)
        self.assertEqual(modified_book.getNumar(),0)
        self.assertRaises(BookNotFoundException,self.__repo.update_book,'567543253',Carte('234','Gigel','Baiat','Mama lui',0,0))


class TestCaseCarteRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo= BookRepoFileInheritance('test_books_repo.txt')
        self.__repo.delete_all()
        self.__populate_list()

    def __populate_list(self):
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

        self.__repo.store_books(carte1)
        self.__repo.store_books(carte2)
        self.__repo.store_books(carte3)
        self.__repo.store_books(carte4)
        self.__repo.store_books(carte5)
        self.__repo.store_books(carte6)
        self.__repo.store_books(carte7)
        self.__repo.store_books(carte8)
        self.__repo.store_books(carte9)
        self.__repo.store_books(carte10)

    def test_find(self):
        p=self.__repo.find('1119')
        self.assertTrue(p.getTitlu()=='Plumb')
        self.assertTrue(p.getDescriere()=='Simbolism')
        self.assertTrue(p.getAutor()=='George Bacovia')
        self.assertEqual(p.getStatus(),0)
        self.assertEqual(p.getNumar(),0)

        p1=self.__repo.find('56784')
        self.assertIs(p1,None)

    def test_size(self):
        initial_size=self.__repo.size()
        self.__repo.delete('1111')
        self.__repo.delete('1117')

        self.assertEqual(self.__repo.size(),initial_size-2)

        self.__repo.store(Carte('12345','Ilie','Alex','Huiban',0,0))
        self.assertEqual(self.__repo.size(),initial_size-1)
        self.__repo.update('12345',Carte('12345','Ilie','Alex','Huiban',1,0))
        self.assertEqual(self.__repo.size(),initial_size-1)

    def test_get_all(self):
        initial_size=self.__repo.size()
        crt_books=self.__repo.get_all()
        self.assertIsInstance(crt_books,list)

        self.assertEqual(len(crt_books),initial_size)

        self.__repo.delete('1111')
        self.__repo.delete('1117')

        crt_books=self.__repo.get_all()
        self.assertEqual(len(crt_books),initial_size-2)

        self.__repo.store(Carte('12345','Ilie','Alex','Huiban',0,0))
        self.assertEqual(self.__repo.size(),initial_size-1)

        self.__repo.update('12345',Carte('12345','Ilie','Alex','Huiban',1,0))
        
        self.assertTrue(self.__repo.size()==initial_size-1)

    def test_store(self):
        initial_size=self.__repo.size()
        book1=Carte('12345','Ilie','Alex','Huiban',0,0)
        self.__repo.store(book1)

        self.assertEqual(self.__repo.size(),initial_size+1)
        book2=Carte('12346','Rares','Constantin','Popa',0,0)
        self.__repo.store(book2)
        self.assertEqual(self.__repo.size(),initial_size+2)

    def test_delete(self):
        initial_size=self.__repo.size()
        book1=Carte('12345','Ilie','Alex','Huiban',0,0)
        self.__repo.store(book1)
        book2=Carte('12346','Rares','Constantin','Popa',0,0)
        self.__repo.store(book2)

        deleted_book=self.__repo.delete('12346')
        self.assertTrue(deleted_book.getTitlu()=='Rares')
        self.assertTrue(self.__repo.size()==initial_size+1)

        book_left=self.__repo.find('12345')
        self.assertEqual(book_left.getTitlu(),'Ilie')
        self.assertRaises(BookNotFoundException,self.__repo.delete,'464757')

    def test_update(self):
        book1=Carte('12345','Ilie','Alex','Huiban',0,0)
        self.__repo.store(book1)
        book2=Carte('12346','Rares','Constantin','Popa',0,0)
        self.__repo.store(book2)
        book3=Carte('12346','Rare','Constantin','Popa',0,0)

        modifiedd_book=self.__repo.update('12346',book3)
        self.assertEqual(modifiedd_book.getTitlu(),'Rare')
        self.assertEqual(modifiedd_book.getDescriere(),'Constantin')
        self.assertEqual(modifiedd_book.getAutor(),'Popa')
        self.assertEqual(modifiedd_book.getStatus(),0)
        self.assertEqual(modifiedd_book.getNumar(),0)
        self.assertRaises(BookNotFoundException,self.__repo.update,'8657643',Carte('12346','Rare','Constantin','Popa',0,0))

    def tearDown(self) -> None:
        self.__repo.delete_all()

