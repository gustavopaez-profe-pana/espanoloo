from espanoloo_compiler.ast import *

class GeneradorCodigo:
    def __init__(self):
        self.codigo = []
        self.indentacion = 0
        self.atributos_clase_actual = []

    def visitar(self, nodo):
        nombre_metodo = f'visitar_{type(nodo).__name__}'
        visitante = getattr(self, nombre_metodo, self.visita_generica)
        return visitante(nodo)

    def visita_generica(self, nodo):
        # Primero, verificamos si el nodo es una instancia de Expresion. 
        # Si es así, podría ser un nodo que no hemos implementado todavía. 
        if isinstance(nodo, Expresion):
            # Podríamos querer registrar una advertencia o un error aquí.
            # Por ahora, simplemente devolvemos una cadena vacía.
            return ""
        # Si no es una expresión, podría ser una sentencia u otra declaración.
        # En ese caso, es más seguro lanzar una excepción si no hay un método de visita.
        raise Exception(f'No hay un método de visita para el nodo {type(nodo).__name__}')

    def agregar_linea(self, linea):
        self.codigo.append('    ' * self.indentacion + linea)

    def generar(self, programa_ast):
        self.visitar(programa_ast)
        return "\n".join(self.codigo)

    def visitar_Programa(self, nodo):
        self.agregar_linea("# Código generado por el compilador de EspañolOO")
        self.agregar_linea("import sys")
        self.agregar_linea("")
        for declaracion in nodo.declaraciones:
            self.visitar(declaracion)

    def visitar_DeclaracionClase(self, nodo):
        herencia = f"({nodo.hereda_de})" if nodo.hereda_de else ""
        self.agregar_linea(f"class {nodo.nombre}{herencia}:")
        self.indentacion += 1
        
        # Recolectar atributos primero
        self.atributos_clase_actual = [m for m in nodo.miembros if isinstance(m, DeclaracionAtributo)]
        
        # Visitar otros miembros (constructor, métodos)
        for miembro in nodo.miembros:
            if not isinstance(miembro, DeclaracionAtributo):
                self.visitar(miembro)
        
        self.indentacion -= 1
        self.agregar_linea("")
        self.atributos_clase_actual = []

    def visitar_DeclaracionConstructor(self, nodo):
        parametros = ", ".join([p.nombre for p in nodo.parametros])
        self.agregar_linea(f"def __init__(self, {parametros}):")
        self.indentacion += 1
        
        # Inicializar atributos
        for attr in self.atributos_clase_actual:
            self.visitar(attr)

        self.visitar(nodo.cuerpo)
        self.indentacion -= 1
        self.agregar_linea("")

    def visitar_DeclaracionMetodo(self, nodo):
        parametros = ", ".join([p.nombre for p in nodo.parametros])
        self.agregar_linea(f"def {nodo.nombre}(self, {parametros}):")
        self.indentacion += 1
        self.visitar(nodo.cuerpo)
        self.indentacion -= 1
        self.agregar_linea("")

    def visitar_DeclaracionAtributo(self, nodo):
        # La inicialización se hace en el constructor
        if nodo.valor:
            valor = self.visitar(nodo.valor)
            self.agregar_linea(f"self.{nodo.nombre} = {valor}")
        else:
            self.agregar_linea(f"self.{nodo.nombre} = None")

    def visitar_ExpresionEste(self, nodo):
        return "self"

    def visitar_ExpresionSuper(self, nodo):
        return "super()"

    def visitar_ExpresionLlamadaSuper(self, nodo):
        argumentos = ", ".join([self.visitar(arg) for arg in nodo.argumentos])
        return f"super().__init__({argumentos})"

    def visitar_ExpresionNuevaInstancia(self, nodo):
        argumentos = ", ".join([self.visitar(arg) for arg in nodo.argumentos])
        return f"{nodo.nombre_clase}({argumentos})"

    def visitar_ExpresionAccesoMiembro(self, nodo):
        objeto = self.visitar(nodo.objeto)
        return f"{objeto}.{nodo.miembro.nombre}"

    def visitar_ExpresionLlamadaMetodo(self, nodo):
        objeto = self.visitar(nodo.objeto)
        argumentos = ", ".join([self.visitar(arg) for arg in nodo.argumentos])
        return f"{objeto}.{nodo.metodo.nombre}({argumentos})"

    def visitar_DeclaracionFuncion(self, nodo):
        parametros = ", ".join([p.nombre for p in nodo.parametros])
        self.agregar_linea(f"def {nodo.nombre}({parametros}):")
        self.indentacion += 1
        self.visitar(nodo.cuerpo)
        self.indentacion -= 1
        self.agregar_linea("")

    def visitar_SentenciaBloque(self, nodo):
        for sentencia in nodo.sentencias:
            self.visitar(sentencia)

    def visitar_SentenciaSi(self, nodo):
        condicion = self.visitar(nodo.condicion)
        self.agregar_linea(f"if {condicion}:")
        self.indentacion += 1
        self.visitar(nodo.entonces)
        self.indentacion -= 1
        if nodo.sino:
            self.agregar_linea("else:")
            self.indentacion += 1
            self.visitar(nodo.sino)
            self.indentacion -= 1

    def visitar_BloqueSentencias(self, nodo):
        for sentencia in nodo.sentencias:
            self.visitar(sentencia)

    def visitar_SentenciaExpresion(self, nodo):
        self.visitar(nodo.expresion)

    def visitar_ExpresionBinaria(self, nodo):
        izquierda = self.visitar(nodo.izquierda)
        derecha = self.visitar(nodo.derecha)
        operador_map = {
            'y': 'and',
            'o': 'or'
        }
        operador = operador_map.get(nodo.operador, nodo.operador)
        return f"({izquierda} {operador} {derecha})"

    def visitar_ExpresionLiteral(self, nodo):
        if isinstance(nodo.valor, str):
            return f'"{nodo.valor}"'
        elif isinstance(nodo.valor, bool):
            return str(nodo.valor)
        elif nodo.valor is None:
            return "None"
        return str(nodo.valor)

    def visitar_ExpresionIdentificador(self, nodo):
        return nodo.nombre

    def visitar_DeclaracionVariable(self, nodo):
        if nodo.valor:
            valor = self.visitar(nodo.valor)
            self.agregar_linea(f"{nodo.nombre} = {valor}")
        else:
            self.agregar_linea(f"{nodo.nombre} = None")

    def visitar_SentenciaMientras(self, nodo):
        condicion = self.visitar(nodo.condicion)
        self.agregar_linea(f"while {condicion}:")
        self.indentacion += 1
        self.visitar(nodo.cuerpo)
        self.indentacion -= 1

    def visitar_SentenciaPara(self, nodo):
        # Nota: La traducción directa de un for de C a Python no es trivial.
        # Esto es una simplificación que asume un bucle while.
        # Una implementación completa requeriría más análisis.
        if nodo.inicializacion:
            self.visitar(nodo.inicializacion)
        condicion = self.visitar(nodo.condicion) if nodo.condicion else "True"
        self.agregar_linea(f"while {condicion}:")
        self.indentacion += 1
        self.visitar(nodo.cuerpo)
        if nodo.actualizacion:
            self.visitar(nodo.actualizacion)
        self.indentacion -= 1

    def visitar_SentenciaParaCada(self, nodo):
        iterable = self.visitar(nodo.iterable)
        self.agregar_linea(f"for {nodo.variable.nombre} in {iterable}:")
        self.indentacion += 1
        self.visitar(nodo.cuerpo)
        self.indentacion -= 1

    def visitar_SentenciaRetornar(self, nodo):
        if nodo.expresion:
            valor = self.visitar(nodo.expresion)
            self.agregar_linea(f"return {valor}")
        else:
            self.agregar_linea("return")

    def visitar_ExpresionUnaria(self, nodo):
        operando = self.visitar(nodo.operando)
        operador_map = {'no': 'not '}
        operador = operador_map.get(nodo.operador, nodo.operador)
        return f"({operador}{operando})"

    def visitar_ExpresionLlamadaFuncion(self, nodo):
        argumentos = ", ".join([self.visitar(arg) for arg in nodo.argumentos])
        return f"{nodo.nombre}({argumentos})"
