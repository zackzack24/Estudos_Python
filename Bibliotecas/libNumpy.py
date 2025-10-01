# calculando a media de um número sem a NUMPY

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0

for n in numero:
      #soma = soma + n
      soma += n

media = soma / len(numero)
print(soma)

# calculando a media de um número com a NUMPY
import numpy

array_numero = numpy.array(numero)
numpy.mean(array_numero)
print("Média com numpy :", media)