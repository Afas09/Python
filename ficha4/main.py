from funcoes import carregar_inventario, guardar_inventario, ver_inventario, adicionar_item, atualizar_quantidade, remover_item, pesquisa_avancada, relatorio_stock

def menu():
    FICHEIRO = "inventario.json"
    inventario = carregar_inventario(FICHEIRO)

    while True:
        print("=========== MENU PRINCIPAL ===========")
        print("1 - Ver inventário")
        print("2 - Adicionar item")
        print("3 - Atualizar quantidade")
        print("4 - Remover item")
        print("5 - Pesquisa avançada")
        print("6 - Relatório de stock")
        print("7 - Guardar e sair")
        print("--------------------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_inventario(inventario)
        elif opcao == "2":
            adicionar_item(inventario)
            guardar_inventario(FICHEIRO, inventario)
        elif opcao == "3":
            atualizar_quantidade(inventario)
            guardar_inventario(FICHEIRO, inventario)
        elif opcao == "4":
            remover_item(inventario)
            guardar_inventario(FICHEIRO, inventario)
        elif opcao == "5":
            pesquisa_avancada(inventario)
        elif opcao == "6":
            relatorio_stock(inventario)
        elif opcao == "7":
            guardar_inventario(FICHEIRO, inventario)
            print("Inventário guardado. A sair...")
            break
        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    menu()