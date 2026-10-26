class DispositivoConectado:
    def conectar(self):
        print("Estableciendo conexión a la red...")


class CamaraSeguridad:
    def grabar(self):
        print("Grabando video HD...")


class CamaraIP(DispositivoConectado, CamaraSeguridad):
    pass


cam = CamaraIP()
cam.conectar()
cam.grabar()

print("Orden de resolución de métodos (MRO):")
print(CamaraIP.mro())
