from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

numeros = [1,2,3]

class ExemploGet1(Resource):
  def get(self):
    return {"numeros":numeros}, 200

class ExemploGet2(Resource):
  def get(self, posicaoNumero):
    return {"numero":numeros[posicaoNumero]}, 200

class ExemploPost(Resource):
  def post(self):
    dados = request.json
    numeros.append(dados["numero"])
    return {"mensagem":"Número inserido"}, 201

class ExemploPut(Resource):
  def put(self):
    global numeros
    dados = request.json
    numeros = dados["novosNumeros"]
    print(numeros, dados)
    return {"mensagem":"Números atualizados"}

class ExemploDelete(Resource):
  def delete(self, posicaoNumero):
    del(numeros[posicaoNumero])
    return {"mensagem":"Número deletado"}

api.add_resource(ExemploGet1, '/')
api.add_resource(ExemploGet2, '/numero/<int:posicaoNumero>')
api.add_resource(ExemploPost, '/insere_numero')
api.add_resource(ExemploPut, '/atualiza_numeros')
api.add_resource(ExemploDelete, '/deleta_numero/<int:posicaoNumero>')

if __name__ == '__main__':
    app.run(debug=True)