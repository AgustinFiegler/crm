import datetime

def input_opcional(mensaje):
    valor = input(mensaje)
    return valor.strip() if valor.strip() else None
