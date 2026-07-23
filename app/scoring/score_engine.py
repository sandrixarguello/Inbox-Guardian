"""
Responsabilidad:
Calcular el puntaje general de calidad del HTML utilizando los resultados
de los distintos analizadores.

Entrada:
- ImageAnalysisResult
- LinkAnalysisResult
- AccessibilityAnalysisResult

Salida:
QAScoreResult

No hace:
- No analiza el HTML.
- No modifica los resultados recibidos.
- No genera reportes.
- No lee archivos.
- No aplica reglas de análisis.
"""

from app.models import QAScoreResult
from app.models import ImageAnalysisResult
from app.models import LinkAnalysisResult
from app.models import AccessibilityAnalysisResult
from app.scoring.scoring_rules import *


def calculate_score(image_result, link_result, accessibility_result) -> QAScoreResult:
    """
    Calcula el puntaje final de calidad del HTML.
    """

    result = QAScoreResult()

    image_score = _calculate_image_score(image_result)
    link_score = _calculate_link_score(link_result)
    accessibility_score = _calculate_accessibility_score(accessibility_result)

    total_score = _calculate_total_score(
        image_score,
        link_score,
        accessibility_score
    )

    result.image_score = image_score
    result.link_score = link_score
    result.accessibility_score = accessibility_score
    result.total_score = total_score
    result.grade = _calculate_grade(total_score)
    result.summary = _generate_summary(total_score)

    return result


def _calculate_image_score(image_result):
    score = 100

    if image_result.images_without_alt > 0:
        score -= image_result.images_without_alt * IMAGE_WITHOUT_ALT

    if image_result.images_without_width > 0:
        score -= image_result.images_without_width * IMAGE_WITHOUT_WIDTH

    if image_result.images_without_height > 0:
        score -= image_result.images_without_height * IMAGE_WITHOUT_HEIGHT

    if image_result.remote_images > 0:
        score -= image_result.remote_images * IMAGE_REMOTE
    return max(score, 0)

def _calculate_link_score(link_result):
    score = 100

    if link_result.http_links > 0:
        score -= link_result.http_links * HTTP_LINK

    if link_result.links_without_href > 0:
        score -= link_result.links_without_href * LINK_WITHOUT_HREF

    if link_result.mailto_links > 0:
        score -= link_result.mailto_links * MAILTO_LINK

    if link_result.tel_links > 0:
        score -= link_result.tel_links * TEL_LINK

    return max(score, 0)


def _calculate_accessibility_score(accessibility_result):
    score = 100

    if accessibility_result.missing_headings > 0:
        score -= accessibility_result.missing_headings * MISSING_HEADINGS

    if accessibility_result.empty_headings > 0:
        score -= accessibility_result.empty_headings * EMPTY_HEADING

    if accessibility_result.buttons_without_text > 0:
        score -= accessibility_result.buttons_without_text * BUTTON_WITHOUT_TEXT

    if accessibility_result.tables_without_headers > 0:
        score -= accessibility_result.tables_without_headers * TABLE_WITHOUT_HEADERS

    return max(score, 0)


def _calculate_total_score(
    image_score,
    link_score,
    accessibility_score
):
    total_score = (
        image_score * IMAGE_WEIGHT +
        link_score * LINK_WEIGHT +
        accessibility_score * ACCESSIBILITY_WEIGHT
    )
    return int(round(total_score))


def _calculate_grade(score):
    if score == 100:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def _generate_summary(score):
    if score >= 80:
        return "Excellent HTML quality. Ready for production."
    elif score >= 60:
        return "Good quality. Some improvements needed."
    else:
        return "Insufficient quality. Significant improvements needed."