import json
import os


# ================================
# A) CARREGAR E GUARDAR DADOS
# ================================

def carregar_inventario(ficheiro):
    if not os.path.exists(ficheiro):
        return []

    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)
            if isinstance(dados, list):
                return dados
            return []
    except:
        return []


def guardar_inventario(ficheiro, inventario):
    with open(ficheiro, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)


# ================================
# B) FUNÇÕES DO MENU (CRUD)
# ================================

def ver_inventario(inventario):
    if not inventario:
        print("\nInventário vazio.\n")
        return

    print("\n================ INVENTÁRIO ================")
    print(f"{'ID':<5}{'TÍTULO':<25}{'AUTOR':<20}{'QTD':<5}{'PREÇO (€)':<10}")
    print("-" * 65)

    for item in inventario:
        print(f"{item['id']:<5}{item['titulo']:<25}{item['autor']:<20}"
              f"{item['quantidade']:<5}{item['preco']:<10.2f}")
    print()


def adicionar_item(inventario):
    titulo = input("Título: ")
    autor = input("Autor: ")

    # Validação quantidade
    while True:
        quantidade = int(input("Quantidade: "))
        if quantidade >= 0:
            break
        print("Quantidade deve ser um número positivo.")

    # Validação preço
    while True:     
            preco = float(input("Preço: "))
            if preco >= 0:
                break
            print("Preço deve ser positivo.")

    # Gerar ID (sem função auxiliar)
    if inventario:
        novo_id = max(item["id"] for item in inventario) + 1
    else:
        novo_id = 1

    novo_item = {
        "id": novo_id,
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade,
        "preco": preco
    }

    inventario.append(novo_item)
    print("Livro adicionado com sucesso!\n")


def atualizar_quantidade(inventario):
    
    id_item = int(input("ID do livro a atualizar: "))

    for item in inventario:
        if item["id"] == id_item:
            while True:
                nova_qtd = int(input("Nova quantidade: "))
                if nova_qtd >= 0:
                    item["quantidade"] = nova_qtd
                    print("Quantidade atualizada!\n")
                    return
                print("Quantidade inválida.")


def remover_item(inventario):

    id_item = int(input("ID do livro a remover: "))

    for item in inventario:
        if item["id"] == id_item:
            inventario.remove(item)
            print("Livro removido com sucesso!\n")
            return

    print("ID não encontrado.\n")


def pesquisa_avancada(inventario):
    termo = input("Pesquisar por título/autor: ").lower()

    resultados = []
    for item in inventario:
        if termo in item["titulo"].lower() or termo in item["autor"].lower():
            resultados.append(item)

    if resultados:
        ver_inventario(resultados)
    else:
        print("Nenhum livro encontrado.\n")


def relatorio_stock(inventario):

    total = 0
    for item in inventario:
        total += item["quantidade"] * item["preco"]

    print(f"\nValor total do inventário: €{total:.2f}\n")