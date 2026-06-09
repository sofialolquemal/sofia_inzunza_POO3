#Prueba de poo 3
from abc import ABC, abstractmethod #se importa una libreria con funciones abstractas
class Trabajador(ABC): #Esta es la clase madre
    def __init__(self, nombre, rut, sueldo_base): #Todo trabajador tiene nombre rut y sueldo
        self.nombre = nombre 
        self.rut = rut
        self.__sueldo_base = sueldo_base
        
    def get_sueldo_base(self): #Aqui se aplica encpasulamiento pues el sueldo es privado asi que se le aplica un metodo get
        return self.__sueldo_base
    def set_sueldo_base(self, nuevo_sueldo): #Si se quiere cambiar el sueldo debe aplicarse un metodo set
        if nuevo_sueldo >= 0:
            self.__sueldo_base = nuevo_sueldo

    @abstractmethod 
    def calcular_sueldo(self): #el metodo abstracto es calcular sueldo, pues en esta clase no es nesesaria pero despues se utilizara
        pass
    
class Vendedor(Trabajador):  #Aqui se aplica herencia
    def __init__(self, nombre, rut, sueldo_base, ventas, comision): 
        super().__init__(nombre, rut, sueldo_base) #se aplica el super para incorporar los atributos que ya tenia la clase madre
        self.ventas = ventas
        self.comision = comision
    def tipo(self): #el tipo de trabajador es vendedor en este caso
        return "(Vendedor)"
    def calcular_sueldo(self): #Aqui se aplica polimorfismo ya que el sueldo se calcula por cuantas ventas hizo mas su sueldo base
        return self.get_sueldo_base() + (self.ventas * self.comision)
        
class Administrador(Trabajador): # herencia
    def __init__(self, nombre, rut, sueldo_base, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.bono = bono
    def tipo(self):
        return "(Administrador)"
    def calcular_sueldo(self): #polimorfismo
        return self.get_sueldo_base() + self.bono
        
class Distribuidor(Trabajador): #herencia
    def __init__(self, nombre, rut, sueldo_base):
        super().__init__(nombre, rut, sueldo_base)
    def tipo(self):
        return "(Distribuidor)"
    def calcular_sueldo(self): #polimorfismo
        return self.get_sueldo_base() # este tiene un sueldo fijo por lo que se devuelve eso nada mas

class Pasante(Trabajador): #herencia
    def __init__(self, nombre, rut, sueldo_base, colacion, transporte, bono):
        super().__init__(nombre, rut, sueldo_base)
        self.colacion = colacion
        self.transporte = transporte
        self.bono = bono
    def tipo(self):
        return "(Pasante)"
    def calcular_sueldo(self): #polimorfismo
        return self.get_sueldo_base() + self.colacion + self.transporte + self.bono #al sueldo base (0), se le añade plata para la colacion y el transporte

trabajadores = [ #Contructor, lisra donde se incluyen los trabajadores y sus datos correpondientes
    Vendedor("Eva", "265211247", 300000, 10, 20000),
    Administrador("Sofia", "229299638", 400000, 50000),
    Distribuidor("Catalina", "229226232", 600000),
    Pasante("Yeral", "221225420", 0, 50000, 20000, 20000)
    ]
    
for tra in trabajadores:
    print (tra.tipo(), "Sueldo",tra.nombre, tra.calcular_sueldo()) #aqui se imprime los sueldos de cada uno