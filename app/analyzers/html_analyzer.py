"""
Responsabilidad:
Recorrer el documento HTML y agrupar los elementos encontrados.

Entrada:
Recibe un objeto BeautifulSoup.

Salida:
Devuelve un HTMLAnalysisResult con los elementos clasificados.

No hace:
- No calcula métricas.
- No analiza accesibilidad.
- No valida imágenes.
- No valida enlaces.
- No modifica el HTML.
- No genera reportes.
"""
from bs4 import BeautifulSoup
from app.models.html_analysis_result import HTMLAnalysisResult


def analyze_html(soup: BeautifulSoup) -> HTMLAnalysisResult:
    """
Analiza un documento HTML previamente parseado.

Args:
    soup (BeautifulSoup): Documento HTML parseado.

Returns:
    HTMLAnalysisResult: Resultado del análisis inicial del HTML.
"""

    result = HTMLAnalysisResult()
    headings = ["h1", "h2", "h3", "h4", "h5", "h6"]

    for tag in soup.find_all():
        if tag.name == "a":
            result.links.append(tag)
        elif tag.name == "img":
            result.images.append(tag)
        elif tag.name == "table":
            result.tables.append(tag)
        elif tag.name in headings:
            result.headings.append(tag)
        elif tag.name == "form":
            result.forms.append(tag)
        elif tag.name == "button":
            result.buttons.append(tag)

    return result