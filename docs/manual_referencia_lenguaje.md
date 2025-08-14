# Manual de Referencia del Lenguaje EspañolOO

## Introducción

EspañolOO es un lenguaje de programación orientado a objetos diseñado con una misión clara: democratizar el acceso al mundo del software para la comunidad hispanohablante. Su principal objetivo es permitir que jóvenes y niños, así como cualquier persona interesada, puedan aprender los fundamentos de la programación y la lógica computacional sin la barrera inicial del idioma inglés.

Creemos firmemente que la habilidad de programar, de pensar algorítmicamente y de resolver problemas mediante el código, es una competencia básica esencial en el siglo XXI, al mismo nivel que el dominio de la lengua nativa, las matemáticas y las ciencias naturales. EspañolOO busca ser el puente que conecte a las nuevas generaciones con esta habilidad fundamental, permitiéndoles concentrarse en los conceptos y la lógica, en lugar de en la memorización de palabras reservadas en un idioma extranjero.

Con una sintaxis intuitiva y palabras reservadas completamente en castellano, EspañolOO facilita una curva de aprendizaje suave, haciendo que la programación sea una experiencia más natural y accesible. Este manual servirá como una guía completa para entender y utilizar EspañolOO, desde sus fundamentos más básicos hasta sus características más avanzadas de programación orientada a objetos.

## Fundamentos del Lenguaje

### Tipos de Datos Básicos

EspañolOO soporta los tipos de datos fundamentales necesarios para construir cualquier aplicación.

*   **`entero`**: Representa números enteros, tanto positivos como negativos.
    ```espanoloo
    edad: entero = 25;
    cantidad_productos: entero = -100;
    ```
*   **`decimal`**: Representa números con punto decimal (números de coma flotante).
    ```espanoloo
    precio: decimal = 19.99;
    temperatura: decimal = 36.5;
    ```
*   **`cadena`**: Representa secuencias de caracteres (texto). Las cadenas deben ir encerradas entre comillas dobles (`"`).
    ```espanoloo
    nombre: cadena = "Juan Pérez";
    mensaje: cadena = "Hola, mundo!";
    ```
*   **`booleano`**: Representa valores lógicos, que pueden ser `verdadero` o `falso`.
    ```espanoloo
    es_activo: booleano = verdadero;
    tiene_permiso: booleano = falso;
    ```
*   **`nulo`**: Representa la ausencia de valor.
    ```espanoloo
    valor_nulo: nulo = nulo;
    ```

### Variables y Asignación

Las variables son contenedores para almacenar datos. En EspañolOO, las variables deben ser declaradas con un tipo explícito antes de ser utilizadas.

**Declaración de Variables:**
Se utiliza la sintaxis `nombre_variable: tipo;` para declarar una variable.

```espanoloo
// Declaración de variables sin valor inicial
contador: entero;
saludo: cadena;
```

**Asignación de Valores:**
Se utiliza el operador de asignación (`=`) para dar un valor a una variable.

```espanoloo
// Declaración y asignación en la misma línea
puntuacion: entero = 100;
esta_logueado: booleano = verdadero;

// Asignación posterior
contador = 50;
saludo = "¡Bienvenido!";
```

**Constantes:**
Para declarar una constante, cuyo valor no puede cambiar una vez asignado, se utiliza la palabra reservada `constante`.

```espanoloo
constante PI: decimal = 3.14159;
constante MAX_INTENTOS: entero = 3;
```

### Operadores

EspañolOO soporta los operadores comunes para realizar operaciones aritméticas, lógicas y de comparación.

#### Operadores Aritméticos

| Operador | Descripción | Ejemplo | Resultado |
| :------- | :---------- | :------ | :-------- |
| `+`      | Suma        | `10 + 5`  | `15`      |
| `-`      | Resta       | `10 - 5`  | `5`       |
| `*`      | Multiplicación | `10 * 5`  | `50`      |
| `/`      | División    | `10 / 4`  | `2.5`     |
| `%`      | Módulo (resto de la división) | `10 % 3`  | `1`       |

```espanoloo
resultado_suma: entero = 20 + 5;     // 25
resultado_resta: entero = 20 - 5;    // 15
resultado_multi: entero = 4 * 5;     // 20
resultado_div: decimal = 10.0 / 4.0; // 2.5
resultado_mod: entero = 10 % 3;      // 1
```

#### Operadores de Comparación

Estos operadores devuelven un valor `booleano` (`verdadero` o `falso`).

| Operador | Descripción | Ejemplo | Resultado |
| :------- | :---------- | :------ | :-------- |
| `==`     | Igual a     | `5 == 5`  | `verdadero` |
| `!=`     | Diferente de | `5 != 10` | `verdadero` |
| `<`      | Menor que   | `5 < 10`  | `verdadero` |
| `>`      | Mayor que   | `10 > 5`  | `verdadero` |
| `<=`     | Menor o igual que | `5 <= 5`  | `verdadero` |
| `>=`     | Mayor o igual que | `10 >= 5` | `verdadero` |

```espanoloo
es_igual: booleano = (10 == 10); // verdadero
es_mayor: booleano = (20 > 15);  // verdadero
```

#### Operadores Lógicos

Estos operadores se utilizan para combinar expresiones booleanas.

| Operador | Descripción | Ejemplo | Resultado |
| :------- | :---------- | :------ | :-------- |
| `y`      | AND lógico  | `verdadero y falso` | `falso` |
| `o`      | OR lógico   | `verdadero o falso` | `verdadero` |
| `no`     | NOT lógico  | `no verdadero` | `falso` |

```espanoloo
condicion1: booleano = verdadero;
condicion2: booleano = falso;

resultado_and: booleano = condicion1 y condicion2; // falso
resultado_or: booleano = condicion1 o condicion2;   // verdadero
resultado_not: booleano = no condicion1;           // falso
```

### Comentarios

Los comentarios son notas que los programadores añaden al código para hacerlo más comprensible. El compilador ignora los comentarios.

*   **Comentarios de una sola línea**: Comienzan con `//` y continúan hasta el final de la línea.
    ```espanoloo
    // Esto es un comentario de una sola línea
    x: entero = 10; // Asignamos 10 a la variable x
    ```
*   **Comentarios multilínea**: Comienzan con `/*` y terminan con `*/`. Pueden abarcar varias líneas.
    ```espanoloo
    /*
      Este es un comentario
      que abarca varias líneas.
      Es útil para explicaciones más largas.
    */
    funcion saludar() {
        // ...
    }
    ```

## Estructuras de Control

Las estructuras de control permiten al programador controlar el flujo de ejecución de un programa, tomando decisiones o repitiendo bloques de código.

### Condicionales

Las sentencias condicionales permiten ejecutar diferentes bloques de código dependiendo de si una condición es `verdadero` o `falso`.

*   **`si`**: Ejecuta un bloque de código si la condición es verdadera.

    ```espanoloo
    edad: entero = 18;
    si (edad >= 18) {
        imprimir("Eres mayor de edad.");
    }
    ```

*   **`sino`**: Se utiliza junto con `si` para ejecutar un bloque de código alternativo si la condición del `si` es falsa.

    ```espanoloo
    temperatura: decimal = 25.5;
    si (temperatura > 30) {
        imprimir("Hace mucho calor.");
    } sino {
        imprimir("La temperatura es agradable.");
    }
    ```

*   **`sino si`**: Permite evaluar múltiples condiciones en secuencia.

    ```espanoloo
    puntuacion: entero = 75;
    si (puntuacion >= 90) {
        imprimir("Excelente.");
    } sino si (puntuacion >= 70) {
        imprimir("Notable.");
    } sino si (puntuacion >= 50) {
        imprimir("Aprobado.");
    } sino {
        imprimir("Reprobado.");
    }
    ```

### Bucles

Los bucles permiten repetir un bloque de código varias veces.

*   **`mientras` (Bucle While)**: Repite un bloque de código mientras una condición sea verdadera.

    ```espanoloo
    contador: entero = 0;
    mientras (contador < 5) {
        imprimir("Contador: " + contador);
        contador = contador + 1;
    }
    ```

*   **`para` (Bucle For)**: Repite un bloque de código un número específico de veces, o itera sobre una secuencia. La sintaxis es `para (inicialización; condición; actualización) { ... }`.

    ```espanoloo
    para (i: entero = 0; i < 3; i = i + 1) {
        imprimir("Iteración número: " + i);
    }
    ```

*   **`hacer mientras` (Bucle Do-While)**: Similar a `mientras`, pero garantiza que el bloque de código se ejecute al menos una vez antes de evaluar la condición.

    ```espanoloo
    opcion: entero = 0;
    hacer {
        imprimir("Ingrese 1 para continuar, 0 para salir.");
        // Aquí iría la lógica para leer la opción del usuario
        // opcion = leer_entrada();
    } mientras (opcion != 0);
    ```

### Control de Flujo en Bucles

EspañolOO proporciona palabras clave para alterar el flujo normal de los bucles.

*   **`romper`**: Termina la ejecución del bucle más interno y continúa el programa en la sentencia inmediatamente posterior al bucle.

    ```espanoloo
    para (i: entero = 0; i < 10; i = i + 1) {
        si (i == 5) {
            romper; // Sale del bucle cuando i es 5
        }
        imprimir("Número: " + i);
    }
    // La ejecución continúa aquí después del bucle
    ```

*   **`continuar`**: Salta la iteración actual del bucle más interno y pasa a la siguiente iteración.

    ```espanoloo
    para (i: entero = 0; i < 5; i = i + 1) {
        si (i == 2) {
            continuar; // Salta la impresión cuando i es 2
        }
        imprimir("Valor: " + i);
    }
    ```

*   **`retornar`**: Se utiliza dentro de funciones para finalizar su ejecución y, opcionalmente, devolver un valor. (Se detallará más en la sección de Funciones).

    ```espanoloo
    funcion sumar(a: entero, b: entero): entero {
        retornar a + b; // Devuelve la suma de a y b
    }
    ```

## Funciones y Procedimientos

Las funciones y procedimientos son bloques de código reutilizables que realizan una tarea específica. Ayudan a organizar el código, hacerlo más modular y fácil de mantener.

### Definición de Funciones

En EspañolOO, las funciones se definen utilizando la palabra clave `funcion`, seguida de un nombre, una lista de parámetros (opcional), y un tipo de retorno (opcional).

**Sintaxis Básica:**

```espanoloo
funcion nombre_funcion(parametro1: Tipo1, parametro2: Tipo2): TipoRetorno {
    // Cuerpo de la función
    // Realiza operaciones
    retornar valor; // Opcional, si la función devuelve un valor
}
```

*   **`nombre_funcion`**: Un identificador único para la función.
*   **`parametroX: TipoX`**: Los parámetros son variables que la función espera recibir. Cada parámetro debe tener un nombre y un tipo.
*   **`TipoRetorno`**: El tipo de dato que la función devolverá. Si la función no devuelve ningún valor (es un procedimiento), se puede omitir el tipo de retorno o especificar `nulo`.

**Ejemplos:**

```espanoloo
// Función que no devuelve valor (procedimiento)
funcion saludar(nombre: cadena) {
    imprimir("Hola, " + nombre + "!");
}

// Función que devuelve un valor
funcion sumar(a: entero, b: entero): entero {
    retornar a + b;
}

// Función sin parámetros
funcion obtener_mensaje(): cadena {
    retornar "Este es un mensaje.";
}
```

### Llamada a Funciones

Para ejecutar una función, se utiliza su nombre seguido de paréntesis, pasando los argumentos necesarios.

```espanoloo
saludar("Ana"); // Llama a la función saludar

resultado_suma: entero = sumar(10, 20); // Llama a sumar y guarda el resultado
imprimir("La suma es: " + resultado_suma);

mensaje_obtenido: cadena = obtener_mensaje();
imprimir(mensaje_obtenido);
```

### Ámbito de Variables (Scopes)

El ámbito de una variable determina dónde puede ser accedida en el programa. EspañolOO maneja ámbitos de bloque y de función.

*   **Ámbito Global:** Las variables declaradas fuera de cualquier función o bloque son globales y pueden ser accedidas desde cualquier parte del programa.

    ```espanoloo
    variable_global: entero = 100;

    funcion mostrar_global() {
        imprimir("Desde la función: " + variable_global);
    }

    mostrar_global(); // Imprime: Desde la función: 100
    imprimir("Desde fuera: " + variable_global); // Imprime: Desde fuera: 100
    ```

*   **Ámbito de Bloque:** Las variables declaradas dentro de un bloque de código (delimitado por `{}`) solo son accesibles dentro de ese bloque.

    ```espanoloo
    si (verdadero) {
        variable_bloque: cadena = "Hola";
        imprimir(variable_bloque);
    }
    // imprimir(variable_bloque); // Esto causaría un error: variable_bloque no está definida aquí
    ```

### Funciones Anónimas (Lambdas)

EspañolOO permite definir funciones sin nombre, conocidas como funciones anónimas o lambdas. Son útiles para tareas cortas o cuando una función solo se necesita una vez.

**Sintaxis:**

```espanoloo
(parametro1: Tipo1, parametro2: Tipo2) => expresion_o_sentencia_unica
```

**Ejemplos:**

```espanoloo
// Asignar una lambda a una variable
multiplicar_por_dos = (x: entero) => x * 2;
resultado: entero = multiplicar_por_dos(5); // resultado será 10

// Usar una lambda directamente (por ejemplo, en una función de orden superior si existiera)
// lista.map((elemento: entero) => elemento * 10);
```

## Programación Orientada a Objetos (POO)

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite organizar el código en torno a "objetos", que son entidades que combinan datos (atributos) y comportamiento (métodos). Este enfoque facilita la creación de programas modulares, reutilizables y fáciles de mantener, modelando el mundo real de una manera más intuitiva.

### Clases y Objetos

En EspañolOO, las clases son los planos o plantillas para crear objetos, mientras que los objetos son instancias concretas de esas clases.

#### Definición de Clases

Las clases se definen utilizando la palabra clave `clase`, seguida de un nombre. Dentro de una clase, se definen sus atributos (variables) y métodos (funciones).

**Sintaxis Básica:**

```espanoloo
clase NombreClase {
    // Atributos (variables de la clase)
    modificador_acceso nombre_atributo: Tipo;

    // Constructor (método especial para crear objetos)
    publico constructor(parametro1: Tipo1) {
        este.nombre_atributo = parametro1;
    }

    // Métodos (funciones de la clase)
    modificador_acceso nombre_metodo(parametro: Tipo): TipoRetorno {
        // Cuerpo del método
        retornar valor;
    }
}
```

*   **`NombreClase`**: Un identificador único para la clase.
*   **`modificador_acceso`**: Define la visibilidad de atributos y métodos (`publico`, `privado`, `protegido`).
*   **`constructor`**: Un método especial que se ejecuta automáticamente cuando se crea un nuevo objeto de la clase. Se utiliza para inicializar los atributos del objeto.
*   **`este`**: Dentro de un método o constructor, `este` se refiere al objeto actual, permitiendo acceder a sus propios atributos y métodos.

**Ejemplo de Clase `Persona`:**

```espanoloo
clase Persona {
    privado nombre: cadena;
    privado edad: entero;

    // Constructor
    publico constructor(nombre_param: cadena, edad_param: entero) {
        este.nombre = nombre_param;
        este.edad = edad_param;
    }

    // Métodos públicos
    publico obtenerNombre(): cadena {
        retornar este.nombre;
    }

    publico obtenerEdad(): entero {
        retornar este.edad;
    }

    publico cumplirAnios() {
        este.edad = este.edad + 1;
        imprimir(este.nombre + " ha cumplido " + este.edad + " años.");
    }
}
```

#### Modificadores de Acceso

EspañolOO soporta tres modificadores de acceso para controlar la visibilidad de los atributos y métodos de una clase:

*   **`publico`**: Los miembros declarados como `publico` son accesibles desde cualquier parte del programa, incluso desde fuera de la clase.
*   **`privado`**: Los miembros declarados como `privado` solo son accesibles desde dentro de la propia clase donde fueron definidos. Esto promueve el encapsulamiento.
*   **`protegido`**: Los miembros declarados como `protegido` son accesibles desde dentro de la propia clase y desde cualquier clase que herede de ella (clases hijas).

**Ejemplo de Uso de Modificadores de Acceso:**

```espanoloo
clase CuentaBancaria {
    privado saldo: decimal;
    publico titular: cadena;

    publico constructor(titular_param: cadena, saldo_inicial: decimal) {
        este.titular = titular_param;
        este.saldo = saldo_inicial;
    }

    publico depositar(cantidad: decimal) {
        si (cantidad > 0) {
            este.saldo = este.saldo + cantidad;
            imprimir("Depósito de " + cantidad + ". Nuevo saldo: " + este.saldo);
        }
    }

    privado verificarSaldo(cantidad: decimal): booleano {
        retornar este.saldo >= cantidad;
    }

    publico retirar(cantidad: decimal) {
        si (este.verificarSaldo(cantidad)) {
            este.saldo = este.saldo - cantidad;
            imprimir("Retiro de " + cantidad + ". Nuevo saldo: " + este.saldo);
        } sino {
            imprimir("Saldo insuficiente.");
        }
    }
}
```

#### Instanciación de Objetos

Una vez que una clase ha sido definida, se pueden crear objetos (instancias) de esa clase utilizando la palabra clave `nuevo` y llamando al constructor de la clase.

**Sintaxis:**

```espanoloo
nombre_objeto: NombreClase = nuevo NombreClase(argumentos_constructor);
```

**Ejemplo de Instanciación y Uso:**

```espanoloo
// Crear un objeto de la clase Persona
juan: Persona = nuevo Persona("Juan Pérez", 30);

// Acceder a métodos públicos del objeto
imprimir("Nombre: " + juan.obtenerNombre()); // Imprime: Nombre: Juan Pérez
imprimir("Edad: " + juan.obtenerEdad());   // Imprime: Edad: 30

juan.cumplirAnios(); // Llama al método cumplirAnios
imprimir("Nueva edad: " + juan.obtenerEdad()); // Imprime: Nueva edad: 31

// Crear un objeto de la clase CuentaBancaria
mi_cuenta: CuentaBancaria = nuevo CuentaBancaria("María López", 1000.0);
mi_cuenta.depositar(200.0);
mi_cuenta.retirar(150.0);
mi_cuenta.retirar(2000.0); // Saldo insuficiente
```

### Herencia

La herencia es un pilar fundamental de la POO que permite a una clase (clase hija o subclase) heredar atributos y métodos de otra clase (clase padre o superclase). Esto promueve la reutilización de código y la creación de jerarquías de clases que modelan relaciones "es un tipo de".

#### Herencia Simple

En EspañolOO, se utiliza la palabra clave `hereda` para indicar que una clase hereda de otra.

**Sintaxis:**

```espanoloo
clase ClaseHija hereda ClasePadre {
    // Nuevos atributos y métodos
    // O sobreescritura de métodos del padre
}
```

*   **`ClaseHija`**: La clase que hereda.
*   **`ClasePadre`**: La clase de la que se hereda.

**Ejemplo de Herencia:**

```espanoloo
clase Animal {
    publico nombre: cadena;

    publico constructor(nombre_param: cadena) {
        este.nombre = nombre_param;
    }

    publico hacerSonido() {
        imprimir("El animal hace un sonido.");
    }
}

clase Perro hereda Animal {
    publico raza: cadena;

    publico constructor(nombre_param: cadena, raza_param: cadena) {
        super(nombre_param); // Llama al constructor de la clase padre
        este.raza = raza_param;
    }

    // Sobreescritura del método hacerSonido
    publico hacerSonido() {
        imprimir("El perro ladra: ¡Guau guau!");
    }

    publico moverCola() {
        imprimir(este.nombre + " mueve la cola.");
    }
}

// Uso de las clases
mi_animal: Animal = nuevo Animal("Genérico");
mi_animal.hacerSonido(); // Imprime: El animal hace un sonido.

mi_perro: Perro = nuevo Perro("Fido", "Labrador");
mi_perro.hacerSonido(); // Imprime: El perro ladra: ¡Guau guau!
mi_perro.moverCola();   // Imprime: Fido mueve la cola.
imprimir("Nombre del perro: " + mi_perro.nombre); // Acceso a atributo heredado
```

#### La palabra clave `super`

La palabra clave `super` se utiliza dentro de una clase hija para referirse a la clase padre. Es comúnmente usada para:

*   **Llamar al constructor de la clase padre**: Como se vio en el ejemplo anterior, `super(argumentos)` invoca el constructor de la clase padre, asegurando que la parte heredada del objeto se inicialice correctamente.
*   **Acceder a métodos sobreescritos del padre**: Si un método ha sido sobreescrito en la clase hija, se puede llamar a la versión del padre usando `super.nombre_metodo()`.

#### Sobreescritura de Métodos

La sobreescritura de métodos permite a una clase hija proporcionar una implementación específica para un método que ya está definido en su clase padre. La firma del método (nombre, número y tipo de parámetros) debe ser la misma.

**Ejemplo de Sobreescritura:**

```espanoloo
clase Gato hereda Animal {
    publico constructor(nombre_param: cadena) {
        super(nombre_param);
    }

    publico hacerSonido() {
        super.hacerSonido(); // Llama al método del padre primero
        imprimir("El gato maúlla: ¡Miau miau!");
    }
}

mi_gato: Gato = nuevo Gato("Bigotes");
mi_gato.hacerSonido();
// Imprime:
// El animal hace un sonido.
// El gato maúlla: ¡Miau miau!
```

#### Clases Abstractas

Una clase abstracta es una clase que no puede ser instanciada directamente. Sirve como una plantilla para otras clases y puede contener métodos abstractos (métodos declarados pero sin implementación) y métodos concretos (con implementación). Las clases que heredan de una clase abstracta deben implementar todos sus métodos abstractos, a menos que también sean abstractas.

*   Se utiliza la palabra clave `abstracto` para declarar una clase o un método como abstracto.

**Sintaxis:**

```espanoloo
abstracto clase NombreClaseAbstracta {
    publico abstracto metodoAbstracto(): nulo;
    publico metodoConcreto() {
        // Implementación
    }
}

clase ClaseConcreta hereda NombreClaseAbstracta {
    publico metodoAbstracto(): nulo {
        // Implementación del método abstracto
    }
}
```

**Ejemplo de Clases Abstractas:**

```espanoloo
abstracto clase FiguraGeometrica {
    publico abstracto calcularArea(): decimal;
    publico abstracto calcularPerimetro(): decimal;

    publico mostrarMensaje() {
        imprimir("Esta es una figura geométrica.");
    }
}

clase Circulo hereda FiguraGeometrica {
    privado radio: decimal;

    publico constructor(radio_param: decimal) {
        este.radio = radio_param;
    }

    publico calcularArea(): decimal {
        retornar 3.14159 * este.radio * este.radio;
    }

    publico calcularPerimetro(): decimal {
        retornar 2 * 3.14159 * este.radio;
    }
}

// Uso
mi_circulo: Circulo = nuevo Circulo(5.0);
mi_circulo.mostrarMensaje(); // Imprime: Esta es una figura geométrica.
imprimir("Área del círculo: " + mi_circulo.calcularArea());
```

### Polimorfismo

El polimorfismo es la capacidad de un objeto de tomar muchas formas. En POO, se refiere a la habilidad de diferentes clases de responder a la misma llamada de método de maneras distintas, siempre que compartan una interfaz común o una jerarquía de herencia.

#### Polimorfismo de Subtipos

El polimorfismo de subtipos permite que una variable de un tipo de clase padre pueda referenciar objetos de cualquier clase hija. Esto significa que se puede escribir código más genérico y flexible.

**Ejemplo:**

```espanoloo
// Reutilizando la clase Animal y Perro del ejemplo de Herencia

funcion hacerSonidoGenerico(animal_param: Animal) {
    animal_param.hacerSonido();
}

mi_animal_generico: Animal = nuevo Animal("Desconocido");
mi_perro_polimorfico: Animal = nuevo Perro("Buddy", "Golden Retriever"); // Una variable de tipo Animal referencia un objeto Perro

hacerSonidoGenerico(mi_animal_generico); // Imprime: El animal hace un sonido.
hacerSonidoGenerico(mi_perro_polimorfico); // Imprime: El perro ladra: ¡Guau guau! (Se llama al método sobreescrito de Perro)
```

#### Interfaces

Una interfaz define un contrato: un conjunto de métodos que una clase debe implementar. A diferencia de las clases abstractas, las interfaces solo contienen declaraciones de métodos (sin implementación) y no pueden tener atributos. Una clase puede implementar múltiples interfaces, lo que permite simular la herencia múltiple de comportamiento.

*   Se utiliza la palabra clave `interfaz` para declarar una interfaz.
*   Las clases utilizan la palabra clave `implementa` para indicar que implementan una o más interfaces.

**Sintaxis:**

```espanoloo
interfaz NombreInterfaz {
    publico metodoA(): TipoRetornoA;
    publico metodoB(param: Tipo): TipoRetornoB;
}

clase MiClase implementa NombreInterfaz {
    publico metodoA(): TipoRetornoA {
        // Implementación de metodoA
    }
    publico metodoB(param: Tipo): TipoRetornoB {
        // Implementación de metodoB
    }
}
```

**Ejemplo de Interfaces:**

```espanoloo
interfaz Volador {
    publico volar(): nulo;
}

interfaz Nadador {
    publico nadar(): nulo;
}

clase Pato hereda Animal implementa Volador, Nadador {
    publico constructor(nombre_param: cadena) {
        super(nombre_param);
    }

    publico hacerSonido() {
        imprimir("Cuac cuac!");
    }

    publico volar() {
        imprimir(este.nombre + " está volando.");
    }

    publico nadar() {
        imprimir(este.nombre + " está nadando.");
    }
}

// Uso
mi_pato: Pato = nuevo Pato("Donald");
mi_pato.hacerSonido();
mi_pato.volar();
mi_pato.nadar();

// Polimorfismo con interfaces
funcion moverEnElAire(objeto_volador: Volador) {
    objeto_volador.volar();
}

moverEnElAire(mi_pato); // Imprime: Donald está volando.
```

#### Genéricos

Los genéricos permiten escribir código que funciona con diferentes tipos de datos sin sacrificar la seguridad de tipos. Esto es útil para crear estructuras de datos (como listas o contenedores) que pueden almacenar elementos de cualquier tipo, pero manteniendo la información de tipo en tiempo de compilación.

**Sintaxis:**

```espanoloo
clase Contenedor<T> { // T es un parámetro de tipo
    privado elemento: T;

    publico constructor(valor: T) {
        este.elemento = valor;
    }

    publico obtener(): T {
        retornar este.elemento;
    }

    publico establecer(nuevo_valor: T) {
        este.elemento = nuevo_valor;
    }
}
```

*   **`<T>`**: Declara `T` como un parámetro de tipo. Se pueden usar múltiples parámetros (ej. `<K, V>`).

**Ejemplo de Uso de Genéricos:**

```espanoloo
// Contenedor de enteros
contenedor_entero: Contenedor<entero> = nuevo Contenedor<entero>(123);
imprimir("Valor entero: " + contenedor_entero.obtener());
contenedor_entero.establecer(456);

// Contenedor de cadenas
contenedor_cadena: Contenedor<cadena> = nuevo Contenedor<cadena>("Hola Mundo");
imprimir("Valor cadena: " + contenedor_cadena.obtener());
contenedor_cadena.establecer("Adiós");

// Esto generaría un error de tipo en tiempo de compilación:
// contenedor_entero.establecer("Esto es una cadena");
```

## Manejo de Excepciones

El manejo de excepciones es un mecanismo fundamental para gestionar errores y situaciones inesperadas que pueden ocurrir durante la ejecución de un programa. Permite que el programa reaccione de manera controlada a estos eventos, evitando que se detenga abruptamente y proporcionando una experiencia de usuario más robusta.

### Definición de Excepciones

En EspañolOO, las excepciones son objetos que representan un error o una condición excepcional. Se pueden crear excepciones personalizadas heredando de la clase base `Excepcion`.

**Sintaxis:**

```espanoloo
clase MiExcepcion hereda Excepcion {
    publico constructor(mensaje: cadena) {
        super(mensaje);
    }
}
```

*   **`Excepcion`**: La clase base de la que deben heredar todas las excepciones personalizadas.

**Ejemplo de Lanzamiento de Excepciones:**

Se utiliza la palabra clave `lanzar` para generar una excepción.

```espanoloo
funcion dividir(a: entero, b: entero): decimal {
    si (b == 0) {
        lanzar nuevo MiExcepcion("No se puede dividir por cero.");
    }
    retornar a / b;
}
```

### Manejo de Excepciones (try-catch-finally)

Para capturar y gestionar las excepciones lanzadas, se utilizan los bloques `intentar`, `atrapar` y `finalmente`.

*   **`intentar`**: Contiene el código que podría generar una excepción.
*   **`atrapar`**: Contiene el código que se ejecuta si se lanza una excepción dentro del bloque `intentar`. Se puede especificar el tipo de excepción a capturar.

*   **`finalmente`**: Contiene el código que se ejecuta siempre, independientemente de si se lanzó o no una excepción, o si fue capturada.

**Sintaxis:**

```espanoloo
intentar {
    // Código que puede lanzar una excepción
} atrapar (nombre_excepcion: TipoExcepcion) {
    // Código para manejar la excepción
} finalmente {
    // Código que siempre se ejecuta
}
```

**Ejemplo de Manejo de Excepciones:**

```espanoloo
intentar {
    resultado: decimal = dividir(10, 0);
    imprimir("El resultado es: " + resultado);
} atrapar (e: MiExcepcion) {
    imprimir("Error capturado: " + e.obtenerMensaje());
} atrapar (e: Excepcion) { // Captura cualquier otra excepción
    imprimir("Error genérico: " + e.obtenerMensaje());
} finalmente {
    imprimir("Operación de división finalizada.");
}
```

### Aserciones

Las aserciones son declaraciones que se utilizan para verificar suposiciones sobre el estado del programa en un punto específico. Son útiles para la depuración y para asegurar que ciertas condiciones se cumplen durante el desarrollo. Si una aserción es falsa, el programa se detiene con un error.

*   Se utiliza la palabra clave `afirmar`.

**Sintaxis:**

```espanoloo
afirmar(condicion, mensaje_opcional);
```

*   **`condicion`**: Una expresión booleana que se espera que sea verdadera.
*   **`mensaje_opcional`**: Una cadena que se mostrará si la condición es falsa.

**Ejemplo de Aserción:**

```espanoloo
funcion establecerEdad(edad: entero) {
    afirmar(edad >= 0, "La edad no puede ser negativa.");
    este.edad = edad;
}

establecerEdad(25); // OK
establecerEdad(-5); // Lanza un error de aserción con el mensaje especificado
```

## Estructuras de Datos Avanzadas

EspañolOO proporciona soporte para varias estructuras de datos avanzadas que permiten organizar y manipular colecciones de información de manera eficiente. Comprender y utilizar estas estructuras es crucial para escribir programas más complejos y optimizados.

### Arrays y Listas

#### Arrays

Un array es una colección de elementos del mismo tipo, almacenados en posiciones de memoria contiguas y accesibles mediante un índice numérico. Los arrays tienen un tamaño fijo una vez declarados.

**Declaración y Uso:**

```espanoloo
// Declaración de un array de enteros de tamaño 5
numeros: entero[5];

// Inicialización de un array
frutas: cadena[] = ["Manzana", "Pera", "Uva"];

// Acceso a elementos
imprimir(frutas[0]); // Imprime: Manzana
frutas[1] = "Mango"; // Modifica el elemento en el índice 1

// Longitud del array
longitud_frutas: entero = frutas.longitud; // longitud_frutas será 3
```

#### Arrays Multidimensionales

Los arrays pueden tener múltiples dimensiones, útiles para representar tablas o matrices.

```espanoloo
// Declaración e inicialización de una matriz 2x3
matriz: entero[2][3] = [[1, 2, 3], [4, 5, 6]];

// Acceso a elementos
imprimir(matriz[0][1]); // Imprime: 2
```

#### Recorrido de Arrays

Los arrays se pueden recorrer utilizando bucles `para` o `mientras`.

```espanoloo
// Recorrido con bucle para tradicional
para (i: entero = 0; i < frutas.longitud; i = i + 1) {
    imprimir("Fruta en índice " + i + ": " + frutas[i]);
}

// Recorrido con bucle para-cada (si estuviera implementado)
// para (fruta: cadena en frutas) {
//     imprimir(fruta);
// }
```

### Colecciones

EspañolOO proporciona estructuras de datos dinámicas que pueden crecer o encogerse según sea necesario.

#### Listas

Una lista es una colección ordenada de elementos que pueden ser de cualquier tipo. A diferencia de los arrays, las listas pueden cambiar de tamaño dinámicamente.

**Sintaxis y Métodos Comunes:**

```espanoloo
// Declaración de una lista de enteros
lista_numeros: Lista<entero> = nuevo Lista<entero>();

// Añadir elementos
lista_numeros.agregar(10);
lista_numeros.agregar(20);
lista_numeros.agregar(30);

// Acceder a elementos por índice
imprimir(lista_numeros.obtener(1)); // Imprime: 20

// Eliminar elementos por índice
lista_numeros.eliminar(0); // Elimina el 10

// Longitud de la lista
longitud_lista: entero = lista_numeros.longitud; // longitud_lista será 2

// Recorrido de lista (similar a arrays)
para (num: entero en lista_numeros) {
    imprimir(num);
}
```

#### Conjuntos

Un conjunto es una colección no ordenada de elementos únicos. No permite duplicados y es útil para operaciones matemáticas de conjuntos como unión, intersección y diferencia.

**Sintaxis y Métodos Comunes:**

```espanoloo
// Declaración de un conjunto de cadenas
conjunto_letras: Conjunto<cadena> = nuevo Conjunto<cadena>();
conjunto_letras.agregar("A");
conjunto_letras.agregar("B");
conjunto_letras.agregar("A"); // Este duplicado será ignorado

imprimir(conjunto_letras.contiene("B")); // Imprime: verdadero

// Operaciones de conjuntos
conjunto1: Conjunto<entero> = nuevo Conjunto<entero>();
conjunto1.agregar(1); conjunto1.agregar(2);
conjunto2: Conjunto<entero> = nuevo Conjunto<entero>();
conjunto2.agregar(2); conjunto2.agregar(3);

union_conjuntos: Conjunto<entero> = conjunto1.union(conjunto2); // {1, 2, 3}
interseccion_conjuntos: Conjunto<entero> = conjunto1.interseccion(conjunto2); // {2}
```

#### Diccionarios (Mapas)

Un diccionario (o mapa) es una colección de pares clave-valor, donde cada clave es única y se utiliza para recuperar su valor asociado. Las claves pueden ser de cualquier tipo inmutable (como `cadena`, `entero`), y los valores pueden ser de cualquier tipo.

**Sintaxis y Métodos Comunes:**

```espanoloo
// Declaración de un diccionario con claves cadena y valores entero
diccionario_edades: Diccionario<cadena, entero> = nuevo Diccionario<cadena, entero>();

// Añadir pares clave-valor
diccionario_edades.agregar("Juan", 30);
diccionario_edades.agregar("María", 25);

// Acceder a valores por clave
imprimir(diccionario_edades.obtener("Juan")); // Imprime: 30

// Modificar un valor
diccionario_edades.agregar("Juan", 31);

// Eliminar un par clave-valor
diccionario_edades.eliminar("María");

// Comprobar si una clave existe
imprimir(diccionario_edades.contieneClave("Juan")); // Imprime: verdadero
```

#### Colas y Pilas

EspañolOO también puede soportar estructuras de datos lineales como colas (FIFO - First In, First Out) y pilas (LIFO - Last In, First Out), útiles para gestionar el orden de procesamiento de elementos.

**Colas (Queue):**

```espanoloo
cola_tareas: Cola<cadena> = nuevo Cola<cadena>();
cola_tareas.encolar("Tarea 1");
cola_tareas.encolar("Tarea 2");

imprimir(cola_tareas.desencolar()); // Imprime: Tarea 1
imprimir(cola_tareas.desencolar()); // Imprime: Tarea 2
```

**Pilas (Stack):**

```espanoloo
pila_libros: Pila<cadena> = nuevo Pila<cadena>();
pila_libros.apilar("Libro A");
pila_libros.apilar("Libro B");

imprimir(pila_libros.desapilar()); // Imprime: Libro B
imprimir(pila_libros.desapilar()); // Imprime: Libro A
```

### Estructuras de Datos Especializadas

EspañolOO, a través de sus bibliotecas estándar o implementaciones personalizadas, puede manejar estructuras de datos más complejas como árboles y grafos, fundamentales para algoritmos avanzados y modelado de relaciones complejas.

#### Árboles

Un árbol es una estructura de datos jerárquica compuesta por nodos, donde cada nodo tiene un nodo padre (excepto la raíz) y cero o más nodos hijos. Los árboles binarios son un tipo común donde cada nodo tiene como máximo dos hijos (izquierdo y derecho).

**Conceptos Clave:**
*   **Raíz:** El nodo superior del árbol.
*   **Nodo:** Un elemento en el árbol.
*   **Hijo/Padre:** Relación jerárquica entre nodos.
*   **Hoja:** Un nodo sin hijos.
*   **Recorridos:** Formas de visitar todos los nodos de un árbol (in-order, pre-order, post-order, BFS, DFS).

**Ejemplo (Representación Conceptual):**

```espanoloo
clase NodoArbol {
    publico valor: entero;
    publico izquierdo: NodoArbol;
    publico derecho: NodoArbol;

    publico constructor(val: entero) {
        este.valor = val;
        este.izquierdo = nulo;
        este.derecho = nulo;
    }
}

clase ArbolBinarioBusqueda {
    privado raiz: NodoArbol;

    publico constructor() {
        este.raiz = nulo;
    }

    publico insertar(valor: entero) {
        // Lógica para insertar un valor en el árbol
    }

    publico buscar(valor: entero): booleano {
        // Lógica para buscar un valor
        retornar falso;
    }

    publico recorridoInOrder() {
        // Lógica para imprimir los nodos en orden
    }
}
```

#### Grafos

Un grafo es una estructura de datos no lineal que representa un conjunto de objetos (vértices o nodos) donde algunos pares de objetos están conectados por enlaces (aristas). Son útiles para modelar redes, relaciones sociales, rutas de transporte, etc.

**Conceptos Clave:**
*   **Vértice (Nodo):** Un punto en el grafo.
*   **Arista (Enlace):** Una conexión entre dos vértices.
*   **Dirigido/No Dirigido:** Las aristas pueden tener una dirección o no.
*   **Ponderado:** Las aristas pueden tener un peso o costo asociado.

**Ejemplo (Representación Conceptual):**

```espanoloo
clase Grafo {
    privado num_vertices: entero;
    privado lista_adyacencia: Lista<Lista<entero>>;

    publico constructor(vertices: entero) {
        este.num_vertices = vertices;
        este.lista_adyacencia = nuevo Lista<Lista<entero>>();
        para (i: entero = 0; i < vertices; i = i + 1) {
            este.lista_adyacencia.agregar(nuevo Lista<entero>());
        }
    }

    publico agregarArista(origen: entero, destino: entero) {
        este.lista_adyacencia.obtener(origen).agregar(destino);
        // Si es no dirigido, también: este.lista_adyacencia.obtener(destino).agregar(origen);
    }

    publico BFS(inicio: entero) {
        // Implementación de Búsqueda en Amplitud
    }

    publico DFS(inicio: entero) {
        // Implementación de Búsqueda en Profundidad
    }
}
```

#### Tablas Hash (Hash Maps)

Una tabla hash es una estructura de datos que implementa un array asociativo, es decir, mapea claves a valores. Utiliza una función hash para calcular un índice en un array de cubetas o ranuras, donde se almacenan los elementos. Permite una búsqueda, inserción y eliminación de elementos muy rápidas en promedio.

**Conceptos Clave:**
*   **Función Hash:** Convierte una clave en un índice.
*   **Colisión:** Cuando dos claves diferentes producen el mismo índice.
*   **Resolución de Colisiones:** Técnicas para manejar las colisiones (encadenamiento, sondeo lineal, etc.).

**Ejemplo (Representación Conceptual):**

```espanoloo
clase TablaHash<K, V> {
    privado capacidad: entero;
    privado cubetas: Lista<Lista<ParClaveValor<K, V>>>; // Lista de listas para encadenamiento

    clase ParClaveValor<K, V> {
        publico clave: K;
        publico valor: V;

        publico constructor(k: K, v: V) {
            este.clave = k;
            este.valor = v;
        }
    }

    publico constructor(cap: entero) {
        este.capacidad = cap;
        este.cubetas = nuevo Lista<Lista<ParClaveValor<K, V>>>();
        para (i: entero = 0; i < cap; i = i + 1) {
            este.cubetas.agregar(nuevo Lista<ParClaveValor<K, V>>());
        }
    }

    privado funcion calcularHash(clave: K): entero {
        // Implementación de la función hash
        retornar clave.obtenerHashCode() % este.capacidad;
    }

    publico insertar(clave: K, valor: V) {
        // Lógica para insertar un par clave-valor
    }

    publico obtener(clave: K): V {
        // Lógica para obtener un valor por clave
        retornar nulo;
    }

    publico eliminar(clave: K) {
        // Lógica para eliminar un par clave-valor
    }
}
```

## Palabras Reservadas

Las palabras reservadas son identificadores que tienen un significado predefinido en EspañolOO y no pueden ser utilizados como nombres de variables, funciones, clases, etc. A continuación, se presenta un listado completo de las palabras reservadas en EspañolOO:

*   `abstracto`
*   `afirmar`
*   `atrapar`
*   `booleano`
*   `cadena`
*   `clase`
*   `constante`
*   `constructor`
*   `continuar`
*   `decimal`
*   `entero`
*   `este`
*   `falso`
*   `finalmente`
*   `funcion`
*   `hacer`
*   `hereda`
*   `implementa`
*   `intentar`
*   `interfaz`
*   `lanzar`
*   `mientras`
*   `no`
*   `nulo`
*   `nuevo`
*   `o`
*   `para`
*   `privado`
*   `protegido`
*   `publico`
*   `retornar`
*   `romper`
*   `si`
*   `sino`
*   `super`
*   `verdadero`
*   `y`
