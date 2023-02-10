import pygame
from Sprites import SpriteParaCasilla
from pygame import Rect, Surface


class Casilla:

    def __init__(self, coordenadas, tablero):
        self.ancho, self.alto = int(tablero.ancho/8), int(tablero.alto/8)
        self.tamano = (self.ancho, self.alto)
        self.coordenadas = coordenadas
        self.x, self.y = coordenadas
        
        self.origen_de_dibujo = (int(self.x*self.ancho)+1, int(self.y*self.alto)+1)

        self.rect = Rect(self.origen_de_dibujo[0],self.origen_de_dibujo[1], self.ancho, self.alto)
        self.imagen = Surface(self.tamano)

        self.color = None
        self.asignar_color()

        self.sprite = SpriteParaCasilla(self)
        self.posicion = None
        self.pieza = None
        self.ocupada = False
        self.seleccionada = False


    def __repr__(self) -> str:
        return f"{self.coordenadas}"


    def asignar_color(self):
        if sum(self.coordenadas)%2:
            self.color = pygame.Color(139,69,19)
            self.imagen.fill(self.color)
        else:
            self.color = pygame.Color(222,184,135)
            self.imagen.fill(self.color)

            
    
    

    


    