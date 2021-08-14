from flask import Flask, app, request, jsonify
from flask_restful import Resource, Api, reqparse



app = Flask(__name__)
api = Api(app)



@app.route('/', methods=['get'])
def pagina_inicial():
    return render_template('index.html')


@app.route('/cadastro', methods=['get'])
def cadastro():
    return render_template("cadastro.html")
    

@app.route('/inserir', methods=['POST'])
def inserir():
    produto = Produto(request.form['nome_produto'],
                    request.form['descricao'],
                    request.form['marca'],
                    request.form['preco'],
                    request.form['cor'])
    db = conexao()
    insert(db, produto)
    return redirect('/cadastro')


@app.route('/deletar', methods=['GET'])
def deletar():
    id = int(request.args['id'])
    db = conexao()
    delete(db, id)
    return redirect('/selecionar/todos/')


@app.route('/selecionar/id', methods=['GET'])
def selecionar_id():
    return render_template('selecionar_id.html')


@app.route('/visualizar', methods=['POST'])
def visualizar_id():
    id = request.form['id']
    return redirect(f'/listar/{id}/')


@app.route('/listar/<int:id>/', methods=['GET'])
def listar_por_id(id):
    db = conexao()
    registro = select_id(db, id)
    novo_produto = Produto(
        id=registro[0],
        nome=registro[1],
        descricao=registro[2],
        marca=registro[3],
        preco=registro[4],
        cor=registro[5])
    return render_template("listar.html", produto= novo_produto)


@app.route('/selecionar/todos/', methods=['GET'])
def selecionar_produtos():
        db = conexao()
        resultado = select(db)
        lista_produtos = []
        for index in resultado:
            lista_produtos.append(Produto(
                id=index[0],
                nome=index[1],
                descricao=index[2],
                marca=index[3],
                preco=index[4],
                cor=index[5]))
        return render_template("listar_todos.html", lista_banco_no_html= lista_produtos)


@app.route('/alterar')
def alterar():
    id = int(request.args['id'])
    db = conexao()
    registro = select_id(db, id)
    novo_produto = Produto(
        id=registro[0],
        nome=registro[1],
        descricao=registro[2],
        marca=registro[3],
        preco=registro[4],
        cor=registro[5])
    return render_template('alterar_produto.html', registro = novo_produto)

@app.route('/alterar/salvar', methods= ["POST"])
def alterar_salvar():
    
    produto = Produto(request.form['nome_produto'],
                    request.form['descricao'],
                    request.form['marca'],
                    request.form['preco'],
                    request.form['cor'],
                    request.form['id'])
    db = conexao()
    update(db, produto)
    return redirect('/selecionar/todos/')

app.run(debug=True)