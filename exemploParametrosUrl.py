from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

produtos = [
  {"nome":"arroz", "preco":12.20},
  {"nome":"carne", "preco":30.00},
  {"nome":"peixe", "preco":10.10},
  {"nome":"suco", "preco":3.70}
]

#Testarrrrrrrrrrr
class Produto(Resource):
  def get(self):
    if(request.args.get("s")):
      for produto in produtos:
        if(produto["nome"] == request.args.get("s")):
          return {"produto":produto}

    if(request.args.get("s")):
      for produto in produtos:
        if(produto["nome"] == request.args.get("s")):
          return {"produto":produto}

    else:
      return {"produtos":produto}


api.add_resource(Produto, "/produto")

if __name__ == '__main__':
    app.run(debug=True)