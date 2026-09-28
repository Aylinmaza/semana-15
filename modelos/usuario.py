class Usuario:
    def __init__(self, identificacion: str, nombre: str, rol: str, password: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol
        self.password = password

    def to_dict(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "rol": self.rol,
            "password": self.password
        }

    @staticmethod
    def from_dict(data: dict) -> "Usuario":
        return Usuario(
            identificacion=data["identificacion"],
            nombre=data["nombre"],
            rol=data["rol"],
            password=data["password"]
        )