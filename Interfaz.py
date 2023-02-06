import pygame
from AdministradorDeImagenes import AdministradorDeImagenes
from Sprites import SpriteParaResaltador, SpriteParaPieza
from TableroDeAjedrez import TableroDeAjedrez


class Interfaz:
    pygame.font.init()
    tamano_ventana_principal = TableroDeAjedrez.tamano
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
    

    def reimprimir_fondo(self):
        self.ventana_principal.blit(self.background, Interfaz.origen_de_dibujo)


    def asignar_sprites_a_piezas(self):        
        for pieza in self.tablero.piezas:
            pieza.sprite = SpriteParaPieza(pieza.imagen, pieza.casilla_ocupada)
        
            
    
    def asignar_imagenes_a_piezas(self):
        diccionario = AdministradorDeImagenes.diccionario_para_vincular_nombres_de_piezas_a_imagenes() 

        for pieza in self.tablero.piezas:
            if pieza.color == "negra":
                imagen = diccionario[pieza.nombre + "_n"]
                pieza.imagen = AdministradorDeImagenes.aplicar_antialiasing(imagen, Interfaz.tamano_casilla)
            elif pieza.color == "blanca":
                imagen = diccionario[pieza.nombre + "_b"]
                pieza.imagen = AdministradorDeImagenes.aplicar_antialiasing(imagen, Interfaz.tamano_casilla)



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


    def resaltar_casilla(self, casilla):
        sprite_resaltador = self.spritesDeResaltado.sprites()[0]
        if casilla != None:
            sprite_resaltador.rect = casilla.rect
            sprite_resaltador.image = casilla.imagen
            self.spritesDeResaltado.update(self.ventana_principal, casilla)


    


    
    
    




