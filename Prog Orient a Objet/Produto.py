class Produto:
    def __init__(self, nome, preco, quantidade, marca):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.marca = marca
    
    def vender(self, quantidade):
        if self.quantidade >= quantidade:
            self.quantidade -= quantidade
            print("Venda realizada com sucesso!")
            print("Quantidade restante: ", self.quantidade)
        else:
            print("Quantidade insuficiente em estoque!")
    
    def comprar(self, quantidade):
        self.quantidade += quantidade
        print(f"Compra realizada. Novo estoque: {self.quantidade}")

# Criando instâncias da classe Produto
produto0 = Produto("Notebook", 3500.00, 50, "Dell")
produto1 = Produto("Smartphone", 1500.00, 200, "Samsung")
produto2 = Produto("Tablet", 3500.00, 20, "Apple")

# Imprimindo os atributos dos objetos
print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)