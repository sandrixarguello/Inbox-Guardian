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

from app.models.qa_score_analysis import QAScoreResult
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
    ...


def _calculate_link_score(link_result):
    ...


def _calculate_accessibility_score(accessibility_result):
    ...


def _calculate_total_score(
    image_score,
    link_score,
    accessibility_score
):
    ...


def _calculate_grade(score):
    ...


def _generate_summary(score):
    ...