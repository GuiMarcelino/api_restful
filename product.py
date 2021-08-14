class Produto():
    def __init__(self, nome, descricao, marca, preco, cor, id=None):
        self.nome_produto = nome
        self.descricao = descricao
        self.marca = marca
        self.preco = preco
        self.cor = cor
        self.id = id