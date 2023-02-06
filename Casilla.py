import pygame
from Sprites import SpriteParaCasilla
from pygame import Rect, Surface


class Casilla:

    def __init__(self, coordenadas, tablero):
        self.ancho = int(tablero.ancho/8)
        self.alto =  int(tablero.alto/8)
        self.tamano = (self.ancho, self.alto)

        self.x, self.y = coordenadas
        self.coordenadas = coordenadas
        self.origen_de_dibujo = (int(self.x*self.ancho)+1, int(self.y*self.alto))
        self.rect = Rect(self.origen_de_dibujo[0],self.origen_de_dibujo[1], self.ancho, self.alto)
        self.imagen = Surface(self.tamano)
        self.paridad = None
        self.color = None
        

        self.paridad_y_color()
        self.sprite = SpriteParaCasilla(self)


    def __repr__(self) -> str:
        return f"{self.coordenadas}"


    def paridad_y_color(self):
        if sum(self.coordenadas)%2:
            self.paridad = True
            self.color = pygame.Color(139,69,19)
            self.imagen.fill(self.color)
        else:
            self.paridad = False
            self.color = pygame.Color(222,184,135)
            self.imagen.fill(self.color)

            
    
    

    


    