class Carte:
    
    def __init__(self,id,titlu,descriere,autor,status,numar):
        """
        Creeaza o noua carte cu id-ul, titlul, descrierea si autorul
        :parm id: id-ul cartii
        :type id: int
        :param titlu: titlul serialului
        :type titlu: str
        :param descriere: descrierea cartii
        :type descriere: str 
        :param autor: autorul cartii 
        :type autor: str
        :param status: statusul cartii (daca este inchiriata/returnata)
        :type status: bool(0/1)
        :param numar: de cate ori a fost inchiriata cartea
        :type numar: int
        """
        #self.dic={}
        #self.dic["id"]=id
        self.__id=id
        self.__titlu=titlu
        self.__descriere=descriere
        self.__autor=autor
        self.__status=status
        self.__numar=numar

    #Get
    def getId(self):
        #return self.dic["id"]
        return self.__id

    def getTitlu(self):
        return self.__titlu

    def getDescriere(self):
        return self.__descriere

    def getAutor(self):
        return self.__autor
    
    def getStatus(self):
        return self.__status

    def getNumar(self):
        return self.__numar

    #Set 
    def setId(self,value):
        #self.dic["id"]=value
        self.__id=value

    def setTitlu(self,value):
        self.__titlu=value

    def setDescriere(self,value):
        self.__descriere=value

    def setAutor(self,value):
        self.__autor=value

    def setStatus(self,value):
        self.__status=value

    def setNumar(self,value):
        self.__numar=value


#    def __eq__(self, other):
        """
        Verifica egalitatea intre cartea curenta si alta carte
        :param other: alta carte
        :type other: Carte
        :return: True daca cartile sunt egale (=au acelasi titlu si acelasi autor), False altfel
        :rtype: bool
        """
#        if self.__titlu==other.getTitlu() and self.__autor==other.getAutor():
#            return True
#        return False
    
    def __str__(self):
        return "ID: "+str(self.__id)+"; Titlu: "+self.__titlu+"; Descriere: "+self.__descriere+"; Autor: "+self.__autor+"; Status: "+self.__status+"; Numar: "+self.__numar


def test_create_carte():
    book1=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    assert (book1.getId()==123)
    assert (book1.getTitlu()=='Moara cu noroc')
    assert (book1.getDescriere()=='Nuvela psihologica')
    assert (book1.getAutor()=='Ioan Slavici')
    assert (book1.getStatus()==0)
    assert (book1.getNumar()==0)

    book1.setId(456)
    book1.setTitlu('O scrisoare pierduta')
    book1.setDescriere('Comedie')
    book1.setAutor('I. L. Caragiale')
    book1.setStatus(1)
    book1.setNumar(100)

    assert (book1.getId()==456)
    assert (book1.getTitlu()=='O scrisoare pierduta')
    assert (book1.getDescriere()=='Comedie')
    assert (book1.getAutor()=='I. L. Caragiale')
    assert (book1.getStatus()==1)
    assert (book1.getNumar()==100)

def test_equals_carte():
    book1=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    book2=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)

    #assert (book1==book2)

    book3=Carte(124,'Moara cu noro','Nuvela psihologica','Ioan Slavici',0,0)
    assert (book1!=book3)


test_create_carte()
test_equals_carte()


class Client:

    def __init__(self,id,nume,cnp):
        """
        Creeaza un nou client cu id, nume si cnp
        :param id: id-ul clientului
        :type id: int
        :param nume: numele clientului
        :type nume: str
        :param cnp: cnp-ul clientului
        :type cnp: int (13 cifre)
        """
        self.__id=id
        self.__nume=nume
        self.__cnp=cnp
    
    #Get
    def getId(self):
        return self.__id

    def getNume(self):
        return self.__nume

    def getCnp(self):
        return self.__cnp

    #Set
    def setId(self,value):
        self.__id=value

    def setNume(self,value):
        self.__nume=value

    def setCnp(self,value):
        self.__cnp=value


    def __eq__(self, other):
        """
        Verifica egalitatea intre serialul curent si serialul other
        :param other:
        :type other: Serial
        :return: True daca serialele sunt egale (=au acelasi titlu si acelasi an de aparitie), False altfel
        :rtype: bool
        """
        if self.__nume==other.getNume() and self.__cnp==other.getCnp():
            return True
        return False

    def __str__(self):
        return "ID: " + str(self.__id) + "; Nume: " + self.__nume + "; Cnp: " + self.__cnp


def test_create_client():
    client1=Client(123,'Popa Rares','5123456789321')
    assert (client1.getId()==123)
    assert (client1.getNume()=='Popa Rares')
    assert (client1.getCnp()=='5123456789321')

    client1.setId(456)
    client1.setNume('Huiban Alexandru')
    client1.setCnp('5030723046222')

    assert (client1.getId()==456)
    assert (client1.getNume()=='Huiban Alexandru')
    assert (client1.getCnp()=='5030723046222')

def test_equals_client():
    client1=Client(123,'Huiban Alexandru','5030723046222')
    client2=Client(123,'Huiban Alexandru','5030723046222')

    assert (client1==client2)

    client3=Client(124,'Huiban Alexandr','5030723046222')
    assert (client1!=client3)


test_create_client()
test_equals_client()


class Inchiriere_Returnare:

    def __init__(self,carte,client,inchiriere_returnare):
        """
        Creeaza o noua carte cu un nou client care au un status de inchiriere
        :parm carte: cartea
        :type carte: Carte
        :param client: client
        :type client: Client
        :param inchiriere: status-ul de inchiriere
        :type inchiriere: bool 
        """
        self.__carte=carte
        self.__client=client
        self.__inchiriere_returnare=inchiriere_returnare

    #Get
    def getCarte(self):
        return self.__carte

    def getClient(self):
        return self.__client

    def getInchiriere_Returnare(self):
        return self.__inchiriere_returnare

    #Set   
    def setcarte(self,value):
        self.__carte=value

    def setClient(self,value):
        self.__client=value

    def setInchiriere_Returnare(self,value):
        self.__inchiriere_returnare=value


    def __eq__(self, other):
        if self.__carte==other.__carte and self.__client==other.__client:
            return True
        return False

    def __str__(self):
        return 'Carte: [' + str(self.__carte.getTitlu()) + '; ' + str(self.__carte.getAutor()) + ']' + \
               'Client: [' + str(self.__client.getNume()) + ';' + str(self.__client.getCnp()) + ']' + \
               'Inchiriere: ' + str(self.__inchiriere)


def test_create_inchiriere_returnare():
    book=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    customer=Client(124,'Popa Rares','1234567890123')

    hire=Inchiriere_Returnare(book,customer,1)

    assert (hire.getCarte()==book)
    assert (hire.getClient()==customer)
    assert (hire.getInchiriere_Returnare()==1)

def test_equals_inchiriere_returnare():
    book=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    customer=Client(124,'Popa Rares','1234567890123')

    hire1=Inchiriere_Returnare(book,customer,1)
    hire2=Inchiriere_Returnare(book,customer,1)
    assert (hire1==hire2)

    book2=Carte(124,'O scrisoare pierduta','Comedie','I. L. Caragiale',0,0)
    hire3=Inchiriere_Returnare(book2,customer,0)
    assert (hire3!=hire2)


test_create_inchiriere_returnare()
test_equals_inchiriere_returnare()




