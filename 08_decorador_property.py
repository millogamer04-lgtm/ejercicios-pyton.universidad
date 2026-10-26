class Empleado:
    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, nuevo_salario: float):
        if nuevo_salario >= 1300.0:
            self.__salario = nuevo_salario
        else:
            raise ValueError("El salario no puede ser inferior al mínimo legal.")


emp = Empleado("Carlos Gómez", 2000.0)
emp.salario = 2500.0
print("Salario:", emp.salario)
