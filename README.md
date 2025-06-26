# CRM Console - Sistema de Gestión de Clientes

Este proyecto es un sistema CRM profesional y minimalista en Python, operando exclusivamente con persistencia en SQLite.

## Características principales
- Registro, búsqueda y listado de usuarios.
- Creación y consulta de facturas asociadas a usuarios.
- Reporte financiero por usuario y general.
- Menú interactivo por consola.
- Persistencia automática en base de datos local `CRM-Entrega.sqlite3`.

## Estructura del Proyecto
```
crm-console/
  crm/
    main.py         # Menú y lógica principal
    models.py       # Clases Usuario y Factura
    services.py     # Funciones de gestión y persistencia
    utils.py        # Utilidades y validaciones
    db.py           # Conexión y estructura de la base de datos
    __init__.py
    __main__.py     # Punto de entrada para python -m crm
  README.md
  ANALISIS.md
  CRM-Entrega.sqlite3
```

## Requisitos
- Python 3.8 o superior

## Instalación del paquete

Puedes instalar el paquete localmente usando:

```bash
pip install .
```

## Ejecución

Para iniciar el sistema CRM desde consola:

```bash
python -m crm
```

## Funcionalidades principales
- Registrar, buscar y listar usuarios.
- Crear y consultar facturas.
- Resumen financiero por usuario y general.
- Limpieza de datos nulos desde el menú.

## Evaluación y entrega
El sistema cumple con los requisitos de la consigna académica, incluyendo validaciones, persistencia, menú y reportes. La base de datos utilizada es `CRM-Entrega.sqlite3`.
