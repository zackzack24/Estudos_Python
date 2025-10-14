from classes.Produto import Produto

def menu():
    print()
    print('1 - Listar Produtos')
    print('2 - Cadastrar Produto')
    print('3 - Atualizar Produto')
    print('4 - Excluir Produto')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1: 
            print()
            print('************************************')
            Produto.listarTodos()
            print('************************************')
            print()
        case 2:
            codigo = input('Digite o código do produto: ')
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade do produto: '))
            valor = int(input('Digite o valor do produto: '))
            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja atualizar?'))
            item = Produto.consultar(selecionado)

            quantidade = int(input('Digite a nova quantidade do produto: '))
            valor = int(input('Digite o novo valor do produto: '))

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)
        case 4:
            Produto.listarTodos()
            selecionado = int(input('Qual item deseja excluir?'))
            Produto.excluir(selecionado)
        case 0:
            print('Saindo...')
            print()