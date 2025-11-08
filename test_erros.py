import pytest
from Erro_relativo_e_absoluto_numero import erro_absoluto, erro_relativo, epsilon_da_maquina

# Testes de erro absoluto

def test_erro_absoluto():
    # Testa erro absoluto com valores do tipo int e float
    assert erro_absoluto(11, 9) == 2
    assert erro_absoluto(0.9, 1.0) == 0.1
    assert erro_absoluto(3, 1.5) == 1.5

def test_erro_absoluto_precisao_padrao():
    # Testa se a precisão decimal padrão é sete
    assert erro_absoluto(1.23456789, 1.0) == round(abs(1.23456789 - 1.0), 7)

def test_erro_absoluto_precisao_customizada():
    # Testa erro absoluto para precisão customizada
    assert erro_absoluto(3.141592, 3, 4) == round(abs(3.141592 - 3), 4)
    assert erro_absoluto(3.1415, 4, 0) == round(abs(3.1415 - 4), 0)

def test_erro_absoluto_precisao_invalida():
    # Precisão é negativa
    assert erro_absoluto(5.6, 4.4, -3) == round(abs(5.6 - 4.4), 0)
    # Precisão é maior que 15
    assert erro_absoluto(0.1234567890123456, 0.0, 16) == round(abs(0.1234567890123456 - 0.0), 15)
    # Precisão não é int nem float
    assert erro_absoluto(5.25446565, 3.65165486, "banana") == round(abs(5.25446565 - 3.65165486), 7)
    # Precisão é float
    assert erro_absoluto(1.23456789, 9.87654321, 6.5) == round(abs(1.23456789 - 9.87654321), 6) 

def test_erro_absoluto_tipos_invalidos():
    mensagem = "valor e/ou valor aproximado não está com tipo válido( inteiro ou float)"
    assert mensagem in erro_absoluto("10", 8)
    assert mensagem in erro_absoluto(10, "8")

