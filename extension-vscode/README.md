# Extensión EspañolOO para Visual Studio Code

[![Version](https://img.shields.io/badge/Version-0.0.1-blue.svg)](https://marketplace.visualstudio.com/items?itemName=MiProfePana.espanoloo)
[![Marketplace](https://img.shields.io/badge/VS%20Code%20Marketplace-Instalar-blue.svg)](https://marketplace.visualstudio.com/items?itemName=MiProfePana.espanoloo)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/gustavopaez-profe-pana/espanoloo/blob/main/LICENSE)

La extensión oficial de EspañolOO para Visual Studio Code proporciona soporte completo para el lenguaje de programación EspañolOO, facilitando el desarrollo y la depuración de tus proyectos.

## Características

*   **Resaltado de Sintaxis**: Colorea tu código EspañolOO para una mejor legibilidad.
*   **Autocompletado**: Sugerencias inteligentes para palabras clave, funciones y variables.
*   **Depuración Integrada**: Depura tus programas EspañolOO directamente desde VS Code.
*   **Snippets de Código**: Fragmentos de código predefinidos para acelerar tu escritura.
*   **Soporte para Archivos `.eoo`**: Reconocimiento automático de archivos con extensión `.eoo`.

## Instalación

1.  Abre Visual Studio Code.
2.  Ve a la vista de Extensiones (`Ctrl+Shift+X` o `Cmd+Shift+X`).
3.  Busca "EspañolOO".
4.  Haz clic en "Instalar".

Alternativamente, puedes instalarla directamente desde el [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=MiProfePana.espanoloo).

## Uso

Una vez instalada la extensión:

1.  Crea o abre un archivo con la extensión `.eoo`.
2.  La extensión proporcionará automáticamente resaltado de sintaxis y autocompletado.

### Depuración

Para depurar un archivo EspañolOO:

1.  Abre tu archivo `.eoo`.
2.  Ve a la vista de Depuración (`Ctrl+Shift+D` o `Cmd+Shift+D`).
3.  Haz clic en el botón "Run and Debug" (Ejecutar y Depurar) o presiona `F5`.
4.  Selecciona la configuración "EspañolOO: Depurar Archivo".

## Ejemplo de Código

Aquí tienes un ejemplo simple de "Hola Mundo" en EspañolOO:

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

## Contribución

¡Nos encanta recibir contribuciones! Si deseas mejorar esta extensión o el lenguaje EspañolOO, por favor, revisa nuestra [guía de contribución](https://github.com/gustavopaez-profe-pana/espanoloo/blob/main/CONTRIBUTING.md) en el repositorio principal.

## Licencia

Esta extensión está licenciada bajo la Licencia MIT. Consulta el archivo [LICENSE](https://github.com/gustavopaez-profe-pana/espanoloo/blob/main/LICENSE) en el repositorio principal para más detalles.

---

**¡Gracias por usar la extensión EspañolOO!**