class Envio:
    def __init__(self, peso_kg, distancia_km):
        self.peso_kg = peso_kg
        self.distancia_km = distancia_km

    def calcular_costo(self, monto_base):
        return monto_base



class EnvioEstandar(Envio):
    def calcular_costo(self, monto_base):
        return monto_base * 1.05



class EnvioExpress(Envio):
    def calcular_costo(self, monto_base):
        return monto_base * 1.15



envios = [
    EnvioEstandar(5, 100),
    EnvioExpress(8, 150),
    EnvioEstandar(3, 50),
    EnvioExpress(10, 200)
]


monto_base = 50000


for envio in envios:
    costo = envio.calcular_costo(monto_base)

    if isinstance(envio, EnvioEstandar):
        tipo = "Estándar"
    else:
        tipo = "Express"

    print("Tipo de envío:", tipo)
    print("Peso:", envio.peso_kg, "kg")
    print("Distancia:", envio.distancia_km, "km")
    print("Costo total: $", costo)
    print("-------------------------")
