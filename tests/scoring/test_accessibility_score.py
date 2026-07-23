from bs4 import BeautifulSoup

from app.analyzers.accessibility_analyzer import analyze_accessibility
from app.analyzers.html_analyzer import analyze_html
from app.analyzers.image_analyzer import analyze_images
from app.readers.html_reader import read_html

from app.scoring.score_engine import (
    _calculate_accessibility_score,
)


def _get_accessibility_score(file_name):

    html = read_html(f"examples/{file_name}")

    soup = BeautifulSoup(html, "html.parser")

    html_result = analyze_html(soup)

    image_result = analyze_images(html_result.images)

    accessibility_result = analyze_accessibility(html_result, image_result)

    score = _calculate_accessibility_score(accessibility_result)

    return score

def test_should_return_100_when_accessibility_is_correct():
    
    score = _get_accessibility_score("perfect.html")

    assert score == 100


def test_should_penalize_missing_headings():

    score = _get_accessibility_score("accessibility_missing_heading.html")

    assert score == 90

def test_should_penalize_empty_headings():

    score = _get_accessibility_score("accessibility_empty_heading.html")

    assert score == 95

def test_should_penalize_buttons_without_text():

    score = _get_accessibility_score("accessibility_button_without_text.html")

    assert score == 90

def test_should_penalize_tables_without_headers():

    score = _get_accessibility_score("accessibility_table_without_headers.html")

    assert score == 90