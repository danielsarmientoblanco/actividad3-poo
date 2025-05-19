from enum import Enum

class Inmueble:
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str):
        self.identificadorInmobiliario = identificadorInmobiliario
        self.area = area
        self.direccion = direccion
        self.precioVenta = 0.0

    def calcularPrecioVenta(self, valorArea: float) -> float:
        self.precioVenta = self.area * valorArea
        return self.precioVenta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self.identificadorInmobiliario}")
        print(f"Area = {self.area}")
        print(f"Dirección = {self.direccion}")
        print(f"Precio de venta = ${self.precioVenta}")

class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.numeroHabitaciones = numeroHabitaciones
        self.numeroBaños = numeroBaños

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self.numeroHabitaciones}")
        print(f"Número de baños = {self.numeroBaños}")

class Casa(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, numeroPisos: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
        self.numeroPisos = numeroPisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self.numeroPisos}")

class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)

    def imprimir(self):
        super().imprimir()

class CasaRural(Casa):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, numeroPisos: int,
                 distanciaCabecera: int, altitud: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self.distanciaCabecera = distanciaCabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self.distanciaCabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros.")
        print()

class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, numeroPisos: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)

    def imprimir(self):
        super().imprimir()

class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, valorAdministracion: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
        self.valorAdministracion = valorAdministracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self.valorAdministracion}")
        print()

class Apartaestudio(Apartamento):
    valorArea = 1500000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str):
        super().__init__(identificadorInmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()

class CasaConjuntoCerrado(CasaUrbana):
    valorArea = 2500000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, numeroPisos: int,
                 valorAdministracion: int, tienePiscina: bool, tieneCamposDeportivos: bool):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self.valorAdministracion = valorAdministracion
        self.tienePiscina = tienePiscina
        self.tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self.valorAdministracion}")
        print(f"Tiene piscina? = {self.tienePiscina}")
        print(f"Tiene campos deportivos? = {self.tieneCamposDeportivos}")
        print()

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str,
                 numeroHabitaciones: int, numeroBaños: int, numeroPisos: int):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)

    def imprimir(self):
        super().imprimir()
        print()

class TipoLocal(Enum):
    INTERNO = "INTERNO"
    CALLE = "CALLE"

class Local(Inmueble):
    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str, tipoLocal: TipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self.tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self.tipoLocal.name}")

class LocalComercial(Local):
    valorArea = 3000000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str, tipoLocal: TipoLocal, centroComercial: str):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self.centroComercial}")
        print()

class Oficina(Local):
    valorArea = 3500000

    def __init__(self, identificadorInmobiliario: int, area: int, direccion: str, tipoLocal: TipoLocal, esGobierno: bool):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self.esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self.esGobierno}")
        print()

if __name__ == "__main__":
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print("Datos apartamento")
    apto1.calcularPrecioVenta(ApartamentoFamiliar.valorArea)
    apto1.imprimir()

    print("Datos apartaestudio")
    aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
    aptestudio1.calcularPrecioVenta(Apartaestudio.valorArea)
    aptestudio1.imprimir()
