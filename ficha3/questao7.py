texto = input("Digite um texto: ")

pontuacoes = ".,:;"
for pontuacao in pontuacoes:
    texto = texto.replace(pontuacao,'')
    
lista = texto.split()
texto = texto.lower()

lista_palavras = {}

for palavra in lista:
    if palavra in lista_palavras.keys:
        lista_palavras[palavra] += 1
    else:
        lista_palavras[palavra] = 1
        
palavras_mais_comuns = sorted(lista_palavras.items(), key=lambda item: item[1])
