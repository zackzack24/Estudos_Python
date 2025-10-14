from classes.AbstractCrud import AbstractCrud

class Produto(AbstractCrud):
    arquivo = 'db/Produto.json'
    def __init__(self, codigo, nome, quantidade= 0, valor= 0):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.valor = valor

    def inserir(self):
        lista = self.consultar()
        produtoDuplicado = [p for p in lista if isinstance(p, dict) and 'codigo' in p and p['codigo'] == self.codigo]
        if len(list(produtoDuplicado)):
            print()
            print("Produto já cadastrado")
            print()
        else: super().inserir()