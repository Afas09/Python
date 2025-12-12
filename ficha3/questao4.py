# 1
quadrados = {x: x*x for x in range(1, 11)}

# 2
palavras = ["ola", "saudade", "tudo", "adeus"]
comprimentos_palavras = {palavra: len(palavra) for palavra in palavras}

# 3
notas = {"Ana": 18, "Bruno": 15, "Carla": 17,"David": 12, "Eva": 19}
superior_igual_15 = {aluno: nota for aluno, nota in notas.items() if nota >= 15}