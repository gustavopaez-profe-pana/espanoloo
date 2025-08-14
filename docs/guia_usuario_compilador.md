# Guía de Usuario del Compilador de EspañolOO

## Introducción

El compilador de EspañolOO es la herramienta fundamental que transforma tu código escrito en EspañolOO (`.eoo`) a código Python (`.py`), haciéndolo ejecutable en cualquier entorno que soporte Python. Actúa como un puente entre la sintaxis intuitiva y en castellano de EspañolOO y la vasta capacidad y ecosistema de Python.

Este manual te guiará a través de la instalación, el uso básico del compilador de línea de comandos, sus opciones avanzadas, el manejo de errores y la interacción con el Intérprete Interactivo (REPL) de EspañolOO.

## Instalación y Requisitos

Para utilizar el compilador de EspañolOO, necesitarás tener un entorno de Python configurado en tu sistema.

### Requisitos del Sistema

*   **Python 3.x**: Asegúrate de tener Python 3.x instalado en tu sistema. Puedes descargarlo desde el sitio web oficial de Python: [python.org](https://www.python.org/downloads/).
*   **Acceso a la línea de comandos**: Familiaridad básica con el uso de la terminal o línea de comandos de tu sistema operativo (CMD en Windows, Terminal en macOS/Linux).

### Configuración del Entorno

1.  **Descargar el proyecto EspañolOO**:
    Clona el repositorio de EspañolOO desde GitHub (o descarga el archivo ZIP y extráelo) en tu máquina local. Por ejemplo:
    ```bash
    git clone https://github.com/tu_usuario/espanoloo_v2.git
    cd espanoloo_v2
    ```
    *(Nota: Reemplaza `https://github.com/tu_usuario/espanoloo_v2.git` con la URL real del repositorio si es diferente).* 

2.  **Estructura de directorios**:
    Asegúrate de que la estructura de directorios del proyecto se mantenga intacta, especialmente la carpeta `espanoloo_compiler`, ya que el compilador depende de la correcta ubicación de sus módulos internos.

Una vez que tengas Python instalado y el proyecto EspañolOO descargado, estarás listo para usar el compilador.

## Uso Básico: Compilación de Archivos

Una vez que tu entorno esté configurado, puedes usar el compilador de EspañolOO para transformar tus archivos `.eoo` en archivos `.py` ejecutables.

### Compilación de un Archivo Simple

Para compilar un archivo de código fuente de EspañolOO, utiliza el script `main.py` ubicado en la carpeta `espanoloo_compiler`.

**Sintaxis básica:**

```bash
python espanoloo_compiler/main.py <ruta_a_tu_archivo.eoo>
```

El compilador generará un archivo Python (`.py`) con el mismo nombre que tu archivo `.eoo` y en la misma ubicación.

**Ejemplo:**

Supongamos que tienes un archivo llamado `mi_programa.eoo` con el siguiente contenido:

```espanoloo
// mi_programa.eoo
funcion saludar(nombre: cadena) {
    imprimir("Hola, " + nombre + "!");
}

saludar("Mundo");
```

Para compilarlo, abre tu terminal en la raíz del proyecto EspañolOO y ejecuta:

```bash
python espanoloo_compiler/main.py mi_programa.eoo
```

Si la compilación es exitosa, verás un mensaje similar a:

```
Compilación exitosa. Código Python generado en: mi_programa.py
```

Ahora tendrás un archivo `mi_programa.py` en el mismo directorio que `mi_programa.eoo`. Puedes ejecutar este archivo Python directamente:

```bash
python mi_programa.py
```

Y verás la salida:

```
Hola, Mundo!
```

## Opciones de Línea de Comandos

El compilador de EspañolOO (`main.py`) ofrece algunas opciones para controlar el proceso de compilación.

### Especificar Archivo de Salida (`-o` o `--output`)

Por defecto, el compilador guarda el archivo Python generado en el mismo directorio que el archivo `.eoo` de entrada y con el mismo nombre (cambiando la extensión a `.py`). Puedes especificar un nombre y/o una ruta diferente para el archivo de salida utilizando la opción `-o` o `--output`.

**Sintaxis:**

```bash
python espanoloo_compiler/main.py <ruta_a_tu_archivo.eoo> -o <ruta_archivo_salida.py>
```

**Ejemplo:**

Para compilar `mi_programa.eoo` y guardar el resultado como `salida/programa_compilado.py`:

```bash
python espanoloo_compiler/main.py mi_programa.eoo -o salida/programa_compilado.py
```

Asegúrate de que el directorio de salida (`salida/` en este ejemplo) exista antes de ejecutar el comando.

### Habilitar Optimizaciones (`--optimizar`)

El compilador de EspañolOO incluye un módulo de optimización que puede aplicar mejoras básicas al código generado para hacerlo más eficiente. Puedes activar estas optimizaciones utilizando la bandera `--optimizar`.

**Sintaxis:**

```bash
python espanoloo_compiler/main.py <ruta_a_tu_archivo.eoo> --optimizar
```

**Ejemplo:**

Para compilar `mi_programa.eoo` con optimizaciones:

```bash
python espanoloo_compiler/main.py mi_programa.eoo --optimizar
```

Si las optimizaciones se aplican, verás un mensaje indicando cuántas optimizaciones se realizaron.

Puedes combinar ambas opciones:

```bash
python espanoloo_compiler/main.py mi_programa.eoo -o salida/programa_optimizado.py --optimizar
```

## Manejo de Errores

Durante el proceso de compilación, el compilador de EspañolOO puede encontrar diferentes tipos de errores. Comprender los mensajes de error es crucial para depurar tu código.

El compilador reporta principalmente dos categorías de errores: **errores de sintaxis** y **errores semánticos**.

### Errores de Sintaxis

Los errores de sintaxis ocurren cuando tu código no sigue las reglas gramaticales del lenguaje EspañolOO. Son detectados en la fase de análisis sintáctico (parsing).

**Ejemplos comunes y cómo se muestran:**

*   **Símbolo inesperado o faltante:**
    ```
    Errores de sintaxis encontrados:
    - Error de sintaxis en la línea X, columna Y: Símbolo inesperado ')'
    ```
    Esto indica que hay un carácter o token que el compilador no esperaba en esa posición, o que falta algo (como un punto y coma al final de una sentencia).

*   **Fin de archivo inesperado:**
    ```
    Errores de sintaxis encontrados:
    - Error de sintaxis: fin de archivo inesperado.
    ```
    Este error suele aparecer cuando un bloque de código (como una función o un `si`) no está cerrado correctamente (por ejemplo, falta una llave `}`).

### Errores Semánticos

Los errores semánticos ocurren cuando el código es sintácticamente correcto, pero no tiene sentido lógico o viola las reglas de significado del lenguaje (por ejemplo, usar una variable no declarada o intentar realizar una operación con tipos de datos incompatibles). Son detectados en la fase de análisis semántico.

**Ejemplos comunes y cómo se muestran:**

*   **Variable no declarada:**
    ```
    Errores semánticos encontrados:
    - Variable 'mi_variable' no declarada en este ámbito.
    ```
    Significa que estás intentando usar una variable que no ha sido definida previamente con un tipo.

*   **Tipo incompatible en asignación:**
    ```
    Errores semánticos encontrados:
    - Tipo incompatible en asignación: no se puede asignar un valor de tipo 'cadena' a una variable de tipo 'entero'.
    ```
    Indica que estás intentando asignar un valor de un tipo a una variable de otro tipo que no son compatibles.

*   **Operación con tipos incompatibles:**
    ```
    Errores semánticos encontrados:
    - Operación binaria '+' no definida para tipos 'cadena' y 'entero'.
    ```
    Ocurre cuando intentas realizar una operación (como suma, resta, etc.) entre tipos de datos que no pueden operarse juntos.

*   **Función/Clase/Método ya declarado:**
    ```
    Errores semánticos encontrados:
    - Función 'mi_funcion' ya declarada.
    - Clase 'MiClase' ya declarada.
    - Método 'mi_metodo' ya declarado en la clase 'MiClase'.
    ```
    Indica que has intentado definir una función, clase o método con un nombre que ya está en uso en el mismo ámbito.

*   **Número incorrecto de argumentos en llamada a función:**
    ```
    Errores semánticos encontrados:
    - Número incorrecto de argumentos para la función 'saludar'. Se esperaban 1, se recibieron 0.
    ```
    Significa que al llamar a una función, no proporcionaste la cantidad correcta de argumentos.

*   **Acceso no permitido (privado/protegido):**
    ```
    Errores semánticos encontrados:
    - Acceso a atributo 'saldo' no permitido. Es privado/protegido.
    ```
    Se produce cuando intentas acceder a un atributo o método de una clase que ha sido declarado como `privado` o `protegido` desde un lugar donde no tienes permiso.

### Otros Errores

*   **Archivo no encontrado:**
    ```
    Error: El archivo de entrada 'archivo_inexistente.eoo' no fue encontrado.
    ```
    Este error es autoexplicativo; el compilador no pudo localizar el archivo `.eoo` que especificaste.

*   **Errores inesperados:**
    ```
    Error inesperado durante la compilación: [Mensaje de error técnico]
    ```
    Estos son errores internos del compilador que no corresponden a errores de tu código EspañolOO. Si encuentras uno de estos, es recomendable reportarlo a los desarrolladores del compilador.

Al revisar los mensajes de error, siempre presta atención a la línea y columna (si se proporcionan) para localizar el problema en tu código.

## Intérprete Interactivo (REPL)

El Intérprete Interactivo de EspañolOO (Read-Eval-Print Loop, REPL) te permite escribir y ejecutar código EspañolOO línea por línea, obteniendo resultados inmediatos. Es una herramienta excelente para experimentar con el lenguaje, probar pequeñas piezas de código o depurar.

### Iniciar el REPL

Para iniciar el REPL, abre tu terminal en la raíz del proyecto EspañolOO y ejecuta el script `repl.py` ubicado en la carpeta `espanoloo_compiler`:

```bash
python espanoloo_compiler/repl.py
```

Verás un mensaje de bienvenida y el prompt `>>>`:

```
Intérpreprete Interactivo de EspañolOO v0.2
Escriba 'salir()' para terminar.
>>>
```

### Uso Básico

Puedes escribir cualquier sentencia o expresión válida de EspañolOO en el prompt. El REPL evaluará tu entrada y mostrará el resultado (si lo hay) o ejecutará la sentencia.

**Ejemplo de operaciones básicas:**

```
>>> x: entero = 10;
>>> imprimir(x + 5);
15
>>> funcion saludar(nombre: cadena) { imprimir("Hola, " + nombre + "!"); }
>>> saludar("Mundo");
Hola, Mundo!
```

### Manejo de Sentencias Multilínea

El REPL es lo suficientemente inteligente como para detectar cuando una sentencia está incompleta y te pedirá más entrada con el prompt `...`.

**Ejemplo de función multilínea:**

```
>>> funcion sumar(a: entero, b: entero): entero {
...     retornar a + b;
... }
>>> resultado: entero = sumar(7, 3);
>>> imprimir(resultado);
10
```

**Ejemplo de estructura de control multilínea:**

```
>>> si (verdadero) {
...     imprimir("Esto es verdadero.");
... } sino {
...     imprimir("Esto es falso.");
... }
Esto es verdadero.
```

### Salir del REPL

Para salir del intérprete interactivo, simplemente escribe `salir()` y presiona Enter:

```
>>> salir()
```

## Ejemplos Prácticos

A continuación, se presentan algunos ejemplos de programas sencillos en EspañolOO para ilustrar el uso del compilador y el REPL.

### Ejemplo 1: Contador Simple

Este programa utiliza un bucle `para` para contar del 1 al 5.

**Código EspañolOO (`contador.eoo`):**

```espanoloo
// contador.eoo
funcion iniciarContador(limite: entero) {
    para (i: entero = 1; i <= limite; i = i + 1) {
        imprimir("Contando: " + i);
    }
}

iniciarContador(5);
```

**Uso con el Compilador:**

```bash
python espanoloo_compiler/main.py contador.eoo
python contador.py
```

**Salida esperada:**

```
Contando: 1
Contando: 2
Contando: 3
Contando: 4
Contando: 5
```

**Uso en el REPL:**

```
>>> funcion iniciarContador(limite: entero) {
...     para (i: entero = 1; i <= limite; i = i + 1) {
...         imprimir("Contando: " + i);
...     }
... }
>>> iniciarContador(3);
Contando: 1
Contando: 2
Contando: 3
```

### Ejemplo 2: Cálculo de Área de un Círculo

Este ejemplo define una función para calcular el área de un círculo.

**Código EspañolOO (`area_circulo.eoo`):**

```espanoloo
// area_circulo.eoo
constante PI: decimal = 3.14159;

funcion calcularAreaCirculo(radio: decimal): decimal {
    retornar PI * radio * radio;
}

radio_circulo: decimal = 10.0;
area: decimal = calcularAreaCirculo(radio_circulo);
imprimir("El área del círculo con radio " + radio_circulo + " es: " + area);
```

**Uso con el Compilador:**

```bash
python espanoloo_compiler/main.py area_circulo.eoo
python area_circulo.py
```

**Salida esperada:**

```
El área del círculo con radio 10.0 es: 314.159
```

### Ejemplo 3: Clase `Libro`

Este ejemplo demuestra la definición y uso de una clase simple.

**Código EspañolOO (`libro.eoo`):**

```espanoloo
// libro.eoo
clase Libro {
    publico titulo: cadena;
    publico autor: cadena;
    privado anio_publicacion: entero;

    publico constructor(titulo_param: cadena, autor_param: cadena, anio_param: entero) {
        este.titulo = titulo_param;
        este.autor = autor_param;
        este.anio_publicacion = anio_param;
    }

    publico obtenerInformacion(): cadena {
        retornar este.titulo + " por " + este.autor + " (" + este.anio_publicacion + ")";
    }
}

mi_libro: Libro = nuevo Libro("Cien años de soledad", "Gabriel García Márquez", 1967);
imprimir("Información del libro: " + mi_libro.obtenerInformacion());
```

**Uso con el Compilador:**

```bash
python espanoloo_compiler/main.py libro.eoo
python libro.py
```

**Salida esperada:**

```
Información del libro: Cien años de soledad por Gabriel García Márquez (1967)
```