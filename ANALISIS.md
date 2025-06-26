# ANÁLISIS Y JUSTIFICACIÓN DEL PROYECTO CRM CONSOLE

## Solución y estrategia
El sistema CRM Console fue desarrollado en Python siguiendo una estructura profesional de paquete, con módulos separados para modelos, servicios, utilidades y acceso a base de datos. Se priorizó la claridad, la validación de datos y la facilidad de uso desde consola.

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

## Mejoras posibles
- Exportación de reportes a CSV.
- Interfaz web o API REST.
- Gestión de usuarios y permisos.

## Conclusión
El sistema está listo para entrega y evaluación, cumpliendo con los requisitos académicos y buenas prácticas de desarrollo en Python.
