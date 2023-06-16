import pygame as pg
from jugador import Jugador
from administradorDeInterfaz import AdministradorDeInterfaz
from tablero import Tablero
from movimiento import Movimiento
import numpy as np

class Partida:
    FPS = 60
    def __init__(self):
        self.tablero = Tablero()
        self.administradorDeInterfaz = AdministradorDeInterfaz(self.tablero)
        self.jugador_blancas = Jugador('blancas', self.tablero.piezas_blancas)
        self.jugador_negras = Jugador('negras', self.tablero.piezas_blancas)
        self.reloj = pg.time.Clock()
        self.partida_en_curso = False
        self.turno = 1
        self.estado_de_tablero = self.get_estado_de_tablero()
        self.historial_de_partida = dict()

    
    def iniciarPartida(self):
        self.partida_en_curso = True 
        
        while self.partida_en_curso:
            eventos = pg.event.get()
            self.administradorDeInterfaz.imprimirTablero()
            self.administradorDeInterfaz.actualizar_posicion_de_piezas(self.tablero)

            for evento in eventos:
                if evento.type == pg.QUIT:
                    self.partida_en_curso = False
                    pg.quit()
                    exit()

                elif evento.type == pg.MOUSEBUTTONDOWN:
                    for casilla in np.array(self.tablero.casillas):
                        if casilla.rect.collidepoint(pg.mouse.get_pos()):
                            casilla_de_partida = self.tablero.casillas[0]
                            casilla_atacada = self.tablero.casillas[60]
                            movimiento = Movimiento(casilla_de_partida, casilla_atacada)
                            self.jugador_blancas.mover_pieza(movimiento)
                            self.guardar_estado_de_tablero_en_historial()
                            self.siguiente_turno()
                            print(casilla_de_partida.pieza)
                            print(casilla_atacada.pieza)

            self.reloj.tick(Partida.FPS)
            pg.display.flip()
    

    def get_estado_de_tablero(self):
        return


    def guardar_estado_de_tablero_en_historial(self):
        informacion_relevante_para_historial = [(casilla.coordenadas, casilla.pieza) for casilla in self.tablero.casillas]
        self.historial_de_partida[self.turno] = self.tablero.casillas


    def siguiente_turno(self):
        self.turno += 1
        

        