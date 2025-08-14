# Plan de Desarrollo del Lenguaje de Programación Orientada a Objetos "EspañolOO"

## Introducción

EspañolOO es un lenguaje de programación orientada a objetos con palabras reservadas en castellano, diseñado para ser simple pero robusto. Inspirado en lenguajes como Latino (que utiliza sintaxis en español) y siguiendo los principios de la programación orientada a objetos, EspañolOO busca facilitar el aprendizaje de la programación a hispanohablantes y proporcionar una alternativa natural para el desarrollo de software en español.

El compilador de EspañolOO se implementará en Python, utilizando la librería PLY (Python Lex-Yacc) para el análisis léxico y sintáctico, similar a como se describe en la documentación proporcionada.

## Análisis Comparativo con Otros Lenguajes en Español

### Latino
- **Ventajas**: Sintaxis simple y natural en español, fácil de aprender, multiplataforma, código abierto.
- **Limitaciones**: Principalmente procedimental (la POO está en desarrollo), menos maduro que otros lenguajes.

### EspañolOO (Propuesto)
- **Ventajas**: Enfoque completo en POO desde el inicio, sintaxis totalmente en español, compilador a código Python (ejecutable), robustez en el manejo de tipos y estructuras.
- **Diferenciación**: Mientras Latino es más un lenguaje de scripting, EspañolOO está diseñado como un lenguaje de programación orientada a objetos completo con su propio compilador.

## Fases de Desarrollo

### Fase 1: Fundamentos del Lenguaje (4-6 semanas)

#### Paso 1.1: Definición del Núcleo del Lenguaje (2 semanas)

##### 1.1.1: Tipos de Datos Básicos (3 días)
- **Entero (`entero`)**: Representación de números enteros positivos y negativos.
- **Decimal (`decimal`)**: Representación de números con punto decimal.
- **Cadena (`cadena`)**: Representación de texto, soportando UTF-8.
- **Booleano (`booleano`)**: Representación de valores lógicos (`verdadero`, `falso`).
- **Nulo (`nulo`)**: Representación de valores nulos.

**Implementación**:
```python
# Ejemplo de definición de tipos en EspañolOO
edad: entero = 25
precio: decimal = 19.99
nombre: cadena = "Juan"
activo: booleano = verdadero
dato: nulo = nulo
```

##### 1.1.2: Operadores Aritméticos, Lógicos y de Comparación (4 días)
- **Aritméticos**: `+`, `-`, `*`, `/`, `%` (módulo)
- **Lógicos**: `y` (AND), `o` (OR), `no` (NOT)
- **Comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`

**Implementación**:
```python
# Ejemplo de operadores en EspañolOO
resultado = (10 + 5) * 2  # 30
esMayor = (edad > 18) y activo  # verdadero o falso
```

##### 1.1.3: Variables y Asignación (2 días)
- Declaración de variables con tipo explícito.
- Asignación simple y múltiple.
- Constantes con la palabra reservada `constante`.

**Implementación**:
```python
# Ejemplo de variables en EspañolOO
x: entero = 10
y: entero = 20
x, y = y, x  # Intercambio de valores
PI: constante decimal = 3.14159
```

##### 1.1.4: Comentarios (1 día)
- Comentarios de una línea: `//`
- Comentarios multilínea: `/* ... */`

**Implementación**:
```python
// Esto es un comentario de una línea
/*
  Esto es un comentario
  multilínea
*/
```

#### Paso 1.2: Estructuras de Control (2 semanas)

##### 1.2.1: Condicionales (3 días)
- `si`, `sino`, `sino si`
- Operador ternario: `(condición) ? valor_verdadero : valor_falso`

**Implementación**:
```python
// Ejemplo de condicionales en EspañolOO
si (edad > 18) {
    imprimir("Mayor de edad")
} sino si (edad > 12) {
    imprimir("Adolescente")
} sino {
    imprimir("Niño")
}

// Operador ternario
mensaje = (edad > 18) ? "Mayor de edad" : "Menor de edad"
```

##### 1.2.2: Bucles (4 días)
- `mientras`: Bucle while
- `para`: Bucle for
- `hacer mientras`: Bucle do-while

**Implementación**:
```python
// Ejemplo de bucles en EspañolOO
// Bucle mientras
contador: entero = 0
mientras (contador < 10) {
    imprimir(contador)
    contador = contador + 1
}

// Bucle para
para (i: entero = 0; i < 10; i = i + 1) {
    imprimir(i)
}

// Bucle hacer mientras
hacer {
    imprimir("Ejecutando al menos una vez")
} mientras (falso)
```

##### 1.2.3: Control de Flujo (3 días)
- `romper`: Break
- `continuar`: Continue
- `retornar`: Return

**Implementación**:
```python
// Ejemplo de control de flujo en EspañolOO
para (i: entero = 0; i < 10; i = i + 1) {
    si (i == 5) {
        continuar  // Salta la iteración actual
    }
    si (i == 8) {
        romper  // Sale del bucle
    }
    imprimir(i)
}

funcion sumar(a: entero, b: entero): entero {
    retornar a + b
}
```

#### Paso 1.3: Funciones y Procedimientos (1 semana)

##### 1.3.1: Definición de Funciones (3 días)
- Palabra reservada `funcion`
- Parámetros con tipo
- Tipo de retorno
- Sobrecarga de funciones

**Implementación**:
```python
// Ejemplo de funciones en EspañolOO
funcion saludar(nombre: cadena): cadena {
    retornar "Hola, " + nombre
}

funcion sumar(a: entero, b: entero): entero {
    retornar a + b
}

funcion sumar(a: decimal, b: decimal): decimal {  // Sobrecarga
    retornar a + b
}
```

##### 1.3.2: Ámbito de Variables (2 días)
- Variables locales y globales
- Paso de parámetros por valor y por referencia

**Implementación**:
```python
// Ejemplo de ámbito de variables en EspañolOO
variableGlobal: entero = 10

funcion modificarVariable() {
    variableLocal: entero = 5
    variableGlobal = variableGlobal + variableLocal
}

funcion modificarPorReferencia(ref: entero) {
    ref = ref + 10
}

valor: entero = 20
modificarPorReferencia(valor)  // valor ahora es 30
```

##### 1.3.3: Funciones Anónimas (Lambdas) (2 días)
- Funciones sin nombre
- Expresiones lambda

**Implementación**:
```python
// Ejemplo de funciones anónimas en EspañolOO
duplicar = (x: entero) => x * 2
resultado = duplicar(5)  // 10
```

### Fase 2: Programación Orientada a Objetos (6-8 semanas)

#### Paso 2.1: Clases y Objetos (2 semanas)

##### 2.1.1: Definición de Clases (4 días)
- Palabra reservada `clase`
- Atributos y métodos
- Constructores
- Destructores

**Implementación**:
```python
// Ejemplo de clases en EspañolOO
clase Persona {
    // Atributos
    privado nombre: cadena
    privado edad: entero
    
    // Constructor
    publico constructor(nombre: cadena, edad: entero) {
        este.nombre = nombre
        este.edad = edad
    }
    
    // Métodos
    publico obtenerNombre(): cadena {
        retornar este.nombre
    }
    
    publico obtenerEdad(): entero {
        retornar este.edad
    }
    
    publico cumplirAnios() {
        este.edad = este.edad + 1
    }
}
```

##### 2.1.2: Instanciación de Objetos (3 días)
- Creación de objetos
- Acceso a atributos y métodos
- Palabra reservada `nuevo`

**Implementación**:
```python
// Ejemplo de instanciación en EspañolOO
juan: Persona = nuevo Persona("Juan", 25)
imprimir(juan.obtenerNombre())  // "Juan"
imprimir(juan.obtenerEdad())    // 25
juan.cumplirAnios()
imprimir(juan.obtenerEdad())    // 26
```

##### 2.1.3: Modificadores de Acceso (3 días)
- `publico`: Acceso desde cualquier lugar
- `privado`: Acceso solo dentro de la clase
- `protegido`: Acceso dentro de la clase y clases hijas

**Implementación**:
```python
// Ejemplo de modificadores de acceso en EspañolOO
clase Ejemplo {
    publico atributoPublico: entero
    privado atributoPrivado: cadena
    protegido atributoProtegido: decimal
    
    publico constructor() {
        este.atributoPublico = 10
        este.atributoPrivado = "secreto"
        este.atributoProtegido = 3.14
    }
    
    publico obtenerPrivado(): cadena {
        retornar este.atributoPrivado  // Acceso permitido dentro de la clase
    }
}
```

#### Paso 2.2: Herencia (2 semanas)

##### 2.2.1: Herencia Simple (4 días)
- Palabra reservada `hereda`
- Clases base y derivadas
- Palabra reservada `super` para acceder a miembros de la clase base

**Implementación**:
```python
// Ejemplo de herencia en EspañolOO
clase Animal {
    protegido nombre: cadena
    
    publico constructor(nombre: cadena) {
        este.nombre = nombre
    }
    
    publico hacerSonido() {
        imprimir("Sonido genérico de animal")
    }
}

clase Perro hereda Animal {
    publico constructor(nombre: cadena) {
        super(nombre)  // Llama al constructor de la clase base
    }
    
    publico hacerSonido() {
        imprimir("Guau guau!")
    }
    
    publico ladrar() {
        imprimir("El perro está ladrando")
    }
}
```

##### 2.2.2: Sobreescritura de Métodos (3 días)
- Redefinición de métodos en clases derivadas
- Palabra reservada `super` para llamar al método de la clase base

**Implementación**:
```python
// Ejemplo de sobreescritura de métodos en EspañolOO
clase Gato hereda Animal {
    publico constructor(nombre: cadena) {
        super(nombre)
    }
    
    publico hacerSonido() {
        super.hacerSonido()  // Llama al método de la clase base
        imprimir("Miau miau!")
    }
}
```

##### 2.2.3: Clases Abstractas (3 días)
- Palabra reservada `abstracto`
- Métodos abstractos
- Clases que no pueden ser instanciadas directamente

**Implementación**:
```python
// Ejemplo de clases abstractas en EspañolOO
abstracto clase Figura {
    publico abstracto calcularArea(): decimal
    publico abstracto calcularPerimetro(): decimal
}

clase Rectangulo hereda Figura {
    privado base: decimal
    privada altura: decimal
    
    publico constructor(base: decimal, altura: decimal) {
        este.base = base
        este.altura = altura
    }
    
    publico calcularArea(): decimal {
        retornar este.base * este.altura
    }
    
    publico calcularPerimetro(): decimal {
        retornar 2 * (este.base + este.altura)
    }
}
```

#### Paso 2.3: Polimorfismo (2 semanas)

##### 2.3.1: Polimorfismo de Subtipos (4 días)
- Uso de referencias a clases base para almacenar objetos de clases derivadas
- Llamada a métodos sobrescritos

**Implementación**:
```python
// Ejemplo de polimorfismo en EspañolOO
funcion hacerSonidoAnimal(animal: Animal) {
    animal.hacerSonido()
}

miPerro: Perro = nuevo Perro("Firulais")
miGato: Gato = nuevo Gato("Misi")

hacerSonidoAnimal(miPerro)  // "Guau guau!"
hacerSonidoAnimal(miGato)  // "Sonido genérico de animal" + "Miau miau!"
```

##### 2.3.2: Interfaces (3 días)
- Palabra reservada `interfaz`
- Definición de contratos
- Implementación de múltiples interfaces

**Implementación**:
```python
// Ejemplo de interfaces en EspañolOO
interfaz Volable {
    publico volar(): nulo
}

interfaz Nadable {
    publico nadar(): nulo
}

clase Pajaro hereda Animal implementa Volable {
    publico constructor(nombre: cadena) {
        super(nombre)
    }
    
    publico hacerSonido() {
        imprimir("Pío pío!")
    }
    
    publico volar() {
        imprimir("El pájaro está volando")
    }
}

clase Pato hereda Animal implementa Volable, Nadable {
    publico constructor(nombre: cadena) {
        super(nombre)
    }
    
    publico hacerSonido() {
        imprimir("Cuac cuac!")
    }
    
    publico volar() {
        imprimir("El pato está volando")
    }
    
    publico nadar() {
        imprimir("El pato está nadando")
    }
}
```

##### 2.3.3: Genéricos (3 días)
- Clases y métodos genéricos
- Parámetros de tipo

**Implementación**:
```python
// Ejemplo de genéricos en EspañolOO
clase Contenedor<T> {
    privado elemento: T
    
    publico constructor(elemento: T) {
        este.elemento = elemento
    }
    
    publico obtener(): T {
        retornar este.elemento
    }
    
    publico establecer(elemento: T): nulo {
        este.elemento = elemento
    }
}

// Uso de la clase genérica
contenedorEntero: Contenedor<entero> = nuevo Contenedor<entero>(10)
contenedorCadena: Contenedor<cadena> = nuevo Contenedor<cadena>("Hola")
```

#### Paso 2.4: Manejo de Excepciones (1 semana)

##### 2.4.1: Definición de Excepciones (2 días)
- Palabras reservadas `intentar`, `atrapar`, `finalmente`, `lanzar`
- Jerarquía de excepciones
- Creación de excepciones personalizadas

**Implementación**:
```python
// Ejemplo de excepciones en EspañolOO
clase MiExcepcion hereda Excepcion {
    publico constructor(mensaje: cadena) {
        super(mensaje)
    }
}

funcion dividir(a: decimal, b: decimal): decimal {
    si (b == 0) {
        lanzar nuevo MiExcepcion("No se puede dividir por cero")
    }
    retornar a / b
}
```

##### 2.4.2: Manejo de Excepciones (3 días)
- Bloques try-catch-finally
- Propagación de excepciones

**Implementación**:
```python
// Ejemplo de manejo de excepciones en EspañolOO
intentar {
    resultado: decimal = dividir(10, 0)
    imprimir("El resultado es: " + resultado)
} atrapar (e: MiExcepcion) {
    imprimir("Error: " + e.obtenerMensaje())
} finalmente {
    imprimir("Operación finalizada")
}
```

##### 2.4.3: Aserciones (2 días)
- Palabra reservada `afirmar`
- Verificación de condiciones durante el desarrollo

**Implementación**:
```python
// Ejemplo de aserciones en EspañolOO
funcion establecerEdad(edad: entero): nulo {
    afirmar(edad >= 0, "La edad no puede ser negativa")
    // Resto del código
}
```

### Fase 3: Estructuras de Datos Avanzadas (3-4 semanas)

#### Paso 3.1: Arrays y Listas (1 semana)

##### 3.1.1: Arrays (3 días)
- Declaración y uso de arrays
- Arrays multidimensionales
- Recorrido de arrays

**Implementación**:
```python
// Ejemplo de arrays en EspañolOO
numeros: entero[] = [1, 2, 3, 4, 5]
matriz: entero[][] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

// Recorrido de array
para (i: entero = 0; i < numeros.longitud; i = i + 1) {
    imprimir(numeros[i])
}

// Recorrido con bucle para-each
para (num: entero en numeros) {
    imprimir(num)
}
```

##### 3.1.2: Listas (2 días)
- Listas dinámicas
- Métodos para añadir, eliminar y acceder elementos

**Implementación**:
```python
// Ejemplo de listas en EspañolOO
lista: Lista<entero> = nuevo Lista<entero>()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)

imprimir(lista.obtener(1))  // 20
lista.eliminar(1)  // Elimina el elemento en la posición 1

para (num: entero en lista) {
    imprimir(num)
}
```

##### 3.1.3: Iteradores (2 días)
- Interfaces para iteración
- Implementación de iteradores personalizados

**Implementación**:
```python
// Ejemplo de iteradores en EspañolOO
iterador: Iterador<entero> = lista.iterador()
mientras (iterador.tieneSiguiente()) {
    imprimir(iterador.siguiente())
}
```

#### Paso 3.2: Colecciones (1 semana)

##### 3.2.1: Conjuntos (3 días)
- Conjuntos de elementos únicos
- Operaciones de unión, intersección y diferencia

**Implementación**:
```python
// Ejemplo de conjuntos en EspañolOO
conjuntoA: Conjunto<entero> = nuevo Conjunto<entero>()
conjuntoA.agregar(1)
conjuntoA.agregar(2)
conjuntoA.agregar(3)

conjuntoB: Conjunto<entero> = nuevo Conjunto<entero>()
conjuntoB.agregar(3)
conjuntoB.agregar(4)
conjuntoB.agregar(5)

union: Conjunto<entero> = conjuntoA.union(conjuntoB)  // {1, 2, 3, 4, 5}
interseccion: Conjunto<entero> = conjuntoA.interseccion(conjuntoB)  // {3}
diferencia: Conjunto<entero> = conjuntoA.diferencia(conjuntoB)  // {1, 2}
```

##### 3.2.2: Diccionarios (Mapas) (3 días)
- Pares clave-valor
- Búsqueda, inserción y eliminación

**Implementación**:
```python
// Ejemplo de diccionarios en EspañolOO
diccionario: Diccionario<cadena, entero> = nuevo Diccionario<cadena, entero>()
diccionario.agregar("uno", 1)
diccionario.agregar("dos", 2)
diccionario.agregar("tres", 3)

imprimir(diccionario.obtener("dos"))  // 2
diccionario.eliminar("dos")

para (clave: cadena en diccionario.claves()) {
    imprimir(clave + ": " + diccionario.obtener(clave))
}
```

##### 3.2.3: Colas y Pilas (1 día)
- Colas (FIFO)
- Pilas (LIFO)

**Implementación**:
```python
// Ejemplo de colas y pilas en EspañolOO
// Cola
cola: Cola<entero> = nuevo Cola<entero>()
cola.encolar(10)
cola.encolar(20)
cola.encolar(30)

imprimir(cola.desencolar())  // 10
imprimir(cola.desencolar())  // 20

// Pila
pila: Pila<entero> = nuevo Pila<entero>()
pila.apilar(10)
pila.apilar(20)
pila.apilar(30)

imprimir(pila.desapilar())  // 30
imprimir(pila.desapilar())  // 20
```

#### Paso 3.3: Estructuras de Datos Especializadas (1-2 semanas)

##### 3.3.1: Árboles (3 días)
- Árboles binarios
- Recorridos (in-order, pre-order, post-order)

**Implementación**:
```python
// Ejemplo de árboles en EspañolOO
clase NodoArbol {
    publico valor: entero
    publico izquierdo: NodoArbol
    publico derecho: NodoArbol
    
    publico constructor(valor: entero) {
        este.valor = valor
        este.izquierdo = nulo
        este.derecho = nulo
    }
}

clase ArbolBinario {
    privado raiz: NodoArbol
    
    publico constructor() {
        este.raiz = nulo
    }
    
    publico insertar(valor: entero): nulo {
        este.raiz = insertarRecursivo(este.raiz, valor)
    }
    
    privado funcion insertarRecursivo(nodo: NodoArbol, valor: entero): NodoArbol {
        si (nodo == nulo) {
            retornar nuevo NodoArbol(valor)
        }
        
        si (valor < nodo.valor) {
            nodo.izquierdo = insertarRecursivo(nodo.izquierdo, valor)
        } sino si (valor > nodo.valor) {
            nodo.derecho = insertarRecursivo(nodo.derecho, valor)
        }
        
        retornar nodo
    }
    
    publico recorrerInOrder(): nulo {
        recorrerInOrderRecursivo(este.raiz)
    }
    
    privado funcion recorrerInOrderRecursivo(nodo: NodoArbol): nulo {
        si (nodo != nulo) {
            recorrerInOrderRecursivo(nodo.izquierdo)
            imprimir(nodo.valor)
            recorrerInOrderRecursivo(nodo.derecho)
        }
    }
}
```

##### 3.3.2: Grafos (3 días)
- Representación de grafos
- Algoritmos de búsqueda (BFS, DFS)

**Implementación**:
```python
// Ejemplo de grafos en EspañolOO
clase Grafo {
    privado vertices: entero
    privado adyacencia: Lista<entero>[]
    
    publico constructor(vertices: entero) {
        este.vertices = vertices
        este.adyacencia = nuevo Lista<entero>[vertices]
        
        para (i: entero = 0; i < vertices; i = i + 1) {
            este.adyacencia[i] = nuevo Lista<entero>()
        }
    }
    
    publico agregarArista(origen: entero, destino: entero): nulo {
        este.adyacencia[origen].agregar(destino)
    }
    
    publico BFS(inicio: entero): nulo {
        visitado: booleano[] = nuevo booleano[este.vertices]
        cola: Cola<entero> = nuevo Cola<entero>()
        
        visitado[inicio] = verdadero
        cola.encolar(inicio)
        
        mientras (!cola.estaVacia()) {
            actual: entero = cola.desencolar()
            imprimir(actual)
            
            para (vecino: entero en este.adyacencia[actual]) {
                si (!visitado[vecino]) {
                    visitado[vecino] = verdadero
                    cola.encolar(vecino)
                }
            }
        }
    }
}
```

##### 3.3.3: Tablas Hash (3 días)
- Funciones hash
- Manejo de colisiones

**Implementación**:
```python
// Ejemplo de tablas hash en EspañolOO
clase TablaHash<K, V> {
    privado capacidad: entero
    privado tamanio: entero
    privado entradas: Entrada<K, V>[]
    
    clase Entrada<K, V> {
        publico clave: K
        publico valor: V
        publico siguiente: Entrada<K, V>
        
        publico constructor(clave: K, valor: V) {
            este.clave = clave
            este.valor = valor
            este.siguiente = nulo
        }
    }
    
    publico constructor(capacidad: entero) {
        este.capacidad = capacidad
        este.tamanio = 0
        este.entradas = nuevo Entrada[capacidad]
        
        para (i: entero = 0; i < capacidad; i = i + 1) {
            este.entradas[i] = nulo
        }
    }
    
    privado funcion obtenerIndice(clave: K): entero {
        retornar clave.obtenerHashCode() % este.capacidad
    }
    
    publico agregar(clave: K, valor: V): nulo {
        indice: entero = obtenerIndice(clave)
        entrada: Entrada<K, V> = este.entradas[indice]
        
        si (entrada == nulo) {
            este.entradas[indice] = nuevo Entrada<K, V>(clave, valor)
            este.tamanio = este.tamanio + 1
        } sino {
            mientras (entrada.siguiente != nulo) {
                si (entrada.clave.igual(clave)) {
                    entrada.valor = valor
                    retornar
                }
                entrada = entrada.siguiente
            }
            
            si (entrada.clave.igual(clave)) {
                entrada.valor = valor
            } sino {
                entrada.siguiente = nuevo Entrada<K, V>(clave, valor)
                este.tamanio = este.tamanio + 1
            }
        }
    }
    
    publico obtener(clave: K): V {
        indice: entero = obtenerIndice(clave)
        entrada: Entrada<K, V> = este.entradas[indice]
        
        mientras (entrada != nulo) {
            si (entrada.clave.igual(clave)) {
                retornar entrada.valor
            }
            entrada = entrada.siguiente
        }
        
        retornar nulo
    }
}
```

### Fase 4: Desarrollo del Compilador (8-10 semanas)

#### Paso 4.1: Análisis Léxico (2 semanas)

##### 4.1.1: Definición de Tokens (3 días)
- Palabras reservadas
- Identificadores
- Literales
- Operadores
- Delimitadores

**Implementación**:
```python
# Ejemplo de tokens en EspañolOO
PALABRAS_RESERVADAS = [
    'clase', 'funcion', 'si', 'sino', 'mientras', 'para', 'retornar',
    'publico', 'privado', 'protegido', 'nuevo', 'este', 'super',
    'hereda', 'implementa', 'abstracto', 'interfaz', 'intentar',
    'atrapar', 'finalmente', 'lanzar', 'afirmar', 'nulo',
    'verdadero', 'falso', 'entero', 'decimal', 'cadena', 'booleano'
]

OPERADORES = [
    '+', '-', '*', '/', '%', '++', '--',
    '==', '!=', '<', '>', '<=', '>=',
    '&&', '||', '!', '=', '+=', '-=', '*=', '/=', '%=',
    '?:'
]

DELIMITADORES = [
    '(', ')', '{', '}', '[', ']', ';', ',', '.', ':'
]
```

##### 4.1.2: Implementación del Analizador Léxico (7 días)
- Uso de PLY (Python Lex-Yacc)
- Reconocimiento de tokens
- Manejo de errores léxicos

**Implementación**:
```python
# Ejemplo de analizador léxico con PLY
import ply.lex as lex

tokens = [
    'PALABRA_RESERVADA', 'IDENTIFICADOR', 'ENTERO', 'DECIMAL', 'CADENA',
    'BOOLEANO', 'OPERADOR', 'DELIMITADOR', 'COMENTARIO'
]

t_OPERADOR = r'\+|\-|\*|\/|%|\+\+|\-\-|==|!=|<|>|<=|>=|&&|\|\||!|=|\+=|\-=|\*=|\/=|%=|\?:'
t_DELIMITADOR = r'\(|\)|\{|\}|\[|\]|;|,|\.|:'

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_CADENA(t):
    r'\".*?\"'
    t.value = str(t.value[1:-1])  # Eliminar las comillas
    return t

def t_BOOLEANO(t):
    r'verdadero|falso'
    t.value = True if t.value == 'verdadero' else False
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in PALABRAS_RESERVADAS:
        t.type = 'PALABRA_RESERVADA'
    return t

def t_COMENTARIO(t):
    r'//.*|/\*(.|\n)*?\*/'
    pass  # Ignorar comentarios

t_ignore = ' \t\n'  # Ignorar espacios, tabulaciones y saltos de línea

def t_error(t):
    print(f"Carácter ilegal: '{t.value[0]}' en la línea {t.lexer.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()
```

##### 4.1.4: Pruebas del Analizador Léxico (4 días)
- Casos de prueba para tokens válidos
- Casos de prueba para manejo de errores

#### Paso 4.2: Análisis Sintáctico (2 semanas)

##### 4.2.1: Definición de la Gramática (3 días)
- Gramática libre de contexto
- Notación BNF (Backus-Naur Form)
- Precedencia y asociatividad de operadores

**Implementación**:
```python
# Ejemplo de gramática en EspañolOO
programa : declaraciones_lista
         ;

declaraciones_lista : declaracion
                   | declaraciones_lista declaracion
                   ;

declaracion : declaracion_clase
            | declaracion_funcion
            | declaracion_variable
            ;

declaracion_clase : 'clase' IDENTIFICADOR ('hereda' IDENTIFICADOR)? '{' miembros_clase '}'
                 ;

miembros_clase : miembro_clase
               | miembros_clase miembro_clase
               ;

miembro_clase : declaracion_funcion
              | declaracion_variable
              ;

declaracion_funcion : ('publico' | 'privado' | 'protegido')? 'funcion' IDENTIFICADOR '(' parametros_lista? ')' ':' tipo_retorno '{' cuerpo '}'
                   ;

parametros_lista : parametro
                 | parametros_lista ',' parametro
                 ;

parametro : IDENTIFICADOR ':' tipo
          ;

tipo_retorno : tipo
             | 'nulo'
             ;

tipo : IDENTIFICADOR
     ;

cuerpo : sentencias_lista
       ;

sentencias_lista : sentencia
                | sentencias_lista sentencia
                ;

sentencia : sentencia_expresion
          | sentencia_si
          | sentencia_mientras
          | sentencia_para
          | sentencia_retornar
          | sentencia_imprimir
          | sentencia_leer
          | bloque
          ;

bloque : '{' sentencias_lista? '}'
       ;

sentencia_si : 'si' '(' expresion ')' bloque ('sino' bloque)?
            ;

sentencia_mientras : 'mientras' '(' expresion ')' bloque
                  ;

sentencia_para : 'para' '(' asignacion? ';' expresion? ';' asignacion? ')' bloque
              ;

sentencia_retornar : 'retornar' expresion? ';'
                  ;

sentencia_imprimir : 'imprimir' '(' expresion ')' ';'
                  ;

sentencia_leer : 'leer' '(' IDENTIFICADOR ')' ';'
              ;

sentencia_expresion : expresion ';'
                    ;

expresion : expresion_asignacion
          ;

expresion_asignacion : IDENTIFICADOR '=' expresion_asignacion
                     | IDENTIFICADOR '+=' expresion_asignacion
                     | IDENTIFICADOR '-=' expresion_asignacion
                     | IDENTIFICADOR '*=' expresion_asignacion
                     | IDENTIFICADOR '/=' expresion_asignacion
                     | IDENTIFICADOR '%=' expresion_asignacion
                     | expresion_condicional
                     ;

expresion_condicional : expresion_logica '?' expresion ':' expresion_condicional
                     | expresion_logica
                     ;

expresion_logica : expresion_logica '&&' expresion_igualdad
                 | expresion_logica '||' expresion_igualdad
                 | '!' expresion_logica
                 | expresion_igualdad
                 ;

expresion_igualdad : expresion_igualdad '==' expresion_relacional
                   | expresion_igualdad '!=' expresion_relacional
                   | expresion_relacional
                   ;

expresion_relacional : expresion_relacional '<' expresion_aditiva
                     | expresion_relacional '>' expresion_aditiva
                     | expresion_relacional '<=' expresion_aditiva
                     | expresion_relacional '>=' expresion_aditiva
                     | expresion_aditiva
                     ;

expresion_aditiva : expresion_aditiva '+' expresion_multiplicativa
                  | expresion_aditiva '-' expresion_multiplicativa
                  | expresion_multiplicativa
                  ;

expresion_multiplicativa : expresion_multiplicativa '*' expresion_unaria
                         | expresion_multiplicativa '/' expresion_unaria
                         | expresion_multiplicativa '%' expresion_unaria
                         | expresion_unaria
                         ;

expresion_unaria : '-' expresion_unaria
                 | '!' expresion_unaria
                 | '++' IDENTIFICADOR
                 | '--' IDENTIFICADOR
                 | IDENTIFICADOR '++'
                 | IDENTIFICADOR '--'
                 | expresion_primaria
                 ;

expresion_primaria : IDENTIFICADOR
                   | ENTERO
                   | DECIMAL
                   | CADENA
                   | BOOLEANO
                   | 'nulo'
                   | '(' expresion ')'
                   | IDENTIFICADOR '(' argumentos_lista? ')'
                   | 'nuevo' IDENTIFICADOR '(' argumentos_lista? ')'
                   | 'este' '.' IDENTIFICADOR
                   | 'super' '.' IDENTIFICADOR
                   ;

argumentos_lista : expresion
                 | argumentos_lista ',' expresion
                 ;

declaracion_variable : IDENTIFICADOR ':' tipo ('=' expresion)? ';'
                    ;
```

##### 4.2.2: Implementación del Analizador Sintáctico (7 días)
- Uso de PLY (Python Lex-Yacc)
- Construcción del Árbol de Sintaxis Abstracta (AST)
- Manejo de errores sintácticos

**Implementación**:
```python
# Ejemplo de analizador sintáctico con PLY
import ply.yacc as yacc

# Definición de la precedencia de operadores
precedence = (
    ('left', '&&', '||'),
    ('left', '==', '!='),
    ('left', '<', '>', '<=', '>='),
    ('left', '+', '-'),
    ('left', '*', '/', '%'),
    ('right', '!', 'UMINUS'),
    ('right', '?:')
)

# Definición de la gramática
def p_programa(p):
    'programa : declaraciones_lista'
    p[0] = Programa(p[1])

def p_declaraciones_lista(p):
    '''declaraciones_lista : declaracion
                          | declaraciones_lista declaracion'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_declaracion_clase(p):
    '''declaracion : declaracion_clase'''
    p[0] = p[1]

def p_declaracion_clase_completa(p):
    '''declaracion_clase : 'clase' IDENTIFICADOR '{' miembros_clase '}'
                         | 'clase' IDENTIFICADOR 'hereda' IDENTIFICADOR '{' miembros_clase '}' '''
    if len(p) == 6:
        p[0] = DeclaracionClase(p[2], None, p[4])
    else:
        p[0] = DeclaracionClase(p[2], p[4], p[6])

# ... más reglas gramaticales ...

def p_error(p):
    if p:
        print(f"Error de sintaxis en '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis: fin de archivo inesperado")

parser = yacc.yacc()
```

##### 4.2.3: Definición del AST (Árbol de Sintaxis Abstracta) (4 días)
- Clases para representar nodos del AST
- Jerarquía de nodos

**Implementación**:
```python
# Ejemplo de clases para el AST
class AST:
    pass

class Programa(AST):
    def __init__(self, declaraciones):
        self.declaraciones = declaraciones

class Declaracion(AST):
    pass

class DeclaracionClase(Declaracion):
    def __init__(self, nombre, hereda_de, miembros):
        self.nombre = nombre
        self.hereda_de = hereda_de
        self.miembros = miembros

class DeclaracionFuncion(Declaracion):
    def __init__(self, nombre, parametros, tipo_retorno, cuerpo):
        self.nombre = nombre
        self.parametros = parametros
        self.tipo_retorno = tipo_retorno
        self.cuerpo = cuerpo

class DeclaracionVariable(Declaracion):
    def __init__(self, nombre, tipo, valor):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor

class Sentencia(AST):
    pass

class SentenciaSi(Sentencia):
    def __init__(self, condicion, entonces, sino):
        self.condicion = condicion
        self.entonces = entonces
        self.sino = sino

class SentenciaMientras(Sentencia):
    def __init__(self, condicion, cuerpo):
        self.condicion = condicion
        self.cuerpo = cuerpo

# ... más clases para el AST ...
```

##### 4.2.4: Pruebas del Analizador Sintáctico (4 días)
- Casos de prueba para construcciones válidas
- Casos de prueba para manejo de errores

#### Paso 4.3: Análisis Semántico (2 semanas)

##### 4.3.1: Tabla de Símbolos (3 días)
- Implementación de la tabla de símbolos
- Manejo de ámbitos (scopes)
- Búsqueda e inserción de símbolos

**Implementación**:
```python
# Ejemplo de tabla de símbolos
class TablaSimbolos:
    def __init__(self, padre=None):
        self.simbolos = {}
        self.padre = padre
    
    def agregar(self, nombre, tipo, valor=None):
        if nombre in self.simbolos:
            raise Exception(f"El símbolo '{nombre}' ya está definido en este ámbito")
        self.simbolos[nombre] = {'tipo': tipo, 'valor': valor}
    
    def obtener(self, nombre):
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        elif self.padre:
            return self.padre.obtener(nombre)
        else:
            return None
    
    def existe(self, nombre):
        return self.obtener(nombre) is not None
    
    def obtener_tipo(self, nombre):
        simbolo = self.obtener(nombre)
        if simbolo:
            return simbolo['tipo']
        return None
```

##### 4.3.2: Verificación de Tipos (7 días)
- Comprobación de tipos en expresiones
- Comprobación de tipos en asignaciones
- Comprobación de tipos en llamadas a funciones

**Implementación**:
```python
# Ejemplo de verificador de tipos
class VerificadorTipos:
    def __init__(self, tabla_simbolos):
        self.tabla_simbolos = tabla_simbolos
        self.errores = []
    
    def verificar(self, nodo):
        metodo = 'verificar_' + nodo.__class__.__name__.lower()
        verificador = getattr(self, metodo, self.verificador_generico)
        return verificador(nodo)
    
    def verificar_programa(self, nodo):
        for declaracion in nodo.declaraciones:
            self.verificar(declaracion)
    
    def verificar_declaracionvariable(self, nodo):
        if nodo.valor:
            tipo_valor = self.verificar(nodo.valor)
            if tipo_valor != nodo.tipo:
                self.errores.append(f"Error de tipo: no se puede asignar {tipo_valor} a una variable de tipo {nodo.tipo}")
        self.tabla_simbolos.agregar(nodo.nombre, nodo.tipo)
    
    def verificar_expresionbinaria(self, nodo):
        tipo_izquierda = self.verificar(nodo.izquierda)
        tipo_derecha = self.verificar(nodo.derecha)
        
        if nodo.operador in ['+', '-', '*', '/', '%']:
            if tipo_izquierda in ['entero', 'decimal'] and tipo_derecha in ['entero', 'decimal']:
                return 'decimal' if 'decimal' in [tipo_izquierda, tipo_derecha] else 'entero'
            else:
                self.errores.append(f"Error de tipo: operador '{nodo.operador}' no aplicable a {tipo_izquierda} y {tipo_derecha}")
                return 'error'
        elif nodo.operador in ['==', '!=', '<', '>', '<=', '>=']:
            if tipo_izquierda == tipo_derecha:
                return 'booleano'
            else:
                self.errores.append(f"Error de tipo: no se pueden comparar {tipo_izquierda} y {tipo_derecha}")
                return 'error'
        elif nodo.operador in ['&&', '||']:
            if tipo_izquierda == 'booleano' and tipo_derecha == 'booleano':
                return 'booleano'
            else:
                self.errores.append(f"Error de tipo: operador '{nodo.operador}' requiere operandos booleanos")
                return 'error'
        
        return 'error'
    
    # ... más métodos de verificación ...
```

##### 4.3.3: Verificación Semántica (4 días)
- Comprobación de declaraciones previas
- Comprobación de retornos en funciones
- Comprobación de clases abstractas

**Implementación**:
```python
# Ejemplo de verificador semántico
class VerificadorSemantico:
    def __init__(self):
        self.tabla_simbolos = TablaSimbolos()
        self.verificador_tipos = VerificadorTipos(self.tabla_simbolos)
        self.errores = []
    
    def verificar(self, nodo):
        metodo = 'verificar_' + nodo.__class__.__name__.lower()
        verificador = getattr(self, metodo, self.verificador_generico)
        return verificador(nodo)
    
    def verificar_programa(self, nodo):
        for declaracion in nodo.declaraciones:
            self.verificar(declaracion)
        
        if self.verificador_tipos.errores:
            self.errores.extend(self.verificador_tipos.errores)
    
    def verificar_declaracionfuncion(self, nodo):
        # Crear un nuevo ámbito para la función
        ambito_anterior = self.tabla_simbolos
        self.tabla_simbolos = TablaSimbolos(ambito_anterior)
        
        # Agregar los parámetros a la tabla de símbolos
        for parametro in nodo.parametros:
            self.tabla_simbolos.agregar(parametro.nombre, parametro.tipo)
        
        # Verificar el cuerpo de la función
        self.verificar(nodo.cuerpo)
        
        # Restaurar el ámbito anterior
        self.tabla_simbolos = ambito_anterior
        
        # Agregar la función a la tabla de símbolos
        self.tabla_simbolos.agregar(nodo.nombre, 'funcion', {
            'parametros': nodo.parametros,
            'tipo_retorno': nodo.tipo_retorno
        })
    
    def verificar_sentenciaretornar(self, nodo):
        # Verificar que el retorno esté dentro de una función
        if not self.en_funcion:
            self.errores.append("Error semántico: retorno fuera de una función")
            return
        
        # Verificar el tipo del valor de retorno
        if nodo.valor:
            tipo_valor = self.verificar(nodo.valor)
            # Aquí debería verificarse que tipo_valor coincida con el tipo de retorno de la función
            # Esto requeriría mantener información sobre la función actual
    
    # ... más métodos de verificación ...
```

##### 4.3.4: Pruebas del Analizador Semántico (4 días)
- Casos de prueba para verificación de tipos
- Casos de prueba para verificación semántica
- Casos de prueba para manejo de errores

#### Paso 4.4: Generación de Código (2-3 semanas)

##### 4.4.1: Diseño del Generador de Código (3 días)
- Estrategia de generación de código
- Selección del lenguaje objetivo (Python)
- Patrones de traducción

**Implementación**:
```python
# Ejemplo de generador de código
class GeneradorCodigo:
    def __init__(self):
        self.codigo = []
        self.indentacion = 0
    
    def generar(self, nodo):
        metodo = 'generar_' + nodo.__class__.__name__.lower()
        generador = getattr(self, metodo, self.generador_generico)
        return generador(nodo)
    
    def agregar_linea(self, linea):
        self.codigo.append('    ' * self.indentacion + linea)
    
    def generar_programa(self, nodo):
        # Generar imports necesarios
        self.agregar_linea("# Código generado por el compilador de EspañolOO")
        self.agregar_linea("import sys")
        self.agregar_linea("")
        
        # Generar las declaraciones
        for declaracion in nodo.declaraciones:
            self.generar(declaracion)
        
        return '\n'.join(self.codigo)
    
    def generar_declaracionclase(self, nodo):
        herencia = f"({nodo.hereda_de})" if nodo.hereda_de else ""
        self.agregar_linea(f"class {nodo.nombre}{herencia}:")
        self.indentacion += 1
        
        # Generar los miembros de la clase
        for miembro in nodo.miembros:
            self.generar(miembro)
        
        self.indentacion -= 1
        self.agregar_linea("")
    
    def generar_declaracionfuncion(self, nodo):
        parametros = ', '.join([f"{p.nombre}" for p in nodo.parametros])
        self.agregar_linea(f"def {nodo.nombre}({parametros}):")
        self.indentacion += 1
        
        # Generar el cuerpo de la función
        self.generar(nodo.cuerpo)
        
        self.indentacion -= 1
        self.agregar_linea("")
    
    # ... más métodos de generación ...
```

##### 4.4.2: Implementación del Generador de Código (10 días)
- Traducción de construcciones de EspañolOO a Python
- Manejo de tipos de datos
- Generación de código para clases y objetos

**Implementación**:
```python
# Ejemplo de implementación del generador de código
class GeneradorCodigo:
    # ... métodos anteriores ...
    
    def generar_sentenciaimprimir(self, nodo):
        expresion = self.generar(nodo.expresion)
        self.agregar_linea(f"print({expresion})")
    
    def generar_sentenciasi(self, nodo):
        condicion = self.generar(nodo.condicion)
        self.agregar_linea(f"if {condicion}:")
        self.indentacion += 1
        self.generar(nodo.entonces)
        self.indentacion -= 1
        
        if nodo.sino:
            self.agregar_linea("else:")
            self.indentacion += 1
            self.generar(nodo.sino)
            self.indentacion -= 1
    
    def generar_sentenciamientras(self, nodo):
        condicion = self.generar(nodo.condicion)
        self.agregar_linea(f"while {condicion}:")
        self.indentacion += 1
        self.generar(nodo.cuerpo)
        self.indentacion -= 1
    
    def generar_sentenciapara(self, nodo):
        inicializacion = self.generar(nodo.inicializacion) if nodo.inicializacion else ""
        condicion = self.generar(nodo.condicion) if nodo.condicion else "True"
        actualizacion = self.generar(nodo.actualizacion) if nodo.actualizacion else ""
        
        self.agregar_linea(f"for {inicializacion}; {condicion}; {actualizacion}:")
        self.indentacion += 1
        self.generar(nodo.cuerpo)
        self.indentacion -= 1
    
    def generar_expresionbinaria(self, nodo):
        izquierda = self.generar(nodo.izquierda)
        derecha = self.generar(nodo.derecha)
        
        # Mapeo de operadores de EspañolOO a Python
        operadores = {
            '+': '+', '-': '-', '*': '*', '/': '/', '%': '%',
            '==': '==', '!=': '!=', '<': '<', '>': '>', '<=': '<=', '>=': '>=',
            '&&': 'and', '||': 'or'
        }
        
        operador = operadores.get(nodo.operador, nodo.operador)
        return f"({izquierda} {operador} {derecha})"
    
    def generar_expresionunaria(self, nodo):
        operando = self.generar(nodo.operando)
        
        if nodo.operador == '-':
            return f"-({operando})"
        elif nodo.operador == '!':
            return f"not ({operando})"
        elif nodo.operador == '++':
            return f"{operando} + 1"
        elif nodo.operador == '--':
            return f"{operando} - 1"
        
        return operando
    
    def generar_expresionliteral(self, nodo):
        if isinstance(nodo.valor, str):
            return f'"{nodo.valor}"'
        elif isinstance(nodo.valor, bool):
            return str(nodo.valor).lower()
        elif nodo.valor is None:
            return "None"
        else:
            return str(nodo.valor)
    
    def generar_expresionidentificador(self, nodo):
        return nodo.nombre
    
    def generar_expresionllamadafuncion(self, nodo):
        argumentos = ', '.join([self.generar(arg) for arg in nodo.argumentos])
        return f"{nodo.nombre}({argumentos})"
    
    # ... más métodos de generación ...
```

##### 4.4.3: Optimizaciones Básicas (4 días)
- Eliminación de código muerto
- Simplificación de expresiones
- Plegado de constantes

**Implementación**:
```python
# Ejemplo de optimizador básico
class Optimizador:
    def __init__(self):
        self.optimizaciones = 0
    
    def optimizar(self, nodo):
        metodo = 'optimizar_' + nodo.__class__.__name__.lower()
        optimizador = getattr(self, metodo, self.optimizador_generico)
        return optimizador(nodo)
    
    def optimizar_expresionbinaria(self, nodo):
        nodo.izquierda = self.optimizar(nodo.izquierda)
        nodo.derecha = self.optimizar(nodo.derecha)
        
        # Plegado de constantes
        if isinstance(nodo.izquierda, ExpresionLiteral) and isinstance(nodo.derecha, ExpresionLiteral):
            izquierda = nodo.izquierda.valor
            derecha = nodo.derecha.valor
            
            if nodo.operador == '+':
                return ExpresionLiteral(izquierda + derecha)
            elif nodo.operador == '-':
                return ExpresionLiteral(izquierda - derecha)
            elif nodo.operador == '*':
                return ExpresionLiteral(izquierda * derecha)
            elif nodo.operador == '/':
                if derecha != 0:
                    return ExpresionLiteral(izquierda / derecha)
            elif nodo.operador == '%':
                if derecha != 0:
                    return ExpresionLiteral(izquierda % derecha)
            elif nodo.operador == '==':
                return ExpresionLiteral(izquierda == derecha)
            elif nodo.operador == '!=':
                return ExpresionLiteral(izquierda != derecha)
            elif nodo.operador == '<':
                return ExpresionLiteral(izquierda < derecha)
            elif nodo.operador == '>':
                return ExpresionLiteral(izquierda > derecha)
            elif nodo.operador == '<=':
                return ExpresionLiteral(izquierda <= derecha)
            elif nodo.operador == '>=':
                return ExpresionLiteral(izquierda >= derecha)
            elif nodo.operador == '&&':
                return ExpresionLiteral(izquierda and derecha)
            elif nodo.operador == '||':
                return ExpresionLiteral(izquierda or derecha)
            
            self.optimizaciones += 1
        
        return nodo
    
    def optimizar_sentenciasi(self, nodo):
        nodo.condicion = self.optimizar(nodo.condicion)
        nodo.entonces = self.optimizar(nodo.entonces)
        
        if nodo.sino:
            nodo.sino = self.optimizar(nodo.sino)
        
        # Eliminación de código muerto
        if isinstance(nodo.condicion, ExpresionLiteral):
            if nodo.condicion.valor:
                return nodo.entonces  # Si la condición es verdadera, solo ejecutar el entonces
            else:
                return nodo.sino if nodo.sino else None  # Si la condición es falsa, ejecutar el sino si existe
        
        return nodo
    
    # ... más métodos de optimización ...
```

##### 4.4.4: Pruebas del Generador de Código (4 días)
- Casos de prueba para generación de código
- Casos de prueba para optimizaciones
- Verificación del código generado

#### Paso 4.5: Integración y Pruebas Finales (1 semana)

##### 4.5.1: Integración de Componentes (2 días)
- Integración del analizador léxico, sintáctico, semántico y generador de código
- Creación del ejecutable principal

**Implementación**:
```python
# Ejemplo de integración de componentes
import sys
import argparse

from lexer import EspanolOOLexer
from parser import EspanolOOParser
from ast import *
from semantic import VerificadorSemantico
from codegen import GeneradorCodigo
from optimizer import Optimizador

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Compilador de EspañolOO')
    parser.add_argument('archivo', help='Archivo de entrada (.eoo)')
    parser.add_argument('-o', '--output', help='Archivo de salida (.py)', default=None)
    parser.add_argument('--optimizar', action='store_true', help='Aplicar optimizaciones')
    args = parser.parse_args()
    
    # Determinar el archivo de salida
    if args.output is None:
        args.output = args.archivo.replace('.eoo', '.py')
    
    try:
        # Leer el archivo de entrada
        with open(args.archivo, 'r', encoding='utf-8') as f:
            codigo_fuente = f.read()
        
        # Análisis léxico
        lexer = EspanolOOLexer()
        tokens = lexer.tokenize(codigo_fuente)
        
        # Análisis sintáctico
        parser = EspanolOOParser()
        ast = parser.parse(tokens)
        
        # Análisis semántico
        verificador = VerificadorSemantico()
        verificador.verificar(ast)
        
        if verificador.errores:
            print("Errores semánticos:")
            for error in verificador.errores:
                print(f"  - {error}")
            sys.exit(1)
        
        # Optimización (opcional)
        if args.optimizar:
            optimizador = Optimizador()
            ast = optimizador.optimizar(ast)
            print(f"Se aplicaron {optimizador.optimizaciones} optimizaciones")
        
        # Generación de código
        generador = GeneradorCodigo()
        codigo_generado = generador.generar(ast)
        
        # Escribir el archivo de salida
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(codigo_generado)
        
        print(f"Compilación exitosa. Código generado en '{args.output}'")
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{args.archivo}'")
        sys.exit(1)
    except Exception as e:
        print(f"Error durante la compilación: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

##### 4.5.2: Pruebas de Integración (3 días)
- Casos de prueba completos
- Verificación del flujo de compilación
- Pruebas de rendimiento

##### 4.5.3: Documentación Final (2 días)
- Documentación del lenguaje
- Guía de uso del compilador
- Ejemplos de código

### Fase 5: Herramientas de Desarrollo (2-3 semanas)

#### Paso 5.1: Entorno de Desarrollo Integrado (IDE) (1 semana)

##### 5.1.1: Resaltado de Sintaxis (2 días)
- Definición de reglas de resaltado
- Integración con editores de texto (VS Code, Sublime Text)

**Implementación**:
```json
// Ejemplo de definición de resaltado de sintaxis para VS Code
{
  "information_for_contributors": [
    "This file has been converted from https://github.com/atom/language-python/blob/master/grammars/python.cson",
    "If you want to provide a fix or improvement, please create a pull request against the original repository.",
    "Once accepted there, we are happy to receive an update request."
  ],
  "version": "https://github.com/atom/language-python/commit/699c7f1e0c7a0f9c8597e4ce5f0f0d4c9f7f7f7f",
  "name": "EspañolOO",
  "scopeName": "source.espanoloo",
  "patterns": [
    {
      "include": "#imports"
    },
    {
      "include": "#function-declarations"
    },
    {
      "include": "#class-declarations"
    },
    {
      "include": "#keywords"
    },
    {
      "include": "#strings"
    },
    {
      "include": "#numbers"
    },
    {
      "include": "#comments"
    }
  ],
  "repository": {
    "keywords": {
      "patterns": [
        {
          "name": "keyword.control.espanoloo",
          "match": "\\b(clase|funcion|si|sino|mientras|para|retornar|publico|privado|protegido|nuevo|este|super|hereda|implementa|abstracto|interfaz|intentar|atrapar|finalmente|lanzar|afirmar|nulo|verdadero|falso|entero|decimal|cadena|booleano)\\b"
        },
        {
          "name": "keyword.operator.espanoloo",
          "match": "\\b(y|o|no)\\b"
        }
      ]
    },
    "strings": {
      "patterns": [
        {
          "name": "string.quoted.double.espanoloo",
          "begin": "\"",
          "end": "\"",
          "patterns": [
            {
              "name": "constant.character.escape.espanoloo",
              "match": "\\\\."
            }
          ]
        },
        {
          "name": "string.quoted.single.espanoloo",
          "begin": "'",
          "end": "'",
          "patterns": [
            {
              "name": "constant.character.escape.espanoloo",
              "match": "\\\\."
            }
          ]
        }
      ]
    },
    "numbers": {
      "patterns": [
        {
          "name": "constant.numeric.espanoloo",
          "match": "\\b([0-9]+(\\.[0-9]+)?|\\.[0-9]+)([eE][+-]?[0-9]+)?\\b"
        }
      ]
    },
    "comments": {
      "patterns": [
        {
          "name": "comment.line.double-slash.espanoloo",
          "begin": "//",
          "end": "$"
        },
        {
          "name": "comment.block.espanoloo",
          "begin": "/\\*",
          "end": "\\*/"
        }
      ]
    },
    "function-declarations": {
      "patterns": [
        {
          "name": "entity.name.function.espanoloo",
          "match": "\\b(funcion)\\s+([a-zA-Z_][a-zA-Z0-9_]*)\\s*\\(",
          "captures": {
            "1": { "name": "keyword.control.espanoloo" },
            "2": { "name": "entity.name.function.espanoloo" }
          }
        }
      ]
    },
    "class-declarations": {
      "patterns": [
        {
          "name": "entity.name.type.class.espanoloo",
          "match": "\\b(clase)\\s+([a-zA-Z_][a-zA-Z0-9_]*)",
          "captures": {
            "1": { "name": "keyword.control.espanoloo" },
            "2": { "name": "entity.name.type.class.espanoloo" }
          }
        }
      ]
    },
    "imports": {
      "patterns": [
        {
          "name": "keyword.control.import.espanoloo",
          "match": "\\b(importar|desde)\\b"
        }
      ]
    }
  }
}
```

##### 5.1.2: Autocompletado (2 días)
- Lista de palabras reservadas
- Sugerencias basadas en contexto

##### 5.1.3: Depuración (3 días)
- Integración con depuradores de Python
- Visualización de variables en EspañolOO

#### Paso 5.2: Herramientas de Línea de Comandos (1 semana)

##### 5.2.1: Compilador de Línea de Comandos (3 días)
- Opciones de compilación
- Mensajes de error en español

**Implementación**:
```bash
# Ejemplo de uso del compilador desde la línea de comandos
# Compilar un archivo
python espanoloo_compiler.py programa.eoo

# Especificar archivo de salida
python espanoloo_compiler.py programa.eoo -o programa.py

# Aplicar optimizaciones
python espanoloo_compiler.py programa.eoo --optimizar

# Mostrar ayuda
python espanoloo_compiler.py --help
```

##### 5.2.2: Intérprete Interactivo (REPL) (4 días)
- Ejecución interactiva de código
- Historial de comandos

**Implementación**:
```python
# Ejemplo de intérprete interactivo
import sys
from lexer import EspanolOOLexer
from parser import EspanolOOParser
from semantic import VerificadorSemantico
from codegen import GeneradorCodigo
import code

def repl():
    print("EspañolOO Intérprete Interactivo v1.0")
    print("Escriba 'salir' para salir")
    
    # Inicializar componentes del compilador
    lexer = EspanolOOLexer()
    parser = EspanolOOParser()
    verificador = VerificadorSemantico()
    generador = GeneradorCodigo()
    
    # Crear un contexto para ejecutar el código
    contexto = {}
    
    while True:
        try:
            # Leer entrada del usuario
            entrada = input(">>> ")
            
            # Comando para salir
            if entrada.lower() in ['salir', 'exit', 'quit']:
                break
            
            # Si la entrada está vacía, continuar
            if not entrada.strip():
                continue
            
            # Compilar y ejecutar la entrada
            tokens = lexer.tokenize(entrada)
            ast = parser.parse(tokens)
            verificador.verificar(ast)
            codigo_generado = generador.generar(ast)
            
            # Ejecutar el código generado
            exec(codigo_generado, contexto)
            
        except KeyboardInterrupt:
            print("\nInterrumpido por el usuario")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == '__main__':
    repl()
```

#### Paso 5.3: Pruebas y Documentación (1 semana)

##### 5.3.1: Suite de Pruebas Automatizadas (3 días)
- Pruebas unitarias para el compilador
- Pruebas de integración
- Pruebas de regresión

**Implementación**:
```python
# Ejemplo de pruebas automatizadas
import unittest
import os
import tempfile
from subprocess import call

class TestCompilador(unittest.TestCase):
    def setUp(self):
        self.compilador = "python espanoloo_compiler.py"
    
    def compilar_y_ejecutar(self, codigo):
        # Crear archivos temporales
        with tempfile.NamedTemporaryFile(mode='w', suffix='.eoo', delete=False) as f_eoo:
            f_eoo.write(codigo)
            archivo_eoo = f_eoo.name
        
        archivo_py = archivo_eoo.replace('.eoo', '.py')
        
        try:
            # Compilar
            call([self.compilador, archivo_eoo], shell=True)
            
            # Ejecutar y capturar la salida
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f_salida:
                archivo_salida = f_salida.name
            
            call([sys.executable, archivo_py, '>', archivo_salida], shell=True)
            
            with open(archivo_salida, 'r') as f:
                salida = f.read()
            
            return salida
        
        finally:
            # Limpiar archivos temporales
            if os.path.exists(archivo_eoo):
                os.unlink(archivo_eoo)
            if os.path.exists(archivo_py):
                os.unlink(archivo_py)
            if os.path.exists(archivo_salida):
                os.unlink(archivo_salida)
    
    def test_hola_mundo(self):
        codigo = '''
        funcion principal() {
            imprimir("Hola, Mundo!")
        }
        '''
        salida = self.compilar_y_ejecutar(codigo)
        self.assertIn("Hola, Mundo!", salida)
    
    def test_operaciones_aritmeticas(self):
        codigo = '''
        funcion principal() {
            a: entero = 10
            b: entero = 5
            imprimir(a + b)
            imprimir(a - b)
            imprimir(a * b)
            imprimir(a / b)
        }
        '''
        salida = self.compilar_y_ejecutar(codigo)
        self.assertIn("15", salida)
        self.assertIn("5", salida)
        self.assertIn("50", salida)
        self.assertIn("2", salida)
    
    def test_condicionales(self):
        codigo = '''
        funcion principal() {
            x: entero = 10
            si (x > 5) {
                imprimir("Mayor que 5")
            } sino {
                imprimir("Menor o igual que 5")
            }
        }
        '''
        salida = self.compilar_y_ejecutar(codigo)
        self.assertIn("Mayor que 5", salida)
    
    def test_bucles(self):
        codigo = '''
        funcion principal() {
            para (i: entero = 0; i < 5; i = i + 1) {
                imprimir(i)
            }
        }
        '''
        salida = self.compilar_y_ejecutar(codigo)
        self.assertIn("0", salida)
        self.assertIn("1", salida)
        self.assertIn("2", salida)
        self.assertIn("3", salida)
        self.assertIn("4", salida)
    
    def test_clases_y_objetos(self):
        codigo = '''
        clase Persona {
            privado nombre: cadena
            
            publico constructor(nombre: cadena) {
                este.nombre = nombre
            }
            
            publico saludar() {
                imprimir("Hola, soy " + este.nombre)
            }
        }
        
        funcion principal() {
            p: Persona = nuevo Persona("Juan")
            p.saludar()
        }
        '''
        salida = self.compilar_y_ejecutar(codigo)
        self.assertIn("Hola, soy Juan", salida)

if __name__ == '__main__':
    unittest.main()
```

##### 5.3.2: Documentación del Lenguaje (4 días)
- Manual de referencia
- Tutoriales y ejemplos
- Guía de estilo

### Fase 6: Lanzamiento y Mantenimiento (continuo)

#### Paso 6.1: Preparación para el Lanzamiento (1 semana)

##### 6.1.1: Empaquetado y Distribución (3 días)
- Creación de paquetes para diferentes sistemas operativos
- Publicación en repositorios (PyPI, GitHub Releases)

##### 6.1.2: Sitio Web y Documentación (4 días)
- Creación de un sitio web para el proyecto
- Publicación de la documentación

#### Paso 6.2: Comunidad y Contribuciones (continuo)

##### 6.2.1: Gestión de Contribuciones (continuo)
- Establecimiento de directrices para contribuciones
- Revisión de pull requests

##### 6.2.2: Soporte a la Comunidad (continuo)
- Foros de discusión
- Respuesta a preguntas y problemas

#### Paso 6.3: Mejoras Continuas (continuo)

##### 6.3.1: Recopilación de Feedback (continuo)
- Encuestas a usuarios
- Análisis de uso

##### 6.3.2: Planificación de Futuras Versiones (continuo)
- Definición de roadmap
- Priorización de funcionalidades

## Cronograma Resumido

| Fase | Descripción | Duración Estimada |
|------|-------------|-------------------|
| Fase 1 | Fundamentos del Lenguaje | 4-6 semanas |
| Fase 2 | Programación Orientada a Objetos | 6-8 semanas |
| Fase 3 | Estructuras de Datos Avanzadas | 3-4 semanas |
| Fase 4 | Desarrollo del Compilador | 8-10 semanas |
| Fase 5 | Herramientas de Desarrollo | 2-3 semanas |
| Fase 6 | Lanzamiento y Mantenimiento | Continuo |

**Total estimado**: 23-31 semanas (aproximadamente 6-8 meses)

## Recursos Necesarios

### Humanos
- 1-2 desarrolladores principales con experiencia en compiladores y Python
- 1 diseñador UX/UI para las herramientas
- 1 redactor técnico para la documentación

### Técnicos
- Python 3.10+
- Librería PLY (Python Lex-Yacc)
- Sistema de control de versiones (Git)
- Entorno de desarrollo integrado (VS Code, PyCharm)
- Herramientas de pruebas automatizadas (unittest, pytest)

### Infraestructura
- Repositorio de código (GitHub, GitLab)
- Sistema de integración continua (GitHub Actions, Travis CI)
- Sitio web para la documentación y descargas
- Foros de discusión (Discord, GitHub Discussions)

## Conclusiones

El desarrollo del lenguaje de programación orientada a objetos "EspañolOO" es un proyecto ambicioso pero factible que busca proporcionar una alternativa natural y robusta para la programación en español. Inspirado en lenguajes como Latino pero con un enfoque más completo en la programación orientada a objetos, EspañolOO tiene el potencial de convertirse en una herramienta valiosa para la enseñanza y el desarrollo de software en el mundo hispanohablante.

El plan de desarrollo presentado abarca desde la definición de los fundamentos del lenguaje hasta la creación de herramientas de desarrollo y el lanzamiento del proyecto. Con una duración estimada de 6-8 meses, este plan establece un camino claro para la implementación de EspañolOO como un lenguaje simple pero robusto, totalmente en castellano y con su propio compilador implementado en Python.

La clave del éxito de este proyecto radica en la simplicidad del diseño, la robustez de la implementación y la calidad de la documentación. Siguiendo este plan, EspañolOO tiene el potencial de convertirse en un referente en el mundo de los lenguajes de programación en español.