
class TarjetaCredito:
    def calcular_cashback(self, monto):
        return 0.0


class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto):
        return monto * 0.02


class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto):
        return monto * 0.05


# Ejemplo de uso
tarjeta_gold = TarjetaGold()
tarjeta_black = TarjetaBlack()

compra = 100000

print("Valor de la compra: $", compra)
print("Cashback Gold: $", tarjeta_gold.calcular_cashback(compra))
print("Cashback Black: $", tarjeta_black.calcular_cashback(compra))

