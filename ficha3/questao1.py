aluno = {
    'nome': 'Ana Silva',
    'idade': 17,
    'disciplinas': ["Matemática", "Física", "Informática"],
    'notas': {"Matemática": 18, "Física": 17, "Informática": 19},
    'aprovado': True
}

# 1
aluno['disciplinas'].append('Português')
aluno['notas']['Português'] = 16

# 2
aluno['Idade'] = 18

# 3
for disciplina, notas in aluno['notas'].items():
    print(f"Disciplina: {disciplina} Nota: {notas}")

# 4
notas_aluno = aluno['notas']
notas = [nota for nota in notas_aluno.values()]
media = sum(notas)/len(notas)
print(f"Média final = {media:.2f} valores")