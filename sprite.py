import pygame as pg

class SpriteCasilla(pg.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = imagen
        self.rect = pg.Rect(self.image.get_rect())
    

    def update(self, ventana:pg.Surface):
        x, y = self.rect.x, self.rect.y
        ventana.blit(self.image, (x,y))


    def actualizar_posicion(self, x, y):
        self.rect.x = x
        self.rect.y = y



class SpritePieza(pg.sprite.Sprite):
    def __init__(self, imagen):
        super().__init__()
        self.image = imagen
        self.rect = pg.Rect(self.image.get_rect())


    def __repr__(self) -> str:
        return str(self.rect)


    def update(self, ventana:pg.Surface):
        x, y = self.rect.x, self.rect.y
        ventana.blit(self.image, (x,y))
    

    def actualizar_posicion(self, x, y):
        self.rect.x = x + 10
        self.rect.y = y + 10