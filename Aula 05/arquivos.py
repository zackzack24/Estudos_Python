arquivo = open('pessoas.txt', 'a+')

arquivo.write('Isaac\n')
arquivo.write('Joao\n')
arquivo.write('Soraya\n')

arquivo.close()

with open('pessoas.txt', 'r') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)