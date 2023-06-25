import pygame as pg
from movimiento import Movimiento

class AdministradorDeEventos:
    def __init__(self, tablero, arbitro):
        self.tablero = tablero
        self.arbitro = arbitro
        self.acciones = {
            pg.QUIT: self.salir_del_juego,
            pg.MOUSEBUTTONDOWN: self.manejar_click
        }
    

    def manejar_eventos(self):
        for evento in pg.event.get():
            if evento.type in self.acciones:
                self.acciones[evento.type]()


    def manejar_click(self):
        coordenadas_click = pg.mouse.get_pos()
        casilla_clickeada = self.get_casilla_clickeada(coordenadas_click)
        casilla_seleccionada = self.tablero.get_casilla_seleccionada()
        jugador_activo = self.arbitro.get_jugador_activo()
        pieza_seleccionada = jugador_activo.get_pieza_seleccionada()

        if casilla_seleccionada is casilla_clickeada:
            
            self.quitar_seleccion_a_casilla(casilla_seleccionada)
            if casilla_clickeada.pieza:
                self.quitar_seleccion_a_pieza(casilla_clickeada.pieza)

        else:

            if self.tablero.get_casilla_seleccionada():
                if pieza_seleccionada:
                    movimiento = Movimiento(casilla_seleccionada, casilla_clickeada)
                    if self.arbitro.validar_movimiento(movimiento):
                        jugador_activo.mover_pieza(movimiento)
                        pieza_seleccionada.generar_ruta(movimiento)
                        self.arbitro.terminar_turno()
                        self.arbitro.set_jugador_activo()

                    self.quitar_seleccion_a_casilla(casilla_seleccionada)
                    self.quitar_seleccion_a_pieza(pieza_seleccionada)                    

                else:
                    self.quitar_seleccion_a_casilla(casilla_seleccionada)
                    self.seleccionar_casilla(casilla_clickeada)
                    if casilla_clickeada.pieza and (jugador_activo.color == casilla_clickeada.pieza.color):
                        self.seleccionar_pieza(casilla_clickeada.pieza)

            else:
                self.seleccionar_casilla(casilla_clickeada)
                if casilla_clickeada.pieza and (jugador_activo.color == casilla_clickeada.pieza.color):
                    self.seleccionar_pieza(casilla_clickeada.pieza)
    

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
