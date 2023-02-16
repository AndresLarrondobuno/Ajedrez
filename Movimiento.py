class Movimiento:
    def __init__(self, partida, casilla_de_partida, casilla_atacada):
        self.tablero = partida.tablero
        self.jugador_activo = partida.jugador_activo

        self.casilla_pieza_atacante = casilla_de_partida
        self.casilla_atacada = casilla_atacada
        self.pieza_atacada = None

        self.pieza_atacante = partida.jugador_activo.pieza_tocada
        self.valido = True

        if self.ataca_pieza_aliada(casilla_atacada) == False:
            
            self.pieza_atacada = casilla_atacada.pieza
            
            self.casilla_atacada.pieza = self.pieza_atacante
            casilla_de_partida.pieza = None
            self.pieza_atacante.casilla_ocupada = casilla_atacada

            casilla_de_partida.ocupada = False
            casilla_atacada.ocupada = True

            self.pieza_atacante.tocada = False
        else:
            self.valido = False


    def ataca_pieza(self, casilla_atacada):
        if casilla_atacada.ocupada:
            return True
        else:
            return False
    

    def ataca_pieza_aliada(self, casilla_atacada):
        if self.ataca_pieza(casilla_atacada) and (casilla_atacada.pieza in self.jugador_activo.piezas):
            return True
        else:
            return False

        