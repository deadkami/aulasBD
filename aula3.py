import mysql.connector

def conectar_ao_mysql(host, usuario, senha, banco_de_dados):
    try:
        # Conectar ao MySQL
        conexao = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "1234",
            database = "HelloWorldMySQL"
        )

        if conexao.is_connected():
            print("Conexão ao MySQL bem-sucedida.")
            return conexao

    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")

def criar_tabela_rh(conexao):
    try:
        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Definir o comando SQL para criar a tabela de RH
        comando_sql = """
        CREATE TABLE IF NOT EXISTS rh (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(255) NOT NULL,
            cargo VARCHAR(255) NOT NULL,
            salario DECIMAL(10, 2) NOT NULL
        )
        """

        # Executar o comando SQL
        cursor.execute(comando_sql)

        # Confirmar as alterações no banco de dados
        conexao.commit()

        print("Tabela de RH criada com sucesso.")

    except mysql.connector.Error as e:
        print(f"Erro ao criar a tabela de RH: {e}")

    finally:
        # Fechar o cursor
        if cursor:
            cursor.close()

def inserir_registro(conexao, nome, cargo, salario):
    try:
        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Definir o comando SQL para inserir um novo registro
        comando_sql = """
        INSERT INTO rh (nome, cargo, salario) VALUES (%s, %s, %s)
        """

        # Dados a serem inseridos
        dados = (nome, cargo, salario)

        # Executar o comando SQL
        cursor.execute(comando_sql, dados)

        # Confirmar as alterações no banco de dados
        conexao.commit()

        print("Registro inserido com sucesso.")

    except mysql.connector.Error as e:
        print(f"Erro ao inserir registro: {e}")

    finally:
        # Fechar o cursor
        if cursor:
            cursor.close()

def buscar_registros(conexao):
    try:
        # Criar um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Definir o comando SQL para buscar todos os registros
        comando_sql = """
        SELECT * FROM rh
        """

        # Executar o comando SQL
        cursor.execute(comando_sql)

        # Recuperar todos os registros
        registros = cursor.fetchall()

        # Exibir os registros
        for registro in registros:
            print(registro)

    except mysql.connector.Error as e:
        print(f"Erro ao buscar registros: {e}")

    finally:
        # Fechar o cursor
        if cursor:
            cursor.close()

# Exemplo de uso das funções
conexao_mysql = conectar_ao_mysql("seu_host", "seu_usuario", "sua_senha", "seu_banco_de_dados")

if conexao_mysql:
    criar_tabela_rh(conexao_mysql)

    # Inserir registros de exemplo
    inserir_registro(conexao_mysql, "João Silva", "Analista de RH", 5000.00)
    inserir_registro(conexao_mysql, "Maria Oliveira", "Gerente de RH", 8000.00)

    # Buscar e exibir todos os registros
    buscar_registros(conexao_mysql)

    conexao_mysql.close()
