class Conta:
    def __init__(self, nro_agencia, saldo=0): #usado _ antes do valor para sinalizar que é privado
        self._saldo = saldo #privado
        self.nr_agencia = nro_agencia

    def depositar(self, valor): #publico
        self._saldo += valor

    def sacar(self, valor): #publico
        self._saldo -= valor

    def mostrar_saldo(self):# publico
        return self._saldo

conta = Conta(100)
conta.depositar(100)
print(conta._saldo)
print(conta.nr_agencia)