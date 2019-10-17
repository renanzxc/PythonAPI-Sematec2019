from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

pessoas = [
    {
        "id": 1,
        "nome": "Renan",
        "idade": 19,
        "genero": "M",
        "contato": "(88) 9 9999-9999"
    },
    {
        "id": 2,
        "nome": "Maria",
        "idade": 22,
        "genero": "F",
        "contato": "(88) 9 8888-8888"
    },
    {
        "id": 3,
        "nome": "João",
        "idade": 33,
        "genero": "M",
        "contato": "(88) 9 1111-1111"
    }
]

class ListarPessoas(Resource):
    def get(self):
        return pessoas, 200

class PessoaPorId(Resource):
    def get(self, idPessoa):
        for pessoa in pessoas:
            if(pessoa["id"] == idPessoa):
                return pessoa, 200
        
        return {"erro": "Usuário não encontrado"}, 404

class AdicionarPessoa(Resource):
    def post(self):
        dadosJson = request.json
        pessoas.append(dadosJson)

        return {"message": "Usuário adicionado"}, 201        

class AtualizarPessoa(Resource):
    def put(self, idPessoa):

        for pessoa in pessoas:
            if pessoa["id"] == idPessoa:
                pessoa["nome"] = request.json["nome"]
                pessoa["idade"] = request.json["idade"]
                pessoa["genero"] = request.json["genero"]
                pessoa["contato"] = request.json["contato"]
                return {"message": "Dados atualizados"}, 201

        return {"erro": "Usuário não encontrado"}, 404

class DeletarPessoa(Resource):
    def delete(self, idPessoa):
        for i in range(len(pessoas)):
            if pessoas[i]["id"] == idPessoa:
                del pessoas[i]
                return {"resposta": "Usuário deletado"}, 200
        
        return {"erro": "Usuário não encontrado"}, 404

api.add_resource(ListarPessoas, "/")
api.add_resource(PessoaPorId, "/pessoa/<int:idPessoa>")
api.add_resource(AdicionarPessoa, "/adicionar_pessoa")
api.add_resource(AtualizarPessoa, "/atualizar_pessoa/<int:idPessoa>")
api.add_resource(DeletarPessoa, "/deletar/<int:idPessoa>")

if __name__ == '__main__':
    app.run(debug=True)