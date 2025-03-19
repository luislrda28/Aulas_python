def verificar_paridade():
    
    while True:
        numero = input("Digite um número inteiro (ou 'sair' para encerrar)" )
        
        if numero.lower() == 'sair':
            print("Até logo!")
            break

        try:
            numero = int(numero)
        except ValueError:
            print("Valor inválido!")
            continue
        
        if numero % 2 == 0:
            print("Número", numero, "é par")
        else:
            print("Número", numero, "não é par")       
        
verificar_paridade()