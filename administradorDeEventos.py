import pygame as pg

class AdministradorDeEventos:
    def __init__(self, tablero):
        self.tablero = tablero
        self.acciones = {
            pg.QUIT: self.salir_del_juego,
            pg.MOUSEBUTTONDOWN: self.manejar_click
        }
    

    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type in self.acciones:
                pass


    def manejar_click(self, evento):
        pass
    

    def salir_del_juego(self):
        pg.quit()
        exit()


    def get_casilla_clickeada(self, coordenadas_click):
        for casilla in self.tablero.casillas:
            if casilla.rect.collidepoint(coordenadas_click):
                return casilla
    

    def seleccionar_casilla(self, casilla):
        casilla.seleccionada = True
    

    def quitar_seleccion_a_casilla(self, casilla):
        casilla.seleccionada = False


    def seleccionar_pieza(self, pieza):
        pieza.seleccionada = True
    

    def quitar_seleccion_a_pieza(self, pieza):
        pieza.seleccionada = False
