from flask import Flask

from models import db, Produto


def criar_app_teste():
    app = Flask(__name__)

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app


def test_integracao_produto_com_banco():
    app = criar_app_teste()

    with app.app_context():
        db.create_all()

        produto = Produto(
            nome="Arroz 5kg",
            quantidade=10,
            preco=25.90
        )

        produto.validar()

        db.session.add(produto)
        db.session.commit()

        produto_salvo = Produto.query.first()

        assert produto_salvo is not None
        assert produto_salvo.nome == "Arroz 5kg"
        assert produto_salvo.quantidade == 10
        assert produto_salvo.preco == 25.90

        db.session.remove()
        db.drop_all()
