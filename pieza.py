import pygame as pg

class Pieza:
    def __init__(self, nombre):
        self.nombre = nombre
        self.color = 'blancas' if '_b' in self.nombre else 'negras'
        self.sprite = None
        self.rect = pg.Rect((0,0,0,0))
        self.seleccionada = False
        self.salta_piezas = True if 'caballo' in self.nombre else False
    

    def __repr__(self) -> str:
        return self.nombre


    def comportamiento(self):
        pass
    

    def casillas_atacadas(self):
        pass


class Peon(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)


    def comportamiento(self, movimiento):
        pass




class Alfil(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.sprite = None


    def respeta_patron_de_movimiento(self, movimiento):
        xi, yi = movimiento.casilla_de_partida.coordenadas[0],  movimiento.casilla_de_partida.coordenadas[1]
        xf, yf =  movimiento.casilla_atacada.coordenadas[0], movimiento.casilla_atacada.coordenadas[0][1]
        return True if abs(xf-xi) == abs(yf-yi) else False
    

class Caballo(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.sprite = None
        self.salta_piezas = True
    

    def comportamiento(self):
            pass


class Torre(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.sprite = None
    

    def comportamiento(self):
            pass


class Rey(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)


    def comportamiento(self):
            pass


class Reina(Pieza):
    def __init__(self, nombre):
        super().__init__(nombre)

    
    def comportamiento(self):
            pass