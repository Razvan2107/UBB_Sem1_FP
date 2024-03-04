import unittest

from validators import CarteValidator,ClientValidator,Inchiriere_ReturnareValidator
from exceptions import ValidationException,BookNotFoundException,ClientNotFoundException,Inchiriere_ReturnareNotFoundException
from repo_books import InMemoryRepositoryBooks
from repo_customers import InMemoryRepositoryCustomers
from repo_hires_returns import InMemoryRepositoryHires_Returns
from service import CarteService,ClientService,Inchirieri_ReturnariService


class TestCaseCarteService(unittest.TestCase):
    def setup(self) -> None:
        repo=InMemoryRepositoryBooks()
        validator=CarteValidator()
        self.__srv=CarteService(repo,validator)
    
    def test_add_book(self):
        added_book=self.__srv.add_book(1234,"Moara cu noroc","Nuvela psihologica","Ioan Slavici",0,0)
        self.assertTrue(added_book.getTitlu()=='Moara cu noroc')
        self.assertTrue(added_book.getDescriere()=='Nuvela psihologica')
        self.assertTrue(added_book.getAutor()=='Ioan Slavici')
        self.assertTrue(added_book.getStatus()==0)
        self.assertTrue(added_book.getNumar()==0)

        self.assertEqual(len(self.__srv.get_all_books(),1))
        self.assertRaises(ValidationException,self.__srv.add_book,1,"Moara cu noroc","Nuvela psihologica","Ioan Slavici",0,0)

    def test_delete_book(self):
        added_book=self.__srv.add_book(123,"Moara cu noroc","Nuvela psihologica","Ioan Slavici",0,0)
        deleted_book=self.__srv.delete_book(123)

        self.assertEqual(len(self.__srv.get_all_books()),0)
        self.assertTrue(deleted_book.getTitlu()=='Moara cu noroc')
        self.assertTrue(deleted_book.getDescriere()=='Nuvela psihologica')
        self.assertTrue(deleted_book.getAutor()=='Ioan Slavici')
        self.assertTrue(deleted_book.getStatus()==0)
        self.assertTrue(deleted_book.getNumar()==0)

        self.assertRaises(BookNotFoundException,self.__srv.delete_book,"Cartea nu a fost gasita.")

    def test_get_all_books(self):
        added_book1=self.__srv.add_book(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        added_book2=self.__srv.add_book(223,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)
        self.assertIsInstance(self.__srv.get_all_books(),list)
        self.assertEqual(len(self.__srv.get_all_books()),2)

    def test_update_book(self):
        added_book=self.__srv.add_book(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        updated_book=self.__srv.update_book(123,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0)

        self.assertTrue(updated_book.getTitlu()=='O scrisoare')
        self.assertTrue(updated_book.getDescriere()=='Comedie')
        self.assertTrue(updated_book.getAutor()=='I. L. Caragiale')
        self.assertTrue(updated_book.getStatus()==0)
        self.assertTrue(updated_book.getNumar()==0)
        self.assertRaises(BookNotFoundException,self.__srv.update_book,'INVALID ID','Luca','1234567890123')


class TestCaseClientService(unittest.TestCase):
    def setUp(self) -> None:
        repo=InMemoryRepositoryCustomers()
        validator=ClientValidator()
        self.__srv=ClientService(repo,validator)

    def test_add_client(self):
        added_client=self.__srv.add_customer('1234','Huiban Ilie','1234567890123')
        self.assertTrue(added_client.getNume()=='Huiban Ilie')
        self.assertTrue(added_client.getCnp()=='1234567890123')

        self.assertEqual(len(self.__srv.get_all_customers(),1))
        self.assertRaises(ValidationException,self.__srv.add_customer('1235','Popa R','7654'))

    def test_delete_client(self):
        #BLACK BOX
        added_client=self.__srv.add_customer('1234','Huiban Ilie','1234567890123')
        deleted_client=self.__srv.delete_customer('1234')

        self.assertEqual(len(self.__srv.get_all_customers()),0)
        self.assertTrue(deleted_client.getNume()=='Huiban Ilie')
        self.assertTrue(deleted_client.getCnp()=='1234567890123')

        self.assertRaises(ClientNotFoundException,self.__srv.delete_customer,"Clientul nu a fost gasit.")

    def test_get_all_clients(self):
        added_client1=self.__srv.add_customer('1234','Huiban Ilie','1234567890123')
        added_client2=self.__srv.add_customer('1235','Popa Rares','1234567890123')
        self.assertIsInstance(self.__srv.get_all_customers(),list)
        self.assertEqual(len(self.__srv.get_all_customers()),2)

    def test_update_client(self):
        added_client=self.__srv.add_customer('1234','Huiban Ilie','1234567890123')
        updated_client=self.__srv.update_customer('1234','Huiban Ilie Alex','1234567890123')

        self.assertTrue(updated_client.getNume()=='Huiban Ilie Alex')
        self.assertTrue(updated_client.getCnp()=='1234567890123')
        self.assertRaises(ClientNotFoundException,self.__srv.update_customer,'INVALID ID','Luca','1234567890123')


class TestCaseHiresReturns(unittest.TestCase):
    def setUp(self) -> None:
        repo=InMemoryRepositoryHires_Returns()
        validator=Inchiriere_ReturnareValidator()
        self.__srv=Inchirieri_ReturnariService(repo,validator)

    def test_get_all_hires(self):
        added_hire1=self.__srv.hire_book((123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0),('1234','Huiban Ilie','1234567890123'),True)
        added_hire2=self.__srv.hire_book((223,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0),('1235','Popa Rares','1234567890123'),True)
        self.assertIsInstance(self.__srv.get_all_hires(),list)
        self.assertEqual(len(self.__srv.get_all_hires()),2)

    def test_get_all_returns(self):
        added_return1=self.__srv.return_book((123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0),('1234','Huiban Ilie','1234567890123'),False)
        added_return2=self.__srv.return_book((223,'O scrisoare pierduta','Comedie','Ion Luca Caragiale',0,0),('1235','Popa Rares','1234567890123'),False)
        self.assertIsInstance(self.__srv.get_all_returns(),list)
        self.assertEqual(len(self.__srv.get_all_returns()),2)


