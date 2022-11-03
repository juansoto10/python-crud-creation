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


## Listas

Las listas en Python son un tipo de dato que permite almacenar datos de cualquier tipo. Son mutables y dinámicas, lo cual es la principal diferencia con los sets y las tuplas.


### Crear listas en Python:

Las listas en Python son uno de los tipos o estructuras de datos más versátiles del lenguaje, ya que permiten almacenar un conjunto arbitrario de datos. Es decir, podemos guardar en ellas prácticamente lo que sea.

`lista = [1, 2, 3, 4]`

También se puede crear usando list y pasando un objeto iterable.

`lista = list("1234")`

Una lista sea crea con [] separando sus elementos con comas (,). Una gran ventaja es que pueden almacenar tipos de datos distintos.

lista = [1, "Hola", 3.67, [1, 2, 3]]

### Algunas propiedades de las listas:

- Son ordenadas, mantienen el orden en el que han sido definidas.

- Pueden ser formadas por tipos arbitrarios.

- Pueden ser indexadas con `[i]`.

- Se pueden anidar.

- Son mutables, ya que sus elementos pueden ser modificados.

- Son dinámicas, ya que se pueden añadir o eliminar elementos.

- Si tenemos una lista a con 3 elementos almacenados en ella, podemos acceder a los mismos usando corchetes y un índice, que va desde 0 a n-1 siendo n el tamaño de la lista.

`a = [90, "Python", 3.11]
 print(a[0]) #90
 print(a[1]) #Python
 print(a[2]) #3.11`


### Operaciones con listas

- Suma (+) Concatena dos o más listas:

`a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]`

- Multiplicación (*) Repite la misma lista:

`a=[1,2]
a * 2 —> [1,2,1,2]`

- Añadir elemento al final de la lista:

`a=[1]
a.append(2)=[1,2]`

- Eliminar elemento al final de la lista:

`a=[1,2]
b=a.pop()
a=[1]`

- Eliminar elemento dado un indice:

`a=[1,2]
b=a.pop(1)
a=[2]`

- Ordenar lista de menor a mayor, esto modifica la lista inicial:

`a=[3,8,1]
a.sort() —> [1,3,8]`

- Ordenar lista de menor a mayor, esto NO modifica la lista inicial:

`a=[3,8,1]
a.sorted() —> [1,3,8]`

- Eliminar elementos de la lista según su índice:

`a=[1,2,3]
del a[0] —> a[2,3]`

- Eliminar elementos de lista - Elimina el elemento de la lista dado su valor:

`a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]`

- Range creación de listas en un rango determinado:

`a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]`

- Tamaño de lista (len()) Devuelve el valor del tamaño de la lista:

`a=[0,2,4,6,8]
len(a)=5`


### Maneras de copiar una lista

En ocasiones puede que se necesite usar una lista y sus valores a lo largo de un programa sin alterar la lista inicial de donde provienen esos datos. Esto lo podemos hacer de varias maneras, como se muestra a continuación.


- Usando el método list.copy():

`new_list = old_list.copy()`

- Usando slices:

`new_list = old_list[:] or new_list = old_list[:]`

- You can use the built in list() function:

`new_list = list(old_list)`

- You can use generic copy.copy():

`import copy`
`new_list = copy.copy(old_list)`

- If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

`import copy`
`new_list = copy.deepcopy(old_list)`


### Algunos métodos de listas

**append(<obj>):** El método append() añade un elemento al final de la lista.

`l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]`

**extend(<iterable>):** El método extend() permite añadir una lista a la lista inicial.

`l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]`

**insert(<index>, <obj>):** El método insert() añade un elemento en una posición o índice determinado.

`l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]`

**remove(<obj>):** El método remove() recibe como argumento un objeto y lo borra de la lista.

`l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]`

**pop(index=-1):** El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último.

`l = [1, 2, 3]
l.pop()
print(l) #[1, 2]`

**reverse():** El método reverse() inverte el órden de la lista.

`l = [1, 2, 3]
l.reverse()
print(l) #[3, 2, 1]`

**sort():** El método sort() ordena los elementos de menos a mayor por defecto.

`l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]`

Y también permite ordenar de mayor a menor si se pasa como parámetro reverse=True.

`l = [3, 1, 2]
l.sort(reverse=True)
print(l) # [3, 2, 1]`

**index(<obj>[,index]):** El método index() recibe como parámetro un objeto y devuelve el índice de su primera aparición. Como hemos visto en otras ocasiones, el índice del primer elemento es el 0.

`l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))`

También permite introducir un parámetro opcional que representa el índice con el cual debe comenzar la búsqueda del objeto. Es como si ignorara todo lo que hay antes de ese índice para la búsqueda, en este caso el 4.

`l = [1, 1, 1, 1, 2, 1, 4, 5]
print(l.index(1, 4)) # 5`