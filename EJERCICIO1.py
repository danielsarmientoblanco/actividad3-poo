class Cuenta:
    def __init__(self, saldo: float, tasaAnual: float):
        self._saldo = saldo
        self._numeroConsignaciones = 0
        self._numeroRetiros = 0
        self._tasaAnual = tasaAnual
        self.comisionMensual = 0.0

    def consignar(self, cantidad: float):
        self._saldo += cantidad
        self._numeroConsignaciones += 1

    def retirar(self, cantidad: float):
        nuevo_saldo = self._saldo - cantidad
        if nuevo_saldo >= 0:
            self._saldo -= cantidad
            self._numeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcularInteres(self):
        tasa_mensual = self._tasaAnual / 12
        interes_mensual = self._saldo * tasa_mensual
        self._saldo += interes_mensual

    def extractoMensual(self):
        self._saldo -= self.comisionMensual
        self.calcularInteres()


class CuentaAhorros(Cuenta):
    def __init__(self, saldo: float, tasaAnual: float):
        super().__init__(saldo, tasaAnual)
        self._activa = saldo >= 10000

    def retirar(self, cantidad: float):
        if self._activa:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        if self._activa:
            super().consignar(cantidad)

    def extractoMensual(self):
        if self._numeroRetiros > 4:
            self.comisionMensual += (self._numeroRetiros - 4) * 1000
        super().extractoMensual()
        if self._saldo < 10000:
            self._activa = False

    def imprimir(self):
        print(f"Saldo = $ {self._saldo:.2f}")
        print(f"Comisión mensual = $ {self.comisionMensual:.2f}")
        total_trans = self._numeroConsignaciones + self._numeroRetiros
        print(f"Número de transacciones = {total_trans}")
        print()


class CuentaCorriente(Cuenta):
    def __init__(self, saldo: float, tasaAnual: float):
        super().__init__(saldo, tasaAnual)
        self._sobregiro = 0.0

    def retirar(self, cantidad: float):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad: float):
        residuo = self._sobregiro - cantidad
        if self._sobregiro > 0:
            if residuo > 0:
                self._sobregiro = 0
                self._saldo = residuo
            else:
                self._sobregiro = -residuo
                self._saldo = 0
        else:
            super().consignar(cantidad)

    def extractoMensual(self):
        super().extractoMensual()

    def imprimir(self):
        print(f"Saldo = $ {self._saldo:.3f}")
        print(f"Cargo mensual = $ {self.comisionMensual:.2f}")
        total_trans = self._numeroConsignaciones + self._numeroRetiros
        print(f"Número de transacciones = {total_trans}")
        print(f"Valor de _sobregiro = $ {self._sobregiro:.2f}")
        print()


def main():
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial= $"))
    tasa = float(input("Ingrese tasa de interés= "))
    cuenta1 = CuentaAhorros(saldo_inicial, tasa)
    deposito = float(input("Ingresar cantidad a consignar: $"))
    cuenta1.consignar(deposito)
    retiro = float(input("Ingresar cantidad a retirar: $"))
    cuenta1.retirar(retiro)
    cuenta1.extractoMensual()
    cuenta1.imprimir()


if __name__ == "__main__":
    main()
