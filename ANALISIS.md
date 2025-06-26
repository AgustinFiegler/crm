# ANÁLISIS Y JUSTIFICACIÓN DEL PROYECTO CRM CONSOLE

## Estado de entrega
El sistema CRM Console se entrega con la base de datos limpia, sin usuarios ni facturas, cumpliendo con la consigna de entrega profesional.

## Solución y estrategia
El sistema fue desarrollado en Python siguiendo una estructura profesional de paquete, con módulos separados para modelos, servicios, utilidades y acceso a base de datos. Se priorizó la claridad, la validación de datos y la facilidad de uso desde consola.

## Justificación de tipos de datos
- **Strings** para nombres, apellidos, emails, descripciones y estados.
- **Integer** para IDs y números de factura (autoincrementales).
- **Float** para montos de facturas, con validación de positivos.
- **Date/Datetime** para fechas de registro y emisión, usando el tipo nativo de SQLite y formateo en pantalla.
- **Listas** para manejar colecciones de usuarios y facturas en memoria.

## Validaciones implementadas
- Email único y con formato válido.
- Campos obligatorios no vacíos.
- Montos positivos y estados válidos para facturas.
- Verificación de existencia de usuario antes de crear facturas.

## Evaluación y criterios
El sistema cumple con los criterios de la consigna:
- Funcionalidad completa por menú.
- Uso correcto de tipos y estructuras de datos.
- Documentación y análisis incluidos.
- Limpieza de datos nulos desde el menú.

## Conclusión
El sistema está listo para entrega y evaluación, cumpliendo con los requisitos académicos y buenas prácticas de desarrollo en Python. La base de datos se entrega limpia.

## Estructura del proyecto
El proyecto sigue la siguiente estructura de carpetas y archivos:

```
crm_console/
│
├── crm_console.py          # Punto de entrada del sistema
├── README.md               # Documentación del proyecto
├── requirements.txt        # Dependencias del proyecto
│
├── modelos/                # Modelos de datos
│   ├── __init__.py
│   ├── usuario.py
│   └── factura.py
│
├── servicios/              # Lógica de negocio
│   ├── __init__.py
│   ├── servicio_usuario.py
│   └── servicio_factura.py
│
├── utilidades/            # Funciones y clases útiles
│   ├── __init__.py
│   ├── validador.py
│   └── formateador.py
│
└── db/                     # Base de datos
    ├── __init__.py
    └── conexion.py
```

### Detalles de la implementación
- **crm_console.py**: Archivo principal que inicia la aplicación y muestra el menú.
- **modelos/**: Contiene las definiciones de los modelos de datos y sus relaciones.
- **servicios/**: Implementa la lógica de negocio, como el cálculo de montos y la generación de reportes.
- **utilidades/**: Funciones auxiliares para validación de datos y formateo de salida.
- **db/**: Manejo de la conexión a la base de datos SQLite y funciones relacionadas.

Esta estructura permite un fácil mantenimiento y escalabilidad del sistema, siguiendo buenas prácticas de desarrollo en Python.
