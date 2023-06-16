import pygame as pg
class Pieza:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sprite = None
        self.rect = pg.Rect((0,0,0,0))
    

    def __repr__(self) -> str:
        return self.nombre


    def comportamiento(self):
        return