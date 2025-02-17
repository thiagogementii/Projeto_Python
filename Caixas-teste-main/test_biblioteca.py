import pytest
from biblioteca import Biblioteca
from unittest.mock import MagicMock

@pytest.fixture
def biblioteca():
    return Biblioteca()

def test_adicionar_livro(biblioteca):
    # Adicionar livro com sucesso
    resultado = biblioteca.adicionar_livro("Python Básico")
    assert resultado == "Livro 'Python Básico' adicionado com sucesso."

    # Adicionar livro duplicado
    with pytest.raises(ValueError, match="O livro já está cadastrado."):
        biblioteca.adicionar_livro("Python Básico")

    # Tentar adicionar livro com título vazio
    with pytest.raises(ValueError, match="O título do livro não pode ser vazio."):
        biblioteca.adicionar_livro("")

def test_emprestar_livro(biblioteca):
    biblioteca.adicionar_livro("Java Avançado")

    # Emprestar livro disponível
    resultado = biblioteca.emprestar_livro("Java Avançado")
    assert resultado == "Livro 'Java Avançado' emprestado com sucesso."

    # Emprestar livro já emprestado
    with pytest.raises(ValueError, match="Livro já emprestado."):
        biblioteca.emprestar_livro("Java Avançado")

    # Tentar emprestar livro não cadastrado
    with pytest.raises(ValueError, match="Livro não encontrado na biblioteca."):
        biblioteca.emprestar_livro("C++ para Iniciantes")

def test_retornar_livro(biblioteca):
    biblioteca.adicionar_livro("HTML e CSS")
    biblioteca.emprestar_livro("HTML e CSS")

    # Retornar livro emprestado
    resultado = biblioteca.retornar_livro("HTML e CSS")
    assert resultado == "Livro 'HTML e CSS' retornado com sucesso."

    # Retornar livro já disponível
    resultado = biblioteca.retornar_livro("HTML e CSS")
    assert resultado == "Livro já está disponível."

    # Tentar retornar livro não cadastrado
    with pytest.raises(ValueError, match="Livro não encontrado na biblioteca."):
        biblioteca.retornar_livro("Javascript Moderno")

def test_listar_livros_mock(biblioteca):
    biblioteca.listar_livros = MagicMock(return_value={"Python Básico": "disponível"})
    resultado = biblioteca.listar_livros()
    assert resultado == {"Python Básico": "disponível"}
    biblioteca.listar_livros.assert_called_once()
