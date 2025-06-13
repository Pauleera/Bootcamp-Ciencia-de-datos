class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn

    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_isbn(self):
        return self.__isbn    
    
    def descripcion(self):
        return f"Título: {self.__titulo} - Autor: {self.__autor}, ISBN: {self.__isbn}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def mostrar_libro(self):
        for libro in self.libros:
            print(libro.descripcion())
    

biblioteca = Biblioteca()
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "DMACKAK341")
libro2 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "DMACKAK342")
libro3 = Libro("El túnel", "Ernesto Sabato", "DMACKAK343")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

biblioteca.mostrar_libro()