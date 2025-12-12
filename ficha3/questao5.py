import os, getpass
from inventario import adicionar, atualizar, remover, abaixo_do_stock, valor_total

def menu():
    print(f" ** TODOS OS PROGRAMAS ** ")
    print(f" 1 - Adicionar produtos")
    print(f" 2 - Atualizar a quantidade de um produto")
    print(f" 3 - Remover produtos")
    print(f" 4 - Mostrar os produtos com quantidade inferior a um valor especificado")
    print(f" 5 - Calcular o valor total do inventário")
    print(f" 6 - Mostrar dicionário de produtos")
    print(f" 7 - Sair do programa")
    numero = int(input("Escolha um número para o programa que deseja utilizar: "))
    return numero

inventario = {}
op = menu()

while op > 0 and op < 8:
    if op == 1:
        inventario = adicionar(inventario)
    elif op == 2:
        qtd = int(input("Quantidade atualizada: "))
        inventario = atualizar(inventario, qtd)
    elif op == 3:
        inventario = remover(inventario)
    elif op == 4:
        qtd = int(input("Quantidade considerada abaixo do stock: "))
        inventario = abaixo_do_stock(inventario, qtd)
    elif op == 5:
        print(f"Valor em stock: {valor_total(inventario)}")
    elif op == 6:
        print(inventario)
    else:
        break
    getpass.getpass("Pressione ENTER para voltar ao menu")
    os.system("cls")
    op = menu()
print("Programa terminado")