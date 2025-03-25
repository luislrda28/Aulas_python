class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


Gui = Estudante("Guilherme", 1)
Gi = Estudante("Giovana", 2)
mostrar_valores(Gui, Gi)


Estudante.escola = "Python" # mudando o valor do atributo de classe
Gui.matricula = 3 # mudando o valor do atributo de instancia
mostrar_valores(Gui, Gi)

Lucas = Estudante("Lucas", 3)
mostrar_valores(Gui, Gi, Lucas)

#self é uma referencia a instancia da classe