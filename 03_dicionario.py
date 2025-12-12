idades_alunos = {"Rui": 17, "Ana": 19, "Carlos": 21}
# Imprimir dicionario
print(idades_alunos)
# Imprimir chaves do dicionarios
for nome in idades_alunos.keys():
    print(nome)
# Imprimir valores do dicionario
for idade in idades_alunos.values():
    print(idade)
    
# Imprimir chaves e valores
for k,v in idades_alunos.items():
    print(f"O(A) aluno(a) {k} tem {v} anos.")