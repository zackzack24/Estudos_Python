import pandas

cidades = [
      {'nome': 'Distrito Federal', 'uf': 'DF', "população": 89002},
      {'nome': 'São Paulo', 'uf': 'SP', "população": 500000},
      {'nome': 'Rio de Janeiro', 'uf': 'RJ', "população": 3124332},
      {'nome': 'Recife', 'uf': 'PE', "população": 7540002},
]

dataFrame = pandas.DataFrame(cidades)
#print(dataFrame)
ordenada = dataFrame.sort_values(by='população', ascending=False)
print(ordenada) 
print(ordenada.head(2)['nome'])