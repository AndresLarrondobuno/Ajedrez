import pygame


class AdministradorDeImagenes:
    
    @staticmethod
    def diccionario_para_vincular_nombres_de_piezas_a_imagenes():
        diccionario_piezas = {}

        diccionario_piezas["peon_b"] = pygame.image.load(r"imagenes de piezas\w_pawn_png_128px.png")
        diccionario_piezas["peon_n"] = pygame.image.load(r"imagenes de piezas\b_pawn_png_128px.png")
        diccionario_piezas["alfil_b"] = pygame.image.load(r"imagenes de piezas\w_bishop_png_128px.png")
        diccionario_piezas["alfil_n"] = pygame.image.load(r"imagenes de piezas\b_bishop_png_128px.png")
        diccionario_piezas["caballo_b"] = pygame.image.load(r"imagenes de piezas\w_knight_png_128px.png")
        diccionario_piezas["caballo_n"] = pygame.image.load(r"imagenes de piezas\b_knight_png_128px.png")
        diccionario_piezas["torre_b"] = pygame.image.load(r"imagenes de piezas\w_rook_png_128px.png")
        diccionario_piezas["torre_n"] = pygame.image.load(r"imagenes de piezas\b_rook_png_128px.png")
        diccionario_piezas["reina_b"] = pygame.image.load(r"imagenes de piezas\w_queen_png_128px.png")
        diccionario_piezas["reina_n"] = pygame.image.load(r"imagenes de piezas\b_queen_png_128px.png")
        diccionario_piezas["rey_b"] = pygame.image.load(r"imagenes de piezas\w_king_png_128px.png")
        diccionario_piezas["rey_n"] = pygame.image.load(r"imagenes de piezas\b_king_png_128px.png")

        return diccionario_piezas
    

    @staticmethod
    def aplicar_antialiasing(imagen, tamano):
        imagen = imagen.convert_alpha()
        imagen_escalada_con_antialiasing = pygame.transform.smoothscale(imagen, tamano)
        return imagen_escalada_con_antialiasing
    

