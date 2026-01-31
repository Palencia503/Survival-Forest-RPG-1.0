class Objeto:
    def __init__(self, tipo, nombre, precio):
        self.tipo = tipo
        self.nombre = nombre
        self.precio = precio

    def clonar(self): 
        return Objeto(self.tipo, self.nombre, self.precio)

class Pocion(Objeto):
    def __init__(self, tipo, cantidad, nombre, precio, cura = 0, dano = 0):
        super().__init__(tipo, nombre, precio)
        self.cantidad = cantidad
        self.cura = cura
        self.dano = dano

    def clonar(self): #El jugador recibe 1 arma 
        return Arma(self.tipo, 1, self.nombre, self.precio, self.dano)
    
    def __str__(self):
        efecto = ""
        if self.cura > 0:
            efecto = f"Cura: {self.cura}"

        if self.dano > 0:
            if efecto:
                efecto += ", "
            efecto += f"Daño: {self.dano}"
            
        return f"{self.nombre} (x{self.cantidad}) - Precio: {self.precio} - {efecto}"
    
    def clonar(self):
        return Pocion(self.tipo, 1, self.nombre, self.precio, self.cura, self.dano)
    
class Arma(Objeto):
    def __init__(self, tipo, cantidad, nombre, precio, dano=0, defensa=0):
        super().__init__(tipo, nombre, precio)
        self.cantidad = cantidad
        self.dano = dano
        self.defensa = defensa

    def __str__(self):
        texto = f"{self.nombre} (x{self.cantidad}) - Precio: {self.precio}"
        if self.dano > 0:
            texto += f" - Dano: {self.dano}"
        if self.defensa > 0:
            texto += f" - Defensa: {self.defensa}"
        return texto

    def clonar(self):
        return Arma(self.tipo, 1, self.nombre, self.precio, self.dano, self.defensa)
