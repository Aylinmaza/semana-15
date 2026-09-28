import tkinter as tk
from tkinter import ttk, messagebox

class MainView(tk.Frame):
    def __init__(self, master, servicio, on_logout):
        super().__init__(master)
        self.servicio = servicio
        self.on_logout = on_logout
        self.pack(fill="both", expand=True)

        # Sidebar con botones
        sidebar = tk.Frame(self, bg="#1f2a44", width=200, padx=16, pady=18)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)

        tk.Button(sidebar, text="Usuarios", command=self.mostrar_usuarios).pack(fill="x", pady=5)
        tk.Button(sidebar, text="Productos", command=self.mostrar_productos).pack(fill="x", pady=5)
        tk.Button(sidebar, text="Ventas", command=self.mostrar_ventas).pack(fill="x", pady=5)
        tk.Button(sidebar, text="Cerrar sesión", command=self.on_logout).pack(fill="x", pady=20)

        # Área principal
        self.content = tk.Frame(self, bg="#f7fafc", padx=20, pady=20)
        self.content.pack(side="left", fill="both", expand=True)

    def limpiar_contenido(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # --- Usuarios ---
    def mostrar_usuarios(self):
        self.limpiar_contenido()
        tk.Label(self.content, text="Usuarios registrados", font=("Arial", 16, "bold")).pack(anchor="w")

        frame_tabla = tk.Frame(self.content)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("identificacion", "nombre", "rol")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        tabla.heading("identificacion", text="Identificación")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("rol", text="Rol")

        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscroll=scroll_y.set)

        tabla.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        usuarios = self.servicio.listar_usuarios()
        for u in usuarios:
            tabla.insert("", tk.END, values=(u["identificacion"], u["nombre"], u["rol"]))

    # --- Productos ---
    def mostrar_productos(self):
        self.limpiar_contenido()
        tk.Label(self.content, text="Gestión de productos", font=("Arial", 16, "bold")).pack(anchor="w")

        frame_tabla = tk.Frame(self.content)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            tabla.heading(col, text=col.capitalize())

        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=tabla.yview)
        tabla.configure(yscroll=scroll_y.set)

        tabla.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        productos = self.servicio.listar_productos()
        for p in productos:
            tabla.insert("", tk.END, values=(p.codigo, p.nombre, p.categoria, p.precio, p.stock))

    # --- Ventas ---
    def mostrar_ventas(self):
        self.limpiar_contenido()
        tk.Label(self.content, text="Registrar venta", font=("Arial", 16, "bold")).pack(anchor="w")

        # Selección de usuario
        tk.Label(self.content, text="Usuario:").pack(anchor="w")
        usuarios = self.servicio.listar_usuarios()
        self.combo_usuario = ttk.Combobox(self.content, values=[u["identificacion"] for u in usuarios])
        self.combo_usuario.pack(anchor="w")

        # Selección de producto
        tk.Label(self.content, text="Producto:").pack(anchor="w")
        productos = self.servicio.listar_productos()
        self.combo_producto = ttk.Combobox(self.content, values=[p.codigo for p in productos])
        self.combo_producto.pack(anchor="w")

        # Botón registrar venta
        tk.Button(self.content, text="Registrar venta", command=self.registrar_venta).pack(pady=10)

        # Tabla de ventas
        frame_tabla = tk.Frame(self.content)
        frame_tabla.pack(fill="both", expand=True)

        columnas = ("id", "usuario", "producto", "fecha")
        self.tabla_ventas = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        for col in columnas:
            self.tabla_ventas.heading(col, text=col.capitalize())

        scroll_y = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla_ventas.yview)
        self.tabla_ventas.configure(yscroll=scroll_y.set)

        self.tabla_ventas.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        self.actualizar_tabla_ventas()

    def registrar_venta(self):
        usuario_id = self.combo_usuario.get()
        producto_codigo = self.combo_producto.get()
        try:
            self.servicio.registrar_venta(usuario_id, producto_codigo)
            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            self.actualizar_tabla_ventas()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def actualizar_tabla_ventas(self):
        # limpiar tabla
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)

        ventas = self.servicio.listar_ventas()
        for v in ventas:
            self.tabla_ventas.insert("", tk.END, values=(v["id"], v["usuario_id"], v["producto_codigo"], v["fecha"]))
