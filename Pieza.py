

class Pieza:
    def __init__(self, partida, nombre, color):
        self.partida = partida
        self.nombre = nombre
        self.color = color
        self.casilla_ocupada = None
        self.tocada = False
        self.sprite = None
        self.posicion = None
    

    def __repr__(self) -> str:
        datos_para_debug = f'{self.nombre} \n{self.color} \n{self.tocada} \n{self.tocada} '
        return datos_para_debug
    

    def comer_pieza(self, pieza_atacada):
        piezas_negras = self.partida.jugador_negras.piezas
        piezas_blancas = self.partida.jugador_blancas.piezas
        jugador_negras = self.partida.jugador_negras
        jugador_blancas = self.partida.jugador_blancas

        if self in piezas_negras:
            jugador_atacado = jugador_blancas
            jugador_atacante = jugador_negras
        elif self in piezas_blancas:
            jugador_atacado = jugador_negras
            jugador_atacante = jugador_blancas
        
        try:
            jugador_atacado.piezas.remove(pieza_atacada)
        except ValueError:
            print(f"pieza atacada: {pieza_atacada}")
        
        jugador_atacante.piezas_comidas.append(pieza_atacada)
        pieza_atacada.sprite.quitar_pieza_del_tablero()
        

class Rey(Pieza):
    
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)
        self.imagen = None
        self.posicion_inicial = None
        self.sprite = None
    

# rey = Rey("Rey", color)

class Reina(Pieza):
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Torre(Pieza):
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)

        self.posicion_inicial = None
        self.sprite = None
    

class Alfil(Pieza):
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Caballo(Pieza):
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)

        self.posicion_inicial = None
        self.sprite = None


class Peon(Pieza):
    def __init__(self, partida, nombre, color):
        super().__init__(partida, nombre, color)

        self.posicion_inicial = None
        self.sprite = None
        