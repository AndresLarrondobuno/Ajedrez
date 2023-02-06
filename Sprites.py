import pygame

class SpriteParaPieza(pygame.sprite.Sprite):
    def __init__(self, imagen, casilla_inicial):
        super().__init__()
        self.image = pygame.transform.scale(imagen, casilla_inicial.tamano )#escalar
        self.rect = casilla_inicial.rect
        self.rect.x, self.rect.y = casilla_inicial.origen_de_dibujo
        
        

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
    
    
    def update(self, superficie, casilla):
        pygame.draw.rect(superficie, "Green", casilla.rect, 1)
        
    

class SpriteParaBoton(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas_de_dibujo=(0, 0)):
        super().__init__(imagen, coordenadas_de_dibujo)
        

        
