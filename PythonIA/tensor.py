import tensorflow as tf
import os # modifica oque podemos receber do sistema operacional, visto no terminal
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'  remove avisos do tensorflow quando o Número 1 é usado.
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # remove tudo, incluindo erros por isso não é recomendado
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # remove avisos do tensorflow e mensagens de informação

class ProdutoEletronicos:
      def __init__(self, marca, nome, preco, categoria):
            self.marca = marca
            self.nome = nome
            self.preco = preco
            self.categoria = categoria
            
produtos = [
      ProdutoEletronicos("Apple", "iPhone 13", 3999.99, "Smartphone"),
      ProdutoEletronicos("Samsung", "Galaxy S21", 2799.99, "Smartphone"),
      ProdutoEletronicos("Motorola", "Edge-25", 2999.99, "Smartphone"),
      ProdutoEletronicos("Google", "Pixel 6", 3499.99, "Smartphone"),
      ProdutoEletronicos("Dell", "XPS 13", 5999.99, "Notebook"),
      ProdutoEletronicos("HP", "Spectre x360", 6499.99, "Notebook"),
      ProdutoEletronicos("Apple", "MacBook Pro", 12999.99, "Notebook"),
      ProdutoEletronicos("Asus", "ROG Zephyrus G14", 7499.99, "Notebook"),
      ProdutoEletronicos("Sony", "WH-1000XM4", 1999.99, "Fone de Ouvido"),
      ProdutoEletronicos("Bose", "QuietComfort 35 II", 1799.99, "Fone de Ouvido"),      
] 

nomes = tf.constant([p.nome for p in produtos])
precos = tf.constant([p.preco for p in produtos]) 
marca = tf.constant([p.marca for p in produtos]) 
# print(nomes, precos)

media = tf.reduce_mean(precos)
# desvio_padrao = tf.math.reduce_std(precos)

eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Apple")) # mostra apenas os produtos da marca Apple
eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Samsung")) # mostra apenas os produtos da marca Samsung
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Motorola")) # mostra apenas os produtos da marca Motorola
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Google")) # mostra apenas os produtos da marca Google
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Dell")) # mostra apenas os produtos da marca Dell
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "HP")) # mostra apenas os produtos da marca HP
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Asus")) # mostra apenas os produtos da marca Asus
# eletronicos = tf.boolean_mask(nomes, tf.equal(marca, "Sony")) # mostra apenas os produtos da marca Sony

print(eletronicos)

     
   


            