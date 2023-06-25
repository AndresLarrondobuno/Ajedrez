import pygame as pg
from movimiento import Movimiento

class Pieza:
    def __init__(self, tablero, nombre):
        self.nombre = nombre
        self.tablero = tablero
        self.color = 'blancas' if '_b' in self.nombre else 'negras'
        self.sprite = None
        self.rect = pg.Rect((0,0,0,0))
        self.seleccionada = False
        self.salta_piezas = True if 'caballo' in self.nombre else False
    

    def __repr__(self) -> str:
        return self.nombre
    

    def respeta_patron_de_movimiento(self, movimiento):
        pass


    def comer_pieza(self):
        pass


    def generar_ruta(self, movimiento):
        pass
        

    def ruta_despejada(self):
        pass
    

    def diagonal_despejada(self):
        pass


    def fila_despejada(self):
        pass


    def columna_despejada(self):
        pass


    def promover_a(self, nombre_de_pieza):
        nueva_pieza = self.tablero.crearPieza(nombre_de_pieza)
        nueva_pieza.sprite
        pass
   

class Peon(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.casilla_inicial = None
        self.casilla_de_promocion = None


    def respeta_patron_de_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        
        ataca_pieza = casilla_atacada.ocupada()
        distancia_ortogonal = casilla_de_partida.distancia_ortogonal(casilla_atacada)
        comparten_columna = casilla_de_partida.comparte_columna_con(casilla_atacada)
        comparten_diagonal = casilla_de_partida.comparte_diagonal_con(casilla_atacada)

        if self.avanza_hacia_promocion(movimiento):
            if ataca_pieza:
                return True if comparten_diagonal and (distancia_ortogonal == 2) else False
            else:
                if casilla_de_partida is self.casilla_inicial:
                    return True if comparten_columna and (distancia_ortogonal <= 2) else False
                else:
                    return True if comparten_columna and (distancia_ortogonal == 1) else False


    def avanza_hacia_promocion(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        if self.color == 'blancas':
            distancia_previa_al_movimiento = casilla_de_partida.distancia_vertical(self.tablero.fila_de_promocion_de_blancas)
            distancia_posterior_al_movimiento = casilla_atacada.distancia_vertical(self.tablero.fila_de_promocion_de_blancas)
        else:
            distancia_previa_al_movimiento = casilla_de_partida.distancia_vertical(self.tablero.fila_de_promocion_de_negras)
            distancia_posterior_al_movimiento = casilla_atacada.distancia_vertical(self.tablero.fila_de_promocion_de_negras)
        return True if distancia_previa_al_movimiento > distancia_posterior_al_movimiento else False
    

    def ruta_despejada(self):
        pass


    def columna_despejada(self):
        pass


class Alfil(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None


    def respeta_patron_de_movimiento(self, movimiento: Movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        return True if casilla_de_partida.comparte_diagonal_con(casilla_atacada) else False


    def ruta_despejada(self):
        return True if self.diagonal_despejada() else False
    

    def diagonal_despejada(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada = movimiento.casilla_atacada
        casillas_en_diagonal = [casilla for casilla in self.tablero.casillas if casilla.comparte_diagonal_con(casilla_de_partida) ]
        for casilla in casillas_en_diagonal:
            if casilla_de_partida.distancia_ortogonal(casilla_atacada) > casilla_de_partida.distancia_ortogonal(casilla):
                return False
        return True


    def generar_ruta(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        pendiente = (casilla_de_partida.x - casilla_atacada.x) / (casilla_de_partida.y - casilla_atacada.y)

    

class Caballo(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None
        self.salta_piezas = True
    

    def respeta_patron_de_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada

        no_comparten_diagonal = not casilla_de_partida.comparte_diagonal_con(casilla_atacada)
        no_son_ortogonales = not casilla_de_partida.ortogonal_con(casilla_atacada)
        distancia_ortogonal_valida = casilla_de_partida.distancia_ortogonal(casilla_atacada) <= 3

        return True if no_comparten_diagonal and no_son_ortogonales and distancia_ortogonal_valida else False


class Torre(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.sprite = None


    def respeta_patron_de_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        return True if casilla_de_partida.ortogonal_con(casilla_atacada) else False


    def generar_ruta(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        ruta = list()
        for casilla in self.tablero.casillas:
            if casilla.en_direccion_del_movimiento(movimiento):
                if casilla not in  [casilla_de_partida, casilla_atacada]:
                    ruta.append(casilla)
        print(len(ruta), ruta)
        return ruta


class Rey(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)


    def respeta_patron_de_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada

        distancia_ortogonal = casilla_de_partida.distancia_ortogonal(casilla_atacada)
        son_ortogonales = casilla_de_partida.ortogonal_con(casilla_atacada)
        comparten_diagonal = casilla_de_partida.comparte_diagonal_con(casilla_atacada)
        
        condicion_uno = son_ortogonales and distancia_ortogonal == 1
        condicion_dos = comparten_diagonal and distancia_ortogonal == 2
        return True if condicion_uno or condicion_dos else False


class Reina(Pieza):
    def __init__(self, tablero, nombre):
        super().__init__(tablero, nombre)
        self.en_jaque = False
    
    def respeta_patron_de_movimiento(self, movimiento):
        casilla_de_partida = movimiento.casilla_de_partida
        casilla_atacada =  movimiento.casilla_atacada
        son_ortogonales = casilla_de_partida.ortogonal_con(casilla_atacada)
        comparten_diagonal = casilla_de_partida.comparte_diagonal_con(casilla_atacada)
        return True if son_ortogonales or comparten_diagonal else False