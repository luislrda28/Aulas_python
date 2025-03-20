def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    for transação in transacoes:
        if abs(transação) > limite:
            transacoes_filtradas.append(transação)
    
        # TODO: Verifique se o valor absoluto da transação é maior que o limite:
        
            # TODO: Adicione a transação à lista filtrada:
            

    # Retorna a lista de transações filtradas
    return transacoes_filtradas


entrada = input()

entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "") 
limite = float(limite.strip())  # Converte o limite para float


transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

resultado = filtrar_transacoes(transacoes, limite)

print(f"Transações: {resultado}")