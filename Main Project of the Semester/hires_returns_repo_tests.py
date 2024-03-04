import unittest

from entities import Carte,Client,Inchiriere_Returnare
from exceptions import Inchiriere_ReturnareAlreadyAssignedException
from repo_hires_returns import InMemoryRepositoryHires_Returns,Hires_ReturnsFileRepo

class TestCaseHiresReturnsRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryHires_Returns()

    def test_store_hires(self):
        book=Carte('1234','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        customer=Client('1234','Huiban Alexandru','1234567890123')

        inchiriere=Inchiriere_Returnare(book,customer,True)

        self.__repo.store_hires(inchiriere)

        self.assertEqual(len(self.__repo.get_all_hires()),1)
        self.assertRaises(ValueError,self.__repo.store_hires,inchiriere)

    def test_store_returns(self):
        book=Carte('1234','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        customer=Client('1234','Huiban Alexandru','1234567890123')

        returnare=Inchiriere_Returnare(book,customer,False)

        self.__repo.store_returns(returnare)

        self.assertEqual(len(self.__repo.get_all_returns()),1)

    def test_find(self):
        book1=Carte('1234','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        book2=Carte('1235','O scrisoare pierduta','Comedie','I. L. Caragiale',0,0)

        customer1=Client('1234','Huiban Alexandru','1234567890123')
        customer2=Client('1235','Popa Rares','1234567890123')

        hier1=Inchiriere_Returnare(book1,customer1,True)
        hier2=Inchiriere_Returnare(book2,customer2,True)
        self.__repo.store_hires(hier1)

        self.assertIsNot(self.__repo.find_customer_id('1234'),customer1)


class TestCaseHiresReturnsRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=Hires_ReturnsFileRepo('test_hires_repo.txt','test_returns_repo.txt')

    def test_store_hires(self):
        book=Carte('1234','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        customer=Client('1234','Huiban Alexandru','1234567890123')

        hire=Inchiriere_Returnare(book,customer,True)

    def test_store_returns(self):
        book=Carte('1234','Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
        customer=Client('1234','Huiban Alexandru','1234567890123')

        returns=Inchiriere_Returnare(book,customer,False)

    def tearDown_hires(self) -> None:
        self.__repo.delete_all_hires()

    def tearDown_returns(self) -> None:
        self.__repo.delete_all_returns()

