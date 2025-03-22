class cachorro:
    def __init__(self, nome, raca, idade, acordado=True): # CONSTUTOR
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.acordado = acordado

    def dormir(self):
        self.acordado = False
        print("Zzzzzzzzzzz")

    def __del__(self):  # DESTRUTOR
        print("Removendo a instancia da classe")

    def acordar(self):
        self.acordado = True
        print("Acordando...")
        print("Au au au")


def criar_cachorro():
    c = cachorro("Rex", "vira-lata", 5)
    print(c.nome)


c = cachorro("Chappie", "vira-lata", 2)
# c.acordar()

# criar_cachorro()


print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
