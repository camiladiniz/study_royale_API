
from flask import Flask, jsonify, request
import json
import urllib.request
import random

app = Flask(__name__)

students = [
    {"ra": "11111", "senha": "123"},
    {"ra": "22222", "senha": "123"},
    {"ra": "33333", "senha": "123"},
    {"ra": "44444", "senha": "123"},
    {"ra": "55555", "senha": "123"},
    {"ra": "66666", "senha": "123"},
    {"ra": "aluno", "senha": "impacta"},
]

atividades = [ { "id": 1, "codigo": 10, "nome": "Publicar tweet API Twitter", "disciplina": "IOT", "professor": "Leonardo", "alunos": [ { "nome": "Camila", "ra": "11111", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 10 }, { "nome": "Christian", "ra": "22222", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 9 }, { "nome": "Cláudio", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 8 }, { "nome": "Gustavo", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 7 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 6 } ] }, { "id": 2, "codigo": 100, "nome": "Fazer POC", "disciplina": "Arquitetura", "professor": "Antonio", "alunos": [ { "nome": "Camila", "ra": "11111", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 6 }, { "nome": "Christian", "ra": "22222", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 7 }, { "nome": "Cláudio", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 8 }, { "nome": "Gustavo", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 9 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 10 } ] }, { "id": 3, "codigo": 10, "nome": "Publicar tweet API Twitter", "disciplina": "IOT", "professor": "Leonardo", "alunos": [ { "nome": "Camila", "ra": "11111", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 10 }, { "nome": "Christian", "ra": "22222", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 9 }, { "nome": "Cláudio", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 8 }, { "nome": "Gustavo", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 7 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 6 } ] }, { "id": 4, "codigo": 100, "nome": "Fazer POC", "disciplina": "Arquitetura", "professor": "Antonio", "alunos": [ { "nome": "Gustavo", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 9 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 10 } ] }, { "id": 5, "codigo": 10, "nome": "Publicar tweet API Twitter", "disciplina": "IOT", "professor": "Leonardo", "alunos": [ { "nome": "Camila", "ra": "11111", "foto": "https://lh3.googleusercontent.com/a/AATXAJwEETMgN3OBQa-SqYjF5pY7CzRrINR0Q_VJfxDz=s192-c-mo", "nota": 10 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 6 } ] }, { "id": 6, "codigo": 100, "nome": "Fazer POC", "disciplina": "Arquitetura", "professor": "Antonio", "alunos": [  { "nome": "Cláudio", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 8 }, { "nome": "Gustavo", "ra": "33333", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 9 }, { "nome": "Leoni", "foto": "https://lh3.googleusercontent.com/a-/AOh14GgEG1eY9dg-TmoB5CcW1vEoZ69x-wkTOT5aCRU0zw=s192-c-mo", "nota": 10 } ] } ];


@app.route("/atividades", methods=['GET'])
def getAtividades():
    return jsonify(atividades)

@app.route("/login", methods=['POST'])
def autenticar():
    payload = request.get_json()

    aluno = [e for e in students if payload["ra"] == e['ra']]

    if aluno :
        if aluno[0]['senha'] == payload['senha'] :
            return jsonify({'sucesso': True})
        return jsonify({'sucesso': False})

    else:
        return jsonify({'sucesso': False})


@app.route("/atividades/<int:id>", methods=['POST'])
def postAtividade(id):
    global atividades
    try:
        content = request.get_json()

        atividade = [e for e in atividades if e["id"] == id]

        if(len(atividade) > 0):
            print(atividade[0])
            atividade[0]['alunos'].append(content)
            return jsonify({"sucesso":True, "msg":"Nota adicionada com sucesso"})
        return jsonify({"sucesso":True, "msg":"Atividade não encontrada"})
    except Exception as ex:
        return jsonify({"sucesso":False, "msg":str(ex)}) 

if __name__ == "__main__":
    app.run(host='0.0.0.0')