from Interpolação_Polinomial import lagrange, newton_coef, plot, newton_eval, vandermonde, eval_vandermonde
import pytest
import numpy as np 

# testes:


"""
    Lagrange
"""

def test_lagrange_de_valores():
    assert lagrange([0,1,2,3], [1,2,0,4],1.5) == 0.8125
    assert lagrange([200,400,600,800,1000,1200,1400], [15,9,5,3,-2,-5,-15],700) == 4.3115234375
    assert lagrange([1],[2],1.5) == 2

def test_lagrange_lista():
    assert len(lagrange([0, 1, 2], [1, 3, 2], [0.5, 1.5, 2.0])) == len([0.5, 1.5, 2.0])
    assert np.allclose(lagrange([0,1,2,3], [1,2,0,4], [ 1.5, 2.0]) , [0.8125,0])
    assert isinstance(lagrange([0, 1, 2], [1, 3, 2], [0.5, 1.5, 2.0]),np.ndarray)


def test_lagrange_entradas_incorretas1():
    with pytest.raises(ValueError): # Python não viu erro
       lagrange([], [2],1.5) # x nulo
def test_lagrange_entradas_incorretas2():
    with pytest.raises(ValueError): # automático do python retorna IndexError
       lagrange([1], [],1.5) # y nulo 
def test_lagrange_entradas_incorretas3():
    with pytest.raises(ValueError): # Não retornaria nada
       lagrange([], [],1.5) # os dois nulos 
def test_lagrange_entradas_incorretas4():
    with pytest.raises(ValueError):  # automático do python retorna IndexError
       lagrange([1,2], [2],1.5)# x > y
def test_lagrange_entradas_incorretas5():
    with pytest.raises(ValueError):  # python não tem erro 
       lagrange([1], [2,6],1.5)
def test_lagrange_entradas_incorretas6():
    with pytest.raises(ValueError): # automático do python retorna ZeroDivisionError
       lagrange([1,2,3,2], [2,3,0,5],1.5)# x repetido
def test_lagrange_entradas_incorretas7(): 
    with pytest.raises(TypeError):#pois deveria ser ou um numero ou uma lista; python da como valueerror
       lagrange([0,1,2,3], [1,2,0,4],"oi")# ponto como string
def test_lagrange_entradas_incorretas8():
    with pytest.raises(ValueError):
       lagrange ([0,1,2,3], [1,2,0,4],["oi","tudo","bem?"]) # ponto como lista de string
def test_lagrange_entradas_incorretas9():
    with pytest.raises(ValueError):
       lagrange ([0,1,2,3], [1,2,0,4],[4,5,"oi",7,"tudo",9,"bem?"]) # ponto como lista de string e numeros
def test_lagrange_entradas_incorretas10():
    with pytest.raises(ValueError):
       lagrange ([0,1,"oi",2,3], [1,2,0,4],[4,5,6]) 
def test_lagrange_entradas_incorretas11():
    with pytest.raises(ValueError):
       lagrange ([0,1,2,3], [1,2,"oi",0,4],[4,5,6]) 
def test_lagrange_entradas_incorretas12():
    with pytest.raises(TypeError): 
       lagrange([0,1,2,3],1.5) 
def test_lagrange_entradas_incorretas13():
    with pytest.raises(TypeError):
       lagrange([0,1,2,3], [1,2,0,4]) 
def test_lagrange_entradas_incorretas14():
    with pytest.raises(TypeError): # python não deu erro nenhum 
       lagrange ([0,1,2,3], [1,2,0,4],None) 
def test_lagrange_entradas_incorretas15():
    with pytest.raises(TypeError):
       lagrange (None, [1,2,0,4],[1,2,4,5]) 
def test_lagrange_entradas_incorretas16():
    with pytest.raises(TypeError):# Python da IndexError
       lagrange ([0,1,2,3], None,[4,2.5,1]) 
def test_lagrange_entradas_incorretas17():
    with pytest.raises(TypeError):
       lagrange(1, 6,1.5)
def test_lagrange_entradas_incorretas18():
    with pytest.raises(TypeError): # python dá erro de Index mas no nosso caso deveria ser Type pois queremos listas
       lagrange([1], 6,1.5)
def test_lagrange_entradas_incorretas19():
    with pytest.raises(TypeError): 
       lagrange(1, [6],1.5)
def test_lagrange_entradas_incorretas20():
    with pytest.raises(TypeError):#python da ValueError
       lagrange("oi", [2,3,0,5],1.5)
def test_lagrange_entradas_incorretas21():
    with pytest.raises(TypeError): 
       lagrange([1,2,3,4], "oi",1.5)# Python dá ValueError
def test_lagrange_entradas_incorretas22():
    with pytest.raises(ValueError): # Python não retornaria nada
       lagrange([1], [None],1.5) 
def test_lagrange_entradas_incorretas23():
    with pytest.raises(ValueError): # Python não retornaria nada
       lagrange([None], [2],1.5) 



