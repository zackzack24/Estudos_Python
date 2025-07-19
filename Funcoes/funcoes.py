'''
try:
    resultado = n1 / n2

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

except Exception:
    print("Ocorreu um erro ao dividir os números.")]
'''

def somar(n1, n2):
    return n1 + n2,

def subtrair(n1, n2):
    return n1 - n2,

def multiplicar(n1, n2):
    return n1 * n2,

def dividir(n1, n2):
   if n2 == 0:
    return ("Não é possível dividir por zero.")
   else:
    resultado = n1/n2
    print(f'O resultado da divisão é {resultado}')
    return resultado 
   
def calcular(n1, n2, operador):
    match operador:
       
        case '+':return somar(n1, n2)
       
        case '-':return subtrair(n1, n2)
       
        case '*':return multiplicar(n1, n2)
       
        case '/':return dividir(n1, n2)
       
        case other: return "Operador não encontrado"
            
'''  
print(somar(900, 700))
print(subtrair(900, 700))
print(multiplicar(900, 700))
print(dividir(900, 700))
'''

'''   
divisao = dividir(5, 80) 
print(f'O resultado da divisão é {divisao}')


divisao = dividir(50, 800)
print(f'O resultado da divisão é {divisao}') 

divisao = dividir(550, 8800) 
print(f'O resultado da divisão é {divisao}')

divisao = dividir(750, 220) 
print(f'O resultado da divisão é {divisao}')
'''
