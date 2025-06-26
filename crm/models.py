import datetime

class Usuario:
    def __init__(self, nombre, apellidos, email, telefono=None, direccion=None):
        self.id = None
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.fecha_registro = datetime.date.today()

    def nombre_completo(self):
        return f"{self.nombre} {self.apellidos}"

class Factura:
    def __init__(self, descripcion, monto, estado):
        self.numero = None
        self.fecha = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto
        self.estado = estado

class Presupuesto:
    def __init__(self, descripcion, monto, estado):
        self.numero = None
        self.fecha = datetime.datetime.now()
        self.descripcion = descripcion
        self.monto = monto
        self.estado = estado
