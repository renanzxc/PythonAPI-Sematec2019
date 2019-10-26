from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

numeros = [1,2,3]

class ExemploRota1(Resource):
  def get(self):
    return {"numeros":numeros}, 200

  def post(self):
    dados = request.json
    numeros.append(dados["numero"])
    return {"mensagem":"Número inserido"}, 201

  def put(self):
    global numeros
    dados = request.json
    numeros = dados["novosNumeros"]
    return {"mensagem":"Números atualizados"}

class ExemploRota2(Resource):
  def get(self, posicaoNumero):
    return {"numero":numeros[posicaoNumero]}, 200
  
class ExemploRota3(Resource):
  def delete(self, numero):
    for i in range(len(numeros)):
      if numeros[i] == numero:
          del numeros[i]
          return {"resposta": "Número deletado"}, 200

    return {"mensagem":"Número não encontrado"}

api.add_resource(ExemploRota1, '/numeros')
api.add_resource(ExemploRota2, '/numero/<int:posicaoNumero>')
api.add_resource(ExemploRota3, '/deleta_numero/<int:numero>')

if __name__ == '__main__':
    app.run(debug=True)