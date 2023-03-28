import mysql.connector

# Cria a conexão mysql e executa a inserção dos dados de cadastro
def registrar_cadastro(dados: dict, config: dict):
    try:
        conexao = mysql.connector.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.db
        )

    except Exception as e:
        print(f'Houve um problema com o banco: {e}')

    cursor = conexao.cursor()

    try:
        cursor.execute(f'''
                            INSERT INTO usuario(nome, email, senha)
                            VALUES('{dados["nome"]}','{dados["email"]}', '{dados["senha"]}')
                        ''')

        conexao.commit()
        return {
            "status": 200,
            "dados":dados
        }
    except Exception as e:
        print(f'Houve um problema ao inserir no banco: {e}')

        return {
            "status": 400
        }