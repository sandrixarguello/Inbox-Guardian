"""
Responsabilidad:
Analizar las etiquetas <img> obtenidas del HTML Analyzer y calcular métricas sobre ellas.

Entrada:
Recibe una lista de etiquetas <img>.

Salida:
Devuelve un ImageAnalysisResult con las métricas obtenidas.

No hace:
- No busca imágenes en el HTML.
- No descarga imágenes.
- No valida accesibilidad completa.
- No calcula el score.
- No modifica el HTML.
"""

from app.models import ImageAnalysisResult


def analyze_images(images) -> ImageAnalysisResult:
    """
    Analiza una lista de etiquetas <img>.

    Args:
        images (list): Lista de etiquetas <img>.

    Returns:
        ImageAnalysisResult: Resultado del análisis.
    """

    result = ImageAnalysisResult()

    for img in images:

        result.total_images += 1

        src = img.get("src")

        if not img.get("alt"):
            result.images_without_alt += 1

        if src and src.startswith("http"):
            result.remote_images += 1
        else:
            result.local_images += 1

        if not img.get("width"):
            result.images_without_width += 1

        if not img.get("height"):
            result.images_without_height += 1

    return result