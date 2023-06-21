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
            casilla.sprite.actualizar_posicion(casilla.rect.x, casilla.rect.y)


    def setSpritesAPiezas(self, piezas):
        mapa_piezas = dict()

        mapa_piezas["peon_b"] = pg.image.load(r"imagenes de piezas\w_pawn_png_128px.png")
        mapa_piezas["peon_n"] = pg.image.load(r"imagenes de piezas\b_pawn_png_128px.png")
        mapa_piezas["alfil_b"] = pg.image.load(r"imagenes de piezas\w_bishop_png_128px.png")
        mapa_piezas["alfil_n"] = pg.image.load(r"imagenes de piezas\b_bishop_png_128px.png")
        mapa_piezas["caballo_b"] = pg.image.load(r"imagenes de piezas\w_knight_png_128px.png")
        mapa_piezas["caballo_n"] = pg.image.load(r"imagenes de piezas\b_knight_png_128px.png")
        mapa_piezas["torre_b"] = pg.image.load(r"imagenes de piezas\w_rook_png_128px.png")
        mapa_piezas["torre_n"] = pg.image.load(r"imagenes de piezas\b_rook_png_128px.png")
        mapa_piezas["reina_b"] = pg.image.load(r"imagenes de piezas\w_queen_png_128px.png")
        mapa_piezas["reina_n"] = pg.image.load(r"imagenes de piezas\b_queen_png_128px.png")
        mapa_piezas["rey_b"] = pg.image.load(r"imagenes de piezas\w_king_png_128px.png")
        mapa_piezas["rey_n"] = pg.image.load(r"imagenes de piezas\b_king_png_128px.png")
        
        for pieza in piezas:
            nombre_de_pieza_sin_sufijo = pieza.nombre[:-2]
            imagen = mapa_piezas[nombre_de_pieza_sin_sufijo]
            pieza.sprite = SpritePieza(self.aplicar_antialiasing(imagen, pieza.rect.size))


    def imprimirTablero(self):
        self.grupo_sprites_casillas.update(self.ventana_principal)
        self.grupo_sprites_piezas.update(self.ventana_principal)
    

    def actualizar_posicion_de_piezas(self, tablero):
        for casilla in tablero.casillas:
            if casilla.pieza:
                if casilla.pieza.seleccionada:
                    x, y = pg.mouse.get_pos()
                    casilla.pieza.sprite.actualizar_posicion(x-30, y-30)
                else:
                    x, y = casilla.rect.x, casilla.rect.y
                    casilla.pieza.sprite.actualizar_posicion(x, y)


    def aplicar_antialiasing(self, imagen, tamano):
        imagen = imagen.convert_alpha()
        imagen_escalada_con_antialiasing = pg.transform.smoothscale(imagen, tamano)
        return imagen_escalada_con_antialiasing