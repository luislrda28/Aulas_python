frutas = ("Uva", "Banana", "Melão", "Pera",) # parecidas com lista, mas são imutaveis e usam o ( )

nome = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brazil",)

frutas[0] # Uva
frutas[-1] # Pera

matriz = (
    (1, "a", 2),
    (4, "b", 7),
    (8, "f", 3),
)

print(matriz[0][1]) # a
print(matriz[2][1]) # f
print(matriz[-1][-3]) # 8

# Fatiamento
print(matriz[-1][:3]) # (8, "f", 3),
print(matriz[1][2:]) # (7,)
print(matriz[-2][::2]) # (4, 7)
print(matriz[::-1]) # ((8, 'f', 3), (4, 'b', 7), (1, 'a', 2))

#Classes da Tupla
# .len, .index, .count