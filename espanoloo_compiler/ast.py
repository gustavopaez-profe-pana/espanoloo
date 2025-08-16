class AST:
    def __init__(self, lineno=None):
        self.lineno = lineno

class Programa(AST):
    def __init__(self, declaraciones, lineno=None):
        super().__init__(lineno)
        self.declaraciones = declaraciones

class Declaracion(AST):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class DeclaracionVariable(Declaracion):
    def __init__(self, nombre, tipo, valor, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor # Expresion o None

class Sentencia(AST):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class SentenciaExpresion(Sentencia):
    def __init__(self, expresion, lineno=None):
        super().__init__(lineno)
        self.expresion = expresion

class BloqueSentencias(Sentencia):
    def __init__(self, sentencias, lineno=None):
        super().__init__(lineno)
        self.sentencias = sentencias

class Expresion(AST):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class ExpresionAsignacion(Expresion):
    def __init__(self, objetivo, valor, lineno=None):
        super().__init__(lineno)
        self.objetivo = objetivo
        self.valor = valor

class ExpresionLlamada(Expresion):
    def __init__(self, callee, argumentos, lineno=None):
        super().__init__(lineno)
        self.callee = callee
        self.argumentos = argumentos

class ExpresionAcceso(Expresion):
    def __init__(self, objeto, miembro, lineno=None):
        super().__init__(lineno)
        self.objeto = objeto
        self.miembro = miembro

class ExpresionAgrupada(Expresion):
    def __init__(self, expresion, lineno=None):
        super().__init__(lineno)
        self.expresion = expresion

# Clases AST para condicionales (Paso 1.2.1)
class SentenciaSi(Sentencia):
    def __init__(self, condicion, entonces, sino, lineno=None):
        super().__init__(lineno)
        self.condicion = condicion
        self.entonces = entonces
        self.sino = sino # Puede ser None

class SentenciaBloque(Sentencia):
    def __init__(self, sentencias, lineno=None):
        super().__init__(lineno)
        self.sentencias = sentencias # Lista de sentencias

class ExpresionBinaria(Expresion):
    def __init__(self, izquierda, operador, derecha, lineno=None):
        super().__init__(lineno)
        self.izquierda = izquierda
        self.operador = operador
        self.derecha = derecha

class ExpresionUnaria(Expresion):
    def __init__(self, operador, operando, lineno=None):
        super().__init__(lineno)
        self.operador = operador
        self.operando = operando

class ExpresionLiteral(Expresion):
    def __init__(self, valor, lineno=None):
        super().__init__(lineno)
        self.valor = valor

class ExpresionIdentificador(Expresion):
    def __init__(self, nombre, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre

# Para el operador ternario (condición ? valor_verdadero : valor_falso)
class ExpresionTernaria(Expresion):
    def __init__(self, condicion, verdadero, falso, lineno=None):
        super().__init__(lineno)
        self.condicion = condicion
        self.verdadero = verdadero
        self.falso = falso

# Clases AST para bucles (Paso 1.2.2)
class SentenciaMientras(Sentencia):
    def __init__(self, condicion, cuerpo, lineno=None):
        super().__init__(lineno)
        self.condicion = condicion
        self.cuerpo = cuerpo

class SentenciaPara(Sentencia):
    def __init__(self, inicializacion, condicion, actualizacion, cuerpo, lineno=None):
        super().__init__(lineno)
        self.inicializacion = inicializacion # Puede ser None
        self.condicion = condicion # Puede ser None
        self.actualizacion = actualizacion # Puede ser None
        self.cuerpo = cuerpo

class SentenciaHacerMientras(Sentencia):
    def __init__(self, cuerpo, condicion, lineno=None):
        super().__init__(lineno)
        self.cuerpo = cuerpo
        self.condicion = condicion

# Clases AST para control de flujo (Paso 1.2.3)
class SentenciaRomper(Sentencia):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class SentenciaContinuar(Sentencia):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class SentenciaRetornar(Sentencia):
    def __init__(self, expresion=None, lineno=None):
        super().__init__(lineno)
        self.expresion = expresion # Puede ser None

# Clases AST para funciones (Paso 1.3.1)
class DeclaracionFuncion(Declaracion):
    def __init__(self, modificador_acceso, nombre, parametros, tipo_retorno, cuerpo, lineno=None):
        super().__init__(lineno)
        self.modificador_acceso = modificador_acceso
        self.nombre = nombre
        self.parametros = parametros
        self.tipo_retorno = tipo_retorno
        self.cuerpo = cuerpo

class Parametro(AST):
    def __init__(self, nombre, tipo, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre
        self.tipo = tipo

# Clases AST para funciones anónimas (Lambdas) (Paso 1.3.3)
class ExpresionLambda(Expresion):
    def __init__(self, parametros, cuerpo, lineno=None):
        super().__init__(lineno)
        self.parametros = parametros # Lista de Parametro
        self.cuerpo = cuerpo # SentenciaBloque o Expresion

# Clases AST para clases (Paso 2.1.1)
class DeclaracionClase(Declaracion):
    def __init__(self, nombre, parametros_tipo, hereda_de, implementa_de, miembros, es_abstracta=False, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre
        self.parametros_tipo = parametros_tipo # Lista de strings (e.g., ['T', 'U'])
        self.hereda_de = hereda_de # String o None
        self.implementa_de = implementa_de # Lista de strings o None
        self.miembros = miembros # Lista de DeclaracionAtributo, DeclaracionMetodo, DeclaracionConstructor
        self.es_abstracta = es_abstracta

# Clase AST para Interfaces (Paso 2.3.2)
class DeclaracionInterfaz(Declaracion):
    def __init__(self, nombre, metodos, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre
        self.metodos = metodos # Lista de DeclaracionMetodo

# Clase AST para Tipos Genéricos (Paso 2.3.3)
class TipoGenerico(Expresion):
    def __init__(self, nombre_base, argumentos_tipo, lineno=None):
        super().__init__(lineno)
        self.nombre_base = nombre_base
        self.argumentos_tipo = argumentos_tipo # Lista de Tipos (pueden ser anidados)

class DeclaracionAtributo(Declaracion):
    def __init__(self, modificador_acceso, nombre, tipo, valor=None, lineno=None):
        super().__init__(lineno)
        self.modificador_acceso = modificador_acceso # publico, privado, protegido
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor # Expresion o None

class DeclaracionMetodo(DeclaracionFuncion): # Hereda de DeclaracionFuncion
    def __init__(self, modificador_acceso, nombre, parametros_tipo, parametros, tipo_retorno, cuerpo, es_abstracto=False, lineno=None):
        super().__init__(modificador_acceso, nombre, parametros, tipo_retorno, cuerpo, lineno)
        self.parametros_tipo = parametros_tipo # Lista de strings
        self.es_abstracto = es_abstracto

class DeclaracionConstructor(Declaracion):
    def __init__(self, modificador_acceso, parametros, cuerpo, lineno=None):
        super().__init__(lineno)
        self.modificador_acceso = modificador_acceso
        self.parametros = parametros
        self.cuerpo = cuerpo

# Clases AST para instanciación de objetos y acceso a miembros (Paso 2.1.2)
class ExpresionNuevaInstancia(Expresion):
    def __init__(self, nombre_clase, argumentos, lineno=None):
        super().__init__(lineno)
        self.nombre_clase = nombre_clase
        self.argumentos = argumentos # Lista de Expresion

class ExpresionAccesoMiembro(Expresion):
    def __init__(self, objeto, miembro, lineno=None):
        super().__init__(lineno)
        self.objeto = objeto # Expresion (puede ser ExpresionIdentificador, ExpresionAccesoMiembro, etc.)
        self.miembro = miembro # ExpresionIdentificador (nombre del miembro)

class ExpresionLlamadaMetodo(Expresion):
    def __init__(self, objeto, metodo, argumentos, lineno=None):
        super().__init__(lineno)
        self.objeto = objeto
        self.metodo = metodo # ExpresionIdentificador
        self.argumentos = argumentos # Lista de Expresion

class ExpresionLlamadaFuncion(Expresion):
    def __init__(self, nombre, argumentos, lineno=None):
        super().__init__(lineno)
        self.nombre = nombre # ExpresionIdentificador
        self.argumentos = argumentos # Lista de Expresion

# Clase AST para la palabra clave 'super' (Paso 2.2.2)
class ExpresionSuper(Expresion):
    def __init__(self, lineno=None):
        super().__init__(lineno)

class ExpresionLlamadaSuper(Expresion):
    def __init__(self, argumentos, lineno=None):
        super().__init__(lineno)
        self.argumentos = argumentos # Lista de Expresion

class ExpresionEste(Expresion):
    def __init__(self, lineno=None):
        super().__init__(lineno)

# Clases AST para Manejo de Excepciones (Paso 2.4.1)
class SentenciaLanzar(Sentencia):
    def __init__(self, expresion, lineno=None):
        super().__init__(lineno)
        self.expresion = expresion

class BloqueAtrapar(AST):
    def __init__(self, tipo_excepcion, variable_excepcion, bloque, lineno=None):
        super().__init__(lineno)
        self.tipo_excepcion = tipo_excepcion
        self.variable_excepcion = variable_excepcion
        self.bloque = bloque

class SentenciaIntentarAtrapar(Sentencia):
    def __init__(self, bloque_intentar, bloques_atrapar, bloque_finalmente, lineno=None):
        super().__init__(lineno)
        self.bloque_intentar = bloque_intentar
        self.bloques_atrapar = bloques_atrapar # Lista de BloqueAtrapar
        self.bloque_finalmente = bloque_finalmente # SentenciaBloque o None

# Clase AST para Aserciones (Paso 2.4.3)
class SentenciaAfirmar(Sentencia):
    def __init__(self, condicion, mensaje, lineno=None):
        super().__init__(lineno)
        self.condicion = condicion
        self.mensaje = mensaje

# Clases AST para Arrays (Paso 3.1.1)
class TipoArray(AST):
    def __init__(self, tipo_elemento, lineno=None):
        super().__init__(lineno)
        self.tipo_elemento = tipo_elemento

class ExpresionLiteralArray(Expresion):
    def __init__(self, elementos, lineno=None):
        super().__init__(lineno)
        self.elementos = elementos # Lista de expresiones

class ExpresionAccesoArray(Expresion):
    def __init__(self, array, indice, lineno=None):
        super().__init__(lineno)
        self.array = array
        self.indice = indice

# Clase AST para Agrupación de Expresiones (ej. paréntesis)
class ExpresionAgrupacion(Expresion):
    def __init__(self, expresion, lineno=None):
        super().__init__(lineno)
        self.expresion = expresion

# Clase AST para Bucle Para-Cada (Paso 3.1.3)
class SentenciaParaCada(Sentencia):
    def __init__(self, variable, iterable, cuerpo, lineno=None):
        super().__init__(lineno)
        self.variable = variable # Parametro (nombre: tipo)
        self.iterable = iterable # Expresion
        self.cuerpo = cuerpo # SentenciaBloque