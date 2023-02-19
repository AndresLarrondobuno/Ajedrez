from Movimiento import Movimiento

class Jugador:

    def __init__(self, partida, color):
        self.partida = partida
        self.tablero = partida.tablero
        self.color = color
        self.piezas_comidas = []
        self.pieza_tocada = None
        
        if self.color == "negras":
            self.piezas = self.tablero.piezas_negras
            self.toca_moverse = False
        elif self.color == "blancas":
            self.piezas = self.tablero.piezas_blancas
            self.toca_moverse = True
    

    def __repr__(self) -> str:
        return f"jugador {self.color}"


    def mover_pieza(self, movimiento:Movimiento):
        if movimiento.valido:
            if movimiento.pieza_atacada:
                movimiento.pieza_atacante.comer_pieza(movimiento.pieza_atacada)

            self.pieza_tocada.sprite.mover_a_casilla(movimiento.casilla_atacada)
            self.pieza_tocada.tocada == False
            self.pieza_tocada == None
            self.partida.controlador_de_turnos.pasar_turno()
        else:
            self.partida.interfaz.resaltar_casilla(movimiento.casilla_atacada, "Red")
        



        


        
        

    


    
    