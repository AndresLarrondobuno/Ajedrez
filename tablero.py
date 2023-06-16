import numpy as np
from casilla import Casilla
from pieza import Pieza

class Tablero:
    tamano = (650, 650)
    tamano_casilla = (tamano[0] / 8, tamano[1] / 8)
    ancho_casilla, alto_casilla = tamano_casilla
    def __init__(self):
        self.casillas = self.agregarCasillas()
        self.piezas = self.agregarPiezas()
        self.piezas_blancas = self.piezas[:16]
        self.piezas_negras = self.piezas[16:]
        self.setColorACasillas()
        self.acomodarPiezasEnPosicionInicial()
        self.setRectAPiezas()


    def __repr__(self) -> str:
        return self.casillas
    

    def agregarCasillas(self):
        x = np.arange(8)
        y = np.arange(8)
        X, Y = np.meshgrid(x,y)
        matriz_de_coordendas_para_tablero = np.stack((X,Y), axis=-1)
        casillas = []
        for fila in matriz_de_coordendas_para_tablero:
            for coordenadas in fila:
                casillas.append(Casilla(coordenadas))
        return casillas
    

    def agregarPiezas(self):
        mapa_piezas ={"peon_b":8,
                    "torre_b":2,
                    "caballo_b":2,
                    "alfil_b":2,
                    "reina_b":1,
                    "rey_b":1,
                    "peon_n":8,
                    "torre_n":2,
                    "caballo_n":2,
                    "alfil_n":2,
                    "reina_n":1,
                    "rey_n":1}
        
        piezas_blancas = []
        piezas_negras = []

        for nombre, cantidad in mapa_piezas.items():
            for x in range(cantidad):
                if '_b' in nombre:
                    piezas_blancas.append(Pieza(nombre))
                else:
                    piezas_negras.append(Pieza(nombre))

        piezas = np.array(piezas_blancas + piezas_negras)

        indices_para_ordenar_piezas = [ 0,1,2,3,4,5,6,7,
                                        8,10,12,14,15,13,11,9,

                                        16,17,18,19,20,21,22,23,
                                        25,29,27,30,31,28,26,24]

        piezas_ordenadas = piezas[indices_para_ordenar_piezas]
        return list(piezas_ordenadas)


    def setColorACasillas(self):
        matriz_tablero = np.reshape(self.casillas, (8,8))
        for numero_de_fila, fila in enumerate(matriz_tablero):
            for casilla in fila:
                if numero_de_fila % 2:
                    casilla.color = 'clara' if casilla.coordenada_en_x % 2 else 'oscura'
                else:
                    casilla.color = 'oscura' if casilla.coordenada_en_x % 2 else 'clara'


    def setRectAPiezas(self):
        for casilla in self.casillas:
            if casilla.pieza:
                casilla.pieza.rect.x = casilla.rect[0] + 10
                casilla.pieza.rect.y = casilla.rect[1] + 10
                casilla.pieza.rect.width = casilla.rect.width * 0.8
                casilla.pieza.rect.height = casilla.rect.height * 0.8


    def colocarPiezasEnCasillas(self, casillas, piezas):
        for casilla, pieza in zip(casillas, piezas):
            casilla.pieza = pieza


    def acomodarPiezasEnPosicionInicial(self):
        matriz_tablero = np.reshape(self.casillas, (8,8))
        fila_siete = matriz_tablero[7]
        fila_seis = matriz_tablero[6]
        fila_uno = matriz_tablero[1]
        fila_cero = matriz_tablero[0]

        piezas_blancas = self.piezas_blancas[8:]
        peones_blancas = self.piezas_blancas[:8]
        piezas_negras = self.piezas_negras[8:]
        peones_negras = self.piezas_negras[:8]

        self.colocarPiezasEnCasillas(fila_siete, piezas_blancas)
        self.colocarPiezasEnCasillas(fila_seis, peones_blancas)
        self.colocarPiezasEnCasillas(fila_uno, peones_negras)
        self.colocarPiezasEnCasillas(fila_cero, piezas_negras)




