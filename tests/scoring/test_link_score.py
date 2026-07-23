from bs4 import BeautifulSoup

from app.analyzers.html_analyzer import analyze_html
from app.analyzers.link_analyzer import analyze_links
from app.models.link_analysis_result import LinkAnalysisResult
from app.readers.html_reader import read_html

from app.scoring.score_engine import (
    _calculate_link_score
)


def _get_link_score(file_name):

    html = read_html(f"examples/{file_name}")

    soup = BeautifulSoup(html, "html.parser")

    html_result = analyze_html(soup)

    link_result = analyze_links(html_result.links)

    score = _calculate_link_score(link_result)

    return score

def test_should_return_100_when_all_links_are_valid():

    score = _get_link_score("perfect.html")

    assert score == 100

def test_should_penalize_http_links():

    score = _get_link_score("link_http.html")

    assert score == 85

def test_should_penalize_missing_href():

    score = _get_link_score("link_missing_href.html")

    assert score == 80

def test_should_not_penalize_https():

    score = _get_link_score("link_https.html")

    assert score == 100

def test_should_not_penalize_mailto():

    score = _get_link_score("mailto_links.html")

    assert score == 100

def test_should_not_penalize_tel():

    score = _get_link_score("tel_links.html")

    assert score == 100