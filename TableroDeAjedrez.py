import pygame
from Casilla import Casilla
from Pieza import Peon, Alfil, Caballo, Torre, Reina, Rey

class TableroDeAjedrez:
    tamano = (650, 650)

    def __init__(self, partida):
        self.partida = partida
        self.ancho, self.alto = TableroDeAjedrez.tamano 
        self.ancho_en_casillas = 8
        self.alto_en_casillas = 8

        self.casillas = []
        self.agregar_casillas()
        
        
        self.casillas_iniciales_para_negras = self.casillas_ocupadas_al_inicio("negras")
        self.casillas_iniciales_para_blancas = self.casillas_ocupadas_al_inicio("blancas")

        self.piezas = TableroDeAjedrez.lista_ordenada_de_piezas()
        self.piezas_negras = self.piezas[:16]
        self.piezas_blancas = self.piezas[16:]
        self.asignar_casillas_a_piezas()



    def agregar_casillas(self):
        for y in range(self.ancho_en_casillas):
            for x in range(self.alto_en_casillas):
                casilla = Casilla((x,y), self)
                self.casillas.append(casilla)
    

    def asignar_casillas_a_piezas(self):        
        casillas_ordenadas_para_colocar_negras = self.casillas_iniciales_para_negras
        casillas_ordenadas_para_colocar_blancas = self.casillas_iniciales_para_blancas
        
        for i, casilla in enumerate(casillas_ordenadas_para_colocar_negras):
            self.piezas_negras[i].casilla_ocupada = casilla

        for i, casilla in enumerate(casillas_ordenadas_para_colocar_blancas):
            self.piezas_blancas[i].casilla_ocupada = casilla
        

    def casillas_ocupadas_al_inicio(self, color):
        if color == "negras":
            casillas_iniciales_para_negras = self.casillas[:16]
            return casillas_iniciales_para_negras
        elif color == "blancas":
            casillas_iniciales_para_blancas = self.casillas[48:]
            return casillas_iniciales_para_blancas
        

    def columnas(self):
        self.columna_a = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 0]
        self.columna_b = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 1]
        self.columna_c = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 2]
        self.columna_d = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 3]
        self.columna_e = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 4]
        self.columna_f = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 5]
        self.columna_g = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 6]
        self.columna_h = [casilla for casilla in self.casillas if casilla.coordenadas[0] == 7]
    




    @staticmethod 
    def lista_ordenada_de_nombres_de_piezas():
        orden_de_piezas_negras = []
        orden_de_figuras_negras = ["torre_n", "caballo_n", "alfil_n", "reina_n", "rey_n", "alfil_n", "caballo_n", "torre_n"]
        peones_de_negras = ["peon_n" for c in range(8)]
        orden_de_piezas_negras.extend(orden_de_figuras_negras + peones_de_negras)

        orden_de_piezas_blancas = []
        orden_de_figuras_blancas = ["torre_b", "caballo_b", "alfil_b", "reina_b", "rey_b", "alfil_b", "caballo_b", "torre_b"]
        peones_de_blancas = ["peon_b" for c in range(8)]
        orden_de_piezas_negras.extend(peones_de_blancas + orden_de_figuras_blancas)

        orden_de_piezas = []
        orden_de_piezas.extend(orden_de_piezas_negras + orden_de_piezas_blancas)

        return orden_de_piezas


    @staticmethod
    def string_a_pieza(string):
        if "peon" in string and "_n" in string:
            pieza = Peon("peon", "negra")
        elif "peon" in string and "_b" in string:
            pieza = Peon("peon", "blanca")
        elif "alfil" in string and "_n" in string:
            pieza = Alfil("alfil", "negra")
        elif "alfil" in string and "_b" in string:
            pieza = Alfil("alfil", "blanca")
        elif "caballo" in string and "_n" in string:
            pieza = Caballo("caballo", "negra")
        elif "caballo" in string and "_b" in string:
            pieza = Caballo("caballo", "blanca")
        elif "torre" in string and "_n" in string:
            pieza = Torre("torre", "negra")
        elif "torre" in string and "_b" in string:
            pieza = Torre("torre", "blanca")
        elif "reina" in string and "_n" in string:
            pieza = Reina("reina", "negra")
        elif "reina" in string and "_b" in string:
            pieza = Reina("reina", "blanca")
        elif "rey" in string and "_n" in string:
            pieza = Rey("rey", "negra")
        elif "rey" in string and "_b" in string:
            pieza = Rey("rey", "blanca")
        
        return pieza


    @staticmethod #devuelve lista de piezas, pudiendo filtrar por color
    def lista_ordenada_de_piezas():
        lista_de_piezas = []
        lista_ordenada_de_nombres = TableroDeAjedrez.lista_ordenada_de_nombres_de_piezas()

        for string in lista_ordenada_de_nombres:
            pieza = TableroDeAjedrez.string_a_pieza(string)
            lista_de_piezas.append(pieza)

        return lista_de_piezas
 



       
    


                

    
        

         