import matplotlib.pyplot as plt

# meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho']
# valoresAdm = [344, 553, 695, 987, 865, 346, 168]
# valoresTi = [664, 63, 57, 76, 67, 14, 63]

# plt.plot(meses, valoresAdm, label="Adm", color= "orange") #marker= "o" 
# plt.plot(meses, valoresTi, label="TI", color= "red") #marker= "x"  
# plt.bar("meses", "chamados")
# plt.title("Chamados da Ti e da Adm")
# plt.xlabel("meses")
# plt.ylabel("Quantidade de Chamados")
# plt.legend()
# plt.show()

plt.title("Uso de Navegadores em 2024")
navegadores = ['Chrome', 'Firefox', 'Edge',]
uso = [64.06, 4.12, 3.45]
plt.pie(uso, labels=navegadores)

plt.axis('equal')
plt.show()