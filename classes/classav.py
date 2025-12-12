class Pessoa:
    total_pessoas = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.total_pessoa += 1
        
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos"
    
    # Getter para o nome da pessoa
    @property
    def nome(self):
        return self.__nome
    
    # Setter para nome
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) < 2:
            print("Nome inválido")
        self.__nome = novo_nome

    # Getter para a idade da pessoa
    @property
    def idade(self):
        return self.__idade
    
    # Setter para idade
    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválido")
        self.__idade = nova_idade
    
# Área de teste
p1 = Pessoa("Henrique", 16)
p2 = Pessoa("António", 62)
p3 = Pessoa("João", 12)

print(Pessoa)