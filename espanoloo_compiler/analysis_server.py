
import sys
import os

# Añadir el directorio padre al sys.path para que pueda encontrar los módulos del compilador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json

from espanoloo_compiler.lexer import EspanolOOLexer
from espanoloo_compiler.parser import EspanolOOParser
from espanoloo_compiler.verificador_semantico import VerificadorSemantico

def analyze_code(code_text):
    lexer = EspanolOOLexer()
    parser = EspanolOOParser()
    verificador_semantico = VerificadorSemantico()

    # Pass the original code_text to parser.parse, PLY will handle lexing internally
    ast = parser.parse(code_text)

    if parser.errores:
        return {"error": "Error de sintaxis", "details": parser.errores}

    verificador_semantico.verificar(ast)

    if verificador_semantico.errores:
        return {"error": "Errores semánticos", "details": verificador_semantico.errores}

    # Extraemos los símbolos relevantes de la tabla de símbolos del verificador semántico.
    symbols = verificador_semantico.tabla_simbolos.obtener_todos_los_simbolos()

    return {"success": True, "symbols": symbols}

if __name__ == "__main__":
    # Lee el código fuente de stdin
    code_input = sys.stdin.read()
    result = analyze_code(code_input)
    print(json.dumps(result))
