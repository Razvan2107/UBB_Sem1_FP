class Tractor:
    def __init__(self,id,denumire,pret,model,data):
        """
        Initializam o clasa de tractoare
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
        """
        self.__id=id
        self.__denumire=denumire
        self.__pret=pret
        self.__model=model
        self.__data=data

    #Get
    def getId(self):
        return self.__id

    def getDenumire(self):
        return self.__denumire

    def getPret(self):
        return self.__pret
    
    def getModel(self):
        return self.__model

    def getData(self):
        return self.__data

    #Set
    def setId(self,value):
        self.__id=value

    def setDenumire(self,value):
        self.__denumire=value

    def setPret(self,value):
        self.__pret=value

    def setModel(self,value):
        self.__model=value

    def setData(self,value):
        self.__data=value

    #Eq
    def __eq__(self,other):
        """
        Verifica egalitatea intre doua obiecte de tip tractor
        :param other: un alt tractor
        :type other: obiect de tip Tractor
        """
        if self.__id==other.getId() and self.__denumire==other.getDenumire():
            return True
        return False

    def __str__(self):
        """
        
        """
        return "Id: "+str(self.__id)+"; Denumire: "+self.__denumire+"; Pret: "+str(self.__pret)+"; Model: "+self.__model+"; Data: "+self.__data


def test_creare_tractor():
    tractor=Tractor(1234,"qwer",5000,"Scania","12.05.23")

    assert (tractor.getId()==1234)
    assert (tractor.getDenumire()=="qwer")
    assert (tractor.getPret()==5000)
    assert (tractor.getModel()=="Scania")
    assert (tractor.getData()=="12.05.23")

    tractor.setId(3456)
    tractor.setDenumire("asdf")
    tractor.setPret(4000)
    tractor.setModel("Volvo")
    tractor.setData("13.07.22")

    assert (tractor.getId()==3456)
    assert (tractor.getDenumire()=="asdf")
    assert (tractor.getPret()==4000)
    assert (tractor.getModel()=="Volvo")
    assert (tractor.getData()=="13.07.22")

test_creare_tractor()

def test_egal_tractor():
    tractor1=Tractor(1234,"qwer",5000,"Scania","12.05.23")
    tractor2=Tractor(3446,"asdf",4000,"Scania","14.06.23")

    assert (tractor1!=tractor2)

    tractor3=Tractor(1234,"qwer",5000,"Scania","12.05.23")

    assert (tractor1==tractor3)

test_egal_tractor()

