from flask import Flask, app, request, jsonify
from flask_restful import Resource, Api, reqparse
from repository import *
from product import Produto


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('nome', type=str)
parser.add_argument('descricao', type=str)
parser.add_argument('marca', type=str)
parser.add_argument('preco', type=float)
parser.add_argument('cor', type=str)

def converte_produto_to_dict(produto):
    produto_dict = {}
    for attr in vars(produto):
        attr_value = getattr(produto, attr)
        produto_dict[attr] = attr_value
    return produto_dict


class BancoDeDados(Resource):
    def get(self):
        db = conexao()        
        resultado = select(db)
        lista_produtos = []
        for index in resultado:
            lista_produtos.append(
                converte_produto_to_dict(
                    Produto(
                        id=index[0],
                        nome=index[1],
                        descricao=index[2],
                        marca=index[3],
                        preco=float(index[4]),
                        cor=index[5]
                    )
                )
            )
        return jsonify(lista_produtos)


    def delete(self):
        args = parser.parse_args()
        db = conexao()
        delete(db, args['id'])
        return 'Produto Deletado com sucesso!!!'


    def post(self):
        args = parser.parse_args()
        db = conexao()
        insert(db, args['nome', 'descricao', 'marca', 'preco', 'cor'])
        return 'Produto Cadastrado com sucesso!!!'


api.add_resource(BancoDeDados, '/')

if __name__ == "__main__":
    app.run(debug=True)
