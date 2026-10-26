class UsuarioSistema:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def autenticar(self):
        print(f"Usuario {self.username} autenticado en el sistema.")


class Administrador(UsuarioSistema):
    def __init__(self, username: str, email: str, nivel_acceso: int):
        super().__init__(username, email)
        self.nivel_acceso = nivel_acceso


admin = Administrador("root_neider", "nhernandez@unicaribe.edu", 1)
admin.autenticar()
