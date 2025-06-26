import re
from crm.db import init_db, get_connection
from crm.services import registrar_usuario, buscar_usuario_email, listar_usuarios, limpiar_datos_nulos
from crm.models import Usuario
from crm.utils import input_opcional
import datetime

ESTADOS_FACTURA = ['Pendiente', 'Pagada', 'Cancelada']

def validar_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email)

def main():
    init_db()
    while True:
        print("\n=== SISTEMA CRM ===")
        print("1. Registrar nuevo usuario")
        print("2. Buscar usuario")
        print("3. Crear factura para usuario")
        print("4. Mostrar todos los usuarios")
        print("5. Mostrar facturas de un usuario")
        print("6. Resumen financiero por usuario")
        print("7. Limpiar datos nulos")
        print("8. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            print("\n=== REGISTRO DE NUEVO USUARIO ===")
            nombre = input("Ingrese nombre: ").strip()
            apellidos = input("Ingrese apellidos: ").strip()
            email = input("Ingrese email: ").strip()
            if not nombre or not apellidos or not email:
                print("[!] Nombre, apellidos y email son obligatorios.")
                continue
            if not validar_email(email):
                print("[!] Email no tiene formato válido.")
                continue
            if buscar_usuario_email(email):
                print("[!] Ya existe un usuario con ese email.")
                continue
            telefono = input_opcional("Ingrese teléfono (opcional): ")
            direccion = input_opcional("Ingrese dirección (opcional): ")
            usuario, error = registrar_usuario(nombre, apellidos, email, telefono, direccion)
            if usuario:
                print(f"Usuario registrado exitosamente!\nID asignado: USR{usuario.id:03d}")
                print(f"Fecha de registro: {usuario.fecha_registro:%d/%m/%Y}")
            else:
                print(f"[!] Error: {error}")
        elif opcion == '2':
            print("\n=== BUSCAR USUARIO ===")
            print("1. Buscar por email")
            print("2. Buscar por nombre")
            metodo = input("Seleccione método de búsqueda: ").strip()
            if metodo == '1':
                email = input("Ingrese email: ").strip()
                usuario = buscar_usuario_email(email)
                if usuario:
                    print("--- USUARIO ENCONTRADO ---")
                    print(f"ID: USR{usuario.id:03d}")
                    print(f"Nombre: {usuario.nombre_completo()}")
                    print(f"Email: {usuario.email}")
                    print(f"Teléfono: {usuario.telefono or 'No especificado'}")
                    print(f"Dirección: {usuario.direccion or 'No especificada'}")
                    print(f"Fecha de registro: {usuario.fecha_registro:%d/%m/%Y}")
                else:
                    print("[!] Usuario no encontrado.")
            elif metodo == '2':
                nombre = input("Ingrese nombre: ").strip()
                usuarios = [u for u in listar_usuarios() if nombre.lower() in u.nombre.lower()]
                if usuarios:
                    for usuario in usuarios:
                        print(f"ID: USR{usuario.id:03d} | Nombre: {usuario.nombre_completo()} | Email: {usuario.email}")
                else:
                    print("[!] No se encontraron usuarios con ese nombre.")
            else:
                print("[!] Opción inválida.")
        elif opcion == '3':
            print("\n=== CREAR FACTURA ===")
            email = input("Ingrese email del usuario: ").strip()
            usuario = buscar_usuario_email(email)
            if not usuario:
                print("[!] Usuario no encontrado.")
                continue
            print(f"Usuario encontrado: {usuario.nombre_completo()}")
            descripcion = input("Ingrese descripción del servicio/producto: ").strip()
            try:
                monto = float(input("Ingrese monto total: ").replace(",", "."))
                if monto <= 0:
                    raise ValueError
            except ValueError:
                print("[!] El monto debe ser un número positivo.")
                continue
            print("Seleccione estado:")
            for i, estado in enumerate(ESTADOS_FACTURA, 1):
                print(f"{i}. {estado}")
            try:
                idx_estado = int(input("Estado: ")) - 1
                estado = ESTADOS_FACTURA[idx_estado]
            except Exception:
                print("[!] Estado inválido.")
                continue
            with get_connection() as conn:
                c = conn.cursor()
                c.execute("INSERT INTO facturas (usuario_id, fecha, descripcion, monto, estado) VALUES (?, ?, ?, ?, ?)",
                          (usuario.id, datetime.datetime.now(), descripcion, monto, estado))
                numero = c.lastrowid
                conn.commit()
            print("Factura creada exitosamente!")
            print(f"Número de factura: FAC{numero:03d}")
            print(f"Fecha de emisión: {datetime.datetime.now():%d/%m/%Y %H:%M}")
            print(f"Cliente: {usuario.nombre_completo()}")
            print(f"Descripción: {descripcion}")
            print(f"Monto: ${monto:.2f}")
            print(f"Estado: {estado}")
        elif opcion == '4':
            print("\n=== LISTA DE USUARIOS ===")
            usuarios = listar_usuarios()
            if not usuarios:
                print("No hay usuarios registrados.")
            for i, usuario in enumerate(usuarios, 1):
                print(f"Usuario #{i}:")
                print(f"ID: USR{usuario.id:03d}")
                print(f"Nombre: {usuario.nombre_completo()}")
                print(f"Email: {usuario.email}")
                print(f"Teléfono: {usuario.telefono or 'No especificado'}")
                print(f"Fecha de registro: {usuario.fecha_registro:%d/%m/%Y}")
            print(f"Total de usuarios registrados: {len(usuarios)}")
        elif opcion == '5':
            print("\n=== FACTURAS POR USUARIO ===")
            email = input("Ingrese email del usuario: ").strip()
            usuario = buscar_usuario_email(email)
            if not usuario:
                print("[!] Usuario no encontrado.")
                continue
            with get_connection() as conn:
                c = conn.cursor()
                c.execute("SELECT numero, fecha, descripcion, monto, estado FROM facturas WHERE usuario_id = ?", (usuario.id,))
                facturas = c.fetchall()
            if not facturas:
                print("No hay facturas para este usuario.")
                continue
            total = 0
            pendiente = 0
            for i, f in enumerate(facturas, 1):
                print(f"Factura #{i}:")
                print(f"Número: FAC{f[0]:03d}")
                print(f"Fecha: {datetime.datetime.strptime(f[1], '%Y-%m-%d %H:%M:%S.%f'):%d/%m/%Y %H:%M}")
                print(f"Descripción: {f[2]}")
                print(f"Monto: ${f[3]:.2f}")
                print(f"Estado: {f[4]}")
                total += f[3]
                if f[4] == 'Pendiente':
                    pendiente += f[3]
            print(f"Total de facturas: {len(facturas)}")
            print(f"Monto total facturado: ${total:.2f}")
            print(f"Monto pendiente: ${pendiente:.2f}")
        elif opcion == '6':
            print("\n=== RESUMEN FINANCIERO ===")
            usuarios = listar_usuarios()
            total_facturas = 0
            ingresos_totales = 0
            ingresos_recibidos = 0
            ingresos_pendientes = 0
            for usuario in usuarios:
                with get_connection() as conn:
                    c = conn.cursor()
                    c.execute("SELECT monto, estado FROM facturas WHERE usuario_id = ?", (usuario.id,))
                    facturas = c.fetchall()
                total = sum(f[0] for f in facturas)
                pagadas = sum(f[0] for f in facturas if f[1] == 'Pagada')
                pendientes = sum(f[0] for f in facturas if f[1] == 'Pendiente')
                print(f"Usuario: {usuario.nombre_completo()} ({usuario.email})- Total facturas: {len(facturas)}- Monto total: ${total:.2f}- Facturas pagadas: ${pagadas:.2f}- Facturas pendientes: ${pendientes:.2f}")
                total_facturas += len(facturas)
                ingresos_totales += total
                ingresos_recibidos += pagadas
                ingresos_pendientes += pendientes
            print("--- RESUMEN GENERAL ---")
            print(f"Total usuarios: {len(usuarios)}")
            print(f"Total facturas emitidas: {total_facturas}")
            print(f"Ingresos totales: ${ingresos_totales:.2f}")
            print(f"Ingresos recibidos: ${ingresos_recibidos:.2f}")
            print(f"Ingresos pendientes: ${ingresos_pendientes:.2f}")
        elif opcion == '7':
            limpiar_datos_nulos()
            print("Datos nulos eliminados correctamente.")
        elif opcion == '8':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("[!] Opción inválida.")
