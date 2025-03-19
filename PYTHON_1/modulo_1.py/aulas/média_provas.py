def calcular_media():
    while True:
        print("--- Calculador de média ---")
        print("Digite a nota de quatro provas: ")
        print("Ou digite 'sair' para encerrar o programa")

        notas = []
        for i in range(1, 5):
            nota = input(f"Digite a nota da prova {i}: ")

            if nota.lower() == 'sair':
                print("Até mais!")
                return

            try:
                nota = float(nota)
                if nota < 0 or nota > 10:
                    print("Nota inválido, apenas valores entre 0 e 10!")
                    break
                notas.append(nota)
            except ValueError:
                print("Valor errado. Digite um valor númerico!")
                break
        
        if len(notas) == 4:
            media = sum(notas) / 4
            print(f"A média de {i} notas ficou com {media:.2f} de média")


calcular_media()


