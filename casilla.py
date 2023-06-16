import numpy as np
import pygame as pg

class Casilla:

    def __init__(self, coordenadas:np.ndarray):
        self.coordenadas = coordenadas
        self.coordenada_en_x, self.coordenada_en_y = coordenadas
        self.rect = self.getRect()

        self.pieza = None
        self.color = None
        self.sprite = None
    

    def __repr__(self) -> str:
        return str((self.coordenada_en_x, self.coordenada_en_y))
    

    def getRect(self):
        from tablero import Tablero
        rect = pg.Rect((0,0,0,0))
        rect.x = self.coordenada_en_x*Tablero.ancho_casilla
        rect.y = self.coordenada_en_y*Tablero.alto_casilla
        rect.width = Tablero.ancho_casilla
        rect.height = Tablero.alto_casilla
        return rect





