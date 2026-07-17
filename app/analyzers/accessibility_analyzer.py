"""
Responsabilidad:
Analizar aspectos básicos de accesibilidad del HTML utilizando los resultados de otros analizadores.

Entrada:
- HTMLAnalysisResult
- ImageAnalysisResult

Salida:
AccessibilityAnalysisResult

No hace:
- No modifica el HTML.
- No calcula el QA Score.
- No genera reportes.
- No valida WCAG completa.
"""

from app.models.accessibility_analysis_result import AccessibilityAnalysisResult

def analyze_accessibility(html_result, image_result) -> AccessibilityAnalysisResult:
    """
    Analiza aspectos básicos de accesibilidad del HTML utilizando los resultados de otros analizadores.

    Args:
        html_result (HTMLAnalysisResult): Resultados del análisis de HTML.
        image_result (ImageAnalysisResult): Resultados del análisis de imágenes.

    Returns:
        AccessibilityAnalysisResult: Resultados del análisis de accesibilidad.
    """
    # Implementación del análisis de accesibilidad aquí
    
    result = AccessibilityAnalysisResult()

    result.images_without_alt = image_result.images_without_alt

    if len(html_result.headings) == 0:
        result.missing_headings = True

    for heading in html_result.headings:
        if heading.get_text(strip=True) == "":
            result.empty_headings += 1

    for button in html_result.buttons:
        if button.get_text(strip=True) == "":
            result.buttons_without_text += 1

    for table in html_result.tables:
        if table.find("th") is None:
            result.tables_without_headers += 1

    return result