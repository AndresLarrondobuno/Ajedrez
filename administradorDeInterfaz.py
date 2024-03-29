import pygame as pg
import numpy as np
from tablero import Tablero
from sprite import SpriteCasilla, SpritePieza

class AdministradorDeInterfaz:

    pg.font.init()
    fuente_base = pg.font.SysFont("Arialblack", 16)
    tamano_ventana_principal = Tablero.tamano
    tamano_casilla = (tamano_ventana_principal[0]/8, tamano_ventana_principal[1]/8)
    origen_de_dibujo = (0,0)

    mapa_piezas = {
    "peon_b" : pg.image.load(r"imagenes de piezas\w_pawn_png_128px.png"),
    "peon_n" : pg.image.load(r"imagenes de piezas\b_pawn_png_128px.png"),
    "alfil_b" : pg.image.load(r"imagenes de piezas\w_bishop_png_128px.png"),
    "alfil_n" : pg.image.load(r"imagenes de piezas\b_bishop_png_128px.png"),
    "caballo_b" : pg.image.load(r"imagenes de piezas\w_knight_png_128px.png"),
    "caballo_n" : pg.image.load(r"imagenes de piezas\b_knight_png_128px.png"),
    "torre_b" : pg.image.load(r"imagenes de piezas\w_rook_png_128px.png"),
    "torre_n" : pg.image.load(r"imagenes de piezas\b_rook_png_128px.png"),
    "reina_b" : pg.image.load(r"imagenes de piezas\w_queen_png_128px.png"),
    "reina_n" : pg.image.load(r"imagenes de piezas\b_queen_png_128px.png"),
    "rey_b" : pg.image.load(r"imagenes de piezas\w_king_png_128px.png"),
    "rey_n" : pg.image.load(r"imagenes de piezas\b_king_png_128px.png")
    }

    def __init__(self, tablero):
        self.ventana_principal = pg.display.set_mode(AdministradorDeInterfaz.tamano_ventana_principal)
        self.setSpritesACasillas(tablero.casillas)
        self.setSpritesAPiezas(tablero.piezas)
        sprites_casillas = [casilla.sprite for casilla in tablero.casillas]
        sprites_piezas = [pieza.sprite for pieza in tablero.piezas]

        self.grupo_sprites_casillas = pg.sprite.Group(sprites_casillas) 
        self.grupo_sprites_piezas = pg.sprite.Group(sprites_piezas) 


    def setSpritesACasillas(self, casillas):
        imagen_casilla_oscura = pg.image.load('imagenes de piezas\square_brown_dark_png_128px.png')
        imagen_casilla_clara = pg.image.load('imagenes de piezas\square_gray_light_png_128px.png')
        lista_casillas = np.ravel(casillas)

        for casilla in lista_casillas:
            casilla.sprite = SpriteCasilla(imagen_casilla_oscura) if casilla.color == 'oscura' else SpriteCasilla(imagen_casilla_clara)
            casilla.sprite.actualizar_posicion(casilla)


    def setSpriteAPieza(self, pieza):
        nombre_de_pieza_sin_sufijo = pieza.nombre[:-2]
        imagen = AdministradorDeInterfaz.mapa_piezas[nombre_de_pieza_sin_sufijo]
        pieza.sprite = SpritePieza(self.aplicar_antialiasing(imagen, pieza.rect.size))


    def setSpritesAPiezas(self, piezas):
        for pieza in piezas:
            self.setSpriteAPieza(pieza)


    def imprimirTablero(self):
        self.grupo_sprites_casillas.update(self.ventana_principal)
        self.grupo_sprites_piezas.update(self.ventana_principal)
    

    def actualizar_posicion_de_piezas(self, tablero):
        for casilla in tablero.casillas:
            if casilla.pieza:
                casilla.pieza.sprite.actualizar_posicion(casilla)


    def aplicar_antialiasing(self, imagen, tamano):
        imagen = imagen.convert_alpha()
        imagen_escalada_con_antialiasing = pg.transform.smoothscale(imagen, tamano)
        return imagen_escalada_con_antialiasing
    

    def mostrar_menu_de_eleccion_para_promocion(self):
        pass