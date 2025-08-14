# Guía de Instalación y Uso de EspañolOO

## Introducción

Esta guía te enseñará paso a paso cómo instalar y usar el lenguaje de programación EspañolOO, incluyendo cómo configurar el entorno, compilar código y utilizar la extensión de VS Code para una experiencia de desarrollo optimizada.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes:

1. **Python 3.10 o superior**: [Descargar Python](https://www.python.org/downloads/)
2. **Visual Studio Code**: [Descargar VS Code](https://code.visualstudio.com/)
3. **Git**: [Descargar Git](https://git-scm.com/downloads)

## Paso 1: Instalación del Compilador de EspañolOO

### 1.1 Clonar el Repositorio

Si aún no tienes el código del proyecto, clónalo desde el repositorio de GitHub:

```bash
git clone https://github.com/tu-usuario/espanoloo.git
cd espanoloo
```

### 1.2 Instalar Dependencias

El compilador de EspañolOO depende de la librería PLY (Python Lex-Yacc). Instálala con pip:

```bash
pip install ply
```

### 1.3 Verificar la Instalación

Para asegurarte de que todo está instalado correctamente, ejecuta el compilador en modo ayuda:

```bash
python espanoloo_compiler/main.py --help
```

Deberías ver un mensaje de ayuda con las opciones disponibles del compilador.

## Paso 2: Instalación de la Extensión de VS Code

### 2.1 Abrir VS Code

Inicia Visual Studio Code.

### 2.2 Instalar la Extensión

1. Abre la vista de extensiones (icono de cuadrados en la barra lateral izquierda o presiona `Ctrl+Shift+X`).
2. Busca "EspañolOO" en el marketplace de VS Code.
3. Haz clic en "Instalar" junto a la extensión EspañolOO.

### 2.3 Configurar la Extensión

La extensión se configurará automáticamente una vez instalada. No requiere configuración adicional, pero puedes verificar que esté activa:

1. Abre un archivo con extensión `.eoo`.
2. Deberías ver el resaltado de sintaxis activado.
3. El autocompletado debería funcionar al escribir código.

## Paso 3: Crear tu Primer Programa en EspañolOO

### 3.1 Crear un Nuevo Archivo

1. En VS Code, ve a `Archivo > Nuevo Archivo` o presiona `Ctrl+N`.
2. Guarda el archivo con extensión `.eoo` (por ejemplo, `mi_programa.eoo`).

### 3.2 Escribir Código

Escribe el siguiente código de ejemplo en el archivo:

```espanoloo
// Mi primer programa en EspañolOO
funcion saludar(nombre: cadena): cadena {
    retornar "Hola, " + nombre + "!";
}

principal {
    mensaje: cadena = saludar("Mundo");
    imprimir(mensaje);
}
```

### 3.3 Guardar el Archivo

Presiona `Ctrl+S` para guardar el archivo.

## Paso 4: Compilar y Ejecutar Código

### 4.1 Usando la Línea de Comandos

Abre una terminal en la carpeta del proyecto (en VS Code, ve a `Terminal > Nueva Terminal`) y ejecuta:

```bash
python espanoloo_compiler/main.py mi_programa.eoo
```

Esto generará un archivo `mi_programa.py` en la misma carpeta.

Para ejecutar el código compilado:

```bash
python mi_programa.py
```

### 4.2 Usando la Extensión de VS Code

La extensión de VS Code facilita la compilación y ejecución:

1. Presiona `F5` para iniciar la depuración (compilación y ejecución).
2. O abre la paleta de comandos (`Ctrl+Shift+P`) y busca "EspañolOO: Compilar y Ejecutar".

La extensión compilará tu código y ejecutará el resultado automáticamente.

## Paso 5: Usar el REPL (Intérprete Interactivo)

### 5.1 Iniciar el REPL

Desde la terminal del proyecto, ejecuta:

```bash
python espanoloo_compiler/repl.py
```

### 5.2 Usar el REPL

El REPL te permite ejecutar código línea por línea:

```
>>> edad: entero = 25
>>> imprimir("Edad: " + edad)
Edad: 25
>>> funcion sumar(a: entero, b: entero): entero {
...     retornar a + b;
... }
>>> sumar(5, 3)
8
```

Para salir del REPL, escribe `salir()` o presiona `Ctrl+C`.

## Paso 6: Depurar Código con VS Code

### 6.1 Establecer Puntos de Interrupción

1. Haz clic en el número de línea a la izquierda del editor para establecer un punto de interrupción (aparecerá un punto rojo).
2. Presiona `F5` para iniciar la depuración.
3. La ejecución se detendrá en el punto de interrupción.
4. Usa la barra de depuración para continuar, paso a paso, inspeccionar variables, etc.

### 6.2 Inspeccionar Variables

Durante la depuración, puedes ver el valor de las variables en el panel "Variables" de VS Code.

## Paso 7: Solución de Problemas Comunes

### 7.1 Error: "No se encuentra el módulo 'ply'"

**Solución**: Instala la librería PLY:
```bash
pip install ply
```

### 7.2 Error: "El archivo no se reconoce como EspañolOO"

**Solución**: Asegúrate de que el archivo tenga la extensión `.eoo` y que la extensión de EspañolOO esté instalada y activa en VS Code.

### 7.3 Error de Compilación

**Solución**: Revisa el código en busca de errores de sintaxis. La extensión de VS Code debería subrayar los errores con líneas rojas.

### 7.4 La Depuración No Funciona

**Solución**: Asegúrate de que estás presionando `F5` en un archivo `.eoo` y que la extensión de EspañolOO está activa.

## Paso 8: Próximos Pasos

Una vez que te sientas cómodo con los pasos básicos, explora:

1. **Leer la documentación completa**:
   - [Manual de Referencia del Lenguaje](manual_referencia_lenguaje.md)
   - [Guía del Usuario del Compilador](guia_usuario_compilador.md)

2. **Explorar ejemplos**:
   - Revisa la carpeta `examples` para ver programas más complejos.

3. **Participar en la comunidad**:
   - Reporta problemas en GitHub.
   - Sugerir nuevas características.

## Conclusión

¡Felicidades! Ahora tienes un entorno de desarrollo completo para programar en EspañolOO. Puedes crear, compilar, depurar y ejecutar programas usando tanto la línea de comandos como la extensión de VS Code.

Para más información y actualizaciones, visita el [repositorio de EspañolOO en GitHub](https://github.com/tu-usuario/espanoloo).
