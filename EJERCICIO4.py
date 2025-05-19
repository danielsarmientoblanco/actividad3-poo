class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def getnombre(self) -> str:
        return self.nombre

    def getdireccion(self) -> str:
        return self.direccion

    def setnombre(self, nombre: str) -> None:
        self.nombre = nombre

    def setdireccion(self, direccion: str) -> None:
        self.direccion = direccion

class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getcarrera(self) -> str:
        return self.carrera

    def getsemestre(self) -> int:
        return self.semestre

    def setcarrera(self, carrera: str) -> None:
        self.carrera = carrera

    def setsemestre(self, semestre: int) -> None:
        self.semestre = semestre

class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getdepartamento(self) -> str:
        return self.departamento

    def getcategoria(self) -> str:
        return self.categoria

    def setdepartamento(self, departamento: str) -> None:
        self.departamento = departamento

    def setcategoria(self, categoria: str) -> None:
        self.categoria = categoria


if __name__ == "__main__":
    persona1= Persona("Ana Pérez", "Calle Colombia 123")
    print(persona1.getnombre(), "-", persona1.getdireccion())

    estudiante1 = Estudiante("Luis Gómez", "Av. Siempre Viva 742", "Ingeniería de Sistemas", 5)
    print(estudiante1.getnombre(), "-", estudiante1.getcarrera(), "-","semestre", estudiante1.getsemestre())

    profesor1 = Profesor("María Ruiz", "Calle Luna 456", "Matemáticas", "Titular")
    print(profesor1.getnombre(), "-", profesor1.getdepartamento(), "-", profesor1.getcategoria())
