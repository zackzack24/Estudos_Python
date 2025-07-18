try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))

    resultado = n1/n2

    print(f'O resultado da divisão é: {resultado}')

except ZeroDivisionError:
    print('Erro: Divisão por zero não é permitida.')

except ValueError:
    print('Erro: Entrada inválida. Por favor, insira números inteiros.')

except Exception:
    print('Erro: Ocorreu um erro inesperado.')

else:
    print('O programa foi executado corretamente!')

finally:
    print('Fim')
