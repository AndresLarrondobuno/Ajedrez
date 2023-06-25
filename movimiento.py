class Movimiento:
    def __init__(self, casilla_de_partida, casilla_atacada):
        self.casilla_de_partida = casilla_de_partida
        self.casilla_atacada = casilla_atacada
        self.eje = self.get_eje()
    

    def get_eje(self):
        if self.casilla_de_partida.comparte_fila_con(self.casilla_atacada):
            return 'horizontal'
        elif self.casilla_de_partida.comparte_columna_con(self.casilla_atacada):
            return 'vertical'
        elif self.casilla_de_partida.comparte_diagonal_con(self.casilla_atacada):
            return 'diagonal'