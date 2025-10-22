class Libro:
    def __init__(self, titulo, autor, ISBN, paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.paginas = paginas
        self.genero = genero
        self.__prestado = False

    def __str__(self):
        return f"El libro '{self.titulo}' de {self.autor} con {self.paginas} paginas es de {self.genero}"
    
    def prestar(self):
        if self.__prestado:
            print(f'El libro "{self.titulo}" ya esta prestado')
            return False
        else:
            self.__prestado = True
            print(f'Libro "{self.titulo}" prestado exitosamente')
            return True
    
    def devolver(self):
        if not self.__prestado:
            print(f'El libro "{self.titulo}" no estaba prestado')
            return False
        else:
            self.__prestado = False
            print(f'Libro "{self.titulo}" devuelto exitosamente')
            return True
    
    def esta_prestado(self):
        return self.__prestado
    
class LibroInfantil(Libro):
    def __init__(self, titulo, autor, ISBN, paginas, genero, edad_recomendada, ilustraciones):
        super().__init__(titulo, autor, ISBN, paginas, genero)
        self.edad_recomendada = edad_recomendada
        self.ilustraciones = ilustraciones
    
    def __str__(self):
        return (f"Libro Infantil '{self.titulo}' de {self.autor} - "
                f"Edad recomendada: {self.edad_recomendada}+ anos - "
                f"Ilustraciones: {'Si' if self.ilustraciones else 'No'}")
    
    def prestar(self, lector):
        if self._prestado:
            print(f'El libro infantil "{self.titulo}" ya esta prestado')
            return False
        
        if lector.edad < self.edad_recomendada:
            print(f'Advertencia: "{self.titulo}" esta recomendado para {self.edad_recomendada}+ anos')
            print(f'   {lector.nombre} tiene {lector.edad} anos')
        
        self._prestado = True
        print(f'Libro infantil "{self.titulo}" prestado a {lector.nombre}')
        return True


class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.libros_publicados = []
    
    def publicar_libro(self, libro):
        self.libros_publicados.append(libro)
        print(f'{self.nombre} ha publicado "{libro.titulo}"')


class Lector:
    def __init__(self, nombre, edad, direccion, numero_socio):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.numero_socio = numero_socio
        self.libros_prestados = []
    
    def solicitar_prestamo(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            if libro.devolver():
                self.libros_prestados.remove(libro)
                return True
        else:
            print(f'{self.nombre} no tiene prestado este libro')
        return False

class LectorSocio(Lector):
    limite_prestamos = 5
    
    def __init__(self, nombre, edad, direccion, numero_socio, fecha_inscripcion):
        super().__init__(nombre, edad, direccion, numero_socio)
        self.fecha_inscripcion = fecha_inscripcion
    
    def solicitar_prestamo(self, libro):
        print(f'Socio Premium: {self.nombre}')
        return super().solicitar_prestamo(libro)
    
class Libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.lectores = []
        self.autores = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f'Libro "{libro.titulo}" agregado a la libreria')
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        print(f'Libro "{titulo}" no encontrado')
        return None
    
    def registrar_lector(self, lector):
        self.lectores.append(lector)
        print(f'Lector {lector.nombre} registrado')
    
    def prestar_libro(self, titulo, lector):
        libro = self.buscar_libro(titulo)
        if libro:
            return lector.solicitar_prestamo(libro)
        return False


libreria = Libreria("Biblioteca Central")

libro1 = Libro("Cien anos de soledad", "Gabriel Marq", "29793", 123, "Realismo magico")
libro2 = Libro("1984", "George Orwell", "978-0451524935", 300, "Distopico")

libreria.agregar_libro(libro1)
libreria.agregar_libro(libro2)

lector1 = Lector("Joe Doe", 25, "Calle 123", "001")
libreria.registrar_lector(lector1)

libreria.prestar_libro("1984", lector1)