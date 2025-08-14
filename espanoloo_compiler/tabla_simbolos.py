

class TablaSimbolos:
    def __init__(self, padre=None):
        self.simbolos = {}
        self.padre = padre
    
    def agregar(self, nombre, tipo, valor=None):
        """Agrega un símbolo a la tabla del ámbito actual."""
        if nombre in self.simbolos:
            raise Exception(f"Error Semántico: El símbolo '{nombre}' ya está definido en este ámbito.")
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}
    
    def obtener(self, nombre):
        """Obtiene un símbolo de la tabla actual o de las tablas padre."""
        simbolo = self.simbolos.get(nombre, None)
        if simbolo:
            return simbolo
        
        if self.padre:
            return self.padre.obtener(nombre)
        
        return None
    
    def existe(self, nombre):
        """Verifica si un símbolo existe en la tabla actual o en las padres."""
        return self.obtener(nombre) is not None

    def obtener_tipo(self, nombre):
        """Obtiene el tipo de un símbolo."""
        simbolo = self.obtener(nombre)
        if simbolo:
            return simbolo['tipo']
        return None

    def obtener_todos_los_simbolos(self):
        """Obtiene todos los símbolos de la tabla actual y de las tablas padre."""
        simbolos_encontrados = []
        current_scope = self
        while current_scope:
            for nombre, info in current_scope.simbolos.items():
                simbolos_encontrados.append({'name': nombre, 'type': info['tipo']})
            current_scope = current_scope.padre
        return simbolos_encontrados

    def __repr__(self):
        return str(self.simbolos)
