from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=0)
    preco = db.Column(db.Float, nullable=False, default=0.0)

    def validar(self):
        if not self.nome or not self.nome.strip():
            raise ValueError("O nome do produto é obrigatório.")

        if self.quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

        if self.preco < 0:
            raise ValueError("O preço não pode ser negativo.")

        return True

    def __repr__(self):
        return f"<Produto {self.nome}>"
