# python-crud-creation

Building the foundation to specialize in the web with Django or in databases and taking a step towards becoming a great developer.


# Curso Práctico de Python: Creación de un CRUD

El objetivo de este curso es crear desde cero los principales comandos para trabajar una base de datos con Python.

En este curso de Platzi se creará un proyecto que enseña a programar las 4 principales funcionalidades para trabajar con una base de datos que serán "Crear, Leer, Actualizar y Borrar" conocidos como CRUD por sus siglas en inglés: Create, Read, Update and Delete.


## Turtle Graphics

Es una librería de Python que permite hacer dibujos con distintas formas mediante una serie de comandos que se proporcionan.

Las funciones principales para animar nuestro objeto son las siguientes:

- **forward(distance):** Avanzar una determinada cantidad de píxeles.

- **backward(distance):** Retroceder una determinada cantidad de píxeles.

- **left(angle):** Girar hacia la izquierda un determinado ángulo.

- **right(angle):** Girar hacia la derecha un determinado ángulo.

Por otro lado, puede que en ocasiones queramos desplazarnos de un punto a otro sin dejar rastro. Para ello utilizaremos las siguientes funciones:

- **home(distance):** Desplazarse al origen de coordenadas.

- **goto((x, y)):** Desplazarse a una coordenada en concreto.

- **penup():** Subir el lápiz para no mostrar el rastro.

- **pendown():** Bajar el lápiz para mostrar el rastro.

Por último, puede que queramos cambiar el color o tamaño del lápiz. En ese caso utilizaremos las siguientes funciones gráficas:

- **shape(‘turtle’):** Cambia al objeto tortuga.

- **pencolor(color):** Cambiar al color especificado.

- **pensize(dimension):** Tamaño de la punta del lápiz.


## Operadores aritméticos

| Operador | Notación |
| ---------- | :----------: |
| Paréntesis | ( ) |
| Potencia | ** |
| Multiplicación | * |
| División | / |
| División entera | // |
| Módulo | % |
| Suma | + |
| Resta | - |
| **Operadores de comparación** |
| mayor que | > |
| menor que | < |
| mayor o igual que | >= |
| menor o igual que | <= |
| diferente de | != |
| igual que | == |
| **Operadores lógicos** |
| Operador And | and |
| Operador Or |	or |
| Operador Not | not |
| **Operadores a nivel bit** |
| Desplazamiento de bits a la derecha |	>> |
| Desplazamiento de bits a la izquierda | << |
| Operador lógico “and” a nivel de bits | & |
| Operador lógico “or” a nivel de bits |
| Operador lógico “xor” a nivel de bits | ^ |
| Operador lógico “not” a nivel de bits | ~ |
| **Operadores de asignación** |
| Suma en Asignación | += |
| Resta en Asignación |	-= |
| Multiplicación en Asignación | *= |
| División en Asignación | /= |
| Potencia en Asignación | ** |
| Módulo en Asignación | %= |


## Reglas de Variables

- Pueden contener números y letras.

- No deben comenzar con un número.

- Múltiples palabras se unen con _.

- No se pueden utilizar palabras reservadas.


## Orden de evaluación de expresiones en Python

PEMDAS = Paréntesis, Exponente, Multiplicación, Adicción, Substracción


## Palabras reservadas del lenguaje

| and | del | for | is | raise | assert |
| if | else | elif | from | lambda | return |
| break | global | not | try | class | except |
| or | while | continue | exec | import | yield |
| def | finally | in | print |


## Convenciones en el nombre de las variables

No existen las variables privadas y la reasignación es muy común en python, por lo que algo que nos puede proteger de no cometer errores graves en el uso de las variables es entender las convenciones de nombrado de variables que utilizan los programadores (ya que se puede nombrar una variable de diversas formas, pero eso no significa que se deba).

- variables_regulares: snake_case

- CONSTANTES: Una variable cuyo nombre esté en mayúscula no debería de modificarse.

- _privada: Single Leading Underscore:: una variable que empieza con guion bajo ( “_” ) se deberá tratar como privada y no se deberá acceder fuera de la clase.

- __importante: variables que empiezan con doble guion bajo ( “__”) son variables importantes, muy susceptibles ante modificaciones. 

- Las variables rodeadas por un prefijo y sufijo de subrayado doble (ej: __ str __) quedan reservadas por el intérprete de Python.


## Métodos de strings


| Method | Description |
| --- | --- |
| capitalize() | Convierte el primer carácter en mayúsculas |
| casefold() | Convierte una cadena en minúsculas |
| center() | Devuelve una cadena centrada |
| count() |	Devuelve el número de veces que un valor especificado se produce en una cadena |
| encode() | Devuelve una versión codificada de la cadena |
| endswith() | Devuelve true si los extremos de cadena con el valor especificado |
| expandtabs() | Establece el tamaño de la pestaña de la cadena |
| find() | Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado |
| format() | Formatos especifican los valores de una serie |
| format_map() | Formatos especifican los valores de una serie |
| index() |	Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado |
| isalnum() | Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos |
| isalpha() | Devuelve True si todos los caracteres de la cadena están en el alfabeto |
| isdecimal() | Devuelve True si todos los caracteres de la cadena son decimales |
| isdigit() | Devuelve verdadero si todos los caracteres de la cadena son dígitos |
| isidentifier() | Devuelve True si la cadena es un identificador |
| islower() | Devuelve verdadero si todos los caracteres de la cadena son minúsculas |
| isnumeric() | Devuelve verdadero si todos los caracteres de la cadena son numéricos |
| isprintable() | Devuelve verdadero si todos los caracteres de la cadena son imprimibles |
| isspace() | Devuelve True si todos los caracteres de la cadena son espacios en blanco |
| istitle() | Devuelve True si la cadena sigue las reglas de un título |
| isupper() | Devuelve True si todos los caracteres de la cadena son mayúsculas |
| join() | Se une a los elementos de un iterable al final de la cadena |
| ljust() |	Devuelve una versión justificada izquierda de la cadena |
| lower() |	Convierte una cadena en minúsculas |
| lstrip() | Devuelve una versión de ajuste izquierdo de la cuerda |
| maketrans() |	Devuelve una tabla de traducción para ser utilizado en traducciones |
| partition() |	Devuelve una tupla donde la cadena se separó en tres partes |
| replace() | Devuelve una serie en un valor especificado es reemplazado con un valor especificado |
| rfind() |	Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| rindex() | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| rjust() |	Devuelve una versión justificada derecha de la cadena |
| rpartition() | Devuelve una tupla donde la cadena se separó en tres partes |
| rsplit() | Divide la cadena en el separador especificado y devuelve una lista |
| rstrip() | Devuelve una versión ajuste correcto de la cadena |
| split() |	Divide la cadena en el separador especificado y devuelve una lista |
| splitlines() | Divide la cadena en los saltos de línea y devuelve una lista |
| startswith() | Devuelve true si la cadena comienza con el valor especificado |
| strip() |	Devuelve una versión recortada de la cadena |
| swapcase() | Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa |
| title() |	Convierte el primer carácter de cada palabra en mayúsculas |
| translate() |	Devuelve una cadena traducida |
| upper() |	Convierte una cadena en mayúsculas |
| zfill() |	Rellena la cadena con un número determinado de valores de 0 a principios |


| Operadores de pertenencia |
| --- |
| in |
| not in |


## Slices

Son porciones especificadas de un string.

- a[inicio:final] desde el elemento ‘inicio’ hasta ‘final’-1
- a[inicio:] desde el elemento ‘inicio’ hasta el final del array
- a[:final] desde el primer elemento hasta elemento ‘final’-1
- a[:] todos los elementos del array
- a[::salto] desde el elemento principio hasta el final del array de dendo saltos de en en x en x letras


Además de estos cuatro casos que son los más comunes, también puedes utilizar un tercer valor opcional llamado step o salto. Desde el elemento ‘inicio’ hasta ‘final’ pero saltando el número de elementos indicado por ‘salto’, es decir, de 2 en 2. Con la siguiente estructura `a[inicio:final:salto]`.


Otra de las opciones más interesantes del slice es que el principio y el final pueden ser números negativos. Esto indica que se empieza a contar desde el final del array:

- a[-1] selecciona el último elemento del array
- a[-2:] selecciona los dos últimos elementos del array
- a[:-2] selecciona todos los elementos excepto los dos últimos


Si existen menos elementos de los que quieres seleccionar, Python se porta bien y no muestra ningún error. Por ejemplo, si el array solo tiene un elemento y tratas de seleccionar a[:-2] el resultado es una lista vacía en vez de un mensaje de error. Como es posible que dependiendo de la situación te interese mostrar un error en estos casos es algo que deberías tener en cuenta.


### Mostrando la palabra completa:

- print(un_slice[0:len(un_slice):1])
- print(un_slice[0:len(un_slice)])
- print(un_slice[:])

### Mostrando una letra concreta de la palabra:

- print(un_slice[0]) Nos muestra la primera letra de la palabra empezando por el principio
- print(un_slice[-2]) Nos muestra la segunda letra de la palabra empezando por el final

### Mostrando la palabra desde una letra concreta:

- print(un_slice[0:]) Nos muestra la pablabra desde la posición cero hasta el final
- print(un_slice[3:]) Nos muestra la pablabra desde la posición tres hasta el final
- print(un_slice[3::2]) Nos muestra la pablabra desde la posición tres hasta el final dando saltos saltos de dos en dos letras

### Mostrando la palabra hasta una letra concreta:

- print(un_slice[:len(un_slice)]) Nos muestra la pablabra completa
- print(un_slice[:len(un_slice)-2]) Nos muestra la pablabra desde la posición cero hasta la posición 2 empezando por el final
- print(un_slice[:len(un_slice):3]) Nos muestra la pablabra desde la posición cero hasta el final dando saltos saltos de tres en tres letras

### Mostrando la palabra dando saltos:

- print(un_slice[0:len(un_slice):2]) Nos muestra la pablabra desde la posición cero hasta el final dando saltos saltos de dos en dos letras
- print(un_slice[2:len(un_slice):4]) Nos muestra la pablabra desde la posición dos hasta el final dando saltos saltos de cuatro en cuatro letras