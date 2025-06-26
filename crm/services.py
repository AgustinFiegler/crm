from crm.models import Usuario, Factura, Presupuesto
from crm.db import get_connection
import datetime

def registrar_usuario(nombre, apellidos, email, telefono=None, direccion=None):
    usuario = Usuario(nombre, apellidos, email, telefono, direccion)
    with get_connection() as conn:
        c = conn.cursor()
        try:
            c.execute("INSERT INTO usuarios (nombre, apellidos, email, telefono, direccion, fecha_registro) VALUES (?, ?, ?, ?, ?, ?)",
                      (usuario.nombre, usuario.apellidos, usuario.email, usuario.telefono, usuario.direccion, usuario.fecha_registro))
            usuario.id = c.lastrowid
            conn.commit()
            return usuario, None
        except Exception as e:
            return None, str(e)

def buscar_usuario_email(email):
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT id, nombre, apellidos, email, telefono, direccion, fecha_registro FROM usuarios WHERE email = ?", (email,))
        row = c.fetchone()
        if row:
            usuario = Usuario(row[1], row[2], row[3], row[4], row[5])
            usuario.id = row[0]
            usuario.fecha_registro = row[6]
            return usuario
        return None

def listar_usuarios():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute("SELECT id, nombre, apellidos, email, telefono, direccion, fecha_registro FROM usuarios")
        usuarios = []
        for row in c.fetchall():
            usuario = Usuario(row[1], row[2], row[3], row[4], row[5])
            usuario.id = row[0]
            usuario.fecha_registro = row[6]
            usuarios.append(usuario)
        return usuarios
