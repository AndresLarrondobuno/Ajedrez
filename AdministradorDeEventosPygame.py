import pygame
from Movimiento import Movimiento

class AdministradorDeEventosPygame:
    
    def __init__(self, partida):
        self.partida = partida
        self.tablero = partida.tablero
        self.lista_de_eventos = []
        self.eventos_mouse_motion = []
        self.eventos_mouse_button_down = []
        self.eventos_teclado_key_down = []
        self.evento_exit = None

    
    def get_evento_por_tipo(self, eventos, tipo_de_evento):
        for evento in eventos:
            if evento.type == tipo_de_evento:
                return evento


    def cerrar(self, evento):
        if evento:
            self.partida.run = False
            pygame.quit()
            exit()

                    
    def get_casilla_bajo_hover(self):
        posicion_mouse = pygame.mouse.get_pos()
        casillas = self.partida.tablero.casillas

        for casilla in casillas:
            if casilla.rect.collidepoint(posicion_mouse):
                return casilla
    

    def get_casilla_seleccionada(self):
        tablero = self.partida.tablero
        for casilla in tablero.casillas:
            if casilla.seleccionada:
                return casilla


    def seleccionar_pieza_aliada(self):
        jugador_activo = self.partida.jugador_activo
        ultima_casilla_seleccionada = self.get_casilla_seleccionada()

        pieza_fue_tocada = ultima_casilla_seleccionada.ocupada
        pieza_es_aliada = ultima_casilla_seleccionada.pieza in jugador_activo.piezas

        if pieza_fue_tocada and pieza_es_aliada:
            self.quitar_seleccion_a_piezas()
            pieza_atacante = ultima_casilla_seleccionada.pieza
            pieza_atacante.tocada = True
            jugador_activo.pieza_tocada = pieza_atacante
            
            

    def seleccionar_casilla(self, evento_click):
        casilla_clickeada_previamente = self.partida.tablero.ultima_casilla_clickeada
        casilla_clickeada_actualmente = self.get_casilla_bajo_hover()
        
        if evento_click:
            partida = self.partida
            jugador_activo = self.partida.jugador_activo
            seleccion_repetida = ( casilla_clickeada_actualmente == casilla_clickeada_previamente )

            if seleccion_repetida == False:
                self.quitar_seleccion_a_casillas()
                casilla_clickeada_actualmente.seleccionada = True
                self.partida.tablero.ultima_casilla_clickeada = casilla_clickeada_actualmente
                if self.pieza_fue_tocada():
                    movimiento = Movimiento(partida, casilla_clickeada_previamente, casilla_clickeada_actualmente )
                    jugador_activo.mover_pieza(movimiento)
                else:
                    self.seleccionar_pieza_aliada()
                                    
            elif seleccion_repetida:
                casilla_clickeada_actualmente.seleccionada = False
                self.partida.tablero.ultima_casilla_clickeada = casilla_clickeada_actualmente


    def pieza_fue_tocada(self):
        jugador_activo = self.partida.jugador_activo
        for pieza in jugador_activo.piezas:
            if pieza.tocada:
                return True

        
    def quitar_seleccion_a_casillas(self):
        for casilla in self.tablero.casillas:
            casilla.seleccionada = False


    def quitar_seleccion_a_piezas(self):
        jugador_activo = self.partida.jugador_activo
        for pieza in jugador_activo.piezas:
            pieza.tocada = False


    def mouse_dentro_del_tablero(self, evento):
        ventana_principal = self.partida.interfaz.ventana_principal
        if evento.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < 0 or mouse_x > ventana_principal.get_width() or mouse_y < 0 or mouse_y > ventana_principal.get_height():
                return False
            else:
                return True