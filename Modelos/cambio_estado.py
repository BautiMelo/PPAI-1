import datetime
from .estado import Estado

class CambioEstado:
    def __init__(self, fechaHoraDesde: datetime.datetime, estado: Estado, fechaHoraHasta: datetime.datetime = None):
        self.__fechaHoraDesde = fechaHoraDesde
        self.__fechaHoraHasta = fechaHoraHasta
        self.__estado = estado

    # FechaHoraDesde
    def getFechaHoraDesde(self):
        return self.__fechaHoraDesde
    
    def setFechaHoraDesde(self, fechaHoraDesde):
        self.__fechaHoraDesde = fechaHoraDesde


    # FechaHoraHasta
    def getFechaHoraHasta(self):
        return self.__fechaHoraHasta
    
    def setFechaHoraHasta(self, fechaHoraHasta):
        """Establece la fecha y hora de finalización del estado"""
        self.__fechaHoraHasta = fechaHoraHasta


    # Estado
    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado
        

    # Método para saber si es el cambio de estado actual
    def esEstadoActual(self):
        return self.__fechaHoraHasta is None


