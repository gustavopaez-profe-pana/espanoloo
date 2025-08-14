# Tutorial de Introducción a la Programación con EspañolOO

## ¿Qué es Programar?

Programar es como darle instrucciones muy claras y precisas a una computadora para que haga algo por nosotros. Imagina que quieres enseñarle a un robot a preparar un sándwich. No puedes simplemente decirle "haz un sándwich". Necesitas darle cada paso, uno por uno, sin saltarte nada y en el orden correcto:

1.  Toma dos rebanadas de pan.
2.  Unta mantequilla en una rebanada.
3.  Unta mermelada en la otra rebanada.
4.  Junta las dos rebanadas.
5.  ¡Listo!

En programación, esas "instrucciones" se llaman **código**, y el conjunto de pasos ordenados para resolver un problema se llama **algoritmo**. Las computadoras son muy buenas siguiendo instrucciones, pero no entienden lo que queremos si no somos extremadamente específicos.

EspañolOO es un lenguaje que nos ayuda a escribir esas instrucciones de una manera que las computadoras entienden, pero usando palabras en español que nos resultan familiares. Así, podemos concentrarnos en la lógica de los pasos (el algoritmo) sin preocuparnos tanto por aprender palabras nuevas en otro idioma.

En este tutorial, aprenderás a pensar como un programador y a darle instrucciones a la computadora usando EspañolOO para crear tus propios programas.

## Primeros Pasos con EspañolOO: "¡Hola Mundo!"

El primer programa que se escribe en cualquier lenguaje de programación es tradicionalmente el "¡Hola Mundo!". Este programa simplemente muestra el mensaje "¡Hola Mundo!" en la pantalla. Es una excelente manera de asegurarnos de que todo está configurado correctamente y de familiarizarnos con la sintaxis básica.

### Tu Primer Programa en EspañolOO

Crea un nuevo archivo de texto y guárdalo con el nombre `hola_mundo.eoo`. Dentro de este archivo, escribe el siguiente código:

```espanoloo
// hola_mundo.eoo
// Este es tu primer programa en EspañolOO

// La función 'imprimir' se usa para mostrar texto en la pantalla.
imprimir("¡Hola Mundo!");
```

### Explicación Paso a Paso

*   `// Este es tu primer programa en EspañolOO`: Esta línea es un **comentario**. Los comentarios son notas que los programadores escriben para sí mismos o para otros. El compilador de EspañolOO ignora completamente los comentarios; no afectan cómo funciona el programa. En EspañolOO, los comentarios de una sola línea comienzan con `//`.
*   `imprimir("¡Hola Mundo!");`: Esta es la línea principal de nuestro programa.
    *   `imprimir`: Es una **función** predefinida en EspañolOO que se encarga de mostrar texto en la pantalla.
    *   `("¡Hola Mundo!")`: Es el **argumento** que le pasamos a la función `imprimir`. En este caso, es una **cadena de texto** (una secuencia de caracteres) que queremos que se muestre. Las cadenas de texto siempre van entre comillas dobles (`"`).
    *   `;`: El **punto y coma** al final de la línea indica que la sentencia ha terminado. En EspañolOO, cada instrucción debe finalizar con un punto y coma.

### Ejecutando tu Programa

Para ver tu programa en acción, necesitas usar el compilador de EspañolOO para transformarlo en código Python, y luego ejecutar ese código Python.

1.  **Abre tu Terminal o Símbolo del Sistema**.
2.  **Navega hasta la carpeta donde guardaste `hola_mundo.eoo`**. Por ejemplo, si lo guardaste en la raíz del proyecto EspañolOO:
    ```bash
    cd /ruta/a/tu/proyecto/espanoloo_v2
    ```
3.  **Compila el código EspañolOO a Python**:
    ```bash
    python espanoloo_compiler/main.py hola_mundo.eoo
    ```
    Si todo va bien, verás un mensaje de "Compilación exitosa" y se creará un archivo `hola_mundo.py` en la misma carpeta.

4.  **Ejecuta el código Python generado**:...
    ```bash
    python hola_mundo.py
    ```

**¡Felicidades!** Deberías ver el siguiente mensaje en tu terminal:

```
¡Hola Mundo!
```

Acabas de escribir, compilar y ejecutar tu primer programa en EspañolOO. ¡Estás programando!

## Variables y Datos: Cómo Guardar Información

En programación, a menudo necesitamos guardar información para usarla más tarde. Por ejemplo, la edad de una persona, un nombre, un precio, o si algo es verdadero o falso. Para esto, usamos **variables**.

Imagina una variable como una caja con una etiqueta. Puedes guardar algo dentro de la caja, y la etiqueta te dice qué tipo de cosa esperas guardar (números, texto, etc.).

### Declarando Variables

En EspañolOO, cuando creas una variable, debes darle un **nombre** y especificar qué **tipo de dato** va a guardar.

**Sintaxis:**

```espanoloo
nombre_de_la_caja: TipoDeDato;
```

**Ejemplo:**

```espanoloo
edad: entero;       // Una caja llamada 'edad' que guardará números enteros.
nombre: cadena;     // Una caja llamada 'nombre' que guardará texto.
precio: decimal;    // Una caja llamada 'precio' que guardará números con decimales.
es_activo: booleano; // Una caja llamada 'es_activo' que guardará verdadero o falso.
```

### Tipos de Datos Básicos

EspañolOO tiene varios tipos de datos para diferentes tipos de información:

*   **`entero`**: Para números completos, sin decimales (ej. 5, -10, 1000).
    ```espanoloo
    cantidad_manzanas: entero = 10;
    ```
*   **`decimal`**: Para números con decimales (ej. 3.14, 99.99, 0.5).
    ```espanoloo
    temperatura: decimal = 23.5;
    ```
*   **`cadena`**: Para texto. Siempre va entre comillas dobles (`"`).
    ```espanoloo
    saludo: cadena = "¡Hola, programador!";
    ```
*   **`booleano`**: Para valores que solo pueden ser `verdadero` o `falso`. Son muy útiles para tomar decisiones.
    ```espanoloo
    hay_luz: booleano = verdadero;
    ```
*   **`nulo`**: Representa la ausencia de valor. Es como una caja vacía.
    ```espanoloo
    valor_vacio: nulo = nulo;
    ```

### Asignando Valores a Variables

Para poner algo dentro de tu "caja" (variable), usas el signo igual (`=`). Puedes hacerlo al mismo tiempo que la declaras o después.

**Declarar y asignar al mismo tiempo:**

```espanoloo
mi_edad: entero = 30;
mi_nombre: cadena = "Ana";
```

**Asignar después de declarar:**

```espanoloo
puntuacion: entero;
puntuacion = 100; // Ahora la caja 'puntuacion' contiene el número 100.

mensaje: cadena;
mensaje = "Bienvenido al curso.";
```

### Constantes

A veces, tienes un valor que sabes que nunca va a cambiar en tu programa (como el valor de PI o un límite máximo). Para estos casos, usamos **constantes**. Una vez que le das un valor a una constante, no puedes cambiarlo.

Para declarar una constante, usa la palabra clave `constante`:

```espanoloo
constante PI: decimal = 3.14159;
constante MAXIMO_INTENTOS: entero = 3;

// PI = 3.0; // ¡Esto daría un error! No puedes cambiar una constante.
```

Las variables y los datos son los bloques de construcción básicos para almacenar y manipular información en tus programas.

## Decisiones: Cómo tu Programa Toma Caminos Diferentes

En la vida real, constantemente tomamos decisiones: "Si llueve, llevo paraguas; si no, no". Los programas también necesitan tomar decisiones para ser útiles. Por ejemplo, un programa de un juego podría decir: "Si el jugador tiene 0 vidas, el juego termina".

En EspañolOO, usamos las palabras clave `si`, `sino` y `sino si` para que nuestro programa pueda elegir qué hacer basándose en una condición.

### La Sentencia `si` (If)

La sentencia `si` es la más básica. Ejecuta un bloque de código **solo si** una condición es verdadera.

**Sintaxis:**

```espanoloo
si (condicion_es_verdadera) {
    // Código que se ejecuta si la condición es verdadera
}
```

*   `condicion_es_verdadera`: Es una expresión que resulta en `verdadero` o `falso` (un valor `booleano`).
*   `{ ... }`: Las llaves encierran el bloque de código que se ejecutará.

**Ejemplo:**

```espanoloo
edad: entero = 18;

si (edad >= 18) {
    imprimir("Eres mayor de edad.");
}

// Si 'edad' fuera 16, el mensaje no se imprimiría.
```

### La Sentencia `si-sino` (If-Else)

A menudo, queremos que el programa haga una cosa si la condición es verdadera y otra cosa si es falsa. Para eso, usamos `si-sino`.

**Sintaxis:**

```espanoloo
si (condicion_es_verdadera) {
    // Código que se ejecuta si la condición es verdadera
} sino {
    // Código que se ejecuta si la condición es falsa
}
```

**Ejemplo:**

```espanoloo
temperatura: entero = 28;

si (temperatura > 25) {
    imprimir("Hace calor.");
} sino {
    imprimir("La temperatura es agradable.");
}
// Si 'temperatura' fuera 20, se imprimiría "La temperatura es agradable."
```

### Múltiples Decisiones: `si-sino si-sino` (If-Else If-Else)

Cuando tienes más de dos opciones, puedes encadenar varias condiciones usando `sino si`. El programa revisará las condiciones en orden y ejecutará el primer bloque cuyo `si` o `sino si` sea verdadero. Si ninguna es verdadera, ejecutará el `sino` final (si existe).

**Sintaxis:**

```espanoloo
si (primera_condicion) {
    // Código si la primera es verdadera
} sino si (segunda_condicion) {
    // Código si la segunda es verdadera
} sino {
    // Código si ninguna de las anteriores es verdadera
}
```

**Ejemplo:**

```espanoloo
puntuacion: entero = 85;

si (puntuacion >= 90) {
    imprimir("Calificación: Excelente");
} sino si (puntuacion >= 70) {
    imprimir("Calificación: Notable");
} sino si (puntuacion >= 50) {
    imprimir("Calificación: Aprobado");
} sino {
    imprimir("Calificación: Reprobado");
}
// En este caso, se imprimiría "Calificación: Notable"
```

Las decisiones son una parte fundamental de la programación, permitiendo que tus programas sean dinámicos y respondan a diferentes situaciones.

## Repeticiones: Bucles para Hacer Tareas Repetitivas

Imagina que necesitas imprimir la frase "¡Hola!" diez veces. Podrías escribir `imprimir("¡Hola!");` diez veces, pero ¿y si fueran cien o mil veces? Sería muy tedioso y propenso a errores. Para esto, la programación nos ofrece los **bucles** (o ciclos).

Un bucle es una estructura que le dice a la computadora que repita un bloque de código varias veces, ya sea un número específico de veces o mientras una condición sea verdadera.

### Bucle `mientras` (While Loop)

El bucle `mientras` repite un bloque de código **mientras** una condición sea verdadera. La condición se verifica antes de cada repetición.

**Sintaxis:**

```espanoloo
mientras (condicion_es_verdadera) {
    // Código que se repite
}
```

**Ejemplo: Contar del 1 al 5**

```espanoloo
contador: entero = 1;

mientras (contador <= 5) {
    imprimir("Número: " + contador);
    contador = contador + 1; // ¡Importante! Si no cambiamos 'contador', el bucle nunca terminará.
}
// Salida:
// Número: 1
// Número: 2
// Número: 3
// Número: 4
// Número: 5
```

### Bucle `para` (For Loop)

El bucle `para` es ideal cuando sabes de antemano cuántas veces quieres que se repita algo, o cuando quieres iterar sobre una secuencia de números.

**Sintaxis:**

```espanoloo
para (inicializacion; condicion; actualizacion) {
    // Código que se repite
}
```

*   `inicializacion`: Se ejecuta una vez al principio del bucle (ej. `i: entero = 0;`).
*   `condicion`: Se verifica antes de cada repetición. Si es `verdadero`, el bucle continúa.
*   `actualizacion`: Se ejecuta al final de cada repetición (ej. `i = i + 1;`).

**Ejemplo: Contar del 0 al 2**

```espanoloo
para (i: entero = 0; i < 3; i = i + 1) {
    imprimir("Iteración: " + i);
}
// Salida:
// Iteración: 0
// Iteración: 1
// Iteración: 2
```

### Bucle `hacer mientras` (Do-While Loop)

El bucle `hacer mientras` es similar al `mientras`, pero con una diferencia clave: el bloque de código se ejecuta **al menos una vez** antes de que se verifique la condición por primera vez.

**Sintaxis:**

```espanoloo
hacer {
    // Código que se repite
} mientras (condicion_es_verdadera);
```

**Ejemplo: Pedir un número hasta que sea positivo**

```espanoloo
numero_ingresado: entero = -1; // Inicializamos con un valor que hará que el bucle se ejecute al menos una vez

hacer {
    // En un programa real, aquí pedirías al usuario que ingrese un número.
    // Por simplicidad, simularemos que el usuario ingresa 5 en la segunda iteración.
    imprimir("Ingrese un número positivo:");
    si (numero_ingresado == -1) { // Simula la primera entrada
        numero_ingresado = -5;
    } sino { // Simula la segunda entrada
        numero_ingresado = 5;
    }
} mientras (numero_ingresado <= 0);

imprimir("¡Gracias! Ingresaste el número positivo: " + numero_ingresado);
// Salida (simulada):
// Ingrese un número positivo:
// Ingrese un número positivo:
// ¡Gracias! Ingresaste el número positivo: 5
```

Los bucles son herramientas poderosas para automatizar tareas repetitivas y son esenciales en casi cualquier programa.

## Funciones: Organizar tu Código

A medida que tus programas crecen, te darás cuenta de que a menudo realizas las mismas tareas o secuencias de instrucciones varias veces. Para evitar repetir código y mantenerlo organizado, usamos las **funciones**.

Una función es como una "mini-programa" dentro de tu programa principal. Es un bloque de código que realiza una tarea específica y que puedes llamar (ejecutar) cuantas veces quieras, desde diferentes partes de tu programa.

### ¿Por qué usar funciones?

*   **Organización**: Dividen tu programa en partes más pequeñas y manejables, haciendo que sea más fácil de entender.
*   **Reutilización**: Escribes el código una vez y lo usas muchas veces.
*   **Mantenimiento**: Si necesitas cambiar cómo funciona una tarea, solo la modificas en un lugar (dentro de la función).
*   **Abstracción**: Puedes usar una función sin saber exactamente cómo funciona por dentro, solo necesitas saber qué hace y qué necesita.

### Definiendo una Función

En EspañolOO, defines una función usando la palabra clave `funcion`, seguida de su nombre, los parámetros (información que necesita para trabajar) y, opcionalmente, el tipo de valor que devolverá.

**Sintaxis:**

```espanoloo
funcion nombre_de_la_funcion(parametro1: Tipo1, parametro2: Tipo2): TipoDeRetorno {
    // Código que la función ejecuta
    retornar valor; // Opcional, si la función devuelve algo
}
```

*   `nombre_de_la_funcion`: Un nombre descriptivo para lo que hace la función.
*   `parametroX: TipoX`: Son las "entradas" que la función espera. Cada parámetro tiene un nombre y un tipo. Son opcionales.
*   `TipoDeRetorno`: El tipo de dato que la función "devuelve" como resultado. Si la función no devuelve nada, puedes omitirlo o usar `nulo`.
*   `retornar valor;`: La palabra clave `retornar` se usa para enviar un resultado de vuelta al lugar donde se llamó la función.

**Ejemplo: Función sin parámetros ni retorno (procedimiento)**

```espanoloo
funcion saludar() {
    imprimir("¡Hola a todos!");
}

saludar(); // Llamamos a la función para que se ejecute
// Salida: ¡Hola a todos!
```

**Ejemplo: Función con parámetros y sin retorno**

```espanoloo
funcion saludar_a_persona(nombre: cadena) {
    imprimir("¡Hola, " + nombre + "!");
}

saludar_a_persona("María"); // Llamamos a la función, pasándole "María" como 'nombre'
saludar_a_persona("Pedro"); // La misma función, con otro nombre
// Salida:
// ¡Hola, María!
// ¡Hola, Pedro!
```

**Ejemplo: Función con parámetros y con retorno**

```espanoloo
funcion sumar(numero1: entero, numero2: entero): entero {
    resultado: entero = numero1 + numero2;
    retornar resultado; // Devolvemos la suma
}

// Llamamos a la función y guardamos su resultado en una variable
suma_total: entero = sumar(5, 3);
imprimir("La suma es: " + suma_total); // Salida: La suma es: 8

// También podemos usar el resultado directamente
imprimir("Otra suma: " + sumar(10, 2)); // Salida: Otra suma: 12
```

Las funciones son una de las herramientas más importantes en programación para escribir código limpio, eficiente y fácil de mantener.

## Objetos: Pensar en el Mundo Real con Código

Hasta ahora, hemos visto cómo guardar información (variables), tomar decisiones (`si-sino`) y repetir acciones (bucles). Pero, ¿cómo modelamos cosas más complejas, como un perro, un coche o un usuario en un sistema? Para eso, usamos la **Programación Orientada a Objetos (POO)**.

La POO nos permite pensar en nuestro programa como un conjunto de "objetos" que interactúan entre sí, al igual que los objetos en el mundo real.

### ¿Qué es un Objeto?

Un objeto es una entidad que tiene:
*   **Características (Atributos)**: Son las propiedades que describen al objeto. Por ejemplo, un perro tiene un nombre, una raza y una edad.
*   **Acciones (Métodos)**: Son las cosas que el objeto puede hacer. Un perro puede ladrar, comer o dormir.

### ¿Qué es una Clase?

Una **clase** es como un "plano" o una "plantilla" para crear objetos. No es el objeto en sí, sino la descripción de cómo deben ser los objetos de ese tipo.

Por ejemplo, la clase `Perro` sería el plano que describe que todos los perros tienen un nombre, una raza y pueden ladrar. Luego, puedes crear muchos objetos `Perro` diferentes (Fido, Max, Luna) a partir de ese mismo plano.

### Definiendo una Clase en EspañolOO

En EspañolOO, defines una clase usando la palabra clave `clase`.

**Sintaxis:**

```espanoloo
clase NombreDeLaClase {
    // Atributos (características)
    publico atributo1: Tipo1;
    privado atributo2: Tipo2;

    // Constructor (método especial para crear objetos)
    publico constructor(parametro1: Tipo1) {
        este.atributo1 = parametro1;
    }

    // Métodos (acciones)
    publico accion1(): TipoDeRetorno {
        // Código de la acción
    }
}
```

*   `publico` / `privado`: Son **modificadores de acceso**. `publico` significa que cualquiera puede ver o cambiar esa característica/acción. `privado` significa que solo la propia clase puede verla o cambiarla.
*   `constructor`: Es un método especial que se ejecuta automáticamente cuando creas un nuevo objeto de esa clase. Se usa para darle valores iniciales a los atributos del objeto.
*   `este`: Dentro de una clase, `este` se refiere al objeto actual que se está usando.

**Ejemplo: Clase `Perro`**

```espanoloo
clase Perro {
    publico nombre: cadena;
    publico raza: cadena;
    privado edad: entero; // La edad es privada, solo la clase Perro la maneja directamente

    // Constructor: se ejecuta al crear un nuevo Perro
    publico constructor(nombre_param: cadena, raza_param: cadena, edad_param: entero) {
        este.nombre = nombre_param;
        este.raza = raza_param;
        este.edad = edad_param;
    }

    // Método: lo que el perro puede hacer
    publico ladrar() {
        imprimir(este.nombre + " dice: ¡Guau guau!");
    }

    publico obtenerEdad(): entero {
        retornar este.edad;
    }
}
```

### Creando Objetos (Instanciación)

Una vez que tienes una clase (el plano), puedes crear objetos (las "casas" reales) a partir de ella usando la palabra clave `nuevo`.

**Sintaxis:**

```espanoloo
nombre_del_objeto: NombreDeLaClase = nuevo NombreDeLaClase(argumentos_para_constructor);
```

**Ejemplo: Creando objetos `Perro`**

```espanoloo
// Creamos un objeto 'Perro' llamado 'fido'
fido: Perro = nuevo Perro("Fido", "Labrador", 3);

// Creamos otro objeto 'Perro' llamado 'max'
max: Perro = nuevo Perro("Max", "Pastor Alemán", 5);

// Accediendo a atributos y llamando métodos
imprimir("El nombre de mi perro es: " + fido.nombre); // Accedemos al atributo 'nombre'
fido.ladrar(); // Llamamos al método 'ladrar' de 'fido'

imprimir("La raza de Max es: " + max.raza);
max.ladrar();

imprimir("La edad de Fido es: " + fido.obtenerEdad()); // Accedemos a la edad a través de un método público
```

La Programación Orientada a Objetos es una forma muy poderosa de organizar programas complejos, haciendo que el código sea más modular, reutilizable y fácil de entender, al modelar las cosas como objetos del mundo real.
