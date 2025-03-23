class Animal:
    def __init__(self, raça, cor, nome):
        self.raça = raça
        self.cor = cor
        self.nome = nome

class Mamifero(Animal):
    def __init__(self, raça, cor, nome, numero_de_mamas):
        self.numero_de_mamas = numero_de_mamas
        super().__init__(raça, cor, nome)

class cachorro(Mamifero, Animal):
    def __init__(self, raça, cor, nome, numero_de_mamas, numero_de_patas):
        self.numero_de_patas = numero_de_patas
        super().__init__(raça, cor, nome, numero_de_mamas)
        