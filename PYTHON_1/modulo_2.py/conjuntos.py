# set - Remove repetições

nome = set("Luis Otávio Rodrigues da Silva")
print(nome)

fruta = set("abacaxi")
print(fruta)

numeros = ([1, 4, 3, 4, 5, 2, 1, 5, 7, 1, 3, 6])

numeros_organzizados = set(sorted(numeros))
print(numeros_organzizados)

# acessando dados!
pedra = {"ametista", "quartzo", "diamante"}

 ## print(pedra[0]) INVALIDO! Precisa transformar o elemento 'pedra' em uma lista
pedras = list(pedra)
print(pedras[0])