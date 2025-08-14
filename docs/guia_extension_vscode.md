# Guía de la Extensión de VS Code para EspañolOO

## Introducción

La extensión de Visual Studio Code para EspañolOO (`EspañolOO`) está diseñada para proporcionar una experiencia de desarrollo fluida y enriquecida para el lenguaje de programación EspañolOO. Al integrar esta extensión en tu entorno de VS Code, podrás disfrutar de características que mejoran significativamente la productividad y la legibilidad del código, haciendo que la programación en EspañolOO sea más intuitiva y eficiente.

Entre los beneficios clave se incluyen:
*   **Resaltado de Sintaxis**: Colorea tu código EspañolOO para facilitar su lectura y comprensión.
*   **Autocompletado Inteligente**: Sugiere automáticamente palabras clave, nombres de variables, funciones y clases mientras escribes.

*   **Snippets de Código**: Inserta rápidamente bloques de código comunes con atajos de teclado.
*   **Depuración Integrada**: Permite ejecutar tu código paso a paso, inspeccionar variables y diagnosticar problemas directamente desde VS Code.
*   **Diagnóstico en Tiempo Real**: Identifica errores y advertencias a medida que escribes, proporcionando retroalimentación instantánea.

Esta guía te ayudará a instalar la extensión y a aprovechar al máximo sus funcionalidades.

## Instalación

La instalación de la extensión de EspañolOO en Visual Studio Code es un proceso sencillo que se realiza directamente desde el Marketplace de VS Code.

### Desde el Marketplace de VS Code

1.  **Abrir VS Code**: Inicia Visual Studio Code.
2.  **Acceder a Extensiones**: Haz clic en el icono de Extensiones en la barra de actividad lateral (o presiona `Ctrl+Shift+X` / `Cmd+Shift+X`).
3.  **Buscar la Extensión**: En la barra de búsqueda de extensiones, escribe `EspañolOO` o `espanoloo`.
4.  **Instalar**: Localiza la extensión con el nombre "EspañolOO" y la descripción "Soporte para el lenguaje de programación EspañolOO en VS Code" (publicada por el autor correspondiente). Haz clic en el botón "Instalar".

### Desde la Línea de Comandos (Opcional)

Si prefieres instalar extensiones desde la terminal, puedes usar el siguiente comando:

```bash
code --install-extension espanoloo
```

Una vez instalada, la extensión se activará automáticamente y comenzará a proporcionar soporte para tus archivos `.eoo`.

## Características

La extensión de EspañolOO para VS Code integra una serie de características que mejoran tu flujo de trabajo de desarrollo.

### Resaltado de Sintaxis

El resaltado de sintaxis proporciona colores distintivos a diferentes elementos de tu código EspañolOO (palabras clave, tipos de datos, cadenas, comentarios, etc.), facilitando la lectura y la identificación rápida de la estructura del código. Esta funcionalidad se basa en el archivo de gramática `espanoloo.tmLanguage.json`.

### Autocompletado Inteligente

A medida que escribes, la extensión ofrece sugerencias de autocompletado basadas en el contexto de tu código. Esto incluye:
*   Palabras clave del lenguaje.
*   Nombres de variables y constantes declaradas.
*   Nombres de funciones y métodos.
*   Nombres de clases y atributos.

Las sugerencias se presentan con iconos que indican el tipo de elemento (función, variable, clase, etc.), lo que agiliza la escritura de código y reduce errores tipográficos. Esta característica es gestionada por la lógica implementada en `src/completion.ts`.

### Snippets de Código

Los snippets son plantillas de código predefinidas que puedes insertar rápidamente en tu editor. La extensión de EspañolOO incluye snippets para las construcciones más comunes del lenguaje, como:
*   Estructuras de control (`si`, `para`, `mientras`).
*   Definiciones de funciones (`funcion`).
*   Definiciones de clases (`clase`).
*   Declaraciones de variables.

Puedes activar los snippets escribiendo un prefijo y presionando `Tab` (o seleccionándolos del menú de autocompletado). Los snippets están definidos en `snippets/espanoloo.json`.

### Depuración Integrada

La extensión proporciona una experiencia de depuración completa directamente dentro de VS Code. Puedes:
*   Establecer puntos de interrupción (breakpoints) en tu código EspañolOO.
*   Ejecutar tu programa paso a paso.
*   Inspeccionar el valor de las variables en tiempo de ejecución.
*   Ver la pila de llamadas.

La depuración se configura automáticamente a través del `DebugConfigurationProvider` (implementado en `src/debug.ts`), que compila tu código EspañolOO a Python y luego utiliza el depurador de Python de VS Code, ofreciendo una experiencia fluida sin configuración manual compleja.

### Diagnóstico en Tiempo Real

La extensión analiza tu código a medida que lo escribes y te proporciona retroalimentación instantánea sobre posibles errores y advertencias. Esto incluye:
*   **Errores de Sintaxis**: Subraya el código incorrecto y muestra mensajes de error detallados.
*   **Errores Semánticos**: Identifica problemas lógicos, como variables no declaradas o incompatibilidades de tipo, antes de la compilación.

Estos diagnósticos te ayudan a corregir problemas rápidamente y a mantener la calidad de tu código.

## Configuración

Actualmente, la extensión de EspañolOO para Visual Studio Code no ofrece opciones de configuración personalizables directamente a través de la interfaz de configuración de VS Code (es decir, no hay ajustes que puedas modificar en `settings.json` específicos para la extensión).

La extensión está diseñada para funcionar de forma óptima con su configuración predeterminada, proporcionando todas sus características sin necesidad de ajustes manuales.

## Solución de Problemas Comunes

Si encuentras algún problema al usar la extensión de EspañolOO para VS Code, aquí tienes algunas soluciones a problemas comunes.

### El Resaltado de Sintaxis no Funciona

*   **Verifica la extensión del archivo**: Asegúrate de que tu archivo tenga la extensión `.eoo`. La extensión de VS Code solo se activa para archivos con esta extensión.
*   **Reinicia VS Code**: A veces, un reinicio completo de Visual Studio Code puede resolver problemas de activación de extensiones.
*   **Reinstala la extensión**: Desinstala y vuelve a instalar la extensión desde el Marketplace de VS Code.

### Problemas con la Depuración

La depuración de EspañolOO depende de que el compilador de EspañolOO funcione correctamente y de que Python esté configurado adecuadamente.

*   **Verifica la instalación de Python**: Asegúrate de que Python 3.x esté correctamente instalado y accesible desde tu terminal.
*   **Verifica la ruta del proyecto EspañolOO**: La extensión necesita poder encontrar los scripts del compilador (`main.py`, `repl.py`, etc.). Asegúrate de que la estructura de directorios del proyecto EspañolOO esté intacta y que VS Code esté abierto en la raíz de ese proyecto o en un subdirectorio que permita resolver las rutas relativas.
*   **Errores de compilación**: Si tu código EspañolOO tiene errores de sintaxis o semánticos, el proceso de depuración no podrá compilarlo a Python. Asegúrate de que tu código esté libre de errores antes de intentar depurarlo. Los diagnósticos en tiempo real de la extensión te ayudarán con esto.
*   **Revisa la Consola de Depuración**: La consola de depuración de VS Code (`Debug Console`) puede mostrar mensajes de error del compilador o del proceso de depuración que te darán pistas sobre el problema.

### La Extensión no Carga o Causa Errores

*   **Verifica la salida de las extensiones**: En VS Code, ve a `Ayuda > Alternar Herramientas de Desarrollo` y luego a la pestaña `Consola`. Busca mensajes de error relacionados con la extensión de EspañolOO.
*   **Deshabilita otras extensiones**: Ocasionalmente, otras extensiones pueden entrar en conflicto. Intenta deshabilitar temporalmente otras extensiones para ver si el problema se resuelve.
*   **Reporta el problema**: Si no puedes resolver el problema, considera reportarlo a los desarrolladores de la extensión, proporcionando tantos detalles como sea posible (versión de VS Code, versión de la extensión, sistema operativo, pasos para reproducir el error y cualquier mensaje de error en la consola de desarrollo).