import datetime
from servicios.archivo_servicio import leer_json, escribir_json
from modelos.producto import Producto
from modelos.venta import Venta

class RestauranteServicio:
    def __init__(self, ruta_productos="datos/productos.json", ruta_usuarios="datos/usuarios.json", ruta_ventas="datos/ventas.json"):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.ruta_ventas = ruta_ventas

    # --- Usuarios ---
    def listar_usuarios(self):
        return leer_json(self.ruta_usuarios)

    def validar_acceso(self, usuario, password):
        usuarios = leer_json(self.ruta_usuarios)
        for u in usuarios:
            if u["identificacion"] == usuario and u["password"] == password:
                return True
        return False

    # --- Productos ---
    def listar_productos(self):
        datos = leer_json(self.ruta_productos)
        return [Producto.from_dict(p) for p in datos]

    def registrar_producto(self, codigo, nombre, categoria, precio, stock):
        productos = leer_json(self.ruta_productos)
        if any(p["codigo"] == codigo for p in productos):
            raise ValueError("El producto ya existe")
        nuevo = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": float(precio),
            "stock": int(stock)
        }
        productos.append(nuevo)
        escribir_json(self.ruta_productos, productos)

    def actualizar_producto(self, codigo, nombre, categoria, precio, stock):
        productos = leer_json(self.ruta_productos)
        encontrado = False
        for p in productos:
            if p["codigo"] == codigo:
                p["nombre"] = nombre
                p["categoria"] = categoria
                p["precio"] = float(precio)
                p["stock"] = int(stock)
                encontrado = True
                break
        if not encontrado:
            raise ValueError("Producto no encontrado")
        escribir_json(self.ruta_productos, productos)

    def eliminar_producto(self, codigo):
        productos = leer_json(self.ruta_productos)
        nuevos = [p for p in productos if p["codigo"] != codigo]
        if len(nuevos) == len(productos):
            raise ValueError("Producto no encontrado")
        escribir_json(self.ruta_productos, nuevos)

    # --- Ventas ---
    def listar_ventas(self):
        return leer_json(self.ruta_ventas)

    def registrar_venta(self, usuario_id, producto_codigo):
        usuarios = leer_json(self.ruta_usuarios)
        productos = leer_json(self.ruta_productos)

        usuario = next((u for u in usuarios if u["identificacion"] == usuario_id), None)
        producto = next((p for p in productos if p["codigo"] == producto_codigo), None)

        if not usuario or not producto:
            raise ValueError("Usuario o producto no válido")

        ventas = leer_json(self.ruta_ventas)
        identificador = str(len(ventas) + 1)
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        venta = Venta(identificador, usuario_id, producto_codigo, fecha)
        ventas.append(venta.to_dict())
        escribir_json(self.ruta_ventas, ventas)

        return True
