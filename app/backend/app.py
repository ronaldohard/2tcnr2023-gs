import json
import mysql.connector
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/cadastro": {"origins": "*"}})


db_config = {
    'host': '',
    'user': '',
    'password': '',
    'database': 'db_alunos'
}

def insert_aluno(aluno):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = """
        INSERT INTO tb_alunos
        (aluno_nome, aluno_email, aluno_telefone, aluno_endereco, aluno_curso, aluno_turma, aluno_ano)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        aluno['nome'],
        aluno['email'],
        aluno['telefone'],
        aluno['endereco'],
        aluno['curso'],
        aluno['turma'],
        aluno['ano']
    )
    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

def fetch_alunos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM tb_alunos"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def clear_table():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "TRUNCATE TABLE tb_alunos"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

@app.route('/limpar', methods=['GET'])
def limpar_tabela():
    clear_table()
    return 'Tabela limpa com sucesso!'

@app.route('/cadastro', methods=['POST'])
def cadastro():
    
    aluno = request.get_json()
    print(request.form)

    insert_aluno(aluno)

    return jsonify({'mensagem': 'Dados do aluno recebidos com sucesso!'})

@app.route('/alunos', methods=['GET'])
def get_alunos():
    alunos = fetch_alunos()
    return jsonify(alunos)


@app.route('/')
def index():
    return 'Bem-vindo ao cadastro de alunos!'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)

