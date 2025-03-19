def c_para_fh(celsius):
    return(celsius * 9/5) + 32

def fh_para_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def conversor_de_temperatura():
    while True:
        print("-- Conversor de temperatura simples --")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Sair")

        escolha = (input("Selecione a opção desejada: "))

        if escolha == '3':
            print("Encerrar programa.")
            break

        if escolha not in ['1', '2', '3']:
            print("Valor Invalido. Tente novamente")
            continue
        
        temperatura = float(input("Digite a temperatura: "))
        
        
        if escolha == '1':
            resultado = c_para_fh(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}°F")
            
        elif escolha == '2':
            resultado = fh_para_c(temperatura)
            print(f"{temperatura}°C é igual a {resultado:.2f}°F")


conversor_de_temperatura()