
from bs4 import BeautifulSoup
from app.analyzers.html_analyzer import analyze_html
from app.models.html_analysis_result import HTMLAnalysisResult
from app.readers.html_reader import read_html

def test_should_find_img():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    result = analyze_html(soup)
    assert isinstance(result, HTMLAnalysisResult)
    assert len(result.images) == 2 

def test_should_find_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    result = analyze_html(soup)
    assert isinstance(result, HTMLAnalysisResult)
    assert len(result.links) == 1

def test_should_find_table():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    result = analyze_html(soup)
    assert isinstance(result, HTMLAnalysisResult)
    assert len(result.tables) == 1

def test_should_find_buttons():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    result = analyze_html(soup)
    assert isinstance(result, HTMLAnalysisResult)
    assert len(result.buttons) == 1
