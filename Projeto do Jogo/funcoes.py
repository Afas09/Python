# funcoes.py
import pickle
import os
import random
from nave import NaveModelo, NaveEspecial
from tabuleiro import criar_tabuleiro, mostrar_tabuleiro, posicionar_naves, posicao_aleatoria

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def capa():
    """Mostra a capa do jogo"""
    print("="*40)
    print("       JOGO DE NAVE ESPACIAL")
    print("="*40)

def menu():
    """Exibe o menu e retorna a opção escolhida"""
    print("\nMENU")
    print("1 - Iniciar Jogo")
    print("2 - Carregar Jogo")
    print("3 - Guardar Jogo")
    print("4 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def salvar_jogo(nome_arquivo, dados):
    """Salva o estado do jogo em arquivo"""
    with open(nome_arquivo, "wb") as f:
        pickle.dump(dados, f)
    print("Jogo salvo com sucesso!")

def carregar_jogo(nome_arquivo):
    """Carrega o estado do jogo de arquivo"""
    try:
        with open(nome_arquivo, "rb") as f:
            dados = pickle.load(f)
        print("Jogo carregado com sucesso!")
        return dados
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return None

def disparos(tabuleiro, naves_posicoes, naves_objetos, tiros_dados):
    """Realiza 3 disparos (aleatórios) e atualiza energia das naves"""
    tamanho = len(tabuleiro)
    tiros = []
    acertos = 0

    for _ in range(3):
        while True:
            linha = random.randint(0, tamanho - 1)
            coluna = random.randint(0, tamanho - 1)
            if (linha, coluna) not in tiros:
                tiros.append((linha, coluna))
                break

    for tiro in tiros:
        for nave in naves_objetos:
            pos_nave = naves_posicoes.get(nave.simbolo)
            if pos_nave == tiro and nave.energia > 0:
                nave.perder_energia()
                acertos += 1

    tiros_dados.extend(tiros)
    return tiros, acertos

def mostrar_estatisticas(naves_objetos, tiros_dados, acertos_total):
    """Mostra estatísticas do jogo"""
    print("\nDADOS DAS NAVES:")
    for nave in naves_objetos:
        if isinstance(nave, NaveEspecial):
            nave.mostrar_dados()
        else:
            print(f"Nave: {nave.denominacao} | Energia: {nave.energia} | Símbolo: {nave.simbolo}")

    total_tiros = len(tiros_dados)
    eficiencia = (acertos_total * 100 / total_tiros) if total_tiros > 0 else 0
    print(f"\nTotal de tiros dados: {total_tiros}")
    print(f"Total de tiros certeiros: {acertos_total}")
    print(f"Eficácia: {eficiencia:.2f}%")

def disparos_usuario(tabuleiro):
    """Permite que o usuário escolha 3 disparos válidos"""
    tamanho = len(tabuleiro)
    tiros = []

    while len(tiros) < 3:
        try:
            entrada = input(f"Digite as coordenadas do tiro {len(tiros)+1} (linha,coluna): ")
            linha, coluna = map(int, entrada.split(","))
            if linha < 0 or linha >= tamanho or coluna < 0 or coluna >= tamanho:
                print("Coordenadas inválidas! Tente novamente.")
                continue
            if (linha, coluna) in tiros:
                print("Você já escolheu essa posição nesta rodada! Tente outra.")
                continue
            tiros.append((linha, coluna))
        except ValueError:
            print("Formato inválido! Digite como linha,coluna (ex: 1,2).")
    return tiros
