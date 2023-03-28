# Procedimento de instalação do projeto

## Requisitos:

- MySQL
- Python3



## Passo 1. Criação do DB

Crie um banco de dados mysql utilizando o comando :

```sql
CREATE DATABASE <nome_do_banco>;
```

Ou utilizando uma ferramenta administradora de banco de dados como o DBeaver ou Workbench.



Logo após criar o banco, execute o script "ddl.sql" localizado em models dentro de src.



## Passo 2. Credenciais

No arquivo config.json altere os campos host, user, password e db para suas credenciais locais do banco.



## Passo 3. Ambiente Python

Na raíz da aplicação, crie um ambiente virtual python:

```bash
python3 -m venv venv
```



E ative-o:

```bash
source ./venv/bin/activate
```

*Nota: Esses códigos podem variar de acordo com o seu sistema operacional, este tutorial contempla o linux.*



Após ativa-lo, instale as dependências listadas em requirements.txt:

```
pip install -r requirements.txt
```



## Passo 4. Rodando!

Após todo esse procedimento, navegue até src e utilizando o comando "*flask run*" execute a aplicação. Ela devera estar rodando [aqui](http://localhost:5000/cadastro)!

## Extra: Teste unitário

Para executar o teste unitário execute o arquivo unity.py.