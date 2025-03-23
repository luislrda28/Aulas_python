class veiculo:
    def __init__(self, cor, placa, numero_de_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_de_rodas = numero_de_rodas

    def ligar_motor(self):
        print("Ligando motor...")
        print("Motor ligado")

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"
        

class motocicleta(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, carregado, cor, placa, numero_de_rodas):
        self.carregado = carregado
        super().__init__(cor, placa, numero_de_rodas)

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} carregado")

class carro(veiculo):
    pass

moto = motocicleta("preta", "ABC-1234", 2)
caminhao = caminhao("branco", "DEF-5678", 6, False)
carro = carro("vermelho", "GHI-9101", 4)

print(moto)
print(caminhao)
print(carro)
