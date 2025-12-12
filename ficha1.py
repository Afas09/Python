# FICHA 1
print(f"FICHA 1")

lista = []
for i in range(1,11):
    lista.append(i)

palavras = ["ola", "tchau", "saudade", "assério"]

# ex 1
nums_pares = [i for i in lista if i % 2 == 0]
print(nums_pares)

# ex 2
quadrados = [i*i for i in lista]
print(quadrados)

# ex 3
tamanho_palavras = [len(i) for i in palavras]
print(tamanho_palavras)

# ex 4
nums_maiores_5 = [i for i in lista if i > 5]
print(nums_maiores_5)

# ex 5
nomes = "AndRé FILipe AzeVEdO SiLvA"
maiusculas = [i for i in nomes if i >= 'A' and i <= 'Z']
print(maiusculas)

# ex 6
multiplos_de_3 = [i*2 if i % 3 == 0 else i for i in lista]
print(multiplos_de_3)

# ex 7
nomes_proprios = ["Ana", "Rui", "João", "Mariana", "Alice", "Luana"]
for nome in nomes_proprios:
    if nome.lower().startswith('A'):
        print(nome)
        
# ex 8
frutas = ["banana", "maçã", "laranja", "melancia", "morango"]
comprimento_frutas_mais_5 = [len(frutas) if len(frutas) > 5 else 0 for fruta in frutas]
print(comprimento_frutas_mais_5)