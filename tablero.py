import numpy as np
from casilla import Casilla
from pieza import Peon, Alfil, Caballo, Torre, Rey, Reina

class Tablero:
    tamano = (650, 650)
    tamano_casilla = (tamano[0] / 8, tamano[1] / 8)
    ancho_casilla, alto_casilla = tamano_casilla
    def __init__(self):
        self.casillas = self.agregarCasillas()
        self.piezas = self.agregarPiezas()
        self.piezas_blancas = self.piezas[:16]
        self.piezas_negras = self.piezas[16:]
        self.fila_de_promocion_de_blancas = 0
        self.fila_de_promocion_de_negras = 7
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
    

    def crearPieza(self, nombre):
        if 'peon' in nombre:
            return Peon(self, nombre)
        elif 'alfil' in nombre:
            return Alfil(self, nombre)
        elif 'caballo' in nombre:
            return Caballo(self, nombre)
        elif 'torre' in nombre:
            return Torre(self, nombre)
        elif 'rey' in nombre:
            return Rey(self, nombre)
        elif 'reina' in nombre:
            return Reina(self, nombre)


    def agregarPiezas(self):
        nombres_ordenados_de_piezas = [
            "peon_b_0",
            "peon_b_1",
            "peon_b_2",
            "peon_b_3",
            "peon_b_4",
            "peon_b_5",
            "peon_b_6",
            "peon_b_7",
            "torre_b_0",
            "caballo_b_1",
            "alfil_b_2",
            "reina_b_3",
            "rey_b_4",
            "alfil_b_5",
            "caballo_b_6",
            "torre_b_7",
            "peon_n_0",
            "peon_n_1",
            "peon_n_2",
            "peon_n_3",
            "peon_n_4",
            "peon_n_5",
            "peon_n_6",
            "peon_n_7",
            "torre_n_0",
            "caballo_n_1",
            "alfil_n_2",
            "reina_n_3",
            "rey_n_4",
            "alfil_n_5",
            "caballo_n_6",
            "torre_n_7"]
        
        piezas = []
        for nombre in nombres_ordenados_de_piezas:
            pieza = self.crearPieza(nombre)
            piezas.append(pieza)

        piezas = np.array(piezas)

        indices_para_ordenar_piezas = [ 0,1,2,3,4,5,6,7,
                                        8,9,10,11,12,13,14,15,

                                        16,17,18,19,20,21,22,23,
                                        24,25,26,27,28,29,30,31]

        piezas_ordenadas = piezas[indices_para_ordenar_piezas]
        return list(piezas_ordenadas)


    def setColorACasillas(self):
        matriz_tablero = np.reshape(self.casillas, (8,8))
        filas_con_indices = enumerate(matriz_tablero)
        for numero_de_fila, fila in filas_con_indices:
            for casilla in fila:
                if numero_de_fila % 2:
                    casilla.color = 'clara' if casilla.x % 2 else 'oscura'
                else:
                    casilla.color = 'oscura' if casilla.x % 2 else 'clara'


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
            pieza.casilla_inicial = casilla


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


    def get_casilla_seleccionada(self):
        for casilla in self.casillas:
            if casilla.seleccionada:
                return casilla


