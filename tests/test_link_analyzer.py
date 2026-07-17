
from bs4 import BeautifulSoup

from app.analyzers.html_analyzer import analyze_html
from app.analyzers.link_analyzer import analyze_links
from app.readers.html_reader import read_html
from app.models.link_analysis_result import LinkAnalysisResult


def test_should_count_total_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert isinstance(link_result, LinkAnalysisResult)
    assert link_result.total_links == 7

def test_should_count_http_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.http_links == 1

def test_should_count_https_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.https_links == 2

def test_should_count_mailto_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.mailto_links == 1

def test_should_count_tel_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.tel_links == 1

def test_should_count_links_without_href():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.links_without_href == 1

def test_should_count_utm_links():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    link_result = analyze_links(html_result.links)
    assert link_result.utm_links == 1