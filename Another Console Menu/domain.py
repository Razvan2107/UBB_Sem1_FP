"""
def generate_numbers():
    
    #Genereaza un dictionar predefinit
    #:return: un dictionar de numere complexe
    #:rtype: dict
    
#    return [{'parte.reala':5,'parte.imaginara':2},
#            {'parte.reala':1,'parte.imaginara':2},
#            {'parte.reala':2,'parte.imaginara':1},
#            {'parte.reala':5,'parte.imaginara':2},
#            {'parte.reala':8,'parte.imaginara':6},
#            {'parte.reala':3,'parte.imaginara':2},
#            {'parte.reala':3,'parte.imaginara':3},
#            {'parte.reala':1,'parte.imaginara':9},
#            {'parte.reala':0,'parte.imaginara':10},
#            {'parte.reala':5,'parte.imaginara':2}
#            ]
    return [create_number(5,2),
            create_number(1,2),
            create_number(2,1),
            create_number(5,2),
            create_number(8,6),
            create_number(3,2),
            create_number(3,3),
            create_number(2,1),
            create_number(1,9),
            create_number(0,10),
            create_number(5,2)
            ]
"""

from termcolor import colored

def get_parte_reala(number):
    """
    Returneaza partea reala a unui numar complex
    :param number: un numar din dictionar
    :type number: int
    :return: partea reala
    :rtype: int
    """
    #return number['parte.reala']
    return number[0]

def get_parte_imaginara(number):
    """
    #Returneaza partea imaginara a unui numar complex
    #:param number: un numar din dictionar
    #:type number: int
    #:return: partea imaginara
    #:rtype: int
    """
    #return number['parte.imaginara']
    return number[1]

def get_undo_list(number):
    return number[1]

def set_number_list(number_list, new_number_list):
    number_list[0] = new_number_list

def set_undo_list(number_list, new_undo_list):
    number_list[1] = new_undo_list





