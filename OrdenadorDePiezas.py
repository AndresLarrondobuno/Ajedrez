from Pieza import Peon, Alfil, Caballo, Torre, Reina, Rey

class OrdenadorDePiezas:

    @staticmethod
    def lista_ordenada_de_piezas(partida):
        lista_de_piezas = []
        lista_ordenada_de_nombres = OrdenadorDePiezas.lista_ordenada_de_nombres_de_piezas()

        for string in lista_ordenada_de_nombres:
            pieza = OrdenadorDePiezas.string_a_pieza(string, partida)
            lista_de_piezas.append(pieza)

        return lista_de_piezas


    @staticmethod
    def string_a_pieza(string, partida):
        if "peon" in string and "_n" in string:
            pieza = Peon(partida, "peon", "negra")
        elif "peon" in string and "_b" in string:
            pieza = Peon(partida, "peon", "blanca")
        elif "alfil" in string and "_n" in string:
            pieza = Alfil(partida, "alfil", "negra")
        elif "alfil" in string and "_b" in string:
            pieza = Alfil(partida, "alfil", "blanca")
        elif "caballo" in string and "_n" in string:
            pieza = Caballo(partida, "caballo", "negra")
        elif "caballo" in string and "_b" in string:
            pieza = Caballo(partida, "caballo", "blanca")
        elif "torre" in string and "_n" in string:
            pieza = Torre(partida, "torre", "negra")
        elif "torre" in string and "_b" in string:
            pieza = Torre(partida, "torre", "blanca")
        elif "reina" in string and "_n" in string:
            pieza = Reina(partida, "reina", "negra")
        elif "reina" in string and "_b" in string:
            pieza = Reina(partida, "reina", "blanca")
        elif "rey" in string and "_n" in string:
            pieza = Rey(partida, "rey", "negra")
        elif "rey" in string and "_b" in string:
            pieza = Rey(partida, "rey", "blanca")
        
        return pieza
    

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

