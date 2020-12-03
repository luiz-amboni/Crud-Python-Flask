from http import HTTPStatus
from __init__ import app
from service import crud
from flask import request, jsonify, Response

#Mapear
@app.route("/")
def presentation():
    return "N3", HTTPStatus.OK

#Salvar 
@app.route("/insert/person", methods=['POST'])
def save():
    dados_recebidos = request.json
    crud_ = crud()
    crud_.save(dados_recebidos)
    return "Registro salvo.", HTTPStatus.CREATED

#Listar todos 
@app.route("/listar/tudo", methods=['GET'])
def ver_todos():
    toda_lista = crud()
    return jsonify(toda_lista.ver_todos())
    

#Listar CPF
@app.route("/listar/cpf", methods=['GET'])
def listar_cpf():
    dados_recebidos = request.json
    crud_ = crud()
    crud_.listar_cpf(dados_recebidos)
    return jsonify(crud_.listar_cpf(dados_recebidos))


#Update nome
@app.route("/atualizar/nome", methods=['PUT'])
def update_nome():
    dados_recebidos = request.json
    crud_ = crud()
    crud_.update_nome(dados_recebidos)
    return "Nome atualizado", HTTPStatus.CREATED

#Update email
@app.route("/atualizar/email", methods=['PUT'])
def update_email():
    dados_recebidos = request.json
    crud_ = crud()
    crud_.update_email(dados_recebidos)
    return "Email atualizado", HTTPStatus.CREATED

#Excluir
@app.route("/deletar/pessoa", methods=['DELETE'])
def deletar_cpf():
    dados_recebidos = request.json
    crud_ = crud()
    crud_.deletar_cpf(dados_recebidos)
    return "Registro excluído", HTTPStatus.CREATED


if __name__ == "__main__":
    app.run(debug=True)