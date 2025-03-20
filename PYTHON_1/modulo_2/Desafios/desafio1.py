def calcular_saldo(transacoes):
    saldo = 0.0

    for transacao in transacoes:
        saldo += transacao
        
    return f"R$ {saldo:.2f}".replace('.', ',')
    

entrada_usuario = input()

entrada_usuario = entrada_usuario.strip("[]").replace(" ", "")

transacoes = [float(valor) for valor in entrada_usuario.split(",") if valor]

# TODO: Calcule o saldo com base nas transações informadas:
resultado = calcular_saldo(transacoes)

print(resultado)
