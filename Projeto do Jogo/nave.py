# naves.py
class NaveModelo:
    def __init__(self, denominacao, cor, perda_energia, simbolo):
        self.denominacao = denominacao  # Nome da nave
        self.cor = cor                  # Cor da nave (para exibir)
        self.energia = 100              # Energia inicial
        self.perda_energia = perda_energia
        self.simbolo = simbolo          # Letra da nave

    def perder_energia(self):
        """Reduz a energia da nave pela perda_energia e retorna a energia atual"""
        self.energia -= self.perda_energia
        if self.energia < 0:
            self.energia = 0
        return self.energia

    def energia_atual(self):
        """Retorna a energia atual da nave"""
        return self.energia


class NaveEspecial(NaveModelo):
    def __init__(self, denominacao, cor, perda_energia, simbolo, energia_extra):
        super().__init__(denominacao, cor, perda_energia, simbolo)
        self.energia_extra = energia_extra

    def mostrar_dados(self):
        """Mostra os dados da nave com cor"""
        # Para simplificação vamos usar códigos ANSI para cores no terminal
        cores = {
            "vermelho": "\033[91m",
            "verde": "\033[92m",
            "amarelo": "\033[93m",
            "azul": "\033[94m",
            "reset": "\033[0m"
        }
        cor_texto = cores.get(self.cor.lower(), cores["reset"])
        print(f"{cor_texto}Nave: {self.denominacao} | Energia: {self.energia} | Símbolo: {self.simbolo}{cores['reset']}")

    def adicionar_energia_extra(self):
        """Adiciona energia extra sem ultrapassar o máximo de 100"""
        self.energia += self.energia_extra
        if self.energia > 100:
            self.energia = 100
