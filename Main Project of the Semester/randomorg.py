import random
import string
from entities import Carte,Client

"""
Genreaza carti si clienti random
"""

def generate_random_books(x):
    sol=[]

    for i in range(0,x):
        id=random.randint(100,1000)
        letters=string.ascii_lowercase
        titlu=''.join(random.choice(letters) for i in range(10))
        descriere=''.join(random.choice(letters) for i in range(10))
        autor=''.join(random.choice(letters) for i in range(6))

        book=Carte(id,titlu,descriere,autor)
        sol.append(book)
    
    return sol 

def generate_random_customers(x):
    sol=[]

    for i in range(0,x):
        id=random.randint(100,1000)
        letters=string.ascii_lowercase
        nume=''.join(random.choice(letters) for i in range(10))
        cnp=random.randint(1000000000000,9999999999999)

        customer=Client(id,nume,cnp)
        sol.append(customer)

    return sol



