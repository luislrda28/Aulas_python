class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod #metodo de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    @staticmethod #metodo estatico
    def eh_adulto(idade):
        return idade >= 18

# p = Pessoa("Lucas", 20)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(2007, 1, 28, "Lucas")
print(p2.nome, p2.idade)

print(Pessoa.eh_adulto(18))
print(Pessoa.eh_adulto(17))