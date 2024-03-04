from entities import Tractor
from repo import TractorFileRepo


class TractorService:
    def __init__(self,repo):
        """
        Initializam service-ul de tractoare
        :param repo: obiect de tip care ne va ajuta sa gestionam multimea de tractoare
        :type repo: TractorFileRepo object
        """
        self.__repo=repo

    def store_trucks(self,id,denumire,pret,model,data):
        """
        Adauga un tractor la sfarsitul listei de tractoare
        :param id: id-ul tractorului
        :type id: int
        :param denumire: denumirea tractorului
        :type denumire: str
        :param pret: pretul tractorului
        :type pret: int
        :param model: modelul tractorului
        :type model: str
        :param data: data la care expira revizia tractorului
        :type data: str
        :raises: ValueError in cazul in care acest tractor exista deja in lista de tractoare
        """
        truck=Tractor(id,denumire,pret,model,data)
        self.__repo.store_truck(truck)
        return truck

    def delete_truck(self,cifra):
        """
        Sterge un tractor din lista de tractoare
        :param cifra: cifra dupa care se va face stergerea
        :typr cifra: int
        :raises: ValueError daca nu exista tractoare a caror pret sa nu contina cifra respectiva
        """
        self.__repo.delete_truck(cifra)

    def delete_all(self):
        """
        Sterge toate cartile din fisier
        :return: -; lista va fi goala
        :rtype: -;
        """
        self.__repo.delete_all()

def test_store_trucks_service():
    repo=TractorFileRepo("test_service.txt")
    test_service=TractorService(repo)
    test_service.delete_all()

    tractor_adaugat=test_service.store_trucks(1234,"qwer",5000,"Scania","12.05.23")
    assert (tractor_adaugat.getId()==1234)
    assert (tractor_adaugat.getDenumire()=="qwer")
    assert (tractor_adaugat.getPret()==5000)
    assert (tractor_adaugat.getModel()=="Scania")
    assert (tractor_adaugat.getData()=="12.05.23")

    try: 
        tractor_adaugat=test_service.store_trucks(1234,"qwer",5000,"Scania","12.05.23")
        assert False
    except ValueError:
        assert True

def test_delete_truck_service():
    repo=TractorFileRepo("test_service.txt")
    test_service=TractorService(repo)
    test_service.delete_all()

    test_service.store_trucks(1234,"qwer",5000,"Scania","12.05.23")
    test_service.store_trucks(3456,"adcv",8000,"Volvo","16.08.23")
    
    try:
        test_service.delete_truck(5)
        assert True
    except ValueError:
        assert False

    try:
        test_service.delete_truck(6)
        assert False
    except ValueError:
        assert True


test_store_trucks_service()

test_delete_truck_service()

