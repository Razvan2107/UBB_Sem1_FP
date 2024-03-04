from entities import Carte,Client,Inchiriere_Returnare
#from exceptions import ValidationException
from termcolor import colored

class CarteValidator:
    def validate(self,carte):
        errors=[]
        if carte.getId()<100:
            errors.append(colored('Id-ul cartii trebuie sa aiba minim 3 cifre!','red'))
        if len(carte.getTitlu())<3:
            errors.append(colored('Titlul cartii trebuie sa aiba mai mult de 2 caractere!','red'))
        if len(carte.getDescriere())<3:
            errors.append(colored('Descrierea cartii trebuie sa fie mai detaliata!','red'))
        if len(carte.getAutor())<3:
            errors.append(colored('Autorul cartii trebuie sa aiba mai mult de 2 caractere!','red'))
        if not (int(carte.getStatus())==1 or int(carte.getStatus())==0):
            errors.append(colored('Statusul unei cartii poate fi 0 (disponibila) sau 1 (inchiriata)!','red'))
        if int(carte.getNumar())<0:
            errors.append(colored('O carte poate sa nu fie inchiriata deloc, avand numarul de ordine minim 0! ','red'))

        if len(errors)>0:
            errors_string='\n'.join(errors)
            #raise ValidationException(errors_string)
            raise ValueError(errors_string)

def test_carte_validator():
    test_validator=CarteValidator()
    
    carte1=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    test_validator.validate(carte1)

    carte2=Carte(1,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    try:
        test_validator.validate(carte2)
        assert False
    except ValueError:
        assert True

    carte3=Carte(123,'','Nuvela psihologica','Ioan Slavici',0,0)
    try:
        test_validator.validate(carte3)
        assert False
    except ValueError:
        assert True

    carte4=Carte(123,'Moara cu noroc','.','Ioan Slavici',0,0)
    try:
        test_validator.validate(carte4)
        assert False
    except ValueError:
        assert True

    carte5=Carte(123,'Moara cu noroc','Nuvela psihologica',' ',0,0)
    try:
        test_validator.validate(carte5)
        assert False
    except ValueError:
        assert True

    carte6=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',4,0)
    try:
        test_validator.validate(carte6)
        assert False
    except ValueError:
        assert True

    carte7=Carte(123,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,-5)
    try:
        test_validator.validate(carte7)
        assert False
    except ValueError:
        assert True


class ClientValidator:
    def validate(self,client):
        errors=[]
        if client.getId()<100:
            errors.append('Id-ul clientului trebuie sa aiba cel putin 3 cifre.')
        if len(client.getNume())<2:
            errors.append('Numele clientului trebuia sa aiba mai mult de 3 caractere.')
        if len(str(client.getCnp()))!=13:
            errors.append('Cnp-ul clientului trebuie sa aiba exact 13 cifre.')

        if len(errors)>0:
            errors_string='\n'.join(errors)
            #raise ValidationException(errors_string)
            raise ValueError(errors_string)

def test_client_validator():
    test_validator=ClientValidator()
    
    client1=Client(123,'Popa Rares','5123456789321')
    test_validator.validate(client1)
   
    client2=Client(1,'Popa Rares','5123456789321')
    try:
        test_validator.validate(client2)
        assert False
    except ValueError:
        assert True

    client3=Client(123,'','5123456789321')
    try:
        test_validator.validate(client3)
        assert False
    except ValueError:
        assert True

    client4=Client(123,'Popa Rares','030721')
    try:
        test_validator.validate(client4)
        assert False
    except ValueError:
        assert True


class Inchiriere_ReturnareValidator:
    def validate(self,inchiriere_returnare):
        errors=[]
        if not (inchiriere_returnare.getInchiriere_Returnare()==1 or inchiriere_returnare.getInchiriere_Returnare()==0 or inchiriere_returnare.getInchiriere_Returnare()==-1):
            errors.append(colored('Inchirierea/Returnarea poate lua doar o valoare egala cu 1,0,-1!','red'))

        if len(errors)>0:
            errors_string='\n'.join(errors)
            #raise ValidationException(errors_string)
            raise ValueError(errors_string)

def test_inchiriere_validator():
    book=Carte(1234,'Moara cu noroc','Nuvela psihologica','Ioan Slavici',0,0)
    customer=Client(1243,'Popa Rares','1234567890123')

    hire=Inchiriere_Returnare(book,customer,True)

    validator=Inchiriere_ReturnareValidator()
    validator.validate(hire)

    hire1=Inchiriere_Returnare(book,customer,1534)
    try:
        validator.validate(hire1)
        assert False
    except ValueError:
        assert True






