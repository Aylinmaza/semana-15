# Proyecto Restaurante – Semana 15

## 📌 Propósito
Este proyecto corresponde a la **Semana 15** de la materia de Programación Orientada a Objetos.  
Su objetivo es mostrar la evolución del sistema de restaurante, integrando la **gestión de ventas** y reforzando el uso de `command=` y callbacks en Tkinter, junto con la persistencia en archivos JSON.

---

## ▶️ Cómo ejecutar
Desde la carpeta del proyecto:

```bash
cd https://github.com/Aylinmaza/semana-15.git

POO\restaurante_app"
py main.py

Credenciales de demostración
Usuario: 005  
Contraseña: 123

Usuario: 1754207486
Contraseña: 456
## Estructura esperada del repositorio:
Repositorio GitHub
├── restaurante_app/
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── usuario.py
│   │   └── venta.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   ├── archivo_servicio.py
│   │   └── restaurante_servicio.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   └── main_view.py
│   ├── assets/              (obligatorio: íconos, logo/logotipo y recursos visuales)
│   └── main.py
└── README.md

Gestión de ventas
Se añaden combobox para seleccionar usuario y producto.

Botón "Registrar venta" con command= que ejecuta un callback (registrar_venta).

El servicio valida la operación, actualiza el stock y guarda la venta en ventas.json.

La tabla de ventas se actualiza automáticamente mostrando el registro
Persistencia
usuarios.json → lista de usuarios registrados con credenciales de prueba.

productos.json → catálogo de productos con stock inicial.

ventas.json → historial de ventas realizadas, con claves uniformes (id, usuario_id, producto_codigo, fecha)
