from Casilla import Casilla
from AdministradorDeOrdenDePiezasAlInicio import AdministradorDeOrdenDePiezasAlInicio

class TableroDeAjedrez:
    tamano = (650, 650)

    def __init__(self, partida):
        self.partida = partida
        self.ancho, self.alto = TableroDeAjedrez.tamano 
        self.ancho_en_casillas, self.alto_en_casillas = 8, 8
        
        self.casillas = []
        self.agregar_casillas()
        self.asignar_posicion_a_casillas()
        self.casillas_iniciales_para_negras = self.casillas_ocupadas_al_inicio("negras")
        self.casillas_iniciales_para_blancas = self.casillas_ocupadas_al_inicio("blancas")

        self.piezas = AdministradorDeOrdenDePiezasAlInicio.lista_ordenada_de_piezas()
        self.asignar_posicion_a_piezas()
        self.piezas_negras = self.piezas_ordenadas_para("negras")
        self.piezas_blancas = self.piezas_ordenadas_para("blancas")
        self.vincular_casillas_y_piezas()

        self.ultima_casilla_clickeada = None


    def agregar_casillas(self):
        for y in range(self.ancho_en_casillas):
            for x in range(self.alto_en_casillas):
                casilla = Casilla((x,y), self)
                self.casillas.append(casilla)
    

    def asignar_posicion_a_casillas(self):
        for posicion, casilla in enumerate(self.casillas):
            casilla.posicion = posicion + 1
    

    def asignar_posicion_a_piezas(self):
        for posicion, pieza in enumerate(self.piezas):
            if posicion < 16:
                pieza.posicion = posicion + 1
            elif posicion >= 16:
                pieza.posicion = posicion + 1


    def vincular_casillas_y_piezas(self):        
        casillas_ordenadas_para_colocar_negras = self.casillas_iniciales_para_negras
        casillas_ordenadas_para_colocar_blancas = self.casillas_iniciales_para_blancas
        
        for i, casilla in enumerate(casillas_ordenadas_para_colocar_negras):
            pieza_negra = self.piezas_negras[i]
            pieza_negra.casilla_ocupada = casilla
            casilla.pieza = pieza_negra
            casilla.ocupada = True

        for i, casilla in enumerate(casillas_ordenadas_para_colocar_blancas):
            pieza_blanca = self.piezas_blancas[i]
            pieza_blanca.casilla_ocupada = casilla
            casilla.pieza = pieza_blanca
            casilla.ocupada = True
            

    def casillas_ocupadas_al_inicio(self, color):
        if color == "negras":
            casillas_iniciales_para_negras = self.casillas[:16]
            casillas_iniciales_para_negras = sorted([casilla for casilla in casillas_iniciales_para_negras], key=lambda casilla: casilla.posicion)
            return casillas_iniciales_para_negras

        elif color == "blancas":
            casillas_iniciales_para_blancas = self.casillas[48:]
            casillas_iniciales_para_blancas = sorted([casilla for casilla in casillas_iniciales_para_blancas], key=lambda casilla: casilla.posicion)
            return casillas_iniciales_para_blancas
    

    def piezas_ordenadas_para(self, color):
        piezas_negras = self.piezas[:16]
        piezas_blancas = self.piezas[16:]

        piezas_negras = sorted([pieza for pieza in piezas_negras], key=lambda pieza: pieza.posicion)
        piezas_blancas = sorted([pieza for pieza in piezas_blancas], key=lambda pieza: pieza.posicion)

        if color == "negras":
            return piezas_negras
        elif color == "blancas":
            return piezas_blancas
        


    






 



       
    


                

    
        

         