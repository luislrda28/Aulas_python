class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim")

    def parar(self):
        print("Parando bicicleta....")
        print("Bicicleta parada.")

    def correr(self):
        print("VRUUUUMMMMMM")

    def trocar_marcha(self, num_marcha):
        print("Trocando marcha....")

        def _trocar_marcha():
            if num_marcha > self.trocar_marcha:
                print("Marcha trocada.")
            else:
                print("não foi possivel trocar de marcha.")


    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self.__dict__.items()]}"



b1 = bicicleta("vermelha", "caloi", "2022", "600")
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2= bicicleta("roxo", "caloi", "2020", "300")

print(b2)