class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if self.prestado:
            print(f"El libro {self.titulo} ya está prestado")
        else:
            self.prestado = True
            print(f"Se ha prestado el libro {self.titulo}")
    
    def devolver(self):
        if not self.prestado:
            print(f"El libro {self.titulo} ya ha sido devuelto")
        else:
            self.prestado = False
            print(f"Se ha devuelto el libro {self.titulo}")

libro_1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro_2 = Libro("El Quijote", "Cervantes")

print(libro_1.titulo)
print(libro_1.autor)
print(libro_2.titulo)
print(libro_2.autor)

libro_1.prestar()

libro_1.devolver()
libro_1.devolver()