from flask import Flask, request, jsonify
from Usuario import Usuario
import database as db

app = Flask(__name__)


@app.route('/', methods=['GET'])
def teste():
    return 'a'

@app.route('/criar_usuario', methods=['POST'])
def criar_usuario():
    nome = request.get_json()['nome']
    documento = request.get_json()['documento']
    data_nascimento = request.get_json()['dataNasc']
    email = request.get_json()['email']
    print(nome)

    user = Usuario()
    user.novo_usuario(nome, documento, email, data_nascimento)
    print(user)
    db.create_user(user)
    return jsonify({"message": "Usuário criado com sucesso"}), 201

app.run()