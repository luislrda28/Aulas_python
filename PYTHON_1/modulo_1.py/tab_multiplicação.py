def tabuada_multiplicacao():
    while True:
        numero = input("Digite um numero (ou 'sair' para cancelar)")

        if numero.lower() == 'sair':
            print("Até logo!")
            break

        try:
            numero = int(numero)
        except ValueError:
            print("Valor inválido!")
            continue

        print(f"Tabuada do {numero}:")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

tabuada_multiplicacao()

