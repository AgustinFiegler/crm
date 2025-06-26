import pytest
from crm import models

def test_cliente_creation():
    cliente = models.Cliente(nombre="Juan", apellido="Pérez", email="juan@example.com")
    assert cliente.nombre == "Juan"
    assert cliente.apellido == "Pérez"
    assert cliente.email == "juan@example.com"

def test_cliente_str():
    cliente = models.Cliente(nombre="Ana", apellido="López", email="ana@example.com")
    assert str(cliente) == "Ana López <ana@example.com>"
