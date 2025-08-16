from __future__ import annotations
import os
import ply.yacc as yacc
from espanoloo_compiler.lexer import EspanolOOLexer
from espanoloo_compiler.ast import *

class EspanolOOParser:
    """
    Analizador Sintáctico para EspañolOO.
    Construye el Árbol de Sintaxis Abstracta (AST) a partir de los tokens.
    """

    def __init__(self):
        self.lexer = EspanolOOLexer()
        self.tokens = self.lexer.tokens
        self.errores = []
        # Construir el parser, especificando el directorio de salida para la tabla de parseo
        output_dir = os.path.dirname(__file__)
        self.parser = yacc.yacc(module=self, start='programa', outputdir=output_dir, debug=False)

    # Precedencia de operadores (de menor a mayor)
    precedence = (
        ('right', 'ASIGNACION', 'ASIGNACION_SUMA', 'ASIGNACION_RESTA', 'ASIGNACION_MULTIPLICACION', 'ASIGNACION_DIVISION', 'ASIGNACION_MODULO'),
        ('right', 'INTERROGACION', 'DOS_PUNTOS'), # Operador ternario
        ('left', 'O'),
        ('left', 'Y'),
        ('left', 'IGUAL', 'NO_IGUAL'),
        ('left', 'MENOR_QUE', 'MAYOR_QUE', 'MENOR_IGUAL_QUE', 'MAYOR_IGUAL_QUE'),
        ('left', 'SUMA', 'RESTA'),
        ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
        ('right', 'NO', 'UMINUS'), # Operadores unarios
        ('left', 'INCREMENTO', 'DECREMENTO'),
        ('left', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET'),
        ('left', 'PUNTO'),
        ('right', 'SINO'),
    )

    # --- REGLA INICIAL ---
    def p_programa(self, p):
        'programa : lista_declaraciones'
        p[0] = Programa(p[1])

    def p_lista_declaraciones(self, p):
        """lista_declaraciones : lista_declaraciones declaracion
                               | empty"""
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = []

    # --- REGLAS DE DECLARACIÓN ---
    def p_declaracion(self, p):
        """declaracion : declaracion_clase
                       | declaracion_funcion
                       | declaracion_variable
                       | sentencia"""
        p[0] = p[1]

    def p_declaracion_variable(self, p):
        """declaracion_variable : IDENTIFICADOR DOS_PUNTOS tipo PUNTO_Y_COMA
                                | IDENTIFICADOR DOS_PUNTOS tipo ASIGNACION expresion PUNTO_Y_COMA"""
        if len(p) == 5:
            p[0] = DeclaracionVariable(p[1], p[3], None)
        else:
            p[0] = DeclaracionVariable(p[1], p[3], p[5])

    def p_declaracion_variable_sin_pc(self, p):
        """declaracion_variable_sin_pc : IDENTIFICADOR DOS_PUNTOS tipo
                                       | IDENTIFICADOR DOS_PUNTOS tipo ASIGNACION expresion"""
        if len(p) == 4:
            p[0] = DeclaracionVariable(p[1], p[3], None)
        else:
            p[0] = DeclaracionVariable(p[1], p[3], p[5])

    def p_declaracion_funcion(self, p):
        'declaracion_funcion : modificador_acceso FUNCION IDENTIFICADOR LPAREN lista_parametros_opcional RPAREN tipo_retorno bloque_sentencias'
        p[0] = DeclaracionFuncion(p[1], p[3], p[5], p[7], p[8])

    def p_declaracion_constructor(self, p):
        'declaracion_constructor : modificador_acceso CONSTRUCTOR LPAREN lista_parametros_opcional RPAREN bloque_sentencias'
        p[0] = DeclaracionConstructor(p[1], p[4], p[6])

    def p_declaracion_clase(self, p):
        'declaracion_clase : CLASE IDENTIFICADOR hereda_opcional LBRACE lista_miembros_clase RBRACE'
        p[0] = DeclaracionClase(p[2], None, p[3], None, p[5])

    def p_hereda_opcional(self, p):
        """hereda_opcional : HEREDA IDENTIFICADOR
                           | empty"""
        p[0] = p[2] if len(p) > 2 else None

    def p_lista_miembros_clase(self, p):
        """lista_miembros_clase : lista_miembros_clase miembro_clase
                                | empty"""
        if len(p) == 3:
            p[0] = p[1] + [p[2]]
        else:
            p[0] = []

    def p_miembro_clase(self, p):
        """miembro_clase : declaracion_atributo
                         | declaracion_funcion
                         | declaracion_constructor"""
        p[0] = p[1]

    def p_declaracion_atributo(self, p):
        """declaracion_atributo : modificador_acceso IDENTIFICADOR DOS_PUNTOS tipo PUNTO_Y_COMA
                                | modificador_acceso IDENTIFICADOR DOS_PUNTOS tipo ASIGNACION expresion PUNTO_Y_COMA"""
        if len(p) == 6:
            p[0] = DeclaracionAtributo(p[1], p[2], p[4], None)
        else:
            p[0] = DeclaracionAtributo(p[1], p[2], p[4], p[6])

    def p_modificador_acceso(self, p):
        """modificador_acceso : PUBLICO
                              | PRIVADO
                              | PROTEGIDO
                              | empty"""
        p[0] = p[1] if p[1] else 'privado'

    # --- REGLAS DE SENTENCIAS ---
    def p_sentencia(self, p):
        """sentencia : sentencia_expresion
                     | bloque_sentencias
                     | sentencia_si
                     | sentencia_mientras
                     | sentencia_para
                     | sentencia_retornar
                     | sentencia_romper
                     | sentencia_continuar"""
        p[0] = p[1]

    def p_sentencia_expresion(self, p):
        'sentencia_expresion : expresion PUNTO_Y_COMA'
        p[0] = SentenciaExpresion(p[1])

    def p_bloque_sentencias(self, p):
        'bloque_sentencias : LBRACE lista_declaraciones RBRACE'
        p[0] = BloqueSentencias(p[2])

    def p_sentencia_si(self, p):
        """sentencia_si : SI LPAREN expresion RPAREN sentencia
                        | SI LPAREN expresion RPAREN sentencia SINO sentencia"""
        if len(p) == 6:
            p[0] = SentenciaSi(p[3], p[5], None)
        else:
            p[0] = SentenciaSi(p[3], p[5], p[7])

    def p_sentencia_mientras(self, p):
        'sentencia_mientras : MIENTRAS LPAREN expresion RPAREN sentencia'
        p[0] = SentenciaMientras(p[3], p[5])

    def p_sentencia_para(self, p):
        'sentencia_para : PARA LPAREN para_inicializador PUNTO_Y_COMA para_condicion PUNTO_Y_COMA para_incremento RPAREN sentencia'
        p[0] = SentenciaPara(p[3], p[5], p[7], p[9])

    def p_para_inicializador(self, p):
        """para_inicializador : declaracion_variable_sin_pc
                              | expresion
                              | empty"""
        p[0] = p[1]

    def p_para_condicion(self, p):
        """para_condicion : expresion
                          | empty"""
        p[0] = p[1]

    def p_para_incremento(self, p):
        """para_incremento : expresion
                           | empty"""
        p[0] = p[1]

    def p_sentencia_retornar(self, p):
        """sentencia_retornar : RETORNAR PUNTO_Y_COMA
                              | RETORNAR expresion PUNTO_Y_COMA"""
        p[0] = SentenciaRetornar(p[2] if len(p) == 4 else None)

    def p_sentencia_romper(self, p):
        'sentencia_romper : ROMPER PUNTO_Y_COMA'
        p[0] = SentenciaRomper()

    def p_sentencia_continuar(self, p):
        'sentencia_continuar : CONTINUAR PUNTO_Y_COMA'
        p[0] = SentenciaContinuar()

    # --- JERARQUÍA DE EXPRESIONES ---
    def p_expresion(self, p):
        'expresion : asignacion'
        p[0] = p[1]

    def p_asignacion(self, p):
        """asignacion : logica_or
                      | unario ASIGNACION asignacion"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionAsignacion(p[1], p[3])

    def p_logica_or(self, p):
        """logica_or : logica_and
                     | logica_or O logica_and"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_logica_and(self, p):
        """logica_and : igualdad
                      | logica_and Y igualdad"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_igualdad(self, p):
        """igualdad : comparacion
                    | igualdad IGUAL comparacion
                    | igualdad NO_IGUAL comparacion"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_comparacion(self, p):
        """comparacion : termino
                       | comparacion MENOR_QUE termino
                       | comparacion MAYOR_QUE termino
                       | comparacion MENOR_IGUAL_QUE termino
                       | comparacion MAYOR_IGUAL_QUE termino"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_termino(self, p):
        """termino : factor
                   | termino SUMA factor
                   | termino RESTA factor"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_factor(self, p):
        """factor : unario
                  | factor MULTIPLICACION unario
                  | factor DIVISION unario
                  | factor MODULO unario"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionBinaria(p[1], p[2], p[3])

    def p_unario(self, p):
        """unario : llamada
                  | NO unario
                  | RESTA unario %prec UMINUS"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = ExpresionUnaria(p[1], p[2])

    def p_llamada(self, p):
        """llamada : primaria
                   | llamada LPAREN lista_argumentos_opcional RPAREN
                   | llamada PUNTO IDENTIFICADOR"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 5:
            p[0] = ExpresionLlamada(p[1], p[3])
        else:
            p[0] = ExpresionAcceso(p[1], p[3])

    def p_expresion_nueva_instancia(self, p):
        'expresion_nueva_instancia : NUEVO IDENTIFICADOR LPAREN lista_argumentos_opcional RPAREN'
        p[0] = ExpresionNuevaInstancia(p[2], p[4])

    def p_primaria(self, p):
        """primaria : VERDADERO
                    | FALSO
                    | NULO
                    | ENTERO
                    | DECIMAL
                    | CADENA
                    | IDENTIFICADOR
                    | ESTE
                    | SUPER
                    | LPAREN expresion RPAREN
                    | expresion_nueva_instancia"""
        if p[1] == '(':
            p[0] = ExpresionAgrupada(p[2])
        elif p.slice[1].type in ('VERDADERO', 'FALSO', 'NULO', 'ENTERO', 'DECIMAL', 'CADENA'):
            p[0] = ExpresionLiteral(p[1])
        elif p.slice[1].type == 'IDENTIFICADOR':
            p[0] = ExpresionIdentificador(p[1])
        elif p.slice[1].type == 'ESTE':
            p[0] = ExpresionEste()
        elif p.slice[1].type == 'SUPER':
            p[0] = ExpresionSuper()
        else:
            p[0] = p[1]

    # --- REGLAS AUXILIARES ---
    def p_tipo(self, p):
        """tipo : ENTERO_TIPO
                | DECIMAL_TIPO
                | CADENA_TIPO
                | BOOLEANO_TIPO
                | IDENTIFICADOR
                | NULO"""
        p[0] = p[1]

    def p_tipo_retorno(self, p):
        """tipo_retorno : DOS_PUNTOS tipo
                        | empty"""
        p[0] = p[2] if len(p) > 2 else 'nulo'

    def p_lista_parametros_opcional(self, p):
        """lista_parametros_opcional : lista_parametros
                                     | empty"""
        p[0] = p[1] if p[1] else []

    def p_lista_parametros(self, p):
        """lista_parametros : parametro
                            | lista_parametros COMA parametro"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_parametro(self, p):
        'parametro : IDENTIFICADOR DOS_PUNTOS tipo'
        p[0] = Parametro(p[1], p[3])

    def p_lista_argumentos_opcional(self, p):
        """lista_argumentos_opcional : lista_argumentos
                                     | empty"""
        p[0] = p[1] if p[1] else []

    def p_lista_argumentos(self, p):
        """lista_argumentos : expresion
                            | lista_argumentos COMA expresion"""
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_empty(self, p):
        'empty :'
        pass

    def p_error(self, p):
        if p:
            mensaje = f"Error de sintaxis en el token '{p.type}' ('{p.value}') en la línea {p.lineno}"
            self.errores.append(mensaje)
            print(mensaje)
        else:
            mensaje = "Error de sintaxis: fin de archivo inesperado."
            self.errores.append(mensaje)
            print(mensaje)

    def parse(self, text):
        self.lexer.build()
        return self.parser.parse(text, lexer=self.lexer.lexer)

if __name__ == '__main__':
    parser = EspanolOOParser()
    code = '''
    clase MiClase {
        funcion miMetodo(a: entero, b: entero) {
            si (a > b) {
                retornar a;
            } sino {
                retornar b;
            }
        }
    }
    '''
    result = parser.parse(code)
    if not parser.errores:
        print("Análisis sintáctico exitoso.")
        # Aquí podrías imprimir el AST si tienes una representación
        # print(result)
    else:
        print("\nErrores de sintaxis encontrados:")
        for error in parser.errores:
            print(error)