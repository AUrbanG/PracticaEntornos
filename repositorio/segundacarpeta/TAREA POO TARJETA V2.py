# TAREA POO TARJETA V2

# Vamos a añadir más funcionalidades a las tarjetas creadas en la sesión anterior.
# En la tarjeta de crédito, le vamos a añadir las acciones de sumar saldo, cuando realizamos una compra, restar saldo cuando hacemos una devolución, y reiniciar el saldo a 0 
# (se usaría por ejemplo cuando llega final de mes y pagamos el saldo de la tarjeta). 

# En la tarjeta descuento, tendremos las acciones de sumar saldo, cuando realizamos una compra, restar saldo cuando hacemos una devolución, y reiniciar el saldo a 0. 
# Además, cuando el saldo llegue a una determinada cantidad, el descuento aumentará, tal como indica la siguiente tabla:

# SALDO		+DESCUENTO %
# 500			2
# 1000			3
# 2000			4


# En todo momento el usuario debe estar informado de todas las acciones realizadas (pista, mostrar por pantalla lo que hacemos). Lógicamente se debe poder mostrar por pantalla el saldo (en ambas tarjetas).


class Tarjeta:
    def __init__(self, num):
        self.num = num
        self.saldo = 0

    def mostrar_saldo(self):
        print(f"El saldo actual de tu tarjeta con ID {self.num} es de: {self.saldo}€")

    def sumar_saldo(self, cantidad):
        self.saldo += cantidad
        print(f"Compra realizada por {cantidad}€. Saldo actualizado: {self.saldo}€")

    def restar_saldo(self, cantidad):
        self.saldo -= cantidad
        print(f"Devolución realizada por {cantidad}€. Saldo actualizado: {self.saldo}€")

    def reiniciar_saldo(self):
        self.saldo = 0
        print("Saldo reiniciado a 0€")


class TarjetaDescuento(Tarjeta):

    def __init__(self, num):
        super().__init__(num)
        self.descuento = 0

    def mostrar_descuento(self):
        print(f"El descuento actual de tu tarjeta con ID {self.num} es de un {self.descuento}%")

    def comprobar_descuento(self):
        if self.saldo >= 2000:
            self.descuento = 4
        elif self.saldo >= 1000:
            self.descuento = 3
        elif self.saldo >= 500:
            self.descuento = 2
        else:
            self.descuento = 0


    def sumar_saldo(self, cantidad):
        super().sumar_saldo(cantidad)
        self.comprobar_descuento()
        self.mostrar_descuento()

    def restar_saldo(self, cantidad):
        super().restar_saldo(cantidad)
        self.comprobar_descuento()
        self.mostrar_descuento()

    def reiniciar_saldo(self):
        super().reiniciar_saldo()
        self.comprobar_descuento()
        self.mostrar_descuento()
