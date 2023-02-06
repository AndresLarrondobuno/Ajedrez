import pygame

class AdministradorDeEventosPygame:
    
    def __init__(self, partida):
        self.partida = partida
        self.tablero = partida.tablero
        self.lista_de_eventos = []
        self.eventos_mouse_motion = []
        self.eventos_mouse_button_down = []
        self.eventos_teclado_key_down = []
        self.evento_exit = None

    def cerrar(self, evento):
        if evento.type == pygame.QUIT:
            self.partida.run = False
            pygame.quit()
            exit()

                    
    def get_casilla_bajo_hover(self, evento):
        posicion_mouse = pygame.mouse.get_pos()
        
        if evento.type == pygame.MOUSEMOTION:
            for casilla in self.partida.tablero.casillas:
                if casilla.rect.collidepoint(posicion_mouse):
                    print(casilla)
                    #casilla.bajoHover = True
                    #cuando vuelve a iterar tengo que buscar la casilla falgeada
                    return casilla
    
    
    def casilla_seleccionada(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN and self.mouse_dentro_del_tablero(evento) and self.partida.eleccion_de_clase_realizada():
            casilla_bajo_hover = self.get_casilla_bajo_hover(evento)
            interfaz = self.partida.interfaz

            self.quitar_seleccion_a_casillas()
            casilla_bajo_hover.seleccionada = True
    

    def quitar_seleccion_a_casillas(self):
        for casilla in self.tablero:
            casilla.seleccionada = False

    

    def mouse_dentro_del_tablero(self, evento):
        ventana_principal = self.partida.interfaz.ventana_principal
        if evento.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x < 0 or mouse_x > ventana_principal.get_width() or mouse_y < 0 or mouse_y > ventana_principal.get_height():
                return False
            else:
                return True