from movimiento import Movimiento

class Jugador:
    def __init__(self, color:str, piezas):
        self.color = color
        self.piezas = piezas
        self.toca_moverse = True if (color == 'blancas') else False


    def mover_pieza(self, movimiento: Movimiento):
        pieza_atacante = movimiento.casilla_de_partida.pieza
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada = movimiento.casilla_atacada
        #chequeos de legalidad del movimiento
        casilla_atacada.pieza.sprite.kill()
        casilla_atacada.pieza = pieza_atacante
        casilla_de_partida.pieza = None

        pieza_atacante.sprite.actualizar_posicion(casilla_atacada)
        #guardar la jugada


    def comer_pieza(self):
        pass


    

