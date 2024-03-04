from entities import Tractor

class TractorFileRepo:
    def __init__(self,filename_truck):
        """
        Initializeaza repository
        :param filename_truck: numele fisierului
        :type filename_truck: file
        """
        self.__filename=filename_truck

    def __load_from_file_repo(self):
        """
        Incarca datele din fisier
        :return: lista de carti din fisier
        :rtype: list of Tractor objects
        :raises: ValueError daca fisierul nu exista
        """
        try:
            f=open(self.__filename,'r')
        except ValueError:
            print("Nu exista acest fisier!")

        lines=f.readlines()
        tractoare=[]
        for line in lines:
            tractor_id,tractor_denumire,tractor_pret,tractor_model,tractor_data=[token.strip() for token in line.split(';')]
            tractor_id=int(tractor_id)
            tractor_pret=int(tractor_pret)

            tractor=Tractor(tractor_id,tractor_denumire,tractor_pret,tractor_model,tractor_data)
            tractoare.append(tractor)

        f.close()
        return tractoare

    def __save_to_file_repo(self,tractoare):
        """
        Salveaza in fisier modificarile efectuate
        :param tractoare: lista de tractoare
        :type tractoare: list of Tractor objects 
        :return: -;
        :rtype: -;
        """
        with open(self.__filename,'w') as f:
            for tractor in tractoare:
                tractor_string=str(tractor.getId())+';'+tractor.getDenumire()+';'+str(tractor.getPret())+';'+tractor.getModel()+';'+str(tractor.getData())+'\n'
                f.write(tractor_string)

    def store_truck(self,tractor):
        """
        Adauga un tractor la sfarsitul listei de tractoare
        :param tractor: tractor
        :type tractor: Tractor object
        :return: -; lista se modifica prin adaugarea tractorului la sfarsitul listei
        :rtype: -;
        :raises: ValueError in caz de acest tractor exista deja
        """
        tractoare=self.__load_from_file_repo()
        for truck in tractoare:
            #if truck==tractor:
            if truck.getId()==tractor.getId():
                raise ValueError("Acest tractor exista deja in aceasta lista!")

        tractoare.append(tractor)
        self.__save_to_file_repo(tractoare)

    def delete_truck(self,cifra):
        """
        Sterge din lista de tractoare toate tractoarele a caror preturi contin o cifra data
        :param cifra: cifra respectiva
        :type cifra: int
        :
        """
        tractoare=self.__load_from_file_repo()
        ok=0
        for tractor in tractoare:
            pret=tractor.getPret()
            while pret:
                if pret%10==cifra:
                    ok=1
                    tractoare.remove(tractor)
                    break
                pret=pret//10

        if ok==0:
            raise ValueError("Nu exista tractoare care sa aiba aceasta cifra in componenta pretului!")

        self.__save_to_file_repo(tractoare)

    def delete_all(self):
        """
        Sterge toate elementele din lista de tractoare
        """
        return self.__save_to_file_repo([])


def test_store_trucks_repo():
    test_repo=TractorFileRepo("test_repo.txt")
    test_repo.delete_all()
    test_repo.store_truck(Tractor(1234,"qwer",5000,"Scania","12.05.23"))

    try:
        test_repo.store_truck(Tractor(1234,"qwer",5000,"Scania","12.05.23"))
        assert False
    except:
        assert True

def test_delete_trucks_repo():
    test_repo=TractorFileRepo("test_repo.txt")
    test_repo.delete_all()
    test_repo.store_truck(Tractor(1234,"qwer",5000,"Scania","12.05.23"))
    test_repo.store_truck(Tractor(1324,"qwfr",4000,"Scania","12.05.23"))
    test_repo.store_truck(Tractor(3456,"asdf",8000,"Volvo","12.05.23"))

    try:
        test_repo.delete_truck(4)
        assert True
    except ValueError:
        assert False

    try:
        test_repo.delete_truck(2)
        assert False
    except ValueError:
        assert True


test_delete_trucks_repo()

test_store_trucks_repo()

