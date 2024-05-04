class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un libro a la biblioteca.

        Args:
            libro (Libro): El libro a agregar.

        Raises:
            ValueError: Si el libro no tiene título o autor.
        """
        if not libro.titulo or not libro.autor:
            raise ValueError("El libro debe tener un título y un autor.")
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        """
        Busca un libro por su título en la biblioteca.

        Args:
            titulo (str): El título del libro a buscar.

        Returns:
            Libro: El libro encontrado.

        Raises:
            ValueError: Si no se encuentra ningún libro con el título especificado.
        """
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise ValueError(f"No se encontró ningún libro con el título '{titulo}'.")

    def mostrar_libros(self):
        """Muestra todos los libros de la biblioteca."""
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")


class ErrorLibroSinTitulo(Exception):
    """Excepción lanzada cuando un libro no tiene título."""
    def __init__(self, mensaje="El libro debe tener un título."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorLibroSinAutor(Exception):
    """Excepción lanzada cuando un libro no tiene autor."""
    def __init__(self, mensaje="El libro debe tener un autor."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorAutorInvalido(Exception):
    """Excepción lanzada cuando el autor de un libro no es válido."""
    def __init__(self, mensaje="El autor del libro debe ser una cadena de caracteres."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ErrorAñoPublicacionInvalido(Exception):
    """Excepción lanzada cuando el año de publicación de un libro no es válido."""
    def __init__(self, mensaje="El año de publicación del libro debe ser un número entero positivo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def obtener_titulo():
    """
    Solicita al usuario que ingrese el título del libro.

    Returns:
        str: El título del libro ingresado por el usuario.
    """
    intentos = 0
    while intentos < 3:
        titulo = input("Ingrese el título del libro: ")
        if titulo:
            return titulo
        else:
            print("El título no puede estar vacío.")
            intentos += 1
    return None


def obtener_autor():
    """
    Solicita al usuario que ingrese el autor del libro.

    Returns:
        str: El autor del libro ingresado por el usuario.
    """
    intentos = 0
    while intentos < 3:
        autor = input("Ingrese el autor del libro: ")
        if all(c.isalpha() or c.isspace() for c in autor):
            return autor
        else:
            print("El autor del libro debe contener solo letras y espacios.")
            intentos += 1
    return None


def obtener_año_publicacion():
    """
    Solicita al usuario que ingrese el año de publicación del libro.

    Returns:
        int: El año de publicación del libro ingresado por el usuario.
    """
    intentos = 0
    while intentos < 3:
        año_publicacion = input("Ingrese el año de publicación del libro: ")
        if año_publicacion.isdigit() and int(año_publicacion) > 0:
            return int(año_publicacion)
        else:
            print("El año de publicación del libro debe ser un número entero positivo.")
            intentos += 1
    return None


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Mostrar todos los libros")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = obtener_titulo()
            if titulo is None:
                print("No se pudo obtener el título del libro después de tres intentos. Regresando al menú principal.")
                continue

            autor = obtener_autor()
            if autor is None:
                print("No se pudo obtener el autor del libro después de tres intentos. Regresando al menú principal.")
                continue

            año_publicacion = obtener_año_publicacion()
            if año_publicacion is None:
                print("No se pudo obtener el año de publicación del libro después de tres intentos. Regresando al menú principal.")
                continue

            libro = Libro(titulo, autor, año_publicacion)
            try:
                biblioteca.agregar_libro(libro)
            except ValueError as e:
                print(e)

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            try:
                libro_encontrado = biblioteca.buscar_libro(titulo)
                print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
