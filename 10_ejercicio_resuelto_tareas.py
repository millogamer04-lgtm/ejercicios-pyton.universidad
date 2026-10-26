from abc import ABC, abstractmethod


class TareaServidor(ABC):
    @abstractmethod
    def ejecutar(self) -> bool:
        pass


class TareaLimpiezaLogs(TareaServidor):
    def ejecutar(self) -> bool:
        print("Depurando archivos .log antiguos en /var/log...")
        return True


class TareaBackupDB(TareaServidor):
    def ejecutar(self) -> bool:
        print("Generando copia de respaldo en Amazon S3...")
        return True


def procesar_cola(tareas: list[TareaServidor]):
    for tarea in tareas:
        tarea.ejecutar()


cola = [TareaLimpiezaLogs(), TareaBackupDB(), TareaLimpiezaLogs()]
procesar_cola(cola)
