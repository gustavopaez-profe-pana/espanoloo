import sys
import json

# Asegurarse de que el directorio del compilador esté en el sys.path
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from espanoloo_compiler.generador_codigo import GeneradorCodigo
from espanoloo_compiler.ast import *

def reconstruct_ast(json_data):
    # Esta es una implementación simplificada.
    # Una implementación completa necesitaría mapear cada tipo de nodo AST
    # del JSON a su clase Python correspondiente y reconstruir la jerarquía.
    # Por ahora, solo manejaremos los nodos que esperamos en el test.
    
    # Ejemplo muy básico para el test actual:
    if isinstance(json_data, dict):
        node_type = json_data.get("type")
        if node_type == "Programa":
            declaraciones = [reconstruct_ast(d) for d in json_data.get("declaraciones", [])]
            return Programa(declaraciones)
        elif node_type == "DeclaracionClase":
            # Asumiendo que el JSON tiene los campos correctos
            nombre = json_data.get("nombre")
            parametros_tipo = json_data.get("parametros_tipo")
            hereda_de = json_data.get("hereda_de")
            implementa_de = json_data.get("implementa_de")
            miembros = [reconstruct_ast(m) for m in json_data.get("miembros", [])]
            es_abstracta = json_data.get("es_abstracta", False)
            return DeclaracionClase(nombre, parametros_tipo, hereda_de, implementa_de, miembros, es_abstracta)
        elif node_type == "DeclaracionVariable":
            nombre = json_data.get("nombre")
            tipo = json_data.get("tipo")
            valor = reconstruct_ast(json_data.get("valor")) if json_data.get("valor") else None
            return DeclaracionVariable(nombre, tipo, valor)
        elif node_type == "DeclaracionFuncion":
            nombre = json_data.get("nombre")
            parametros = [reconstruct_ast(p) for p in json_data.get("parametros", [])]
            tipo_retorno = json_data.get("tipo_retorno")
            cuerpo = reconstruct_ast(json_data.get("cuerpo"))
            return DeclaracionFuncion(nombre, parametros, tipo_retorno, cuerpo)
        elif node_type == "SentenciaBloque":
            sentencias = [reconstruct_ast(s) for s in json_data.get("sentencias", [])]
            return BloqueSentencias(sentencias)
        elif node_type == "SentenciaExpresion":
            expresion = reconstruct_ast(json_data.get("expresion"))
            return SentenciaExpresion(expresion)
        elif node_type == "ExpresionAsignacion":
            objetivo = reconstruct_ast(json_data.get("objetivo"))
            valor = reconstruct_ast(json_data.get("valor"))
            return ExpresionAsignacion(objetivo, valor)
        elif node_type == "ExpresionLiteral":
            return ExpresionLiteral(json_data.get("valor"))
        elif node_type == "ExpresionIdentificador":
            return ExpresionIdentificador(json_data.get("nombre"))
        elif node_type == "Parametro":
            nombre = json_data.get("nombre")
            tipo = json_data.get("tipo")
            return Parametro(nombre, tipo)
        # Añadir más tipos de nodos AST según sea necesario
    return json_data # Si no es un dict o no es un nodo AST conocido, devolverlo tal cual

if __name__ == "__main__":
    try:
        # Lee el JSON del AST desde stdin
        json_input = sys.stdin.read()
        ast_data = json.loads(json_input)

        # Reconstruye el AST
        programa_ast = reconstruct_ast(ast_data)

        # Genera el código Python
        generador = GeneradorCodigo()
        codigo_python = generador.generar(programa_ast)

        # Imprime el código Python generado a stdout
        print(codigo_python)

    except Exception as e:
        print(f"Error en compiler_bridge.py: {e}", file=sys.stderr)
        sys.exit(1)
