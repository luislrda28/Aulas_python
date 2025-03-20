import random

def jogo_de_adivinhacao():
    num_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem vindo ao jogo de adivinhação!!!")
    print("Tente adivinhas o número misteriosoooo de 1 a 100")

    while True:
        tentativa = input("Digite o número que deseja tentar (ou 'sair para encerrar) ")

        if tentativa.lower() == 'sair':
            print("Obrigado por jogar, volte sempre!")
            break

        try:
            tentativa = int(tentativa)
        except ValueError:
            print("Numero invalido")
            continue

        tentativas += 1

        if tentativa < num_secreto:
            print("Número muito baixo. Tente novamente!")
        elif tentativa > num_secreto:
            print("Número muito alto. Tente novamente")
        else:
            print(f"Parabéns, você acertou o número {num_secreto} em {tentativas} tentativas.")
            break

jogo_de_adivinhacao()
