
class Jugador:
    def __init__(self, color):
        self.color = color
        self.piezas = None


    def mover_pieza(self, pieza, casilla_destino):
        casilla_de_partida = pieza.casilla_ocupada
        casilla_de_partida.ocupada == False

        casilla_destino.pieza = pieza
        casilla_destino.ocupada = True


    
    