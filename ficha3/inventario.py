def adicionar(inv):
    nome = input("Nome do produto: ")
    if nome in inv.keys():
        print("Produto já pertence ao inventário")
        return inv
    inv[nome] = {}
    inv[nome]['qtd'] = int(input("Quantidade do produto: "))
    inv[nome]['preço'] = float(input("Preço do produto: "))
    return inv

def atualizar(inv, qt):
    produto = input("Nome do produto que deseja atualizar: ")
    if produto not in inv.keys():
        print("Produto não existe mo inventário")
        return inv
    inv[produto]['qtd'] = qt
    return inv
    
def remover(inv):
    produto = input("Nome do produto que deseja remover: ")
    if produto not in inv.keys():
        print("Produto não existe mo inventário")
        return inv
    del inv[produto]
    return inv

def abaixo_do_stock(inv, qt):
    for produto, dados in inv.items():
        if dados['qtd'] < qt:
            print(produto)
            
def valor_total(inv):
    total = 0
    for dados in inv.values():
        total += dados['qtd'] * dados['preço']
        return total