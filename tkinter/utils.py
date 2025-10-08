from datetime import datetime
import csv
import os
from tkinter import messagebox

CSV_FILE = "registros_edad.csv"

def parsear_fecha(dia_str: str, mes_str: str, anio_str: str) -> datetime:
    dia = int(dia_str)
    mes = int(mes_str)
    anio = int(anio_str)
    return datetime(anio, mes, dia)

def validar_nombre(nombre: str) -> bool:
    return bool(nombre and nombre.strip())

def validar_fecha_no_futura(fecha_nacimiento: datetime) -> bool:
    return fecha_nacimiento <= datetime.now()

def guardar_registro_csv(nombre: str, fecha_nac: datetime, edad: int, es_mayor: bool) -> None:
    existe = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(["Nombre", "Fecha de Nacimiento", "Edad", "Mayor de Edad", "Fecha de Consulta"])
        writer.writerow([
            nombre.strip(),
            fecha_nac.strftime("%d/%m/%Y"),
            edad,
            "Sí" if es_mayor else "No",
            datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        ])

def alert_error(msg: str) -> None:
    messagebox.showerror("Error", msg)

def alert_warn(msg: str) -> None:
    messagebox.showwarning("Advertencia", msg)