class Animal:
    def __init__(self, nro_patas):
        self.nm_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"


class Ave(Animal):
    def __init__(self, nro_patas):
        super().__init__(nro_patas)

class Mamifero(Animal):
    def __init__(self, nro_patas, cor_pelo):
        self.cor_pelo = cor_pelo
        super().__init__(nro_patas)


class gato(Mamifero, Animal):
    pass

gato = gato(4)
print(gato)