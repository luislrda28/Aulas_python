# pessoa = {"nome": "Luis", "idade": 21}

# pessoa = dict(nome="Guilherme", idade= 21)

# pessoa["telefone"] = "4002-8922"
# print(pessoa["nome"])
# print(pessoa["idade"])
# print(pessoa["telefone"])

contatos = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"},
    "samanta@gmail.com": {"nome": "Samantha", "numero": "9928-1923"},
    "jorge123@gmail.com": {"nome": "Jorge", "numero": "2221-2311"},
    "joaolucas@gmail.com": {"nome": "João", "numero": "9999-8888"},
}

numero = contatos["luisotavio@gmail.com"]["numero"]
print(numero)

for chave, valor in contatos.items():
    print(chave, valor)
