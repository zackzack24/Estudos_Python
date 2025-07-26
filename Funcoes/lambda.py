numeros = [10, 28, 43, 43, 205]

'''
resultado = []
for n in numeros:
    resultado.append(n*2)

print(numeros, resultado)

def multiplicar(n1):
    return n1 * 2


resultado = map(multiplicar, numeros)
print(numeros, list(resultado))
'''

resultado = map(lambda n: n*2, numeros)
print(numeros, list(resultado))