# jogo.py
import time
from nave import NaveModelo, NaveEspecial
from tabuleiro import criar_tabuleiro, mostrar_tabuleiro, posicionar_naves, criar_tabuleiro_tiros
from funcoes import capa, menu, limpar_tela, salvar_jogo, carregar_jogo, disparos_usuario, mostrar_estatisticas

def main():
    tiros_dados = []
    acertos_total = 0
    arquivo_save = "save_jogo.pkl"

    while True:
        limpar_tela()
        capa()
        opcao = menu()

        if opcao == "1":  # Iniciar Jogo
            limpar_tela()
            
            tamanho_tabuleiro = 3  # tamanho desejado do tabuleiro

            # Tabuleiro inicial
            tabuleiro = criar_tabuleiro(tamanho_tabuleiro)

            # Criar naves
            nave1 = NaveEspecial("Falcon", "vermelho", 20, "F", 30)
            nave2 = NaveEspecial("Eagle", "verde", 15, "E", 25)
            nave3 = NaveEspecial("Hawk", "azul", 10, "H", 20)
            naves = [nave1, nave2, nave3]

            energia_extra_usada = False

            # Tabuleiros de tiros
            tabuleiro_tiros_jogador = criar_tabuleiro_tiros(tamanho_tabuleiro)
            tabuleiro_tiros_rodada = criar_tabuleiro_tiros(tamanho_tabuleiro)

            # Posicionar naves da primeira rodada
            naves_posicoes = posicionar_naves(tabuleiro, naves)

            tiros_dados.clear()
            acertos_total = 0

            # ---------- LOOP DAS RODADAS ----------
            while True:
                # MOSTRAR TABULEIROS INICIAIS (ANTES DOS TIROS)
                limpar_tela()
                
                print("\nTABULEIRO PARA A PRÓXIMA RODADA:")
                mostrar_tabuleiro(tabuleiro_tiros_jogador)

                # JOGADOR FAZ OS 3 DISPAROS
                tiros = disparos_usuario(tabuleiro_tiros_jogador)
                tiros_dados.extend(tiros)

                # CALCULAR ACERTOS
                acertos = 0
                for tiro in tiros:
                    for nave in naves:
                        pos_nave = naves_posicoes.get(nave.simbolo)
                        if pos_nave == tiro and nave.energia > 0:
                            nave.perder_energia()
                            acertos += 1

                acertos_total += acertos

                # MARCAR TIROS DA RODADA
                tabuleiro_tiros_rodada = criar_tabuleiro_tiros(tamanho_tabuleiro)
                for tiro in tiros:
                    tabuleiro_tiros_rodada[tiro[0]][tiro[1]] = "X"

                # MOSTRAR FINAL DA RODADA
                limpar_tela()
                print("POSIÇÕES DAS NAVES NESTA RODADA:")
                mostrar_tabuleiro(tabuleiro)
                
                print("\nTIROS REALIZADOS NESTA RODADA:")
                mostrar_tabuleiro(tabuleiro_tiros_rodada)

                mostrar_estatisticas(naves, tiros_dados, acertos_total)

                # ENERGIA EXTRA APÓS 45 TIROS
                if len(tiros_dados) >= 45 and not energia_extra_usada:
                    for nave in naves:
                        if isinstance(nave, NaveEspecial):
                            nave.adicionar_energia_extra()
                    energia_extra_usada = True

                # REMOVER NAVES MORTAS DO TABULEIRO
                for nave in naves:
                    if nave.energia <= 0:
                        pos = naves_posicoes.get(nave.simbolo)
                        if pos:
                            tabuleiro[pos[0]][pos[1]] = " "

                # ---------- COMEÇAR NOVA RODADA ----------
                input("\nPressione Enter para continuar para a próxima rodada...")

                # Criar tabuleiro vazio para naves da próxima rodada
                tabuleiro = criar_tabuleiro(tamanho_tabuleiro)

                # Reset tabuleiro dos tiros do jogador
                tabuleiro_tiros_jogador = criar_tabuleiro_tiros(tamanho_tabuleiro)

                # Reposicionar apenas naves vivas
                vivas = [nave for nave in naves if nave.energia > 0]
                naves_posicoes = posicionar_naves(tabuleiro, vivas)

                # FIM DO JOGO
                if len(tiros_dados) >= 105 or all(nave.energia <= 0 for nave in naves):
                    print("\nFIM DO JOGO!")
                    break

        elif opcao == "2":
            dados = carregar_jogo(arquivo_save)
            if dados:
                tiros_dados, acertos_total, naves, tabuleiro, naves_posicoes = dados

        elif opcao == "3":
            dados = (tiros_dados, acertos_total, naves, tabuleiro, naves_posicoes)
            salvar_jogo(arquivo_save, dados)

        elif opcao == "4":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)


if __name__ == "__main__":
    main()