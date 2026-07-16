"""
Inbox Guardian

HTML Parser

Responsabilidad:
Interpretar un documento HTML y convertirlo en una estructura navegable para que otros módulos puedan recorrerla.

Entrada:
Recibe un string que contiene un documento HTML.

Salida:
Devuelve un objeto BeautifulSoup listo para ser recorrido.

No hace:
- No lee archivos.
- No analiza imágenes.
- No analiza links.
- No calcula métricas.
- No genera reportes.
- No modifica el HTML.
"""

from bs4 import BeautifulSoup
from app.exceptions import InvalidHtmlError, EmptyFileError

def parse_html(html_content: str) -> BeautifulSoup:
    """
    Interpreta un documento HTML y lo convierte en una estructura navegable.

    Args:
        html_content (str): Un string que contiene un documento HTML.

    Returns:
        BeautifulSoup: Documento HTML parseado listo para ser recorrido por otros módulos.
    """
    if not isinstance(html_content, str):
        raise InvalidHtmlError("HTML content must be a string.")
    if html_content.strip() == "":
        raise EmptyFileError("The HTML content is empty.")
    
    return BeautifulSoup(html_content, "html.parser")