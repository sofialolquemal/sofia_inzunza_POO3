#Prueba de poo 3
from abc import ABC, abstractmethod
class Trabajador(ABC):
    def __init__(self, nombre, rut, sueldo_base):
        self.nombre = nombre
        self.rut = rut
        self.__sueldo_base = sueldo_base
        
    def get_sueldo_base(self):
        return self.__sueldo_base
    
    @abstractmethod
    def calcular_sueldo(self):
        pass
    
class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, ventas, comision):
        super().__init__(nombre, rut, sueldo_base)
        self.ventas = ventas
        self.comision = comision
    def tipo(self):
        return "(Vendedor)"
    def calcular_sueldo(self):
        return self.get_sueldo_base() + (self.ventas * self.comision)
        
class Administrador(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.bono = bono
    def tipo(self):
        return "(Administrador)"
    def calcular_sueldo(self):
        return self.get_sueldo_base() + self.bono
        
class Distribuidor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base):
        super().__init__(nombre, rut, sueldo_base)
    def tipo(self):
        return "(Distribuidor)"
    def calcular_sueldo(self):
        return self.get_sueldo_base()

class Pasante(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, colacion, transporte, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.colacion = colacion
        self.transporte = transporte
        self.bono = bono
    def tipo(self):
        return "(Pasante)"
    def calcular_sueldo(self):
        return self.get_sueldo_base() + self.colacion + self.transporte + self.bono

trabajadores = [
    Vendedor("Eva", "265211247", 300000, 10, 20000),
    Administrador("Sofia", "229299638", 400000, 50000),
    Distribuidor("Catalina", "229226232", 600000),
    Pasante("Yeral", "221225420", 0, 50000, 20000, 20000)
    ]
    
for tra in trabajadores:
    print (tra.tipo(), "Sueldo",tra.nombre, tra.calcular_sueldo())