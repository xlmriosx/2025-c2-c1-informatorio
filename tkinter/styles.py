import tkinter as tk

BG_COLOR = "#2C3E50"
FG_COLOR = "#ECF0F1"
ACCENT_COLOR = "#3498DB"
SUCCESS_COLOR = "#2ECC71"
WARNING_COLOR = "#E74C3C"
CARD_BG = "#34495E"
MUTED = "#95A5A6"

def config_root(root: tk.Tk) -> None:
    root.title("Calculadora de Edad")
    root.geometry("500x600")
    root.resizable(False, False)
    root.configure(bg=BG_COLOR)

def crear_entry(parent, width, placeholder=None):
    e = tk.Entry(parent, font=("Helvetica", 12), width=width, relief="flat",
                 bg=CARD_BG, fg=FG_COLOR, insertbackground=FG_COLOR)
    if placeholder:
        e.insert(0, placeholder)
    return e

def crear_button(parent, text, bg, fg="white", cmd=None, font=("Helvetica", 12, "bold"), padx=24, pady=10):
    return tk.Button(parent, text=text, font=font, bg=bg, fg=fg, relief="flat",
                     cursor="hand2", command=cmd, padx=padx, pady=pady)

def crear_label(parent, text, size=12, bold=False, bg=BG_COLOR, fg=FG_COLOR):
    font = ("Helvetica", size, "bold" if bold else "normal")
    return tk.Label(parent, text=text, font=font, bg=bg, fg=fg)