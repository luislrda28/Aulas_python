# .clear
contatos = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"},
    "samanta@gmail.com": {"nome": "Samantha", "numero": "9928-1923"},
    "jorge123@gmail.com": {"nome": "Jorge", "numero": "2221-2311"},
    "joaolucas@gmail.com": {"nome": "João", "numero": "9999-8888"},
}

# contatos.clear() # {}

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------

# .copy()

copia = contatos.copy()
copia["luisotavio@gmail.com"] = {"nome": "Lucas"} # {'luisotavio@gmail.com': {'nome': 'Lucas'}}
contatos["luisotavio@gmail.com"] #  {"luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------

# .fromkeys

dict.fromkeys(["placa", "modelo"]) # Deixa os dois valores como Null
dict.fromkeys(["placa", "modelo"], "Vazio") # Declara os dois valores como 'Vazio'

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .get

contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}

contato.get("uva") # None
contato.get("luisotavio@gmail.com") # {'nome': 'Luis', 'numero': '4002-8922'}
contato.get("joao", {}) # se não encontrar a palavra joão em contato, retorna dicionarios vazio

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .items
contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}

contato.items() # dict_items([('luisotavio@gmail.com', {'nome': 'Luis', 'numero': '4002-8922'})])

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .keys
contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}

contato.keys() # dict_keys(['luisotavio@gmail.com'])

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .pop
contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}
resultado = contato.pop("luisotavio@gmail.com")
resultado = contato.pop("luisotavio@gmail.com", "não encontrou") # não encontrou pois o pop de cima ja removeu o luisotavio@gmail.com

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .setdefault !!!!! Se nome for Luis e tentar usar .setdefault para mudar o nome, não mudará, pois ele ja tem o valor Luis !!!!!

contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}

contato.setdefault("idade", 18) # {'luisotavio@gmail.com': {'nome': 'Luis', 'numero': '4002-8922'}, 'idade': 18}

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# .update
contato = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"}
}

contato.update({"luisotavio@gmail.com": {"nome": "Luisotavio", "numero": "4002-8922"}}) # {'luisotavio@gmail.com': {'nome': 'Luisotavio', 'numero': '4002-8922'}}
contato.update({"jorge123@gmail.com": {"nome": "Jorge", "numero": "2221-2311"}}) # {'luisotavio@gmail.com': {'nome': 'Luisotavio', 'numero': '4002-8922'}, 
                                                                                 # {'jorge123@gmail.com': {'nome': 'Jorge', 'numero': '2221-2311'}}

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# in

contatos = {
    "luisotavio@gmail.com": {"nome": "Luis", "numero": "4002-8922"},
    "samanta@gmail.com": {"nome": "Samantha", "numero": "9928-1923"},
    "jorge123@gmail.com": {"nome": "Jorge", "numero": "2221-2311"},
    "joaolucas@gmail.com": {"nome": "João", "numero": "9999-8888"},
}

resultado = "numero" in contatos # True
resultado = "idade" in contatos # False
resultado = "numero" in contatos["luisotavio@gmail.com"] # True
resultado = "idade" in contatos["luisotavio@gmail.com"] # False

# //////////////---------------//////////////---------------//////////////---------------//////////////---------------//////////////---------------
# del

del contato["luisotavio@gmail.com"] # {}
del contato["luisotavio@gmail.com"]["numero"] # remove o numero do luisotavio
