import pygame as pg
from jugador import Jugador
from administradorDeInterfaz import AdministradorDeInterfaz
from tablero import Tablero
import numpy as np

class Partida:
    FPS = 60
    def __init__(self):
        self.tablero = Tablero()
        self.reloj = pg.time.Clock()

        self.arbitro = None
        self.administradorDeEventos = None
        self.administradorDeInterfaz = AdministradorDeInterfaz(self.tablero)
        self.jugador_blancas = Jugador('blancas', self.tablero.piezas_blancas)
        self.jugador_negras = Jugador('negras', self.tablero.piezas_negras)
        
        self.historial_de_partida = np.array(list())
        self.turno = 1
        self.jugador_activo = self.jugador_blancas


    def guardar_estado_de_tablero_en_historial(self):
        self.historial_de_partida = np.append(self.historial_de_partida, self.tablero.casillas.copy())


    def mostrar_historial_de_partida(self):
        for estado_de_partida in self.historial_de_partida:
            print(estado_de_partida)
            print()