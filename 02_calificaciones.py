
class Estudiante:
    def __init__(self, nombre):
        self._nombre = nombre
        self._notas = []

    @property
    def nombre(self):
        return self._nombre

    @property
    def notas(self):
        return self._notas.copy()

    @notas.setter
    def notas(self, nuevas_notas):
        for nota in nuevas_notas:
            if not isinstance(nota, (int, float)) or isinstance(nota, bool):
                raise ValueError("Las notas deben ser números.")
            if nota < 0 or nota > 5.0:
                raise ValueError("La nota debe estar entre 0.0 y 5.0.")

        self._notas = list(nuevas_notas)

    def agregar_nota(self, nota):
        self.notas = self._notas + [nota]

    def calcular_promedio(self):
        if not self._notas:
            return 0.0
        return sum(self._notas) / len(self._notas)


# Ejemplo de uso
estudiante = Estudiante("Carlos")

estudiante.agregar_nota(4.0)
estudiante.agregar_nota(4.5)
estudiante.agregar_nota(3.8)

print("Estudiante:", estudiante.nombre)
print("Notas:", estudiante.notas)
print("Promedio:", round(estudiante.calcular_promedio(), 2))
