salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

valor_com_bonus = salario_bonus(500)
print(valor_com_bonus)