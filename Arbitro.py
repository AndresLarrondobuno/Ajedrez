
class Arbitro:
    def __init__(self, partida):
        self.partida = partida

    
    def pasar_turno(self):
        turno = self.partida.turno
        turno.numero_de_turno += 1
        self.set_jugador_activo()


    def jugador_activo(self):
        return self.partida.jugador_activo


    def set_jugador_activo(self):
        turno = self.partida.turno
        jugador_negras, jugador_blancas = self.partida.jugador_negras, self.partida.jugador_blancas

        if turno.numero_de_turno % 2:
            self.partida.jugador_activo = jugador_blancas
            jugador_blancas.toca_moverse = True
            jugador_negras.toca_moverse = False
        else:
            self.partida.jugador_activo = jugador_negras
            jugador_negras.toca_moverse = True
            jugador_blancas.toca_moverse = False