from Turno import Turno

class ControladorDeTurnos:
    def __init__(self, partida):
        self.partida = partida
        self.turno_actual = Turno(1)
        self.turnos = []
    

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    
    def pasar_turno(self):
        self.turno_actual.posicion = self.partida.tablero.posicion()
        self.agregar_turno(self.turno_actual)

        self.nuevo_turno()
        self.set_jugador_activo()
        

    def nuevo_turno(self):
        numero_de_turno = len(self.turnos) + 1
        self.turno_actual = Turno(numero_de_turno)


    def jugador_activo(self):
        return self.partida.jugador_activo


    def set_jugador_activo(self):
        turno = self.turno_actual
        jugador_negras, jugador_blancas = self.partida.jugador_negras, self.partida.jugador_blancas

        if turno.numero_de_turno % 2:
            self.partida.jugador_activo = jugador_blancas
            jugador_blancas.toca_moverse = True
            jugador_negras.toca_moverse = False
        else:
            self.partida.jugador_activo = jugador_negras
            jugador_negras.toca_moverse = True
            jugador_blancas.toca_moverse = False
            