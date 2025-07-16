numeros = [10, 20, 30, 17, 58, 3, 7]    
# print(numeros[5])

carros =["Palio", "Fusca", "Civic", "Onix", "Gol", "Palio", "Fusca", "Civic", "Onix", "Gol", "Palio",]
print('1 ->', carros)

carros.append("Corsa")
print('2 ->',carros)

carros.remove("Fusca")
print('3 ->',carros)

del carros[3]
print('4 ->',carros)

carros = sorted(carros)
print('5 ->',carros)

carros.append("Civic")
print('6 ->',carros)

carros.append("Corolla")
print('7 ->',carros)

print(carros[0])
print(carros[1])
print(carros[2])
print(carros[3])
print(carros[4])
print(carros[5])

for item in carros:
    print(item)
