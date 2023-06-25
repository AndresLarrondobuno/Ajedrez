import pygame as pg

class GestorDePartida:
    def __init__(self, partida):
        self.partida = partida
    

    def agregarArbitro(self, arbitro):
        self.partida.arbitro = arbitro
    

    def agregarAdministradorDeEventos(self, administradorDeEventos):
        self.partida.administradorDeEventos = administradorDeEventos
    

    def iniciarPartida(self):
        while True:
            self.partida.administradorDeInterfaz.imprimirTablero()

            self.partida.administradorDeInterfaz.actualizar_posicion_de_piezas(self.partida.tablero)

            self.partida.administradorDeEventos.manejar_eventos()   

            self.partida.reloj.tick(self.partida.FPS)

            pg.display.flip()
    