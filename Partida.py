import pygame
from AdministradorDeEventosPygame import AdministradorDeEventosPygame
from Tablero import Tablero
from Interfaz import Interfaz
from Jugador import Jugador
from Turno import Turno
from Arbitro import Arbitro

pygame.init()

class Partida:
    FPS = 60

    def __init__(self):
        self.tablero = Tablero(self)
        self.interfaz = Interfaz(self)
        self.administrador_de_eventos_pygame = AdministradorDeEventosPygame(self)
        self.arbitro = Arbitro(self)
        self.turno = Turno(self)
        self.jugador_negras, self.jugador_blancas = Jugador(self, "negras"), Jugador(self, "blancas")

        self.jugador_activo = self.jugador_blancas

        self.reloj = pygame.time.Clock()
        self.run = True
        self.bucle_principal()
    

    def bucle_principal(self):
        
        administrador_de_eventos_pygame = self.administrador_de_eventos_pygame
        interfaz = self.interfaz
        
        while self.run:
            eventos = pygame.event.get()
            evento_mouse_button_down = administrador_de_eventos_pygame.get_evento_por_tipo(eventos, pygame.MOUSEBUTTONDOWN)
            evento_exit = administrador_de_eventos_pygame.get_evento_por_tipo(eventos, pygame.QUIT)

            interfaz.imprimir_tablero()
            administrador_de_eventos_pygame.seleccionar_casilla(evento_mouse_button_down)
            interfaz.sostener_pieza(self.jugador_activo.pieza_tocada)
            administrador_de_eventos_pygame.cerrar(evento_exit)
            

            self.reloj.tick(Partida.FPS)
            pygame.display.flip()
            pygame.event.pump()
  
    

if __name__ == "__main__":
    Partida()

