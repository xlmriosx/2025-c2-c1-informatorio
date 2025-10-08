import tkinter as tk

ventana = tk.Tk()
ventana.title('Informatorio')
ventana.geometry("800x600")
ventana.configure(bg="#FF722C")

etiqueta = tk.Label(ventana, text='Bienvenidos!', font=('Arial', 50), fg="red")
etiqueta.pack()

ventana.mainloop()
