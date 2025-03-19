import datetime

tipo_carro = "P" # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + datetime.timedelta(days=tempo_pequeno)
    print(f"Carro chegou: {data_atual} e ficara pronto {data_estimada}")

elif tipo_carro == 'M':
    data_estimada = data_atual + datetime.timedelta(days=tempo_medio)
    print(f"Carro chegou: {data_atual} e ficara pronto {data_estimada}")

else: # G
    data_estimada = data_atual + datetime.timedelta(days=tempo_grande)
    print(f"Carro chegou: {data_atual} e ficara pronto {data_estimada}")

print(data_atual - datetime.timedelta(days=1))

resultado = (datetime.datetime.now() - datetime.timedelta(hours=1))
print(resultado.time()) # Mostrar apenas a hora que foi subtraido

print(datetime.datetime.now().date()) # Mostrar apenas a data de hoje