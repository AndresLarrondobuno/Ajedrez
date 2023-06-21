import pygame as pg
from jugador import Jugador
from administradorDeInterfaz import AdministradorDeInterfaz
from administradorDeEventos import AdministradorDeEventos
from tablero import Tablero
from movimiento import Movimiento
import numpy as np

class Partida:
    FPS = 60
    def __init__(self):
        self.tablero = Tablero()
        self.administradorDeInterfaz = AdministradorDeInterfaz(self.tablero)
        self.administradorDeEventos = AdministradorDeEventos(self.tablero)
        self.jugador_blancas = Jugador('blancas', self.tablero.piezas_blancas)
        self.jugador_negras = Jugador('negras', self.tablero.piezas_negras)
        self.reloj = pg.time.Clock()
        self.historial_de_partida = np.array(list())
        self.turno = 1
        self.jugador_activo = self.jugador_blancas

    
    def iniciarPartida(self):
        
        while True:
            eventos = pg.event.get()
            self.administradorDeInterfaz.imprimirTablero()
            self.administradorDeInterfaz.actualizar_posicion_de_piezas(self.tablero)

            for evento in eventos:
                if evento.type == pg.QUIT:
                    self.administradorDeEventos.salir_del_juego()

                elif evento.type == pg.MOUSEBUTTONDOWN:
                    coordenadas_click = pg.mouse.get_pos()
                    casilla_clickeada = self.administradorDeEventos.get_casilla_clickeada(coordenadas_click)
                    casilla_seleccionada = self.tablero.get_casilla_seleccionada()
                    pieza_seleccionada_de_jugador_activo = self.jugador_activo.get_pieza_seleccionada()

                    if casilla_seleccionada is casilla_clickeada:
                        
                        self.administradorDeEventos.quitar_seleccion_a_casilla(casilla_seleccionada)
                        if casilla_clickeada.pieza:
                            self.administradorDeEventos.quitar_seleccion_a_pieza(casilla_clickeada.pieza)

                    else:

                        if self.tablero.get_casilla_seleccionada(): #existe casilla seleccionada por el click anterior
                            if pieza_seleccionada_de_jugador_activo:
                                self.jugador_activo.mover_pieza(Movimiento(casilla_seleccionada, casilla_clickeada))
                                self.administradorDeEventos.quitar_seleccion_a_casilla(casilla_seleccionada)
                                self.administradorDeEventos.quitar_seleccion_a_pieza(pieza_seleccionada_de_jugador_activo)
                                self.terminar_turno()
                                self.set_jugador_activo()
                                
                            else:
                                self.administradorDeEventos.quitar_seleccion_a_casilla(casilla_seleccionada)
                                self.administradorDeEventos.seleccionar_casilla(casilla_clickeada)
                                if casilla_clickeada.pieza and (self.jugador_activo.color == casilla_clickeada.pieza.color):
                                    self.administradorDeEventos.seleccionar_pieza(casilla_clickeada.pieza)

                        else: #no existe casilla seleccionada
                            self.administradorDeEventos.seleccionar_casilla(casilla_clickeada)
                            if casilla_clickeada.pieza and (self.jugador_activo.color == casilla_clickeada.pieza.color):
                                self.administradorDeEventos.seleccionar_pieza(casilla_clickeada.pieza)

            self.reloj.tick(Partida.FPS)
            pg.display.flip()


    def guardar_estado_de_tablero_en_historial(self):
        self.historial_de_partida = np.append(self.historial_de_partida, self.tablero.casillas.copy())


    def mostrar_historial_de_partida(self):
        for estado_de_partida in self.historial_de_partida:
            print(estado_de_partida)
            print()
    

    def set_jugador_activo(self):
        self.jugador_activo = self.jugador_blancas if self.turno % 2 else self.jugador_negras
        print(f'turno: {self.turno} juega: {self.jugador_activo}')


    def terminar_turno(self):
        self.turno += 1