# EspañolOO - Lenguaje de Programación Orientada a Objetos en Castellano

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![VS Code](https://img.shields.io/badge/VS%20Code-1.70+-blue.svg)](https://code.visualstudio.com/)

EspañolOO es un lenguaje de programación orientada a objetos con palabras reservadas en castellano, diseñado para ser simple pero robusto. Inspirado en lenguajes como Latino, EspañolOO busca facilitar el aprendizaje de la programación a hispanohablantes y proporcionar una alternativa natural para el desarrollo de software en español.

## Características

- 🌐 **Sintaxis en español**: Palabras reservadas y conceptos en castellano
- 🐍 **Compilación a Python**: El código se compila a Python ejecutable
- 🎨 **Extensión VS Code**: Soporte completo con resaltado de sintaxis, autocompletado y depuración
- 🔄 **REPL interactivo**: Intérprete interactivo para pruebas rápidas
- 🧪 **Pruebas unitarias**: Suite completa de pruebas automatizadas
- 📚 **Documentación completa**: Manuales, guías y tutoriales detallados

## Estructura del Proyecto

```
espanoloo/
├── espanoloo_compiler/          # Código fuente del compilador
│   ├── lexer.py                # Analizador léxico
│   ├── parser.py               # Analizador sintáctico
│   ├── ast.py                  # Árbol de sintaxis abstracta
│   ├── verificador_semantico.py # Verificador semántico
│   ├── verificador_tipos.py    # Verificador de tipos
│   ├── generador_codigo.py     # Generador de código Python
│   ├── optimizador.py          # Optimizador de código
│   ├── main.py                 # Punto de entrada del compilador
│   ├── repl.py                 # Intérprete interactivo (REPL)
│   └── analysis_server.py      # Servidor de análisis para VS Code
├── extension-vscode/            # Extensión de VS Code
│   ├── src/                    # Código fuente TypeScript
│   ├── syntaxes/               # Archivos de sintaxis
│   ├── snippets/               # Fragmentos de código
│   ├── themes/                 # Temas personalizados
│   └── package.json            # Configuración de la extensión
├── docs/                       # Documentación
│   ├── manual_referencia_lenguaje.md
│   ├── guia_usuario_compilador.md
│   ├── guia_extension_vscode.md
│   ├── tutorial_introduccion_programacion.md
│   └── guia_instalacion_uso.md
├── examples/                   # Ejemplos de código

└── README.md                   # Este archivo
```

## Instalación

### Requisitos Previos

- Python 3.10 o superior
- Visual Studio Code (opcional, para desarrollo con IDE)
- Git

### Pasos de Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/espanoloo.git
   cd espanoloo
   ```

2. **Instala las dependencias**:
   ```bash
   pip install ply
   ```

3. **Verifica la instalación**:
   ```bash
   python espanoloo_compiler/main.py --help
   ```

## Guías de Uso

- [Guía de Instalación y Uso](docs/guia_instalacion_uso.md) - Pasos detallados para instalar y usar EspañolOO
- [Manual de Referencia del Lenguaje](docs/manual_referencia_lenguaje.md) - Documentación completa del lenguaje
- [Guía del Usuario del Compilador](docs/guia_usuario_compilador.md) - Cómo usar el compilador y el REPL
- [Guía de la Extensión de VS Code](docs/guia_extension_vscode.md) - Instrucciones para la extensión de VS Code
- [Tutorial de Introducción a la Programación](docs/tutorial_introduccion_programacion.md) - Aprende a programar con EspañolOO

## Ejemplo de Código

Hola Mundo en EspañolOO:

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

## Compilación y Ejecución

### Usando la Línea de Comandos

1. Guarda el código en un archivo con extensión `.eoo` (ej. `hola.eoo`)
2. Compila el código:
   ```bash
   python espanoloo_compiler/main.py hola.eoo
   ```
3. Ejecuta el código generado:
   ```bash
   python hola.py
   ```

### Usando la Extensión de VS Code

1. Instala la extensión EspañolOO desde el marketplace de VS Code
2. Abre un archivo `.eoo`
3. Presiona `F5` para compilar y ejecutar directamente

### Usando el REPL

```bash
python espanoloo_compiler/repl.py
```

## Características del Lenguaje

### Tipos de Datos

- `entero`: Números enteros
- `decimal`: Números con punto decimal
- `cadena`: Texto
- `booleano`: Valores lógicos (`verdadero`, `falso`)
- `nulo`: Valor nulo

### Estructuras de Control

- `si-sino-sino si`: Condicionales
- `mientras`, `para`, `hacer mientras`: Bucles
- `romper`, `continuar`, `retornar`: Control de flujo

### Programación Orientada a Objetos

- Clases y objetos
- Herencia simple y múltiple
- Polimorfismo
- Encapsulamiento (modificadores de acceso: `publico`, `privado`, `protegido`)
- Interfaces y clases abstractas

### Manejo de Excepciones

- `intentar-atrapar-finalmente`: Manejo de errores
- `lanzar`: Lanzar excepciones personalizadas

## Contribución

¡Nos encanta recibir contribuciones! Aquí tienes algunas formas de ayudar:

1. **Reporta errores**: Abre un issue en GitHub
2. **Sugiere características**: Envía una propuesta de mejora
3. **Contribuye con código**: Revisa nuestra [guía de contribución](CONTRIBUTING.md)
4. **Mejora la documentación**: Ayuda a hacer la documentación más clara y completa

### Pasos para Contribuir

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Realiza tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Haz push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ve el archivo [LICENSE](LICENSE) para más detalles.

## Reconocimientos

- Inspirado en el lenguaje [Latino](https://github.com/cesarbs/latino)
- Implementado con PLY (Python Lex-Yacc)
- Extensión de VS Code desarrollada con TypeScript

## Contacto

- **Proyecto**: [EspañolOO en GitHub](https://github.com/tu-usuario/espanoloo)
- **Issues**: [Reportar un problema](https://github.com/tu-usuario/espanoloo/issues)
- **Discusiones**: [Unirse a las discusiones](https://github.com/tu-usuario/espanoloo/discussions)

---

**¡Gracias por usar EspañolOO! Si te gusta el proyecto, no olvides darle una estrella ⭐.**
