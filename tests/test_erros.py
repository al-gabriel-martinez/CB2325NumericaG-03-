import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.erros import erro_absoluto, erro_relativo, epsilon_da_maquina
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

# Testes de erro relativo

def test_erro_relativo():
    # Testa erro relativo com valores do tipo int e float
    assert erro_relativo( 4, 7) == 3/4
    assert erro_relativo( 1.0, 0.8) == 0.2/1.0
    assert erro_relativo(2.5, 5) == 2.5/2.5

def test_erro_relativo_precisao_padrao():
    # Testa se a precisão decimal padrão é sete
    assert erro_relativo(2.0, 6.88888888) == round((abs(6.88888888 - 2.0))/2.0, 7)

def test_erro_relativo_precisao_customizada():
    # Testa erro relativo para precisão customizada
    assert erro_relativo(2, 4.222222, 4) == round((abs(4.222222 - 2))/2, 4)
    assert erro_relativo(4, 8.8484, 0) == round((abs(8.8484 - 4))/4, 0)

def test_erro_relativo_precisao_invalida():
    # Precisão é negativa
    assert erro_relativo( 2.4, 8.6, -3) == round((abs(8.6 - 2.4))/2.4, 0)
    # Precisão é maior que 15
    assert erro_relativo(2.0, 4.6666666666666666, 16) == round((abs(4.6666666666666666 - 2.0))/2.0, 15)
    # Precisão não é int nem float
    assert erro_relativo( 2.22222222,10.22244666, "banana") == round((abs(10.22244666 -  2.22222222))/ 2.22222222, 7)
    # Precisão é float
    assert erro_relativo(3.87654321, 6.23456789, 6.5) == round((abs(6.23456789 - 3.87654321))/3.87654321, 6) 

def test_erro_relativo_tipos_invalidos():
    mensagem = "valor e/ou valor aproximado não está com tipo válido( inteiro ou float)"
    assert mensagem in erro_relativo("16", 2)
    assert mensagem in erro_relativo(16, "2")

    #divisão por zero
    with pytest.raises(ZeroDivisionError, match="Valor real é zero"):
        erro_relativo(0, 1.23)

def test_epsilon_aproximado():
    eps = epsilon_da_maquina()

    # checagens básicas 
    assert isinstance(eps, float)
    assert eps > 0.0
    assert eps < 1e-12  # bem folgado (o real é ~2.22e-16)

    # propriedades essenciais:
    assert 1.0 + eps > 1.0
    assert 1.0 + eps/2.0 == 1.0
    


