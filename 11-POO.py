class Punto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"Punto({self.x}, {self.y})"
    
    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y
        
punto_1 = Punto(5, 6)

print(punto_1.x)