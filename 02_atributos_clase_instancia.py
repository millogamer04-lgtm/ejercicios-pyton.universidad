class ConexionBaseDatos:
    total_conexiones = 0

    def __init__(self, db_name: str):
        self.db_name = db_name
        ConexionBaseDatos.total_conexiones += 1


c1 = ConexionBaseDatos("Ventas")
c2 = ConexionBaseDatos("Inventario")
print("Total de conexiones:", ConexionBaseDatos.total_conexiones)
