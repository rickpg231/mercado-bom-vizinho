from models import Produto


def test_criacao_produto():
    produto = Produto(
        nome="Arroz 5kg",
        quantidade=10,
        preco=25.90
    )

    assert produto.nome == "Arroz 5kg"
    assert produto.quantidade == 10
    assert produto.preco == 25.90


def test_quantidade_inicial_produto():
    produto = Produto(
        nome="Feijão 1kg",
        quantidade=5,
        preco=8.50
    )

    assert produto.quantidade >= 0
