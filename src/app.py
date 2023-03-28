from controller.cadastro import cadastro
from config import config
from flask import Flask

app = Flask(__name__)

# Rota padrão de cadastro
@app.route("/cadastro", methods=["GET"])
def cadastro_get():
    return cadastro.get()

# Rota post de cadastro
@app.route("/cadastro", methods=["POST"])
def cadastro_post():
    return cadastro.post(config)