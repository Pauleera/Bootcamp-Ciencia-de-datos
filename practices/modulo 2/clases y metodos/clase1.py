

class Estudiante:

    def __init__(self, nombre, matriculado):
        self.nombre = nombre
        self.matricula = matriculado

    def presentarse(self):
        return f"Hola {self.nombre} !"

estudiante1 = Estudiante("Paula", True)
print(estudiante1.presentarse())