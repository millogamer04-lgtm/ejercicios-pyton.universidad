from abc import ABC, abstractmethod


class ProcesadorPago(ABC):
    @abstractmethod
    def procesar(self, monto: float) -> bool:
        pass


class PagoTarjetas(ProcesadorPago):
    def procesar(self, monto: float) -> bool:
        print(f"Cobrando ${monto} vía Pasarela de Tarjeta.")
        return True


# No se puede crear directamente un objeto ProcesadorPago porque es abstracta.
pago = PagoTarjetas()
pago.procesar(150.50)
