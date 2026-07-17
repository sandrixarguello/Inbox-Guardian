from bs4 import BeautifulSoup

from app.readers.html_reader import read_html
from app.analyzers.html_analyzer import analyze_html
from app.analyzers.image_analyzer import analyze_images
from app.models import ImageAnalysisResult

def test_should_count_total_images():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.total_images == 2

def test_should_count_images_without_alt():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.images_without_alt == 1
    
def test_should_count_remote_images():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.remote_images == 0

def test_should_count_local_images():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.local_images == 2

def test_should_count_images_without_width():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.images_without_width == 2

def test_should_count_images_without_height():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    soup = BeautifulSoup(html_content, "html.parser")
    html_result = analyze_html(soup)
    image_result = analyze_images(html_result.images)
    assert isinstance(image_result, ImageAnalysisResult)
    assert image_result.images_without_height == 2