import sys
import os

# Añadir el directorio padre al sys.path para que pueda encontrar los módulos del compilador
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from espanoloo_compiler.parser import EspanolOOParser
from espanoloo_compiler.verificador_semantico import VerificadorSemantico
from espanoloo_compiler.generador_codigo import GeneradorCodigo

# Constante para el mensaje de error específico de fin de archivo
FIN_DE_ARCHIVO_INESPERADO = "Error de sintaxis: fin de archivo inesperado."

def start_repl():
    """
    Inicia el Intérprete Interactivo (REPL) para EspañolOO.
    """
    print("Intérpreprete Interactivo de EspañolOO v0.2")
    print("Escriba 'salir()' para terminar.")

    # Instanciar componentes del compilador una sola vez
    parser = EspanolOOParser()
    verificador = VerificadorSemantico()
    generador = GeneradorCodigo()

    # Contexto para mantener el estado entre ejecuciones
    contexto_global = {}

    buffer_codigo = ""

    while True:
        try:
            prompt = ">>> " if not buffer_codigo else "... "
            linea = input(prompt)

            if linea.lower() == "salir()":
                break
            
            if not linea and not buffer_codigo:
                continue

            buffer_codigo += linea + "\n"

            # Limpiar errores previos antes de un nuevo intento de parseo
            parser.errores = []
            ast = parser.parse(buffer_codigo)

            # Comprobar si el parseo falló
            if parser.errores:
                # Si el único error es un EOF inesperado, la sentencia está incompleta.
                if len(parser.errores) == 1 and parser.errores[0] == FIN_DE_ARCHIVO_INESPERADO:
                    continue # Esperar más input
                else:
                    # Si hay otros errores de sintaxis, mostrarlos y reiniciar.
                    print("Errores de sintaxis encontrados:", file=sys.stderr)
                    for error in parser.errores:
                        if error != FIN_DE_ARCHIVO_INESPERADO:
                            print(f"- {error}", file=sys.stderr)
                    buffer_codigo = ""
                    continue
            
            # Si el AST se generó sin errores, la sentencia está completa.
            verificador.errores = []
            verificador.verificar(ast)
            if verificador.errores:
                print("Errores semánticos encontrados:", file=sys.stderr)
                for error in verificador.errores:
                    print(f"- {error}", file=sys.stderr)
                buffer_codigo = ""
                continue

            # Generar y ejecutar el código
            generador.codigo = [] # Limpiar el generador
            codigo_python = generador.generar(ast)
            exec(codigo_python, contexto_global)
            
            # Reiniciar para la siguiente sentencia
            buffer_codigo = ""

        except KeyboardInterrupt:
            print("\nInterrupción por teclado. Escriba 'salir()' para terminar.")
            buffer_codigo = ""
        except Exception as e:
            print(f"Error inesperado en el REPL: {e}", file=sys.stderr)
            buffer_codigo = ""

if __name__ == "__main__":
    start_repl()