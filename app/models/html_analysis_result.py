from bs4.element import Tag

class HTMLAnalysisResult:
    """
    Almacena el resultado del análisis inicial del HTML.

    Contiene los distintos elementos encontrados para que
    otros analizadores puedan utilizarlos.
    """

    def __init__(self):
        self.images: list[Tag] = []
        self.links: list[Tag] = []
        self.tables: list[Tag] = []
        self.headings: list[Tag] = []
        self.forms: list[Tag] = []
        self.buttons: list[Tag] = []