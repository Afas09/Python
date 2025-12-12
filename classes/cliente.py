class Cliente:
    totalCliente = 0
    def __init__(self, nome, altura, peso, vip=False):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.vip = vip
        
    def imc(self):
        return self.peso / (self.altura * self.altura)
    
c1 = Cliente("André", 1.71, 58, True)
Cliente.totalCliente += 1
c2 = Cliente("Henrique", 1.01, 102)
Cliente.totalCliente += 1
print(c1.nome)
if c2.vip:
    print("Cliente VIP")
else:
    print("Ciente normal")
print(c1.imc())