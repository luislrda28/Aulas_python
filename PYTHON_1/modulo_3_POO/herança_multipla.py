class Animal:
    def __init__(self, nro_patas):
        self.nm_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return 'Ave'

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

    def __str__(self):
        return 'Mamifero'

class gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        print("oi estou falando")



class ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # print(ornitorrinco.__mro__)
        print(ornitorrinco.mro())

        super().__init__(cor_bico=cor_bico, cor_pelo=cor_pelo, nro_patas=nro_patas)

    def __str__(self):
        return 'Ornitorrinco'


# gato = gato(nro_patas=4, cor_pelo='Vermelho')
# print(gato)

ornitorrinco1 = ornitorrinco(nro_patas=4, cor_pelo='Cinza', cor_bico="Laranja")
print(ornitorrinco1)