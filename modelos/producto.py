class Producto:
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        if cantidad <= 0 or cantidad > self.stock:
            raise ValueError("Cantidad inválida o stock insuficiente.")
        self.stock -= cantidad

    def to_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }

    @staticmethod
    def from_dict(data: dict) -> "Producto":
        return Producto(
            codigo=data["codigo"],
            nombre=data["nombre"],
            categoria=data["categoria"],
            precio=data["precio"],
            stock=data.get("stock", 0)
        )

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.categoria}) ${self.precio:.2f} | Stock: {self.stock}"