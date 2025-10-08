from datetime import datetime

def calcular_edad(fecha_nacimiento: datetime, fecha_actual: datetime | None = None) -> int:
    if fecha_actual is None:
        fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day):
        edad -= 1
    return edad

def es_mayor_de_edad(edad: int, mayoria: int = 18) -> bool:
    return edad >= mayoria