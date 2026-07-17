"""
Responsabilidad:
Analizar las etiquetas <a> obtenidas del HTML Analyzer y clasificar los enlaces encontrados.

Entrada:
Lista de etiquetas <a>.

Salida:
Objeto LinkAnalysisResult con las métricas obtenidas.

No hace:
- No busca enlaces en el HTML.
- No descarga páginas web.
- No valida si un enlace existe.
- No calcula el QA Score.
- No modifica el HTML.
"""
from app.models.link_analysis_result import LinkAnalysisResult

def analyze_links(links: list) -> LinkAnalysisResult:
    """
    Analiza una lista de enlaces y devuelve un objeto con métricas sobre los enlaces encontrados.

    Args:
        links (list): Lista de etiquetas <a>.

    Returns:
        LinkAnalysisResult: Objeto con las métricas obtenidas.
    """
    result = LinkAnalysisResult()

    for link in links:
        result.total_links += 1
        
        href = link.get("href")

        # Verificar si no tiene href o es "#"
        if href is None or href == "#" or href.strip() == "":
            result.links_without_href += 1
            continue  # Si no tiene href válido, no procesamos más este enlace

        if href and ("utm_source" in href or "utm_medium" in href or "utm_campaign" in href or "utm_term" in href or "utm_content" in href):  
            result.utm_links += 1

        if href.startswith("https://"):
            result.https_links += 1
        elif href.startswith("http://"):
            result.http_links += 1
        elif href.startswith("mailto:"):
            result.mailto_links += 1
        elif href.startswith("tel:"):
            result.tel_links += 1

    return result