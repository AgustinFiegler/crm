# CRM Console - Sistema de Gestión de Clientes

Este proyecto está limpio y listo para entrega. La base de datos `CRM-Entrega.sqlite3` no contiene usuarios ni facturas al momento de la entrega.

## Características principales
- Registro, búsqueda y listado de usuarios.
- Creación y consulta de facturas asociadas a usuarios.
- Reporte financiero por usuario y general.
- Menú interactivo por consola.
- Limpieza de datos nulos desde el menú.
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

## Instalación y ejecución

```bash
pip install .
crm-console
```

## Estado de la base de datos
- Sin usuarios ni facturas al momento de la entrega.

## Evaluación y entrega
El sistema cumple con los requisitos de la consigna académica, incluyendo validaciones, persistencia, menú y reportes. La base de datos utilizada es `CRM-Entrega.sqlite3`.
