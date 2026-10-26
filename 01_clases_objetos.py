class ServidorCloud:
    proveedor = "Unicaribe Cloud"

    def __init__(self, hostname: str, ram_gb: int):
        self.hostname = hostname
        self.ram_gb = ram_gb
        self.encendido = False

    def encender(self):
        self.encendido = True
        print(f"Servidor {self.hostname} operando correctamente.")


srv01 = ServidorCloud("srv-db-01", 64)
srv01.encender()
