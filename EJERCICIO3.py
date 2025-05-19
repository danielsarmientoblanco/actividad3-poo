class Mascota:
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"nombre={self.nombre!r}, edad={self.edad}, color={self.color!r})")

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"nombre={self.nombre!r}, edad={self.edad}, color={self.color!r}, "
                f"peso={self.peso}, muerde={self.muerde})")

class PerroPequeno(Perro):
    pass

class Caniche(PerroPequeno):
    pass

class YorkshireTerrier(PerroPequeno):
    pass

class Schnauzer(PerroPequeno):
    pass

class Chihuahua(PerroPequeno):
    pass

class PerroMediano(Perro):
    pass

class Collie(PerroMediano):
    pass

class Dalmata(PerroMediano):
    pass

class Bulldog(PerroMediano):
    pass

class Galgo(PerroMediano):
    pass

class Sabueso(PerroMediano):
    pass

class PerroGrande(Perro):
    pass

class PastorAleman(PerroGrande):
    pass

class Doberman(PerroGrande):
    pass

class Rotweiller(PerroGrande):
    pass

class Gato(Mascota):
    def __init__(self, nombre: str, edad: int, color: str,
                 altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def __str__(self):
        return (f"{self.__class__.__name__}("
                f"nombre={self.nombre!r}, edad={self.edad}, color={self.color!r}, "
                f"altura_salto={self.altura_salto}, longitud_salto={self.longitud_salto})")

class GatoSinPelo(Gato):
    pass

class Esfinge(GatoSinPelo):
    pass

class Elfo(GatoSinPelo):
    pass

class Donskoy(GatoSinPelo):
    pass

class GatoPeloLargo(Gato):
    pass

class Angora(GatoPeloLargo):
    pass

class Himalayo(GatoPeloLargo):
    pass

class Balines(GatoPeloLargo):
    pass

class Somali(GatoPeloLargo):
    pass

class GatoPeloCorto(Gato):
    pass

class AzulRuso(GatoPeloCorto):
    pass

class Britanico(GatoPeloCorto):
    pass

class Manx(GatoPeloCorto):
    pass

class DevonRex(GatoPeloCorto):
    pass

if __name__ == "__main__":
    Perro.sonido()
    Gato.sonido()

    luna = Caniche("Luna", 3, "Blanco", peso=5.0, muerde=False)
    biggles = Esfinge("Mr. Biggles", 2, "Beige", altura_salto=0.5, longitud_salto=1.2)

    print(luna)
    print(biggles)
