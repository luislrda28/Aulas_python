class Pessoa:
    def __init__(self, nome, ano_de_nascimento):
        self.nome = nome
        self._ano_de_nascimento = ano_de_nascimento
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_de_nascimento
    
pessoa = Pessoa("Luis", 2007)
print(f"Nome {pessoa.nome}, Idade: {pessoa.idade}")
    