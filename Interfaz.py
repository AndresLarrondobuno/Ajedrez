import pygame
from AdministradorDeImagenes import AdministradorDeImagenes
from Sprites import SpriteParaResaltador, SpriteParaPieza
from Tablero import Tablero
from TransformadorDeRects import TransformadorDeRects


class Interfaz:
    pygame.font.init()
    tamano_ventana_principal = Tablero.tamano
    tamano_casilla = (tamano_ventana_principal[0]/8, tamano_ventana_principal[1]/8)
    origen_de_dibujo = (0,0)
    fuente_base = pygame.font.SysFont("Arialblack", 16)
    

    def __init__(self, partida):
        self.partida = partida
        self.tablero = partida.tablero
        self.ventana_principal = pygame.display.set_mode(Interfaz.tamano_ventana_principal)

        self.asignar_imagenes_a_piezas()
        self.asignar_sprites_a_piezas()
        
        self.sprites_para_casillas = self.sprite_group_casillas()
        self.sprites_para_piezas = self.sprite_group_piezas()
        self.spritesDeResaltado = pygame.sprite.Group(SpriteParaResaltador())
        
    

    def imprimir_tablero(self):
        self.sprites_para_casillas.draw(self.ventana_principal)
        self.sprites_para_piezas.draw(self.ventana_principal)


    def asignar_sprites_a_piezas(self):        
        for pieza in self.tablero.piezas:
            pieza.sprite = SpriteParaPieza(pieza.imagen, pieza.casilla_ocupada)
        
            
    def asignar_imagenes_a_piezas(self):
        diccionario = AdministradorDeImagenes.diccionario_para_vincular_nombres_de_piezas_a_imagenes() 
        tamano_de_pieza = tuple([0.8 * elemento for elemento in Interfaz.tamano_casilla])

        for pieza in self.tablero.piezas:
            if pieza.color == "negra":
                imagen = diccionario[pieza.nombre + "_n"]
                pieza.imagen = AdministradorDeImagenes.aplicar_antialiasing(imagen, tamano_de_pieza)
            elif pieza.color == "blanca":
                imagen = diccionario[pieza.nombre + "_b"]
                pieza.imagen = AdministradorDeImagenes.aplicar_antialiasing(imagen, tamano_de_pieza)


    def sprite_group_piezas(self):
        grupo = pygame.sprite.Group()
        piezas = self.tablero.piezas

        for pieza in piezas:
            grupo.add(pieza.sprite)
        
        return grupo


    def sprite_group_casillas(self):
        casillas = self.partida.tablero.casillas
        grupo = pygame.sprite.Group()

        for casilla in casillas:
            grupo.add(casilla.sprite)
            
        return grupo


    def resaltar_casilla(self, casilla, color):
        sprite_resaltador = self.spritesDeResaltado.sprites()[0]
        sprite_resaltador.rect = casilla.rect
        sprite_resaltador.image = None
        self.spritesDeResaltado.update(self.ventana_principal, casilla, color)
    

    def sostener_pieza(self, pieza):
        if pieza and pieza.tocada:
            posicion_mouse = pygame.mouse.get_pos()
            a = posicion_mouse[0] - Interfaz.tamano_casilla[0]//2
            b = posicion_mouse[1] - Interfaz.tamano_casilla[1]//2
            pieza.sprite.rect.topleft = a, b

    

        

        


    


    
    
    




