from repo import *
from domain import *

# teste
def teste_F1():
     assert add_number_to_list([{1,2},{2,3},{4,5},{6,7},{8,9}],{4,5}) == [{1,2},{2,3},{4,5},{6,7},{8,9},{4,5}]
     assert add_number_to_list([{1,2},{2,3},{4,5},{6,7},{8,9}],{100,100}) == [{1,2},{2,3},{4,5},{6,7},{8,9},{100,100}]

def teste_F2():
     assert adauga_numar1([{1,2},{2,3},{4,5},{6,7},{8,9}],3,{4,5}) == [{1,2},{2,3},{4,5},{4,5},{6,7},{8,9}]
     assert adauga_numar1([{1,2},{2,3},{4,5},{6,7},{8,9}],0,{100,100}) == [{100,100},{1,2},{2,3},{4,5},{6,7},{8,9}]

def teste_F3():
     assert remove_number_from_list([{1,2},{2,3},{4,5},{6,7},{8,9}],3) == [{1,2},{2,3},{4,5},{8,9}]
     assert remove_number_from_list([{1,2},{2,3},{4,5},{6,7},{8,9}],0) ==[{2,3},{4,5},{6,7},{8,9}]

def teste_F4():
     assert sterge_interval_pozitii_parte_reala([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],1,3) == [1, 8]
     assert sterge_interval_pozitii_parte_imaginara([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],2,4) == [2, 3]

def teste_F5():
     assert inlocuieste_numar1([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],1,2,54,54) == [create_number(54,54),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]
     assert inlocuieste_numar1([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],6,7,123,321) == [create_number(1,2),create_number(2,3),create_number(4,5),create_number(123,321),create_number(8,9)]

def teste_F6():
     assert interval_pozitii1([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],1,3) == [3, 5, 7]
     assert interval_pozitii1([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],0,2) == [2, 3, 5]

def teste_F7():
     assert modul_mai_mic_decat_10_parte_reala([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]) == [1, 2, 4, 6]
     assert modul_mai_mic_decat_10_parte_imaginara([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]) == [2, 3, 5, 7]

def teste_F8():
     assert modul_egal_10_parte_reala([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,8),create_number(8,6)]) == [6, 8]
     assert modul_egal_10_parte_imaginara([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,8),create_number(8,6)]) == [8, 6]

def teste_F9():
     assert suma([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],1,3) == (12, 15)
     assert suma([create_number(2,1),create_number(3,2),create_number(5,4),create_number(7,6),create_number(9,10)],0,2) == (10, 7)

def teste_F10():
     assert produs([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],2,3) != (132, 47)
     assert produs([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],1,4) != (5, 42)

def teste_F11():
     assert sortare_list([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]) == [create_number(8,9),create_number(6,7),create_number(4,5),create_number(2,3),create_number(1,2)]
     assert sortare_list([create_number(1,134),create_number(1,45),create_number(4,5),create_number(6,3),create_number(8,9)]) == [create_number(1,134),create_number(1,45),create_number(8,9),create_number(4,5),create_number(6,3)]

def teste_F12():
     assert filtrare_parte_reala_prim([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]) == [create_number(1,2),create_number(4,5),create_number(6,7),create_number(8,9)]
     assert filtrare_parte_reala_prim([create_number(13,2),create_number(11,3),create_number(29,5),create_number(7,7),create_number(17,9)]) == []

def teste_F13():
     assert filtrare_modul([create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)],20,1) != [create_number(1,2),create_number(2,3),create_number(4,5),create_number(6,7),create_number(8,9)]
     assert filtrare_modul([create_number(100,20),create_number(13,14),create_number(23,26),create_number(6,7),create_number(8,9)],20,1) != [create_number(6,7),create_number(8,9)]

#def teste_F14():
    # add
    #test_manager = setup_show_manager(False)

    #add_number_to_list(test_manager,(1234,1234))
    #assert (len(get_show_list(test_manager)) == 1)

    #undo(test_manager)
    #assert (len(get_number_list(test_manager)) == 0)

    # delete
    #test_manager = setup_show_manager(True)
    #initial_length = len(get_show_list(test_manager))

    #delete_show_from_manager(test_manager, 2000, 2022)
    #assert (len(get_show_list(test_manager)) == 2)

    #undo(test_manager)
    #assert (len(get_show_list(test_manager)) == initial_length)

def testall():
     teste_F1()
     teste_F2()
     teste_F3()
     teste_F4()
     teste_F5()
     teste_F6()
     teste_F7()
     teste_F8()
     teste_F9()
     teste_F10()
     teste_F11()
     teste_F12()
     teste_F13()
     #teste_F14()








