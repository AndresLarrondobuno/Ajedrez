class Movimiento:
    def __init__(self, partida, casilla_de_partida, casilla_destino):
        self.tablero = partida.tablero
        self.casilla_pieza_atacante = casilla_de_partida
        self.casilla_atacada = casilla_de_partida

        pieza_atacante = partida.jugador_activo.pieza_tocada
        pieza_atacada = casilla_destino.pieza

        casilla_de_partida = pieza_atacante.casilla_ocupada
        
        
        casilla_destino.pieza = pieza_atacante
        casilla_de_partida.pieza = None
        pieza_atacante.casilla_ocupada = casilla_destino

        casilla_de_partida.ocupada == False
        casilla_destino.ocupada = True

        pieza_atacante.tocada = False
    

    def es_valido(self):
        if self.casilla_atacada.ocupada:
            return True
        else:
            return False


    def ataca_pieza(self):
        if
        