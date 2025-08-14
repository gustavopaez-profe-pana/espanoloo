from __future__ import annotations
import ply.lex as lex

class EspanolOOLexer:
    """
    Analizador Léxico para EspañolOO.
    Define los tokens que el lenguaje reconoce.
    """

    # Palabras reservadas: Mapea la palabra en el código a su tipo de token
    palabras_reservadas = {
        'clase': 'CLASE',
        'hereda': 'HEREDA',
        'implementa': 'IMPLEMENTA',
        'interfaz': 'INTERFAZ',
        'abstracto': 'ABSTRACTO',
        'funcion': 'FUNCION',
        'retornar': 'RETORNAR',
        'constructor': 'CONSTRUCTOR',
        'este': 'ESTE',
        'super': 'SUPER',
        'nuevo': 'NUEVO',
        'si': 'SI',
        'sino': 'SINO',
        'mientras': 'MIENTRAS',
        'para': 'PARA',
        'en': 'EN',
        'hacer': 'HACER',
        'romper': 'ROMPER',
        'continuar': 'CONTINUAR',
        'intentar': 'INTENTAR',
        'atrapar': 'ATRAPAR',
        'finalmente': 'FINALMENTE',
        'lanzar': 'LANZAR',
        'afirmar': 'AFIRMAR',
        'publico': 'PUBLICO',
        'privado': 'PRIVADO',
        'protegido': 'PROTEGIDO',
        'constante': 'CONSTANTE',
        # Tipos y Literales
        'entero': 'ENTERO_TIPO',
        'decimal': 'DECIMAL_TIPO',
        'cadena': 'CADENA_TIPO',
        'booleano': 'BOOLEANO_TIPO',
        'nulo': 'NULO',
        'verdadero': 'VERDADERO',
        'falso': 'FALSO',
        'excepcion': 'TIPO_EXCEPCION',
        # Operadores Lógicos como palabra
        'no': 'NO',
    }

    # Lista completa de tokens
    tokens = list(palabras_reservadas.values()) + [
        # Literales
        'IDENTIFICADOR', 'ENTERO', 'DECIMAL', 'CADENA',

        # Operadores de Asignación
        'ASIGNACION', 'ASIGNACION_SUMA', 'ASIGNACION_RESTA',
        'ASIGNACION_MULTIPLICACION', 'ASIGNACION_DIVISION', 'ASIGNACION_MODULO',

        # Operadores Aritméticos y de Comparación
        'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION', 'MODULO',
        'INCREMENTO', 'DECREMENTO',
        'IGUAL', 'NO_IGUAL', 'MENOR_QUE', 'MAYOR_QUE', 'MENOR_IGUAL_QUE', 'MAYOR_IGUAL_QUE',

        # Operadores Lógicos
        'Y', 'O',

        # Operador Ternario
        'INTERROGACION',

        # Delimitadores y otros
        'PUNTO_Y_COMA', 'COMA', 'PUNTO', 'DOS_PUNTOS',
        'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
        'LAMBDA',
    ]

    # Reglas de Expresiones Regulares para tokens simples
    t_Y = r'&&'
    t_O = r'\|\|'
    t_SUMA = r'\+'
    t_RESTA = r'-'
    t_MULTIPLICACION = r'\*'
    t_DIVISION = r'/'
    t_MODULO = r'%'
    t_INCREMENTO = r'\+\+'
    t_DECREMENTO = r'--'

    t_ASIGNACION = r'='
    t_ASIGNACION_SUMA = r'\+='
    t_ASIGNACION_RESTA = r'-='
    t_ASIGNACION_MULTIPLICACION = r'\*='
    t_ASIGNACION_DIVISION = r'/='
    t_ASIGNACION_MODULO = r'%='

    t_IGUAL = r'=='
    t_NO_IGUAL = r'!='
    t_MENOR_QUE = r'<'
    t_MAYOR_QUE = r'>'
    t_MENOR_IGUAL_QUE = r'<='
    t_MAYOR_IGUAL_QUE = r'>='

    t_INTERROGACION = r'\?'
    t_DOS_PUNTOS = r':'

    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LBRACKET = r'\['
    t_RBRACKET = r'\]'
    t_PUNTO_Y_COMA = r';'
    t_COMA = r','
    t_PUNTO = r'\.'
    t_LAMBDA = r'=>'

    # Ignorar espacios y tabulaciones
    t_ignore = ' \t'

    # Definiciones de tokens con funciones
    def t_IDENTIFICADOR(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.palabras_reservadas.get(t.value, 'IDENTIFICADOR')
        return t

    def t_DECIMAL(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_ENTERO(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_CADENA(self, t):
        r'\"([^\"\\]|\\.)*\"'
        t.value = t.value[1:-1].encode().decode('unicode_escape')
        return t

    def t_COMENTARIO_BLOQUE(self, t):
        r'/\*(.|\n)*?\*/'
        t.lexer.lineno += t.value.count('\n')
        pass

    def t_COMENTARIO_LINEA(self, t):
        r'//.*'
        pass

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(self, t):
        print(f"Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}")
        t.lexer.skip(1)

    # Construcción del lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

    # Método de prueba para el lexer
    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok)

if __name__ == '__main__':
    lexer = EspanolOOLexer()
    lexer.build()
    data = '''
    // Esto es una prueba
    clase MiClase {
        privado mi_variable: entero = 10;
        publico funcion miFuncion(param1: cadena) {
            si (mi_variable > 5) {
                retornar "Hola " + param1;
            } sino {
                retornar "Adiós";
            }
        }
    }
    '''
    lexer.test(data)