from flask import render_template, request
from service.registrar_cadastro import registrar_cadastro

class Cadastro:
    # Retorna o template com form post
    def get():
        return render_template("cadastro.html")

    # Faz a persistência no banco
    def post(config: dict): 
        dados = {
            "nome": request.form.get("nome"),
            "email": request.form.get("email"),
            "senha": request.form.get("senha")
        } 

        registrar_cadastro(dados, config)

        return "Dados cadastrados!"
    
cadastro = Cadastro