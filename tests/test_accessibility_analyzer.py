
from bs4 import BeautifulSoup

from app.analyzers.accessibility_analyzer import analyze_accessibility
from app.analyzers.html_analyzer import analyze_html
from app.analyzers.image_analyzer import analyze_images
from app.readers.html_reader import read_html


def test_should_detect_missing_alt_images():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")

    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)

    accessibility_result = analyze_accessibility(html_result, image_result)

    assert accessibility_result.images_without_alt == 1

def test_should_detect_empty_headings():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")

    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    
    accessibility_result = analyze_accessibility(html_result, image_result)
    assert accessibility_result.empty_headings == 1

def test_should_detect_buttons_without_text():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")

    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)

    accessibility_result = analyze_accessibility(html_result, image_result)
    
    assert accessibility_result.buttons_without_text == 1

def test_should_detect_tables_without_headers():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")

    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)

    accessibility_result = analyze_accessibility(html_result, image_result)
    
    assert accessibility_result.tables_without_headers == 1

def test_should_detect_missing_headings():
    html_path = "examples/no_headings.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")

    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    accessibility_result = analyze_accessibility(html_result, image_result)
    assert accessibility_result.missing_headings is True