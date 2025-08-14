import sys
import argparse
import os

# Añadir el directorio padre al sys.path para que pueda encontrar los módulos del compilador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from espanoloo_compiler.lexer import EspanolOOLexer
from espanoloo_compiler.parser import EspanolOOParser
from espanoloo_compiler.verificador_semantico import VerificadorSemantico
from espanoloo_compiler.generador_codigo import GeneradorCodigo
from espanoloo_compiler.optimizador import Optimizador

import argparse

def compile_espanoloo(input_file, output_file=None, optimize=False):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            code_text = f.read()

        parser = EspanolOOParser()
        verificador_semantico = VerificadorSemantico()
        generador_codigo = GeneradorCodigo()

        # 1. Análisis Sintáctico (Lexer y Parser)
        ast = parser.parse(code_text)

        if parser.errores:
            print("Errores de sintaxis encontrados:")
            for error in parser.errores:
                print(f"- {error}")
            return False

        # 2. Análisis Semántico
        verificador_semantico.verificar(ast)

        if verificador_semantico.errores:
            print("Errores semánticos encontrados:")
            for error in verificador_semantico.errores:
                print(f"- {error}")
            return False

        # 3. Optimización (Opcional)
        if optimize:
            print("Aplicando optimizaciones...")
            optimizador = Optimizador()
            ast = optimizador.optimizar(ast)
            print(f"Se aplicaron {optimizador.optimizaciones} optimizaciones.")

        # 4. Generación de Código
        python_code = generador_codigo.generar(ast)

        # Determinar archivo de salida
        if output_file is None:
            output_file = input_file.replace('.eoo', '.py')
            if output_file == input_file: # Fallback if .eoo is not in name
                output_file = input_file + '.py'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(python_code)

        print(f"\nCompilación exitosa. Código Python generado en: {output_file}")
        return True

    except FileNotFoundError:
        print(f"Error: El archivo de entrada '{input_file}' no fue encontrado.")
        return False
    except Exception as e:
        print(f"Error inesperado durante la compilación: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Compilador de EspañolOO a Python.")
    parser.add_argument("input_file", help="Archivo de código fuente de EspañolOO (.eoo).")
    parser.add_argument("-o", "--output", help="Archivo de salida para el código Python generado (.py).", default=None)
    parser.add_argument("--optimizar", action="store_true", help="Aplica optimizaciones básicas al código.")

    args = parser.parse_args()

    success = compile_espanoloo(args.input_file, args.output, args.optimizar)
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
