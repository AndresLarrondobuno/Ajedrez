import pygame
from AdministradorDeEventosPygame import AdministradorDeEventosPygame
from TableroDeAjedrez import TableroDeAjedrez
from Interfaz import Interfaz


pygame.init()

class Partida:
    FPS = 60

    def __init__(self):
        self.tablero = TableroDeAjedrez(self)
        self.interfaz = Interfaz(self)
        self.reloj = pygame.time.Clock()
        self.administrador_de_eventos_pygame = AdministradorDeEventosPygame(self)
        self.run = True
       
        self.bucle_principal()
    

    def bucle_principal(self):
        administrador_de_eventos_pygame = self.administrador_de_eventos_pygame
        interfaz = self.interfaz
        
        while self.run ==True:
            posicion_mouse = pygame.mouse.get_pos()
            eventos = pygame.event.get()
            eventos_mouse_motion = [evento for evento in eventos if evento.type == pygame.MOUSEMOTION]
            eventos_mouse_button_down = [evento for evento in eventos if evento.type == pygame.MOUSEBUTTONDOWN]
            evento_exit = [evento for evento in eventos if evento.type == pygame.QUIT]

            #interfaz.reimprimir_fondo()
            interfaz.imprimir_tablero()

            for evento in eventos:
                administrador_de_eventos_pygame.cerrar(evento)
                administrador_de_eventos_pygame.get_casilla_bajo_hover(evento)


            self.reloj.tick(Partida.FPS)
            pygame.display.flip()
  


    


partida = Partida()

