class TransformadorDeRects:
    @staticmethod
    def escalar(rect, factor_de_escalado):
        rect.width, rect.height = rect.width * factor_de_escalado, rect.height * factor_de_escalado
    

    @staticmethod
    def centrar(rect_contenedor, rect_contenido):
        diferencia_de_ancho = rect_contenedor.width - rect_contenido.width
        rect_contenido.x += diferencia_de_ancho //2
        rect_contenido.y += diferencia_de_ancho //2 + 3