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
        pieza_atacante = self.pieza_tocada
        pieza_atacada = casilla_destino.pieza
        casilla_de_partida = pieza_atacante.casilla_ocupada
        
        
        casilla_destino.pieza = pieza_atacante
        casilla_de_partida.pieza = None
        pieza_atacante.casilla_ocupada = casilla_destino

        casilla_de_partida.ocupada == False
        casilla_destino.ocupada = True

        pieza_atacante.tocada = False
        
        if pieza_atacada:
            print(f"pieza comida: {pieza_atacada}")
            self.comer_pieza(pieza_atacada)
            
        
        self.pieza_tocada.sprite.mover_a_casilla(movimiento.casilla_atacada)
        self.partida.arbitro.pasar_turno()
        

    def comer_pieza(self, pieza_atacada):
        if self == self.partida.jugador_negras:
            jugador_atacado = self.partida.jugador_blancas
        elif self == self.partida.jugador_blancas:
            jugador_atacado = self.partida.jugador_negras
        
        try:
            jugador_atacado.piezas.remove(pieza_atacada)
        except ValueError:
            print(f"pieza atacada: {pieza_atacada}")
        
        self.piezas_comidas.append(pieza_atacada)
        pieza_atacada.sprite.quitar_pieza_del_tablero()


        


        
        

    


    
    