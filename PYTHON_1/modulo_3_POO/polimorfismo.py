class Passaro:
    def voar(self):
        print("Passaro voando")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voando")

class Aveztruz(Passaro):
    def voar(self):
        print("Avestruz não voa")


# exemplo ruim do uso de herança para "ganhar" o metodo voar
class Aviao(Passaro):
    def voar(self):
       print("Aviao esta decolando...")


def plano_de_voo(passaro):
    passaro.voar()

aviao = Aviao()
pardal = Pardal()
ave = Aveztruz()

plano_de_voo(pardal)
plano_de_voo(ave)
plano_de_voo(aviao)
