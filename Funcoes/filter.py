numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#print(2 % 1)
#def impar(n):
    #return n % 2 == 0

resultado = filter(lambda n: n % 2 == 1, numeros)
print(numeros, list(resultado))