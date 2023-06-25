
class Arbitro:
    def __init__(self, partida):
        self.partida = partida
    

    def set_jugador_activo(self):
        self.partida.jugador_activo = self.partida.jugador_blancas if self.partida.turno % 2 else self.partida.jugador_negras


    def get_jugador_activo(self):
        return self.partida.jugador_activo
    

    def terminar_turno(self):
        self.partida.turno += 1


    def validar_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada = movimiento.casilla_atacada
        pieza_atacante = movimiento.casilla_de_partida.pieza
        pieza_atacada = movimiento.casilla_atacada.pieza

        jugador_valido = self.jugador_valido(movimiento)
        respeta_patron_de_movimiento = pieza_atacante.respeta_patron_de_movimiento(movimiento)
        #no_ataca_pieza_aliada = pieza_atacante.color != pieza_atacada.color if pieza_atacante
        return True

        #validar ruta despejada
        #validar autojaque


    def jugador_valido(self, movimiento):
        jugador_activo = self.get_jugador_activo()
        pieza_atacante = movimiento.casilla_de_partida.pieza
        if pieza_atacante in jugador_activo.piezas:
            return True
         

