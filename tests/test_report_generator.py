
from bs4 import BeautifulSoup

from app.analyzers.accessibility_analyzer import analyze_accessibility
from app.analyzers.html_analyzer import analyze_html
from app.analyzers.image_analyzer import analyze_images
from app.analyzers.link_analyzer import analyze_links
from app.readers.html_reader import read_html
from app.reports.report_generator import generate_report
from app.scoring.score_engine import calculate_score
from app.models.inbox_guardian_report import InboxGuardianReport


def _generate_report(file_name):
    html = read_html(f"examples/{file_name}")
    soup = BeautifulSoup(html, "html.parser")
    html_result = analyze_html(soup)    
    image_result = analyze_images(html_result.images)
    link_result = analyze_links(html_result.links)
    accesibility_result = analyze_accessibility(html_result, image_result)
    score_result = calculate_score(image_result, link_result, accesibility_result)
    report = generate_report(score_result, image_result, link_result, accesibility_result, score_result)

    return report

def test_should_generate_report():
    report = _generate_report("perfect.html")
    assert isinstance(report, InboxGuardianReport)

def test_should_include_score_result():
    report = _generate_report("perfect.html")
    assert report.score is not None

def test_should_include_html_result():
    report = _generate_report("perfect.html")
    assert report.html is not None

def test_should_include_image_result():
    report = _generate_report("perfect.html")
    assert report.images is not None

def test_should_include_link_result():
    report = _generate_report("perfect.html")
    assert report.links is not None

def test_should_include_accessibility_result():
    report = _generate_report("perfect.html")
    assert report.accessibility is not None

