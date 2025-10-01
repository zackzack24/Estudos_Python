from sklearn.cluster import  KMeans
import numpy as np

class Produto:
      def __init__(self, nome, preco, peso):
            self.nome = nome
            self.preco = preco
            self.peso = peso
            
produtos = [
      Produto("Arroz", 25, 1.5),
      Produto("Biscoito", 5, 0.5),     
      Produto("Coxinha", 5, 0.5),
      Produto("Damasco", 20, 1.0),
      Produto("Espinafre", 16, 1.0)
]

preco = [[p.preco, p.peso] for p in produtos]
# print(preco)
matriz = np.array(preco)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)
# print(kmeans.labels_) 
# print(kmeans.cluster_centers_)
# print(matriz)

labels = kmeans.labels_
print(labels)

for i in range(2):
      print(f"Grupo {i+1}:")
      for j in range(len(produtos)):
            if labels[j] == i:
                  print(" - ", produtos[j].nome)