def criar_poema(*args, **kwargs):
    poema = ""
    
    # Adiciona as linhas do poema passadas como argumentos
    for linha in args:
        poema += linha + "\n"
    
    # Adiciona o título e o autor, se fornecidos
    if 'titulo' in kwargs:
        poema = f"'{kwargs['titulo']}'\n" + poema
    if 'autor' in kwargs:
        poema += f"\n- {kwargs['autor']}"
    
    return poema

# Exemplo de uso
print(criar_poema(
    "A lua brilha no céu estrelado,", 
    "O vento canta suave, encantado,", 
    "Nas sombras da noite, sussurros ecoam,", 
    titulo="Noite Encantada", 
    autor="Luís Otávio Rodrigues da Silva"
))
