# Guía de Contribución a EspañolOO

¡Gracias por tu interés en contribuir al proyecto EspañolOO! Este documento te guiará a través del proceso de contribución al proyecto.

## Tabla de Contenidos

1. [Código de Conducta](#código-de-conducta)
2. [Cómo Contribuir](#cómo-contribuir)
   - [Reportar Errores](#reportar-errores)
   - [Sugerir Características](#sugerir-características)
   - [Contribuir con Código](#contribuir-con-código)
3. [Desarrollo Local](#desarrollo-local)
   - [Requisitos](#requisitos)
   - [Configuración del Entorno](#configuración-del-entorno)
   - [Estructura del Proyecto](#estructura-del-proyecto)
4. [Guía de Estilo](#guía-de-estilo)
   - [Python](#python)
   - [TypeScript](#typescript)
5. [Proceso de Pull Request](#proceso-de-pull-request)
6. [Reconocimiento](#reconocimiento)

## Código de Conducta

Este proyecto adopta el [Código de Conducta de Contribuyente de Python](https://www.python.org/psf/conduct/). Al participar en este proyecto, te comprometes a respetar y seguir estas pautas.

## Cómo Contribuir

### Reportar Errores

Si encuentras un error en el proyecto, por favor sigue estos pasos:

1. Revisa los [issues existentes](https://github.com/tu-usuario/espanoloo/issues) para asegurarte de que el error no haya sido reportado previamente.
2. Si no existe un issue similar, crea uno nuevo.
3. Proporciona la siguiente información:
   - Descripción clara y concisa del error
   - Pasos para reproducir el error
   - Comportamiento esperado vs. actual
   - Entorno (versión de Python, sistema operativo, etc.)
   - Mensajes de error completos (si los hay)

### Sugerir Características

Si tienes una idea para mejorar el proyecto:

1. Revisa los [issues existentes](https://github.com/tu-usuario/espanoloo/issues) para ver si la característica ya ha sido sugerida.
2. Si no, crea un nuevo issue con la etiqueta "enhancement".
3. Describe la característica en detalle, incluyendo:
   - El problema que resuelve
   - Cómo se implementaría
   - Ejemplos de uso
   - Cualquier consideración de diseño relevante

### Contribuir con Código

Si deseas contribuir con código al proyecto, sigue estas pautas:

1. **Fork el repositorio**: Haz un fork del repositorio principal en GitHub.
2. **Crea una rama de características**: Crea una nueva rama para tu contribución.
   ```bash
   git checkout -b feature/nueva-caracteristica
   ```
3. **Realiza tus cambios**: Implementa tus cambios siguiendo las pautas de estilo y asegurándote de que todo funcione correctamente.
4. **Prueba tus cambios**: Ejecuta la suite de pruebas para asegurarte de que no has roto nada.
   ```bash
   python -m unittest discover tests
   ```
5. **Documenta tus cambios**: Si has agregado o modificado funcionalidades, actualiza la documentación correspondiente.
6. **Envía un Pull Request**: Abre un Pull Request desde tu rama al repositorio principal.

## Desarrollo Local

### Requisitos

- Python 3.10 o superior
- Node.js 16 o superior (para la extensión de VS Code)
- Git
- Herramientas de desarrollo:
  - Para Python: `pip install pytest flake8 black`
  - Para TypeScript: `npm install -g typescript`

### Configuración del Entorno

1. Clona tu fork del repositorio:
   ```bash
   git clone https://github.com/tu-usuario/espanoloo.git
   cd espanoloo
   ```

2. Instala las dependencias del compilador:
   ```bash
   pip install ply
   ```

3. Instala las dependencias de la extensión de VS Code:
   ```bash
   cd extension-vscode
   npm install
   cd ..
   ```

4. Ejecuta las pruebas para asegurarte de que todo funciona:
   ```bash
   python -m unittest discover tests
   ```

### Estructura del Proyecto

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
├── examples/                   # Ejemplos de código
├── tests/                      # Pruebas unitarias
└── bitacora_desarrollo.md      # Registro de desarrollo
```

## Guía de Estilo

### Python

El código del compilador sigue las convenciones de estilo de Python:

- Usa [PEP 8](https://www.python.org/dev/peps/pep-0008/) como guía general
- Usa `black` para formateo automático
- Usa `flake8` para verificación de estilo
- Usa docstrings para documentar funciones y clases
- Usa nombres descriptivos para variables y funciones

Ejemplo:

```python
def verificar_tipos(expresion, contexto):
    """
    Verifica los tipos de una expresión en un contexto dado.
    
    Args:
        expresion: Nodo del AST de la expresión a verificar
        contexto: Contexto actual de verificación de tipos
        
    Returns:
        Tipo de la expresión verificada
        
    Raises:
        TypeError: Si hay un error de tipo
    """
    # Implementación
    pass
```

### TypeScript

El código de la extensión de VS Code sigue las convenciones de TypeScript:

- Usa [TypeScript ESLint](https://typescript-eslint.io/) para verificación de estilo
- Usa [Prettier](https://prettier.io/) para formateo automático
- Usa tipos explícitos siempre que sea posible
- Usa interfaces para definir estructuras de datos
- Usa nombres descriptivos para variables y funciones

Ejemplo:

```typescript
interface CompletionItem {
    label: string;
    kind: CompletionItemKind;
    documentation?: string;
}

class CompletionProvider implements CompletionItemProvider {
    provideCompletionItems(
        document: TextDocument,
        position: Position,
        token: CancellationToken,
        context: CompletionContext
    ): ProviderResult<CompletionItem[]> {
        // Implementación
    }
}
```

## Proceso de Pull Request

1. **Prepara tu Pull Request**:
   - Asegúrate de que tu código pase todas las pruebas
   - Sigue las guías de estilo
   - Incluye pruebas para cualquier nueva funcionalidad
   - Actualiza la documentación si es necesario

2. **Abre el Pull Request**:
   - Usa un título claro y descriptivo
   - Proporciona una descripción detallada de los cambios
   - Incluye cualquier información relevante sobre pruebas o consideraciones de diseño
   - Asigna la etiqueta adecuada al PR (bugfix, feature, documentation, etc.)

3. **Revisión**:
   - Los mantenedores revisarán tu PR
   - Es posible que te pidan cambios o aclaraciones
   - Responde a los comentarios de manera constructiva

4. **Integración**:
   - Una vez aprobado, tu PR será fusionado al repositorio principal
   - Serás reconocido en los registros de contribuyentes

## Reconocimiento

Agradecemos a todos los contribuyentes que han ayudado a hacer de EspañolOO un mejor proyecto. Los contribuyentes son reconocidos en:

- La lista de colaboradores en el archivo `CONTRIBUTORS.md`
- Los registros de commits
- Los issues y pull requests cerrados

Si tu contribución es significativa, puedes ser invitado a ser un mantenedor del proyecto.

## Preguntas

Si tienes preguntas sobre cómo contribuir, no dudes en abrir un issue o contactar a los mantenedores del proyecto.

¡Gracias por tu contribución!
