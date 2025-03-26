class ContaBancaria:
  def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
        self.operacoes = []

  def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.operacoes.append(f"+{valor}")
        elif valor == 0:
            self.operacoes.append("0") 

  def sacar(self, valor):
        if self.saldo >= abs(valor):
            self.saldo -= abs(valor)
            self.operacoes.append(f"-{abs(valor)}")
        else:
            self.operacoes.append("Saque não permitido")

  def extrato(self):
      operacoes_formatadas = ", ".join(self.operacoes)
      print(f"Operações: {operacoes_formatadas}; Saldo: {self.saldo}")
    
nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
try:
  transacoes = [int(valor) for valor in entrada_transacoes.split(",")]
except ValueError:
  print("Erro: Certifique-se de que a entrada contém apenas números inteiros separados por vírgulas.")
  transacoes = []

for valor in transacoes:
  if valor > 0:
    conta.depositar(valor)
  else:
    conta.sacar(valor)

conta.extrato()
