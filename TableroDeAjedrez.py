from Casilla import Casilla
from AdministradorDePiezas import AdministradorDePiezas

class TableroDeAjedrez:
    tamano = (650, 650)

    def __init__(self, partida):
        self.partida = partida
        self.ancho, self.alto = TableroDeAjedrez.tamano 
        self.ancho_en_casillas, self.alto_en_casillas = 8, 8
        
        self.casillas = []
        self.agregar_casillas()
        
        self.casillas_iniciales_para_negras = self.casillas_ocupadas_al_inicio("negras")
        self.casillas_iniciales_para_blancas = self.casillas_ocupadas_al_inicio("blancas")

        self.piezas = AdministradorDePiezas.lista_ordenada_de_piezas()
        self.piezas_negras = self.piezas[:16]
        self.piezas_blancas = self.piezas[16:]
        self.vincular_casillas_y_piezas()


    def agregar_casillas(self):
        for y in range(self.ancho_en_casillas):
            for x in range(self.alto_en_casillas):
                casilla = Casilla((x,y), self)
                self.casillas.append(casilla)
    

    def vincular_casillas_y_piezas(self):        
        casillas_ordenadas_para_colocar_negras = self.casillas_iniciales_para_negras
        casillas_ordenadas_para_colocar_blancas = self.casillas_iniciales_para_blancas
        
        for i, casilla in enumerate(casillas_ordenadas_para_colocar_negras):
            pieza_negra = self.piezas_negras[i]
            pieza_negra.casilla_ocupada = casilla
            casilla.pieza = pieza_negra

        for i, casilla in enumerate(casillas_ordenadas_para_colocar_blancas):
            pieza_blanca = self.piezas_blancas[i]
            pieza_blanca.casilla_ocupada = casilla
            casilla.pieza = pieza_blanca
        

    def casillas_ocupadas_al_inicio(self, color):
        if color == "negras":
            casillas_iniciales_para_negras = self.casillas[:16]
            return casillas_iniciales_para_negras
        elif color == "blancas":
            casillas_iniciales_para_blancas = self.casillas[48:]
            return casillas_iniciales_para_blancas
        


    






 



       
    


                

    
        

         