import numpy as np
import pygame as pg

class Casilla:

    def __init__(self, coordenadas:np.ndarray):
        self.coordenadas = coordenadas
        self.x, self.y = coordenadas
        self.rect = self.getRect()

        self.pieza = None
        self.color = None
        self.sprite = None
        self.seleccionada = False
    

    def __repr__(self) -> str:
        return str(self.coordenadas) + ' ' + self.pieza.nombre if self.pieza else str(self.coordenadas)
    

    def getRect(self):
        from tablero import Tablero
        rect = pg.Rect((0,0,0,0))
        rect.x = self.x*Tablero.ancho_casilla
        rect.y = self.y*Tablero.alto_casilla
        rect.width = Tablero.ancho_casilla
        rect.height = Tablero.alto_casilla
        return rect


    def ocupada(self):
        return True if self.pieza else False


    def distancia_horizontal(self, otra_casilla):
        xi = self.x
        xf = otra_casilla.x
        return abs(xf - xi)


    def distancia_vertical(self, otra_casilla):
        if isinstance(otra_casilla, Casilla):
            yf = otra_casilla.y
        elif isinstance(otra_casilla, int):
            yf = otra_casilla
        yi = self.y
        return abs(yf - yi)


    def distancia_ortogonal(self, otra_casilla):
        distancia_horizontal = self.distancia_horizontal(otra_casilla)
        distancia_vertical = self.distancia_vertical(otra_casilla)
        return distancia_horizontal + distancia_vertical


    def comparte_diagonal_con(self, otra_casilla):
        xi, yi = self.x,  self.y
        xf, yf =  otra_casilla.x,  otra_casilla.y
        return True if abs(xf-xi) == abs(yf-yi) else False


    def comparte_fila_con(self, otra_casilla):
        yi = self.y
        yf = otra_casilla.y
        return True if yf == yi else False


    def comparte_columna_con(self, otra_casilla):
        xi = self.x
        xf = otra_casilla.x
        return True if xf == xi else False
    

    def ortogonal_con(self, otra_casilla):
        return True if self.comparte_fila_con(otra_casilla) or self.comparte_columna_con(otra_casilla) else False
    

    def en_direccion_del_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada = movimiento.casilla_atacada
        eje_del_movimiento = movimiento.get_eje()
        direccion_hacia_casilla_de_partida = casilla_de_partida.get_direccion(self, eje_del_movimiento)
        direccion_hacia_casilla_atacada = casilla_atacada.get_direccion(self, eje_del_movimiento)

        print(f'C: {self}  / direccion_hacia_c_partida: {direccion_hacia_casilla_de_partida}  / direccion_hacia_casilla_atacada: {direccion_hacia_casilla_atacada}')
        return direccion_hacia_casilla_de_partida != direccion_hacia_casilla_atacada
    

    def get_direccion(self, otra_casilla, eje):
        if eje == 'horizontal' and self.comparte_fila_con(otra_casilla):
            direccion = True if (self.x - otra_casilla.x) > 0 else False

        elif eje == 'vertical' and self.comparte_columna_con(otra_casilla):
            direccion = True if (self.y - otra_casilla.y) > 0 else False

        elif eje == 'diagonal' and self.comparte_diagonal_con(otra_casilla):
            direccion = True if self.get_pendiente(otra_casilla) > 0 else False

        else:
            direccion = None

        return direccion


    def get_pendiente(self, otra_casilla):
        return (self.x - otra_casilla.x) / (self.y - otra_casilla.y)
        









