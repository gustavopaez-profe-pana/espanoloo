"""
archivo: verificador_tipos.py
Descripción: Verificador de tipos para EspañolOO.
Autor: Gustavo Páez
Contacto: contacto@email.com
Fecha: 12/08/2025
Versión: 1.0
Licencia: GPL
"""

from espanoloo_compiler.tabla_simbolos import TablaSimbolos
from espanoloo_compiler.ast import *

class VerificadorTipos:
    def __init__(self, tabla_simbolos):
        self.tabla_simbolos = tabla_simbolos
        self.errores = []
        self.current_class_name = None # Para el control de acceso

    def son_tipos_compatibles(self, tipo_esperado, tipo_encontrado):
        """Verifica si el tipo encontrado puede ser asignado a una variable de tipo esperado."""
        if tipo_esperado == tipo_encontrado:
            return True
        # Permitir asignar un entero a un decimal
        if tipo_esperado == 'decimal' and tipo_encontrado == 'entero':
            return True
        # En un futuro, aquí se podría manejar la herencia (upcasting)
        return False

    def _es_subclase(self, clase_hija_nombre, clase_padre_nombre):
        if clase_hija_nombre == clase_padre_nombre:
            return True
        
        simbolo_clase_hija = self.tabla_simbolos.obtener(clase_hija_nombre)
        if not simbolo_clase_hija or simbolo_clase_hija['tipo'] != 'clase':
            return False # No es una clase o no existe
        
        hereda_de = simbolo_clase_hija['valor'].get('hereda_de')
        if hereda_de:
            return self._es_subclase(hereda_de['tipo'], clase_padre_nombre)
        
        return False

    def visitar(self, nodo):
        nombre_metodo = f'visitar_{type(nodo).__name__}'
        visitante = getattr(self, nombre_metodo, self.visita_generica)
        return visitante(nodo)

    def visita_generica(self, nodo):
        # Para nodos que no necesitan una verificación especial, simplemente continuamos.
        # En una implementación más robusta, podríamos querer manejar todos los tipos de nodos explícitamente.
        pass

    def visitar_Programa(self, nodo):
        for declaracion in nodo.declaraciones:
            self.visitar(declaracion)

    def visitar_ExpresionBinaria(self, nodo):
        tipo_izquierda = self.visitar(nodo.izquierda)
        tipo_derecha = self.visitar(nodo.derecha)

        # Lógica de ejemplo para operadores aritméticos
        if nodo.operador in ['+', '-', '*', '/', '%']:
            if tipo_izquierda in ['entero', 'decimal'] and tipo_derecha in ['entero', 'decimal']:
                # La promoción de tipo resulta en decimal si uno de los operandos es decimal
                return 'decimal' if 'decimal' in [tipo_izquierda, tipo_derecha] else 'entero'
            else:
                self.errores.append(f"Error de tipo: El operador '{nodo.operador}' no se puede aplicar a los tipos '{tipo_izquierda}' y '{tipo_derecha}'.")
                return 'error' # Tipo de error para detener la cascada

        # Lógica de ejemplo para operadores de comparación
        elif nodo.operador in ['==', '!=', '<', '>', '<=', '>=']:
            if tipo_izquierda == tipo_derecha:
                return 'booleano'
            else:
                self.errores.append(f"Error de tipo: No se pueden comparar los tipos '{tipo_izquierda}' y '{tipo_derecha}'.")
                return 'error'

        # Lógica de ejemplo para operadores lógicos
        elif nodo.operador in ['y', 'o']:
            if tipo_izquierda == 'booleano' and tipo_derecha == 'booleano':
                return 'booleano'
            else:
                self.errores.append(f"Error de tipo: El operador '{nodo.operador}' requiere operandos de tipo booleano.")
                return 'error'
        
        return 'error' # Operador no reconocido

    def visitar_ExpresionLiteral(self, nodo):
        if isinstance(nodo.valor, int):
            return 'entero'
        elif isinstance(nodo.valor, float):
            return 'decimal'
        elif isinstance(nodo.valor, str):
            return 'cadena'
        elif isinstance(nodo.valor, bool):
            return 'booleano'
        elif nodo.valor is None:
            return 'nulo'
        return 'desconocido'

    def visitar_ExpresionIdentificador(self, nodo):
        tipo = self.tabla_simbolos.obtener_tipo(nodo.nombre)
        if tipo is None:
            self.errores.append(f"Error: La variable '{nodo.nombre}' no ha sido declarada.")
            return 'error'
        return tipo

    def visitar_ExpresionEste(self, nodo):
        tipo = self.tabla_simbolos.obtener_tipo('este')
        if tipo is None:
            self.errores.append("Error: 'este' solo puede ser usado dentro de un método de una clase.")
            return 'error'
        return tipo

    def visitar_ExpresionSuper(self, nodo):
        # La validación de si 'super' es válido se hace en el VerificadorSemantico.
        # Aquí solo obtenemos su tipo, que es el de la clase padre.
        simbolo_clase_actual = self.tabla_simbolos.obtener(self.tabla_simbolos.obtener_tipo('este'))
        if not simbolo_clase_actual or not simbolo_clase_actual['valor'].get('hereda_de'):
            self.errores.append("Error: 'super' solo puede ser usado en una clase que hereda de otra.")
            return 'error'
        return simbolo_clase_actual['valor']['hereda_de']['tipo']

    def visitar_ExpresionLlamadaSuper(self, nodo):
        # La llamada al constructor padre no retorna un valor.
        # La validación de los argumentos se hará en el VerificadorSemantico.
        return 'nulo'

    def visitar_ExpresionNuevaInstancia(self, nodo):
        nombre_clase = nodo.nombre_clase
        simbolo_clase = self.tabla_simbolos.obtener(nombre_clase)

        if not simbolo_clase or simbolo_clase.get('tipo') != 'clase':
            self.errores.append(f"Error Semántico: La clase '{nombre_clase}' no ha sido declarada.")
            return 'error'

        return nombre_clase

    def visitar_ExpresionAccesoMiembro(self, nodo):
        tipo_objeto = self.visitar(nodo.objeto)
        if tipo_objeto == 'error':
            return 'error'

        # Necesitamos obtener la tabla de símbolos de la clase para buscar el miembro
        simbolo_clase = self.tabla_simbolos.obtener(tipo_objeto)
        if not simbolo_clase or simbolo_clase['tipo'] != 'clase':
            self.errores.append(f"Error de tipo: No se puede acceder al miembro '{nodo.miembro.nombre}' de un tipo no-clase '{tipo_objeto}'.")
            return 'error'

        tabla_clase = simbolo_clase['valor']
        simbolo_miembro = tabla_clase.obtener(nodo.miembro.nombre)

        if simbolo_miembro is None:
            self.errores.append(f"Error: El miembro '{nodo.miembro.nombre}' no existe en la clase '{tipo_objeto}'.")
            return 'error'
        
        # Comprobación de modificadores de acceso
        modificador_acceso = simbolo_miembro.get('modificador_acceso')
        if modificador_acceso == 'privado':
            if tipo_objeto != self.current_class_name:
                self.errores.append(f"Error de acceso: El miembro '{nodo.miembro.nombre}' es privado y solo puede ser accedido desde la clase '{tipo_objeto}'.")
                return 'error'
        elif modificador_acceso == 'protegido':
            if not self._es_subclase(self.current_class_name, tipo_objeto):
                self.errores.append(f"Error de acceso: El miembro '{nodo.miembro.nombre}' es protegido y solo puede ser accedido desde la clase '{tipo_objeto}' o sus subclases.")
                return 'error'
        
        return simbolo_miembro['tipo']

    def visitar_ExpresionLlamadaMetodo(self, nodo):
        tipo_objeto = self.visitar(nodo.objeto)
        if tipo_objeto == 'error':
            return 'error'

        simbolo_clase = self.tabla_simbolos.obtener(tipo_objeto)
        if not simbolo_clase or simbolo_clase['tipo'] != 'clase':
            self.errores.append(f"Error de tipo: No se puede llamar al método '{nodo.metodo.nombre}' de un tipo no-clase '{tipo_objeto}'.")
            return 'error'

        tabla_clase = simbolo_clase['valor']
        simbolo_metodo = tabla_clase.obtener(nodo.metodo.nombre)

        if simbolo_metodo is None or simbolo_metodo['tipo'] != 'metodo':
            self.errores.append(f"Error: El método '{nodo.metodo.nombre}' no existe en la clase '{tipo_objeto}'.")
            return 'error'

        # Comprobación de modificadores de acceso
        modificador_acceso = simbolo_metodo.get('modificador_acceso')
        if modificador_acceso == 'privado':
            if tipo_objeto != self.current_class_name:
                self.errores.append(f"Error de acceso: El método '{nodo.metodo.nombre}' es privado y solo puede ser llamado desde la clase '{tipo_objeto}'.")
                return 'error'
        elif modificador_acceso == 'protegido':
            if not self._es_subclase(self.current_class_name, tipo_objeto):
                self.errores.append(f"Error de acceso: El método '{nodo.metodo.nombre}' es protegido y solo puede ser llamado desde la clase '{tipo_objeto}' o sus subclases.")
                return 'error'

        # Aquí iría la validación de argumentos y tipos de retorno
        firma_metodo = simbolo_metodo['valor']['firma']
        
        # Comprobar número de argumentos
        if len(nodo.argumentos) != len(firma_metodo.parametros):
            self.errores.append(f"Error: Número incorrecto de argumentos para el método '{nodo.metodo.nombre}'. Se esperaban {len(firma_metodo.parametros)} pero se recibieron {len(nodo.argumentos)}.")
            return firma_metodo.tipo_retorno # Devolver el tipo esperado para no encadenar errores

        # Comprobar tipos de argumentos
        for i, arg_nodo in enumerate(nodo.argumentos):
            tipo_arg = self.visitar(arg_nodo)
            tipo_param = firma_metodo.parametros[i].tipo
            if tipo_arg != tipo_param:
                self.errores.append(f"Error de tipo: El argumento {i+1} del método '{nodo.metodo.nombre}' es de tipo '{tipo_arg}', se esperaba '{tipo_param}'.")

        return firma_metodo.tipo_retorno