# tabuleiro.py
import random

def criar_tabuleiro(tamanho=5):
    """Cria uma matriz quadrada vazia do tamanho indicado"""
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_tabuleiro(tabuleiro):
    tamanho = len(tabuleiro)

    # Cabeçalho das colunas
    cabecalho = "    "  # espaço para o índice das linhas
    for i in range(tamanho):
        cabecalho += f" {i} "  # cada coluna tem 3 espaços
    print(cabecalho)

    # Linhas do tabuleiro
    for idx, linha in enumerate(tabuleiro):
        linha_str = f"{idx}  "  # índice da linha com 2 espaços
        for celula in linha:
            linha_str += f"[{celula}]"  # cada célula com colchetes
        print(linha_str)
        
def posicao_aleatoria(tabuleiro):
    """Retorna uma posição aleatória vazia no tabuleiro"""
    tamanho = len(tabuleiro)
    while True:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        if tabuleiro[linha][coluna] == " ":
            return linha, coluna

def posicionar_naves(tabuleiro, naves):
    """Posiciona cada nave em uma posição aleatória no tabuleiro"""
    posicoes = {}
    for nave in naves:
        linha, coluna = posicao_aleatoria(tabuleiro)
        tabuleiro[linha][coluna] = nave.simbolo
        posicoes[nave.simbolo] = (linha, coluna)
    return posicoes

# tabuleiro.py (adicione no final ou perto das outras funções)

def criar_tabuleiro_tiros(tamanho=5):
    """Cria um tabuleiro vazio para marcar os tiros"""
    return [[" " for _ in range(tamanho)] for _ in range(tamanho)]
