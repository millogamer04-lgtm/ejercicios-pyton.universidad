class Producto:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__precios_historicos = []
        self.__precio = 0

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if 0 <= nuevo_precio <= 10000:
            self.__precio = nuevo_precio
            self.__precios_historicos.append(nuevo_precio)
            print("Precio registrado correctamente.")
        else:
            print("Advertencia: el precio debe estar entre 0 y 10000.")

    def calcular_promedio(self):
        if len(self.__precios_historicos) == 0:
            return 0

        return sum(self.__precios_historicos) / len(self.__precios_historicos)

    def mostrar_historial(self):
        return self.__precios_historicos


producto1 = Producto("Camisa")


producto1.precio = 5000
producto1.precio = 7000
producto1.precio = 8000

producto1.precio = 15000

print("\nProducto:", producto1._Producto__nombre)
print("Precio actual:", producto1.precio)
print("Historial:", producto1.mostrar_historial())
print("Precio promedio:", producto1.calcular_promedio())
