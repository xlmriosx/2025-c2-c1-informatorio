import tkinter as tk
from datetime import datetime

from calculos import calcular_edad, es_mayor_de_edad
from utils import (
    parsear_fecha, validar_nombre, validar_fecha_no_futura,
    guardar_registro_csv, alert_error, alert_warn
)
from styles import (
    config_root, crear_entry, crear_button, crear_label,
    BG_COLOR, FG_COLOR, ACCENT_COLOR, SUCCESS_COLOR, WARNING_COLOR, CARD_BG, MUTED
)

def on_calcular(nombre_entry, dia_entry, mes_entry, anio_entry, resultado_label):
    try:
        nombre = nombre_entry.get().strip()
        if not validar_nombre(nombre):
            alert_warn("Por favor ingresa un nombre.")
            return

        fecha_nac = parsear_fecha(dia_entry.get(), mes_entry.get(), anio_entry.get())
        if not validar_fecha_no_futura(fecha_nac):
            alert_error("La fecha de nacimiento no puede ser ftura.")
            return

        edad = calcular_edad(fecha_nac, datetime.now())
        mayor = es_mayor_de_edad(edad)

        estado = "✅ Mayor de edad" if mayor else "⚠️Menor de edad"
        color = SUCCESS_COLOR if mayor else WARNING_COLOR
        resultado = f"{nombre}\n\nTiene {edad} años\n\n{estado}"
        resultado_label.config(text=resultado, fg=color)

        guardar_registro_csv(nombre, fecha_nac, edad, mayor)

    except ValueError:
        alert_error("Por favor ingresa una fecha válida (números correctos).")
    except Exception as e:
        alert_error(f"Ocurrió un error: {e}")

def on_limpiar(nombre_entry, dia_entry, mes_entry, anio_entry, resultado_label):
    nombre_entry.delete(0, tk.END)
    dia_entry.delete(0, tk.END);  dia_entry.insert(0, "DD")
    mes_entry.delete(0, tk.END);  mes_entry.insert(0, "MM")
    anio_entry.delete(0, tk.END); anio_entry.insert(0, "AAAA")
    resultado_label.config(text="", fg=FG_COLOR)

def construir_ui(root: tk.Tk):
    config_root(root)

    main = tk.Frame(root, bg=BG_COLOR)
    main.pack(expand=True, fill="both", padx=30, pady=30)

    titulo = crear_label(main, "🎂 Calculadora de Eda", size=24, bold=True)
    titulo.pack(pady=(0, 30))

    inputs = tk.Frame(main, bg=BG_COLOR)
    inputs.pack(pady=20)

    crear_label(inputs, "Nombre:").grid(row=0, column=0, sticky="w", pady=10)
    nombre_entry = crear_entry(inputs, width=25)
    nombre_entry.grid(row=0, column=1, padx=10, pady=10, ipady=8)

    crear_label(inputs, "Fecha de Nacimiento:").grid(row=1, column=0, sticky="w", pady=10)
    fecha_frame = tk.Frame(inputs, bg=BG_COLOR)
    fecha_frame.grid(row=1, column=1, padx=10, pady=10)

    dia_entry = crear_entry(fecha_frame, width=4, placeholder="DD");  dia_entry.pack(side="left", ipady=8)
    crear_label(fecha_frame, "/", bg=BG_COLOR, fg=FG_COLOR).pack(side="left", padx=5)
    mes_entry = crear_entry(fecha_frame, width=4, placeholder="MM");  mes_entry.pack(side="left", ipady=8)
    crear_label(fecha_frame, "/", bg=BG_COLOR, fg=FG_COLOR).pack(side="left", padx=5)
    anio_entry = crear_entry(fecha_frame, width=6, placeholder="AAAA"); anio_entry.pack(side="left", ipady=8)

    calcular_btn = crear_button(main, "Calcular Edad", ACCENT_COLOR,
                                cmd=lambda: on_calcular(nombre_entry, dia_entry, mes_entry, anio_entry, resultado_label),
                                font=("Helvetica", 14, "bold"), padx=30, pady=12)
    calcular_btn.pack(pady=30)

    resultado_frame = tk.Frame(main, bg=CARD_BG, relief="flat")
    resultado_frame.pack(pady=20, fill="x")

    resultado_label = tk.Label(resultado_frame, text="", font=("Helvetica", 14),
                               bg=CARD_BG, fg=FG_COLOR, wraplength=400, justify="center")
    resultado_label.pack(pady=20)

    limpiar_btn = crear_button(main, "Limpiar", MUTED, cmd=lambda: on_limpiar(nombre_entry, dia_entry, mes_entry, anio_entry, resultado_label),
                               font=("Helvetica", 11), padx=20, pady=8)
    limpiar_btn.pack(pady=10)

def main():
    root = tk.Tk()
    construir_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()