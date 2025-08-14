"""
Este módulo proporciona una instancia Singleton del parser de EspañolOO.
Esto es necesario para evitar problemas de estado con ply.yacc durante las pruebas.
"""
from espanoloo_compiler.parser import EspanolOOParser

# Instanciar el parser una sola vez
_parser_instance = EspanolOOParser()

def get_parser():
    """Devuelve la instancia única del parser."""
    return _parser_instance
