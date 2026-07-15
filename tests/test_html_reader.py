from app.readers.html_reader import read_html

def test_should_read_html_file():
    html_path = "examples/valid_email.html"
    result = read_html(html_path)
    assert isinstance(result, str)
    assert result.strip() != ""
    
    