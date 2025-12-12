# Exercício 01
# Crie um programa que peça o comprimento e a largura
# de um retângulo e mostre a área e o perímetro

# Exercício 02
# Crie uma lista com 10 números e imprima apenas os números pares

# Exercício 03
# Crie um dicionário em que as chaves sejam nomes de produtos.
# Os valores sejam o preço de cada produto.
# Deve devolver o produto mais caro e a média dos preços.


# Exercício 01
print("\nEXERCÍCIO 1")

comprimento = float(input("Digite o comprimento do retângulo: "))
largura = float(input("Digite a largura do retângulo: "))
area = comprimento * largura
perimetro = comprimento * 2 + largura * 2
print(f"A área do retângulo é igual a {area}")
print(f"O perímetro do retângulo é igual a {perimetro}")


# Exercício 02
print("\nEXERCÍCIO 2")

nums = [1,8,5,12,23,7,18,2,9,6]

print(f"Números pares: ")

for i in nums:
    if i% 2 == 0:
        print(i, end = ", ")
        

# Exercício 03
print("\nEXERCÍCIO 3")

produtos = {"Lápis": 1.00, "Porta-Lápis": 5.50, "Borracha": 1.54, "Caneta": 2.03}
soma = 0
preco_maior = 0
produto_caro = ""
for produto, preco in produtos.items():
    soma = soma + preco
    if preco > preco_maior:
        preco_maior = preco
        produto_caro = produto

media = soma / len(produtos)

print(f"O produto mas caro é {produto_caro}")
print(f"A média dos produtos é {media:.2f}")