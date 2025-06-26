import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'CRM-Entrega.sqlite3')

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        # Tabla de usuarios
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefono TEXT,
            direccion TEXT,
            fecha_registro DATE NOT NULL
        )''')
        # Tabla de facturas
        c.execute('''CREATE TABLE IF NOT EXISTS facturas (
            numero INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            fecha DATETIME NOT NULL,
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL CHECK(monto > 0),
            estado TEXT NOT NULL CHECK(estado IN ('Pendiente', 'Pagada', 'Cancelada')),
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )''')
        conn.commit()
