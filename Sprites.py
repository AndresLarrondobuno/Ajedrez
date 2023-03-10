import pygame
from TransformadorDeRects import TransformadorDeRects

class SpriteParaPieza(pygame.sprite.Sprite):
    def __init__(self, imagen, casilla_inicial):
        super().__init__()
        self.image = imagen
        self.rect = None
        self.mover_a_casilla(casilla_inicial)


    def mover_a_casilla(self, casilla):
        casilla_x, casilla_y = casilla.origen_de_dibujo
        rect_pieza = pygame.Rect(casilla_x, casilla_y, casilla.ancho*0.8, casilla.alto*0.8)

        TransformadorDeRects.centrar(casilla.rect, rect_pieza)
        self.rect = rect_pieza


 
    


    def quitar_pieza_del_tablero(self):
        self.kill()
        
        

class SpriteParaCasilla(pygame.sprite.Sprite):
    def __init__(self, casilla):
        super().__init__()
        self.origen_de_dibujo = casilla.origen_de_dibujo
        self.image = casilla.imagen
        self.rect = casilla.rect
        self.rect.x = casilla.origen_de_dibujo[0]
        self.rect.y = casilla.origen_de_dibujo[1]
    


class SpriteParaResaltador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = None
        self.image= None
    
    
    def update(self, superficie, casilla, color):
        pygame.draw.rect(superficie, color, casilla.rect, 2)
        
    

class SpriteParaBoton(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas_de_dibujo=(0, 0)):
        super().__init__(imagen, coordenadas_de_dibujo)
        

        
