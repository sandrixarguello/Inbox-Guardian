"""
Responsabilidad:
Consolidar todos los resultados del análisis en un único objeto de reporte.

Entrada:
- HTMLAnalysisResult
- ImageAnalysisResult
- LinkAnalysisResult
- AccessibilityAnalysisResult
- QAScoreResult

Salida:
InboxGuardianReport

No hace:
- No analiza HTML.
- No calcula puntajes.
- No modifica resultados.
- No genera archivos.
- No imprime información.
"""

from app.models.accessibility_analysis_result import AccessibilityAnalysisResult
from app.models.html_analysis_result import HTMLAnalysisResult
from app.models.image_analysis_result import ImageAnalysisResult
from app.models.inbox_guardian_report import InboxGuardianReport
from app.models.link_analysis_result import LinkAnalysisResult
from app.models.qa_score_analysis import QAScoreResult


def generate_report(
        html_result: HTMLAnalysisResult, 
        image_result: ImageAnalysisResult, 
        link_result: LinkAnalysisResult, 
        accessibility_result: AccessibilityAnalysisResult, 
        score_result: QAScoreResult) -> InboxGuardianReport:
    """
    Genera un reporte consolidado con todos los resultados del análisis.

    Args:
        html_result (HTMLAnalysisResult): Resultado del análisis HTML.
        image_result (ImageAnalysisResult): Resultado del análisis de imágenes.
        link_result (LinkAnalysisResult): Resultado del análisis de enlaces.
        accessibility_result (AccessibilityAnalysisResult): Resultado del análisis de accesibilidad.
        score_result (QAScoreResult): Resultado del cálculo del QA Score.

    Returns:
        InboxGuardianReport: Reporte consolidado del análisis.
    """
    report = InboxGuardianReport()
    report.html = html_result
    report.images = image_result
    report.links = link_result
    report.accessibility = accessibility_result
    report.score = score_result

    return report
