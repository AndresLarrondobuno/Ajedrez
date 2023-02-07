from Pieza import Peon, Alfil, Caballo, Torre, Reina, Rey

class AdministradorDePiezas:

    @staticmethod #devuelve lista de piezas, pudiendo filtrar por color
    def lista_ordenada_de_piezas():
        lista_de_piezas = []
        lista_ordenada_de_nombres = AdministradorDePiezas.lista_ordenada_de_nombres_de_piezas()

        for string in lista_ordenada_de_nombres:
            pieza = AdministradorDePiezas.string_a_pieza(string)
            lista_de_piezas.append(pieza)

        return lista_de_piezas


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

