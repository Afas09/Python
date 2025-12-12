from math import sqrt
class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        
    def formarTriangulo(self):
        c1 = self.lado1 > self.lado2 + self.lado3
        c2 = self.lado2 > self.lado1 + self.lado3
        c3 = self.lado3 > self.lado1 + self.lado2
        return c1 and c2 and c3
    
    def perimetro(self):
        p = self.lado1 + self.lado2 + self.lado3
        return p
    
    def area(self):
        p = self.perimetro() / 2
        return sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))
    
    def tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return 'Equilátero'
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return 'Isósceles'
        return 'Escaleno'
    
class Retangulo:
    def __init__(self, lado1, lado2, cor):
        self.lado1 = lado1
        self.lado2 = lado2
        self.cor = cor
        
    def quadrado(self):
        return self.lado1 == self.lado2
    
    def diagonal(self):
        return sqrt(pow(self.lado1,2) + pow(self.lado2,2))
    
    def perimetro(self):
        return 2 * self.lado1 + 2 * self.lado2
    
    def mesmoPerimetro(self,rect):
        if not isinstance(rect, Retangulo):
            return False
        return self.perimetro() == rect.perimetro()
    
    def mesmaCor(self, rect):
        if not isinstance(rect, Retangulo):
            return False
        return self.cor == rect.cor
    
class ComandoTV:
    def __init__(self, marca, anoFabrico, canal, volume, ligado):
        self.marca = marca
        self.anoFabrico = anoFabrico
        self.__canal = canal
        self.__volume = volume
        self.ligado = ligado
    
    # Getter para o canal
    @property
    def canal(self):
        return self.__canal
    
    # Setter para canal
    @canal.setter
    def canal(self, novo_canal):
        if novo_canal < 1 and novo_canal > 99:
            print("Canal inválido")
        self.__canal = novo_canal
        
    # Getter para o volume
    @property
    def volume(self):
        return self.__volume
    
    # Setter para volume
    @volume.setter
    def volume(self, novo_volume):
        if novo_volume < 0 and novo_volume > 20:
            print("volume inválido")
        self.__volume = novo_volume
    
    def trocarCanal(self, canal):
        if canal >= 1 and canal <= 99:
            return canal
        else:
            print(f"Só existe do canal 1 até ao 99, ficou no mesmo canal")
            return self.canal
    
    def alterarVolume(self, tecla):
        if tecla == '+':
            if self.volume < 20:
                return self.volume + 1
        elif tecla == '-':
            if self.volume > 0:
                return self.volume - 1
        else: 
            return self.volume

    def volume0(self):
        self.volume = 0
        return self.volume
    
    def ligar(self):
        if self.ligado:
            return False
        return True
    
    def dados_comando(self):
        return f"MARCA: {self.marca} ANO FABRICO: {self.anoFabrico} CANAL: {self.canal} VOLUME: {self.volume} LIGADO/DESLIGADO: {self.ligado}"
    
# TESTE DO SISTEMA - TRIANGULO
t = Triangulo(10,15,11)
if t.formarTriangulo():
    print(f"Perímetro: {t.perimetro()}")
    print(f"Área: {t.area():.2f}")
    print(t.tipo())
    
# TESTE DO SISTEMA - COMANDO
c = ComandoTV("LG", 2019, 11, 5, False)
c.trocarCanal(23)
c.alterarVolume('+')
c.volume0()
c.ligar()
c.dados_comando()