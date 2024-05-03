#faça a ligação entre Carro tem um motor


# crie uma classe carro (Nome)
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self.Motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor
        
    @property
    def fabricante(self):
        return self._motor
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor
        
#crie um classe motor (Nome)
class Motor:
    def __init__(self, nome):
        self.nome = nome
        
#crie uma classe fabricante
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        
fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

