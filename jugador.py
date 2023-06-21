from movimiento import Movimiento

class Jugador:
    def __init__(self, color:str, piezas):
        self.color = color
        self.piezas = piezas
        self.pieza_seleccionada = None
    

    def __repr__(self) -> str:
        return f'Jugador de {self.color}'


    def mover_pieza(self, movimiento: Movimiento):
        pieza_atacante = movimiento.casilla_de_partida.pieza
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada = movimiento.casilla_atacada

        #chequeos de legalidad del movimiento
        
        if casilla_atacada.pieza:
            casilla_atacada.pieza.sprite.kill()

        casilla_atacada.pieza = pieza_atacante
        casilla_de_partida.pieza = None

        pieza_atacante.sprite.actualizar_posicion(casilla_atacada.rect.x, casilla_atacada.rect.y)
        #guardar la jugada


    def comer_pieza(self):
        pass


    def get_pieza_seleccionada(self):
        for pieza in self.piezas:
            if pieza.seleccionada:
                return pieza
    

