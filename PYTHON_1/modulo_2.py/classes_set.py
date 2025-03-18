conjunto_a = {1, 2}
conjunto_b = {3, 4}

união = conjunto_a.union(conjunto_b) # {1, 2, 3, 4} --- .union()
print(união)

conjunto_c = {1, 2, 3}
conjunto_d = {3, 4, 1}

# Valores que tem nos dois sets --- .intersection
interseção = conjunto_c.intersection(conjunto_d) # {1, 3}
print(interseção)

# Diferença do set c com o set d
conjunto_c = {1, 2, 3}
conjunto_d = {3, 4, 1}

# Valores que tem no set c e não no d --- .difference
diferenca = conjunto_c.difference(conjunto_d) # 2
print(diferenca)

# Valores que tem no set d e não no c --- .difference
diferenca = conjunto_d.difference(conjunto_c) # 4
print(diferenca)

# Todos os numero que não estão nos dois sets --- .symmetric.difference()
simetria = conjunto_c.symmetric_difference(conjunto_d) # {2, 4}
print(simetria)

# Se o valores são subsets um do outro --- .issusubset()
conjunto_f = {1, 2, 3}
conjunto_g = {3, 4, 1, 2, 5}
conjunto_h = {5}

conjunto_f.issubset(conjunto_g) # True
conjunto_g.issubset(conjunto_f) # False

# Contrario do .issubset() -- .issuperset()
conjunto_f.issuperset(conjunto_g) # False
conjunto_g.issuperset(conjunto_f) # True

#Se o conjunto não tem nenhum valor igual ao outro --- .isdisjoint()
conjunto_f.isdisjoint(conjunto_g) # False
conjunto_f.isdisjoint(conjunto_h) # True

#Adicionar novo valor ao set --- .add
conjunto_h.add(10) # {5, 10}

# Discartar um valor do set --- .discard
conjunto_h.discard(10) # {5}

# Diferença entre remove e discard, discard segue normalmente mesmo após tentar remover um número não existe no set, ja o remove para o programa

#Remover --- .remove
conjunto_h.remove(5) # {}

# função in
1 in conjunto_h #False
1 in conjunto_a # True
