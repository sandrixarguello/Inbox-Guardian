import pytest

from bs4 import BeautifulSoup

from app.parsers.html_parser import parse_html
from app.readers.html_reader import read_html 
from app.exceptions import InvalidHtmlError, EmptyFileError

def test_should_parse_valid_html():
    html_path = "examples/valid_email.html"
    html_content = read_html(html_path)
    result = parse_html(html_content)
    assert isinstance(result, BeautifulSoup)
    assert result.html is not None

def test_should_raise_error_when_html_is_empty():
    with pytest.raises(EmptyFileError):
        parse_html("")

def test_should_raise_error_when_input_is_none():
   with pytest.raises(InvalidHtmlError):
        parse_html(None)

def test_should_raise_error_when_input_is_not_string():
    with pytest.raises(InvalidHtmlError):
        parse_html(123)

def test_should_parse_invalid_html_structure():
    invalid_html = "<html><head><title>Test</title></head><body><h1>Header</h1></body>"
    result = parse_html(invalid_html)
    assert isinstance(result, BeautifulSoup)
    assert result.h1 is not None