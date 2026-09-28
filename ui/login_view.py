import tkinter as tk
from tkinter import messagebox

class LoginView(tk.Frame):
    def __init__(self, master, servicio, on_login_success):
        super().__init__(master)
        self.servicio = servicio
        self.on_login_success = on_login_success

        # Logo arriba del formulario
        self.logo = tk.PhotoImage(file="assets/logo.png")  # asegúrate de tener logo.png en assets
        tk.Label(self, image=self.logo).pack(pady=20)

        # Campos de login
        tk.Label(self, text="Usuario:").pack()
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack()

        tk.Label(self, text="Contraseña:").pack()
        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        # Botón Entrar
        tk.Button(self, text="Entrar", command=self.validar_login).pack(pady=10)

    def validar_login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        if self.servicio.validar_acceso(usuario, password):
            self.on_login_success()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
