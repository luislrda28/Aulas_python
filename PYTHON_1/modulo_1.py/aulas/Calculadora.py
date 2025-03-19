def calculadora():
    while True:
        print("---- Calculadora ----")
        print("1 Adição")
        print("2 Subtração")
        print("3 Multiplicação")
        print("4 Divisão")
        print("5 Sair")
        escolha = input("Digite o número da operação desejada!")

        if escolha == '5':
            print("Até logo!")
            break

        if escolha not in ['1', '2', '3', '4', '5']:
            print("Valor inválido. Tente novamente")
            continue

        valor1 = float(input("Digite o primeiro número:"))
        valor2 = float(input("Digite o segundo número:"))

        if escolha == '1':
            resultado = valor1 + valor2
            print(valor1, "+", valor2, "=", resultado)
        
        elif escolha == '2':
            resultado = valor1 - valor2
            print(valor1, "-", valor2, "=", resultado)
        
        elif escolha == '3':
            resultado = valor1 * valor2
            print(valor1, "*", valor2, "=", resultado)
        
        elif escolha == '4':
            if valor2 == 0:
                print("Não pode fazer divisão com 0")
            else:
                resultado = valor1 / valor2
                print(valor1, "/", valor2, resultado)

calculadora()

        
