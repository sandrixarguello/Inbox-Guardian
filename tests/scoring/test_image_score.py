from bs4 import BeautifulSoup

from app.analyzers.html_analyzer import analyze_html
from app.analyzers.image_analyzer import analyze_images
from app.readers.html_reader import read_html

from app.scoring.score_engine import (
    _calculate_image_score,
)


def _get_image_result(file_name):

    html = read_html(f"examples/{file_name}")

    soup = BeautifulSoup(html, "html.parser")

    html_result = analyze_html(soup)

    return analyze_images(html_result.images)


def test_should_return_full_score_when_images_have_no_issues():

    image_result = _get_image_result("perfect.html")

    score = _calculate_image_score(image_result)

    assert score == 100


def test_should_penalize_missing_alt():

    image_result = _get_image_result("image_missing_alt.html")

    score = _calculate_image_score(image_result)

    assert score == 85


def test_should_penalize_missing_width():

    image_result = _get_image_result("image_missing_width.html")

    score = _calculate_image_score(image_result)

    assert score == 95


def test_should_penalize_missing_height():

    image_result = _get_image_result("image_missing_height.html")

    score = _calculate_image_score(image_result)

    assert score == 95


def test_should_penalize_remote_images():

    image_result = _get_image_result("image_remote.html")

    score = _calculate_image_score(image_result)

    assert score == 98


def test_should_never_return_negative_score():

    image_result = _get_image_result("negative.html")

    score = _calculate_image_score(image_result)

    assert score == 0