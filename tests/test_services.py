import pytest
from crm import services, models

def test_agregar_y_buscar_cliente(tmp_path):
    db_path = tmp_path / "test_crm.sqlite3"
    services.inicializar_db(str(db_path))
    cliente = models.Cliente(nombre="Test", apellido="User", email="test@user.com")
    services.agregar_cliente(cliente, str(db_path))
    resultado = services.buscar_cliente_por_email("test@user.com", str(db_path))
    assert resultado is not None
    assert resultado.nombre == "Test"
    assert resultado.apellido == "User"
    assert resultado.email == "test@user.com"
