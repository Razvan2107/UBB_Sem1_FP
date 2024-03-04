import unittest

from entities import Client
from exceptions import DuplicateIDException, ClientNotFoundException
from repo_customers import InMemoryRepositoryCustomers,CustomerFileRepo,ClientFileRepoInheritance

class TestCaseClientRepoInMemory(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo=InMemoryRepositoryCustomers()
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
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

        self.__repo.store_customers(client1)
        self.__repo.store_customers(client2)
        self.__repo.store_customers(client3)
        self.__repo.store_customers(client4)
        self.__repo.store_customers(client5)
        self.__repo.store_customers(client6)
        self.__repo.store_customers(client7)
        self.__repo.store_customers(client8)
        self.__repo.store_customers(client9)
        self.__repo.store_customers(client10)

    def test_find(self):
        p=self.__repo.find_customer('1119')
        self.assertTrue(p.getNume()=='Vlad Teodora')
        self.assertTrue(p.getCnp()=='1234567890123')

        p1=self.__repo.find_customer('1101')
        self.assertIs(p1,None)

    def test_size(self):
        self.assertEqual(self.__repo.size_customer(),10)
        self.__repo.delete_by_id_customer('1119')
        self.__repo.delete_by_id_customer('1118')

        self.assertEqual(self.__repo.size_customer(),8)

        self.__repo.store_customers(Client('1011','Popa Rares','1234567890123'))
        self.assertEqual(self.__repo.size_customer(),9)
        self.__repo.update_customer('1011', Client('1011','Huiban Alexandru','1234567890123'))
        self.assertEqual(self.__repo.size_customer(),9)

    def test_get_all(self):
        crt_customers=self.__repo.get_all_customers()
        self.assertIsInstance(crt_customers,list)
        self.assertEqual(len(crt_customers),10)

        self.__repo.delete_by_id_customer('1112')
        self.__repo.delete_by_id_customer('1113')

        crt_customers=self.__repo.get_all_customers()
        self.assertEqual(len(crt_customers),8)

    def test_store(self):
        initial_size=self.__repo.size_customer()
        customer1=Client('1101','Popa Rares Constantin','1234567890123')
        self.__repo.store_customers(customer1)
        
        self.assertEqual(self.__repo.size_customer(),initial_size+1)
        customer2=Client('1102','Huiban Alexandru','1234567890123')
        self.__repo.store_customers(customer2)
        self.assertEqual(self.__repo.size_customer(),initial_size+2)
        self.assertRaises(ValueError,self.__repo.store_customers,customer2)

    def delete(self):
        initial_size=self.__repo.size_customer()
        deleted_customer=self.__repo.delete_by_id_customer('1111')
        self.assertTrue(deleted_customer.getNume()=='Popa Rares')
        self.assertTrue(self.__repo.size_customer()==initial_size-1)

        self.assertRaises(ClientNotFoundException,self.__repo.delete_by_id_customer,"Clientul nu a fost gasit.")

    def test_update(self):
        customer3=Client('1141','Bratu Luca','1234567890123')
        self.__repo.store_customers(customer3)

        modified_customer=self.__repo.update_customer('1141',customer3)
        self.assertEqual(modified_customer.getNume(),'Bratu Luca')
        self.assertEqual(modified_customer.getCnp(),'1234567890123')
        self.assertRaises(ValueError,self.__repo.update_customer,'87654',Client('5623','Alfred','1234567890123'))

class TestCaseClientRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = ClientFileRepoInheritance('test_clients_repo.txt')
        self.__add_predefined_clients()

    def __add_predefined_clients(self):
        client1 = Client('1111','Alexandra', '1234567890123')
        client2 = Client('2222','Mara','1234567890123')
        client3 = Client('3333','Mircea','1234567890123')
        client4 = Client('4444','Adrian','1234567890123')
        client5 = Client('5555','Rafa','1234567890123')

        self.__repo.store(client1)
        self.__repo.store(client2)
        self.__repo.store(client3)
        self.__repo.store(client4)
        self.__repo.store(client5)

    def test_find(self):
        p = self.__repo.find('1111')
        self.assertEqual(p.getNume(),'Alexandra')
        self.assertEqual(p.getCnp(), '1234567890123')

        p1 = self.__repo.find('765')
        self.assertIs(p1, None)

    def test_size(self):
        self.assertEqual(self.__repo.size(), 5)

        self.__repo.delete('1111')
        self.__repo.delete('2222')

        self.assertEqual(self.__repo.size(), 3)

        self.__repo.store(Client('7777', 'Marjorie', '1234567890123'))
        self.assertEqual(self.__repo.size(), 4)
        self.__repo.update('7777', Client('7777', 'Marge', '1234567890123'))
        self.assertEqual(self.__repo.size(), 4)

    def test_get_all(self):
        crt_clients = self.__repo.get_all()
        self.assertIsInstance(crt_clients, list)

        self.assertEqual(len(crt_clients), 5)

        self.__repo.delete('1111')
        self.__repo.delete('2222')

        crt_clients = self.__repo.get_all()
        self.assertEqual(len(crt_clients), 3)

    def test_store(self):
        initial_size = self.__repo.size()
        client1 = Client('2323', 'Cristiana', '1234567890123')
        self.__repo.store(client1)

        self.assertEqual(self.__repo.size(), initial_size + 1)
        client2 = Client('4731', 'Dana',  '1234567890123')
        self.__repo.store(client2)
        self.assertEqual(self.__repo.size(), initial_size + 2)
        self.assertRaises(ValueError, self.__repo.store, client2)

    def test_delete(self):
        initial_size = self.__repo.size()
        deleted_client = self.__repo.delete('4444')
        self.assertTrue(deleted_client.getNume() == 'Adrian')
        self.assertTrue(self.__repo.size() == initial_size - 1)

        self.assertRaises(ClientNotFoundException, self.__repo.delete, "Clientul nu a fost gasit.")

    def test_delete_black(self):
        initial_size = self.__repo.size()
        deleted_client = self.__repo.delete('4444')
        self.assertTrue(deleted_client.getNume() == 'Adrian')
        self.assertTrue(self.__repo.size() == initial_size - 1)

        self.assertRaises(ClientNotFoundException, self.__repo.delete, "Clientul nu a fost gasit.")

    def test_update(self):
        client3 = Client('3333', 'Kim',  '1234567890123')

        modified_client = self.__repo.update('3333', client3)
        self.assertEqual(modified_client.getNume(), 'Kim')
        self.assertEqual(modified_client.getCnp(),  '1234567890123')
        self.assertRaises(ValueError, self.__repo.update, '243545', Client('3333', 'Alfred', '1234567890123'))

    def tearDown(self) -> None:
        self.__repo.delete_all()

