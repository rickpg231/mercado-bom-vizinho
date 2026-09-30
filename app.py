from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/movimentacoes")
def movimentacoes():
    return render_template("movimentacoes.html")


if __name__ == "__main__":
    app.run(debug=True)
