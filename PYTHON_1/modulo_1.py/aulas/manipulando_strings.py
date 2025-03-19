curso = 'pYtHon'

print(curso.lower())
print(curso.upper())
print(curso.title())

print(curso.title().strip())
print(curso.lstrip())
print(curso.lower().rstrip())

# lstrip() - remove espaços em branco no lado esquerdo
# rstrip() - remove espaços em branco no lado direito
# strip() - remove todos os espaços em branco da string
# .title() - primeira letra maiscula
#.lower() e .upper() - tudo minusculo e tudo maiusculo

print(curso.center(16, '#')) # faz isso aqui ##python##, o numero é de acordo com a quantidade de caracteres
print("-".join(curso.lower())) # faz o - se juntar a palavra curso p.y.t.h.o.n