from exercice.src.fonctions_simples import add_integer 
from exercice.src.fonctions_simples import divide
import pytest

def test_two_elements():
    assert add_integer(5,2) == 7


def test_divide_two_elements():
    assert divide (8,2) == 4



def test_error_when_integer():
    with pytest.raises(TypeError): #equivalent de l'assertion d'une erreur
        add_integer(5,'n') == 7


from exercice.src.fonctions_simples import add, divide, add_integer, alea_uniform
import pytest

####### Test add #######

def test_add_integers():
    assert add(1,2) == 3
    assert add(0,0) == 0
    assert add(-1,1) == 0
    assert add(-1,-1) == -2
    assert add(1,3.8) == 4.8

def test_add_integer_float():
    assert add(1,2.3) == 3.3

def test_add_floats():
    assert add(1.0,2.0) == 3.0
    assert add(0.0,0.0) == 0.0
    assert add(-1.0,1.0) == 0.0
    assert add(-1.0,-1.0) == -2.0

def test_add_strings():
    assert add("a","b") == "ab"
    assert add("","") == ""
    assert add("a","") == "a"
    assert add("","b") == "b"

def test_add_list():
    assert add([1,2,3],[4,5,6]) == [1,2,3,4,5,6]
    assert add([1,2,3],[]) == [1,2,3]
    assert add([],[4,5,6]) == [4,5,6]
    assert add([],[]) == []

def test_add_error_mixed_type():
    with pytest.raises(TypeError):
        add(1,"a")
    with pytest.raises(TypeError):
        add(2,[1,2])
    with pytest.raises(TypeError):
        add("2",["1","2"])

####### Test divide ####### 

def test_divide_ok():
    assert divide(1,1) == 1
    assert divide(1,2) == 0.5
    assert divide(2.2,2) == 1.1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(8,0)


######### Test add integrer #########

def test_add_integrer_ok():
    assert add_integer(1,2) == 3


def test_add__integrer_typeerror():
    with pytest.raises(TypeError):
        add_integer(1.2,2.6)

##########" Test alea_uniform ###########"
def test_alea_uniform():
    assert isinstance(alea_uniform(0,10), float)
    assert alea_uniform(0,10) >= 0
    assert alea_uniform(0,10) <=10