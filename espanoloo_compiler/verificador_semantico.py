from espanoloo_compiler.tabla_simbolos import TablaSimbolos
from espanoloo_compiler.verificador_tipos import VerificadorTipos
from espanoloo_compiler.ast import *

class VerificadorSemantico:
    def __init__(self):
        self.tabla_simbolos = TablaSimbolos()
        self.verificador_tipos = VerificadorTipos(self.tabla_simbolos) # El verificador de tipos usará nuestra tabla
        self.errores = []
        self.clase_actual = None # Para rastrear la clase que se está visitando

    def visitar(self, nodo):
        nombre_metodo = f'visitar_{type(nodo).__name__}'
        visitante = getattr(self, nombre_metodo, self.visita_generica)
        return visitante(nodo)

    def visita_generica(self, nodo):
        # Para la mayoría de los nodos, simplemente continuamos el recorrido.
        # Los nodos con hijos deben asegurarse de llamara self.visitar en ellos.
        pass

    def verificar(self, programa_ast):
        self.visitar(programa_ast)
        # Combinar errores del verificador de tipos
        self.errores.extend(self.verificador_tipos.errores)

    def visitar_Programa(self, nodo):
        for declaracion in nodo.declaraciones:
            self.visitar(declaracion)

    def visitar_DeclaracionFuncion(self, nodo):
        # Comprobar si la función ya existe en el ámbito actual
        if self.tabla_simbolos.existe(nodo.nombre):
            self.errores.append(f"Error Semántico: La función '{nodo.nombre}' ya ha sido declarada.")

        # Agregar la función a la tabla de símbolos del ámbito actual ANTES de entrar en su cuerpo
        # para permitir la recursividad.
        # En una implementación completa, guardaríamos la signatura de la función.
        self.tabla_simbolos.agregar(nodo.nombre, 'funcion')

        # Crear un nuevo ámbito para la función
        ambito_funcion = TablaSimbolos(padre=self.tabla_simbolos)
        
        # Guardar y reemplazar la tabla de símbolos actual
        tabla_anterior = self.tabla_simbolos
        self.tabla_simbolos = ambito_funcion
        self.verificador_tipos.tabla_simbolos = ambito_funcion # Actualizar la referencia en el verificador de tipos

        # Agregar los parámetros a la nueva tabla de símbolos
        for parametro in nodo.parametros:
            self.tabla_simbolos.agregar(parametro.nombre, parametro.tipo)

        # Visitar el cuerpo de la función
        self.visitar(nodo.cuerpo)

        # Restaurar la tabla de símbolos anterior
        self.tabla_simbolos = tabla_anterior
        self.verificador_tipos.tabla_simbolos = tabla_anterior

    def visitar_BloqueSentencias(self, nodo):
        # Crear un nuevo ámbito para el bloque
        ambito_bloque = TablaSimbolos(padre=self.tabla_simbolos)
        tabla_anterior = self.tabla_simbolos
        self.tabla_simbolos = ambito_bloque
        self.verificador_tipos.tabla_simbolos = ambito_bloque

        for sentencia in nodo.sentencias:
            self.visitar(sentencia)

        # Restaurar la tabla de símbolos anterior
        self.tabla_simbolos = tabla_anterior
        self.verificador_tipos.tabla_simbolos = tabla_anterior

    def visitar_DeclaracionVariable(self, nodo):
        # Comprobar si la variable ya existe en el ámbito actual (sin mirar padres)
        if nodo.nombre in self.tabla_simbolos.simbolos:
            self.errores.append(f"Error Semántico: La variable '{nodo.nombre}' ya ha sido declarada en este ámbito.")
            return

        tipo_declarado = nodo.tipo
        
        if nodo.valor:
            # Usamos el verificador de tipos para obtener el tipo de la expresión
            tipo_valor = self.verificador_tipos.visitar(nodo.valor)
            
            # Comprobación de compatibilidad de tipos
            if tipo_valor != 'error': # Solo comprobar si no hubo ya un error en la expresión
                if not self.verificador_tipos.son_tipos_compatibles(tipo_declarado, tipo_valor):
                    self.errores.append(f"Error de tipo: No se puede asignar un valor de tipo '{tipo_valor}' a una variable de tipo '{tipo_declarado}'.")

        # Agregar la variable a la tabla de símbolos del ámbito actual
        self.tabla_simbolos.agregar(nodo.nombre, tipo_declarado)

    def visitar_DeclaracionClase(self, nodo):
        if self.tabla_simbolos.existe(nodo.nombre):
            self.errores.append(f"Error Semántico: El símbolo '{nodo.nombre}' ya ha sido declarado.")
            return

        # Guardar clase actual y establecer la nueva
        clase_anterior = self.clase_actual
        self.clase_actual = nodo.nombre

        # Guardar el nombre de la clase actual en el verificador de tipos
        verificador_tipos_clase_anterior = self.verificador_tipos.current_class_name
        self.verificador_tipos.current_class_name = nodo.nombre

        # Crear un nuevo ámbito para la clase
        ambito_clase = TablaSimbolos(padre=self.tabla_simbolos)
        simbolo_clase = {'tipo': 'clase', 'valor': ambito_clase, 'hereda_de': None}

        # Manejar herencia
        if nodo.hereda_de:
            simbolo_padre = self.tabla_simbolos.obtener(nodo.hereda_de)
            if not simbolo_padre or simbolo_padre.get('tipo') != 'clase':
                self.errores.append(f"Error Semántico: La clase padre '{nodo.hereda_de}' no ha sido declarada.")
            else:
                simbolo_clase['hereda_de'] = simbolo_padre
                # Copiar miembros heredados
                tabla_padre = simbolo_padre['valor']['valor']
                for nombre, simbolo in tabla_padre.simbolos.items():
                    if simbolo.get('modificador_acceso') in ['publico', 'protegido']:
                        ambito_clase.simbolos[nombre] = simbolo

        # Agregar la clase a la tabla de símbolos antes de procesar miembros
        self.tabla_simbolos.agregar(nodo.nombre, 'clase', simbolo_clase)

        # Cambiar al ámbito de la clase para procesar sus miembros
        tabla_anterior = self.tabla_simbolos
        self.tabla_simbolos = ambito_clase
        self.verificador_tipos.tabla_simbolos = ambito_clase

        for miembro in nodo.miembros:
            self.visitar(miembro)

        # Restaurar el ámbito y la clase anterior
        self.tabla_simbolos = tabla_anterior
        self.verificador_tipos.tabla_simbolos = tabla_anterior
        self.clase_actual = clase_anterior
        self.verificador_tipos.current_class_name = verificador_tipos_clase_anterior

    def visitar_DeclaracionAtributo(self, nodo):
        # Comprobar si el atributo ya existe en el ámbito de la clase actual (sin mirar padres)
        if nodo.nombre in self.tabla_simbolos.simbolos:
            self.errores.append(f"Error Semántico: El atributo '{nodo.nombre}' ya ha sido declarado en esta clase.")
            return # No continuar si ya hay un error
        
        tipo_declarado = nodo.tipo
        if nodo.valor:
            tipo_valor = self.verificador_tipos.visitar(nodo.valor) # Esto delegará al VerificadorTipos
            print(f"Debug: tipo_valor = {tipo_valor}")
            print(f"Debug: tipo_valor = {tipo_valor}")
            
            # Lógica de compatibilidad de tipos (simplificada por ahora)
            if tipo_valor != tipo_declarado and tipo_valor != 'error':
                # Permitir asignar un entero a un decimal
                if tipo_declarado == 'decimal' and tipo_valor == 'entero':
                    pass # Esto es válido
                else:
                    self.errores.append(f"Error de tipo: No se puede asignar un valor de tipo '{tipo_valor}' al atributo '{nodo.nombre}' de tipo '{tipo_declarado}'.")
        
        # Agregar el atributo a la tabla de símbolos de la clase
        self.tabla_simbolos.agregar(nodo.nombre, tipo_declarado, {'modificador_acceso': nodo.modificador_acceso})

    def visitar_DeclaracionMetodo(self, nodo):
        if nodo.nombre in self.tabla_simbolos.simbolos:
            self.errores.append(f"Error Semántico: El método '{nodo.nombre}' ya ha sido declarado en esta clase.")

        # Comprobar sobreescritura
        if self.clase_actual:
            simbolo_clase_actual = self.tabla_simbolos.obtener(self.clase_actual)
            if simbolo_clase_actual and simbolo_clase_actual['valor'].get('hereda_de'):
                simbolo_clase_padre = simbolo_clase_actual['valor']['hereda_de']
                tabla_clase_padre = simbolo_clase_padre['valor']
                
                metodo_padre = tabla_clase_padre.obtener(nodo.nombre)
                
                if metodo_padre and metodo_padre.get('tipo') == 'metodo':
                    # Es una sobreescritura, ahora verificar la firma
                    firma_padre = metodo_padre['valor']['firma']
                    
                    # 1. Número de parámetros
                    if len(nodo.parametros) != len(firma_padre.parametros):
                        self.errores.append(f"Error Semántico: El método '{nodo.nombre}' en '{self.clase_actual}' intenta sobreescribir un método con un número de parámetros diferente.")
                    else:
                        # 2. Tipos de parámetros
                        for i, param_actual in enumerate(nodo.parametros):
                            param_padre = firma_padre.parametros[i]
                            if param_actual.tipo != param_padre.tipo:
                                self.errores.append(f"Error de tipo: El parámetro '{param_actual.nombre}' del método '{nodo.nombre}' en '{self.clase_actual}' es de tipo '{param_actual.tipo}', se esperaba '{param_padre.tipo}' (del método padre).")
                        
                        # 3. Tipo de retorno
                        if nodo.tipo_retorno != firma_padre.tipo_retorno:
                            self.errores.append(f"Error de tipo: El método '{nodo.nombre}' en '{self.clase_actual}' retorna '{nodo.tipo_retorno}', se esperaba '{firma_padre.tipo_retorno}' (del método padre).")

        self.tabla_simbolos.agregar(nodo.nombre, 'metodo', {'modificador_acceso': nodo.modificador_acceso, 'firma': nodo})

        # Crear un nuevo ámbito para el método
        ambito_metodo = TablaSimbolos(padre=self.tabla_simbolos)
        
        tabla_anterior = self.tabla_simbolos
        self.tabla_simbolos = ambito_metodo
        self.verificador_tipos.tabla_simbolos = ambito_metodo

        # Agregar 'este' al ámbito del método
        if self.clase_actual:
            self.tabla_simbolos.agregar('este', self.clase_actual)

        for parametro in nodo.parametros:
            self.tabla_simbolos.agregar(parametro.nombre, parametro.tipo)

        if nodo.cuerpo:
            self.visitar(nodo.cuerpo)

        self.tabla_simbolos = tabla_anterior
        self.verificador_tipos.tabla_simbolos = tabla_anterior