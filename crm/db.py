import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'crm.sqlite3')

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellidos TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            telefono TEXT,
            direccion TEXT,
            fecha_registro DATE NOT NULL
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS facturas (
            numero INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            fecha DATETIME NOT NULL,
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL,
            estado TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS presupuestos (
            numero INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            fecha DATETIME NOT NULL,
            descripcion TEXT NOT NULL,
            monto REAL NOT NULL,
            estado TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
        )''')
        conn.commit()
