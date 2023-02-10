

class Pieza:
    def __init__(self, nombre, color):

        self.nombre = nombre
        self.color = color
        self.casilla_ocupada = None
        self.tocada = False
        self.sprite = None
        self.posicion = None
    

    def __repr__(self) -> str:
        return f"{self.nombre} ({self.color})"
        

class Rey(Pieza):
    
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
        self.imagen = None
        self.posicion_inicial = None
        self.sprite = None

# rey = Rey("Rey", color)

class Reina(Pieza):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Torre(Pieza):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

        self.posicion_inicial = None
        self.sprite = None
    


class Alfil(Pieza):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Caballo(Pieza):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Peon(Pieza):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

        self.posicion_inicial = None
        self.sprite = None
        