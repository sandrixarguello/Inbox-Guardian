"""
Inbox Guardian

HTML Analyzer

Responsabilidad:
Leer archivos HTML y devolver su contenido para ser analizado por otros módulos.
"""

def read_html(file_path: str) -> str:
    """
    Lee un archivo HTML y devuelve su contenido.

    Args:
        file_path (str): Ruta del archivo HTML.

    Returns:
        str: Contenido del archivo HTML.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
        if html_content.strip() == "":
            raise ValueError("The HTML file is empty.")
    return html_content
    
