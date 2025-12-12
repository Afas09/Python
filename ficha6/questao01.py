class Veiculo:
    total_veiculos = 0
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        Veiculo.total_veiculos += 1

    # Getters 
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo

    @property
    def ano(self):
        return self._ano

    # Setters
    @marca.setter
    def marca(self, nova_marca):
        if len(nova_marca) < 2:
            print("marca inválido")
        self._marca = nova_marca
        
    @modelo.setter
    def modelo(self, novo_modelo):
        if len(novo_modelo) < 2:
            print("modelo inválido")
        self._modelo = novo_modelo
        
    @ano.setter
    def ano(self, novo_ano):
        if novo_ano < 0 and novo_ano > 2025:
            print("ano inválido")
        self._ano = novo_ano

    def descrever(self):
        return f"Veículo: Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas
        Veiculo.total_veiculos += 1

    # Getter
    @property
    def portas(self):
        return self._portas

    # Setter
    @portas.setter
    def portas(self, novas_portas):
        if novas_portas <= 0:
            print("Número de portas inválido")
        self._portas = novas_portas

    def descrever(self):
        return f"Carro: Marca: {self._marca}, Modelo: {self._modelo}, Ano: {self._ano}, Portas: {self._portas}"


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
        Veiculo.total_veiculos += 1

    # Getter
    @property
    def cilindrada(self):
        return self._cilindrada

    # Setter
    @cilindrada.setter
    def cilindrada(self, nova_cilindrada):
        if nova_cilindrada <= 0:
            print("Número de cilindrada inválido")
        self._cilindrada = nova_cilindrada

    # Sobrescrita do método
    def descrever(self):
        return f"Moto: Marca: {self._marca}, Modolo: {self._modelo}, Ano: {self._ano}, {self._cilindrada}cc"
