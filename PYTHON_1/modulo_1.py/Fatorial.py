def calcular_fatorial():
    while True:
        numero = input("Digite um numero (ou 'sair' para cancelar)")

        if numero.lower() == 'sair':
            print("Obrigado!")
            break

        try:
            numero = int(numero)
            if numero < 0:
                print("Digite um valor válido!")
                continue
        except ValueError:
            print("Número Inválido! Tente novamente.")
            continue

        fatorial = 1

        for i in range(1, numero + 1):
            fatorial *= i

        print(f"O fatorial do {numero} é {fatorial}")

calcular_fatorial()     

