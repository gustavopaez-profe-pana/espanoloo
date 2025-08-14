"""
archivo: optimizador.py
Descripción: Optimizador de AST para EspañolOO.
Autor: Gustavo Páez
Contacto: contacto@email.com
Fecha: 12/08/2025
Versión: 1.0
Licencia: GPL
"""

from espanoloo_compiler.ast import *

class Optimizador:
    def __init__(self):
        self.optimizaciones = 0

    def optimizar(self, nodo):
        # Usamos un bucle while para aplicar optimizaciones repetidamente
        # hasta que no se puedan realizar más cambios.
        while True:
            self.optimizaciones = 0
            nodo = self.visitar(nodo)
            if self.optimizaciones == 0:
                break
        return nodo

    def visitar(self, nodo):
        nombre_metodo = f'visitar_{type(nodo).__name__}'
        visitante = getattr(self, nombre_metodo, self.visita_generica)
        return visitante(nodo)

    def visita_generica(self, nodo):
        # Si no hay un método de visita específico, no hacemos nada.
        return nodo

    def visitar_ExpresionBinaria(self, nodo):
        nodo.izquierda = self.visitar(nodo.izquierda)
        nodo.derecha = self.visitar(nodo.derecha)

        # Plegado de constantes
        if isinstance(nodo.izquierda, ExpresionLiteral) and isinstance(nodo.derecha, ExpresionLiteral):
            self.optimizaciones += 1
            izquierda = nodo.izquierda.valor
            derecha = nodo.derecha.valor
            
            if nodo.operador == '+': return ExpresionLiteral(izquierda + derecha)
            if nodo.operador == '-': return ExpresionLiteral(izquierda - derecha)
            if nodo.operador == '*': return ExpresionLiteral(izquierda * derecha)
            if nodo.operador == '/': return ExpresionLiteral(izquierda / derecha) if derecha != 0 else nodo
            if nodo.operador == '%': return ExpresionLiteral(izquierda % derecha) if derecha != 0 else nodo
            if nodo.operador == '==': return ExpresionLiteral(izquierda == derecha)
            if nodo.operador == '!=': return ExpresionLiteral(izquierda != derecha)
            if nodo.operador == '<': return ExpresionLiteral(izquierda < derecha)
            if nodo.operador == '>': return ExpresionLiteral(izquierda > derecha)
            if nodo.operador == '<=': return ExpresionLiteral(izquierda <= derecha)
            if nodo.operador == '>=': return ExpresionLiteral(izquierda >= derecha)
            if nodo.operador == 'y': return ExpresionLiteral(izquierda and derecha)
            if nodo.operador == 'o': return ExpresionLiteral(izquierda or derecha)

        return nodo

    def visitar_SentenciaSi(self, nodo):
        nodo.condicion = self.visitar(nodo.condicion)
        nodo.entonces = self.visitar(nodo.entonces)
        if nodo.sino:
            nodo.sino = self.visitar(nodo.sino)

        # Eliminación de código muerto
        if isinstance(nodo.condicion, ExpresionLiteral):
            self.optimizaciones += 1
            if nodo.condicion.valor: # si (verdadero)
                return nodo.entonces
            else: # si (falso)
                return nodo.sino if nodo.sino else SentenciaBloque([]) # Devuelve un bloque vacío si no hay sino
        
        return nodo

    # Necesitamos recorrer el AST completo
    def visitar_Programa(self, nodo):
        nuevas_declaraciones = []
        for declaracion in nodo.declaraciones:
            nuevas_declaraciones.append(self.visitar(declaracion))
        nodo.declaraciones = nuevas_declaraciones
        return nodo

    def visitar_DeclaracionFuncion(self, nodo):
        nodo.cuerpo = self.visitar(nodo.cuerpo)
        return nodo

    def visitar_SentenciaBloque(self, nodo):
        nuevas_sentencias = []
        for sentencia in nodo.sentencias:
            nuevas_sentencias.append(self.visitar(sentencia))
        nodo.sentencias = nuevas_sentencias
        return nodo
