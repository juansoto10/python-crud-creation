# python-crud-creation

Building the foundation to specialize in the web with Django or in databases and taking a step towards becoming a great developer.


## Curso Práctico de Python: Creación de un CRUD

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

- `_privada`: se deberá tratar como privada y no se deberá acceder fuera de la clase.

- `__importante`: variables que empiezan con doble guion bajo ( “__”) son variables importantes, muy susceptibles ante modificaciones.

- Las variables rodeadas por un prefijo y sufijo de subrayado doble (ej: `__str__`) quedan reservadas por el intérprete de Python.


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
| ljust() | Devuelve una versión justificada izquierda de la cadena |
| lower() | Convierte una cadena en minúsculas |
| lstrip() | Devuelve una versión de ajuste izquierdo de la cuerda |
| maketrans() | Devuelve una tabla de traducción para ser utilizado en traducciones |
| partition() | Devuelve una tupla donde la cadena se separó en tres partes |
| replace() | Devuelve una serie en un valor especificado es reemplazado con un valor especificado |
| rfind() | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| rindex() | Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado |
| rjust() | Devuelve una versión justificada derecha de la cadena |
| rpartition() | Devuelve una tupla donde la cadena se separó en tres partes |
| rsplit() | Divide la cadena en el separador especificado y devuelve una lista |
| rstrip() | Devuelve una versión ajuste correcto de la cadena |
| split() | Divide la cadena en el separador especificado y devuelve una lista |
| splitlines() | Divide la cadena en los saltos de línea y devuelve una lista |
| startswith() | Devuelve true si la cadena comienza con el valor especificado |
| strip() | Devuelve una versión recortada de la cadena |
| swapcase() | Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa |
| title() | Convierte el primer carácter de cada palabra en mayúsculas |
| translate() | Devuelve una cadena traducida |
| upper() | Convierte una cadena en mayúsculas |
| zfill() | Rellena la cadena con un número determinado de valores de 0 a principios |


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

```py
lista = [1, 2, 3, 4]
```

También se puede crear usando list y pasando un objeto iterable.

```py
lista = list("1234")
```

Una lista sea crea con [] separando sus elementos con comas (,). Una gran ventaja es que pueden almacenar tipos de datos distintos.

```py
lista = [1, "Hola", 3.67, [1, 2, 3]]
```

### Algunas propiedades de las listas:

- Son ordenadas, mantienen el orden en el que han sido definidas.

- Pueden ser formadas por tipos arbitrarios.

- Pueden ser indexadas con `[i]`.

- Se pueden anidar.

- Son mutables, ya que sus elementos pueden ser modificados.

- Son dinámicas, ya que se pueden añadir o eliminar elementos.

- Si tenemos una lista a con 3 elementos almacenados en ella, podemos acceder a los mismos usando corchetes y un índice, que va desde 0 a n-1 siendo n el tamaño de la lista.

```py
a = [90, "Python", 3.11]
print(a[0]) #90
print(a[1]) #Python
print(a[2]) #3.11
```


### Operaciones con listas

- Suma (+) Concatena dos o más listas:

```py
a=[1,2]
b=[3,4]
print(a + b) # [1,2,3,4]
```

- Multiplicación (*) Repite la misma lista:

```py
a=[1,2]
a * 2 —> [1,2,1,2]
```

- Añadir elemento al final de la lista:

```py
a=[1]
a.append(2)=[1,2]
```

- Eliminar elemento al final de la lista:

```py
a=[1,2]
b=a.pop()
a=[1]
```

- Eliminar elemento dado un indice:

```py
a=[1,2]
b=a.pop(1)
a=[2]
```

- Ordenar lista de menor a mayor, esto modifica la lista inicial:

```py
a=[3,8,1]
a.sort() —> [1,3,8]
```

- Ordenar lista de menor a mayor, esto NO modifica la lista inicial:

```py
a=[3,8,1]
a.sorted() —> [1,3,8]
```

- Eliminar elementos de la lista según su índice:

```py
a=[1,2,3]
del a[0] —> a[2,3]
```

- Eliminar elementos de lista - Elimina el elemento de la lista dado su valor:

```py
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
```

- Range creación de listas en un rango determinado:

```py
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
```

- Tamaño de lista (len()) Devuelve el valor del tamaño de la lista:

```py
a=[0,2,4,6,8]
len(a)=5
```


### Maneras de copiar una lista

En ocasiones puede que se necesite usar una lista y sus valores a lo largo de un programa sin alterar la lista inicial de donde provienen esos datos. Esto lo podemos hacer de varias maneras, como se muestra a continuación.


- Usando el método list.copy():

```py
new_list = old_list.copy()
```

- Usando slices:

```
new_list = old_list[:] o new_list = old_list[:]
```

- You can use the built in list() function:

```py
new_list = list(old_list)
```

- You can use generic copy.copy():

```py
import copy
new_list = copy.copy(old_list)
```

- If the list contains objects and you want to copy them as well, use generic copy.deepcopy():

```py
import copy
new_list = copy.deepcopy(old_list)
```


### Algunos métodos de listas

**append(<obj>):** El método append() añade un elemento al final de la lista.

```py
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]
```

**extend(<iterable>):** El método extend() permite añadir una lista a la lista inicial.

```py
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
```

**insert(<index>, <obj>):** El método insert() añade un elemento en una posición o índice determinado.

```py
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]
```

**remove(<obj>):** El método remove() recibe como argumento un objeto y lo borra de la lista.

```py
l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]
```

**pop(index=-1):** El método pop() elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite borrar elementos diferentes al último.

```py
l = [1, 2, 3]
l.pop()
print(l) #[1, 2]
```

**reverse():** El método reverse() inverte el órden de la lista.

```py
l = [1, 2, 3]
l.reverse()
print(l) #[3, 2, 1]
```

**sort():** El método sort() ordena los elementos de menos a mayor por defecto.

```py
l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
```

Y también permite ordenar de mayor a menor si se pasa como parámetro reverse=True.

```py
l = [3, 1, 2]
l.sort(reverse=True)
print(l) # [3, 2, 1]
```

**index(<obj>[,index]):** El método index() recibe como parámetro un objeto y devuelve el índice de su primera aparición. Como hemos visto en otras ocasiones, el índice del primer elemento es el 0.

```py
l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))
```

También permite introducir un parámetro opcional que representa el índice con el cual debe comenzar la búsqueda del objeto. Es como si ignorara todo lo que hay antes de ese índice para la búsqueda, en este caso el 4.

```py
l = [1, 1, 1, 1, 2, 1, 4, 5]
print(l.index(1, 4)) # 5
```


## Decoradores

Los decoradores sirven para ejecutar lógica del código antes y/o después de otra función, esto nos ayuda a generar funciones y código que pueda ser reutilizado fácilmente sin hacerse más extenso. Hay que recordar que si se genera una función dentro de otra esta solo existirá en ese scope (dentro de la función padre), si se quiere invocar una función varias veces dentro de otras se tiene que generar de manera global.

### Ejemplo

```py
PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What\'s your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('Incorrect password')

    return wrapper


@password_required
def needs_password():
    print('The password is correct!')


# Otra forma de declarar decoradores: Cuando la función recibe parámetros en sí misma

def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper
    

@upper
def say_my_name(name):
    return f'Hi, {name}'


if __name__ == '__main__':
    needs_password() 
    # Si se ingresa la contraseña correcta: The password is correct!
    # Si se ingresa la contraseña incorrecta: Incorrect password

    print(say_my_name('Juan')) 
    # Hi, Juan
```

### `*args y **kwargs`

Básicamente lo que hacen es pasar tal cual los valores de los argumentos que se pasan a la función. `args` hace referencias a listas y `kwargs` a elementos de un diccionario (llave: valor).

#### `*args`

```py
def test_valor_arg(n_arg, *args):
    print('primer valor normal: ', n_arg)

    for arg in args:
        print('este es un valor de *args: ', arg)

    print(type(args))


if__name__ == '__main__':
    test_valor_args('Carlos','Kari','Paola','Maria')
```

- El tipo de dato de args es una tupla.

- Solo poniendo argumentos divididos por comas los convierte.


#### `**kwargs`

```py
def test_valor_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            print('%s == %s' %(key,value))

    print(type(kwargs))


if __name__ == '__main__':
    test_valor_kwargs(caricatura='batman')
```

- El tipo de dato que retorna es un diccionario.

- toma los valores en los extremos de un signo igual.


**Este es un ejemplo usando los 2 en una función:**

```py
def test_valor_args_kwargs(*args, **kwargs):
    print(type(kwargs))
    print(kwargs)
    print('----------')
    print(type(args))
    print(args)


if __name__ == '__main__':
    test_valor_kwargs_args('flash', 'batman', caricatura='batman', empresa = 'dc')
```


## Programación orientada a objetos

Es un paradigma de programación que usa objetos y sus interacciones, para diseñar aplicaciones y programas informáticos. Este otorga los medios para estructurar programas de tal manera que las propiedades y comportamientos estén envueltos en objetos individuales.

Para poder entender cómo modelar estos objetos tenemos que tener claros cuatro principios:

- **Encapsulamiento (Encapsulation):** Cada objeto tiene sus propias funciones y datos sin afectar a otros, son lógica interna.

- **Abstracción(Abstraction):** El usuario podrá interactuar con el objeto sin necesidad de conocer toda la lógica detrás del mismo.

- **Herencia (Inheritance):** Si se declara un método en una clase todas las subclases heredarán ese método. Por ejemplo, si se declaras un método “imprime” que ejecute un print en una clase, las subclases podrán usar el método imprime, sin necesidad de declararlo en cada una.

- **Polimorfismo (Polymorphism):** Usando el ejemplo anterior, en cada subclase se puede modificar el método “imprime” por lo tal cada sub clase contara con un método imprime pero acorde a las necesidades de cada subclase.


### POO en Python

#### Ejemplo

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')


if __name__ == '__main__':
    name = input('What is your name? ')
    age = int(input('What is your age? '))

    person = Person(name, age)

    print(f'Age: {person.age}')
    person.say_hello()
```

## Scopes and namespaces

En Python, un name, también conocido como identifier, es simplemente una forma de otorgarle un nombre a un objeto. Mediante el nombre, podemos acceder al objeto. Vamos a ver un ejemplo:

```py
my_var = 5

id(my_var) # 4561204416
id(5) # 4561204416
```

En este caso, el identifier my_var es simplemente una forma de acceder a un objeto en memoria (en este caso el espacio identificado por el número 4561204416). Es importante recordar que un name puede referirse a cualquier tipo de objeto (aún las funciones).

```py
def echo(value):
    return value

a = echo

a(‘Billy’) # 3
```

Ahora que ya entendimos qué es un name podemos avanzar a los namespaces (espacios de nombres). Para ponerlo en palabras llanas, un namespace es simplemente un conjunto de names.

En Python, te puedes imaginar que existe una relación que liga a los nombres definidos con sus respectivos objetos (como un diccionario). Pueden coexistir varios namespaces en un momento dado, pero se encuentran completamente aislados. Por ejemplo, existe un namespace específico que agrupa todas las variables globales (por eso puedes utilizar varias funciones sin tener que importar los módulos correspondientes) y cada vez que declaramos una módulo o una función, dicho módulo o función tiene asignado otro namespace.

A pesar de existir una multiplicidad de namespaces, no siempre tenemos acceso a todos ellos desde un punto específico en nuestro programa. Es aquí donde el concepto de scope (campo de aplicación) entra en juego.

Scope es la parte del programa en el que podemos tener acceso a un namespace sin necesidad de prefijos.

En cualquier momento determinado, el programa tiene acceso a tres scopes:

- El scope dentro de una función (que tiene nombres locales)

- El scope del módulo (que tiene nombres globales)

- El scope raíz (que tiene los built-in names)

Cuando se solicita un objeto, Python busca primero el nombre en el scope local, luego en el global, y por último, en el raíz. Cuando anidamos una función dentro de otra función, su scope también queda anidado dentro del scope de la función padre.

```py
def outer_function(some_local_name):
    def inner_function(other_local_name):
         # Tiene acceso a la built-in function print y al nombre local some_local_name
         print(some_local_name) 
        
         # También tiene acceso a su scope local
         print(other_local_name)
```

Para poder manipular una variable que se encuentra fuera del scope local podemos utilizar los keywords global y nonlocal.

```py
some_var_in_other_scope = 10

def some_function():
     global some_var_in_other_scope
     
     Some_var_in_other_scope += 1
```

En Python, la palabra clave global permite modificar la variable fuera del alcance actual. Se utiliza para crear una variable global y realizar cambios en la variable en un contexto local.

### Reglas de palabra clave global

Las reglas básicas para la palabra clave `global` en Python son:

- Cuando creamos una variable dentro de una función, es local por defecto.

- Cuando definimos una variable fuera de una función, es global por defecto. No tienes que usar la palabra clave global.

- Utilizamos la palabra clave `global` para leer y escribir una variable global dentro de una función.

- El uso de `global` fuera de una función no tiene efecto

En lo referente a la palabra `nonlocal`, actúa de manera similar, solo que orientada a lo que sería un alcance de funciones y funciones anidadas, a continuación un ejemplo:

```py
def method():

    def method_2():
        # Este método no tiene acceso a la variable value, por cuanto se usa -nonlocal- para poder acceder.
        nonlocal value
        value = 100

    # Variable local.
    value = 10
    method2()
```


## Click

Click es un framework que nos permite crear aplicaciones de línea de comandos y que utiliza docoradores para implementar su funcionalidad. Nos provee una interfaz que podemos personalizar, genera ayuda automáticamente para el usuario y realiza las conversiones de tipo por nosotros, haciendo que el desarrollo sea más fácil y el código más legible.

Tiene 4 decoradores básicos:

1. **@click.group:** Agrupa una serie de comandos.

2. **@click.command:** Defe los comandos de nuestra app.

3. **@click.argument:** Parámetros necesarios.

4. **@click.option:** Parámetros opcionales.

La documentación de click la encuentras en el siguiente link: [Documentación - Click](URL 'https://click.palletsprojects.com/en/8.1.x/')


### Implementando Click en nuestra aplicación

Para explicar mejor cómo implementar la funcionalidad de click vamos a tomar como ejemplo la aplicación desarrollada en este repositorio en la carpeta vcau_store, explicando la configuración del entorno y otros detalles más.


#### Implementación en vcau_store

Dentro del directorio donde de trabajo vamos a generar dos archivos: `vcau.py` y `setup.py`. También crearemos una carpeta llamada `clients` y dentro de ella unos archivos llamados `commands.py`, `models.py`, `services.py`. Por el momento iniciaremos con estos archivos y progresivamente se irán añadiendo otros a medida que desarrollemos nuestra aplicación.


Dentro de `vcau.py` escribiremos lo siguiente, importando `click`.

```py
import click

from clients import commands as clients_commands


CLIENTS_TABLE = '.clients.csv'


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
```

Ahora modificaremos el archivo `commands.py` dentro de la carpeta `clients`:

```py
import click

from clients.services import ClientService
from clients.models import Client


@click.group()
def clients():
    """Manages the clients lifecycle."""
    pass


@clients.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The client name')
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client."""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])

    client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
    """Lists all clients."""
    pass


@clients.command()
@click.pass_context
def update(ctx, client_uid):
    """Updates a client."""
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client."""
    pass


all = clients
```

Los docstrings son muy importantes al utilizar `click` ya que estos serán los textos que se mostrarán como ayuda al usuario en la aplicación.

Ahora modificaremos el archivo `setup.py` para invocar directamente nuestra aplicación sin tener que llamar al intérprete de Python.

```py
from setuptools import setup


setup(
    name='vcau',
    version='0.1',
    py_modules=['vcau'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        vcau=vcau:cli
    ''',
)
```

Ahora debemos crear un entorno o ambiente virtual para no instalar la aplicación globalmente. Podemos hacerlo con los siguientes comandos (En Linux o Mac):

```bash
virtualenv --python=python3 venv
o
python3 -m venv venv
```

Activamos el entorno virtual con:

```bash
source venv/bin/activate
o
. venv/bin/activate
```

Una vez activado el entorno virtual instalamos nuestra aplicación con el siguiente comando:

`pip install --editable .`

Si todo se ha ejecutado correctamente al ejecutar el comando `which vcau` en nuestra terminal nos debe salir lo siguiente: `/<ruta_directorio_trabajo>/venv/bin/vcau`.

Si escribimos en la terminal `vcau --help`, `vcau clients --help`nos debe mostrar los mensajes de ayuda de nuestra aplicación.

```bash
$ vcau --help

Usage: vcau [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  clients  Manages the clients lifecycle.
```

```bash
$ vcau clients --help

Usage: vcau clients [OPTIONS] COMMAND [ARGS]...

  Manages the clients lifecycle.

Options:
  --help  Show this message and exit.

Commands:
  create  Creates a new client.
  delete  Deletes a client.
  list    Lists all clients.
  update  Updates a client.
```

******
**Nota útil al usar tree:** Podemos omitir mostrar ciertas carpetas con el comando `tree -I '__pycache__|*.egg-info|venv'`. Esto nos mostrará la estructura de carpetas omitiendo las especificadas, lo cual resultará en un árbol menos saturado y nos permitirá visualizar únicamente lo necesario. Para ver todo dentro de la carpeta simplemente escribimos `tree .`
******

Normalmente una aplicación se divide entre *la interfaz* (cómo interactúa nuestro software con el exterior), *la lógica de negocio* (lógica específica de nuestro programa) y por último, *las asbtracciones* o *los objetos* sobre los cuales estamos interactuando (en el caso de esta app, los clientes).

Vamos a crear la clase `Client` dentro del archivo `
models.py`

```py
import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)

    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
```

`vars(self)` crea un diccionario para el objeto de clase `Client`. Por otra parte el decorador `@staticmethod` nos permite declarar métodos estáticos en nuestra clase, es decir, un método que se puede ejecutar sin necesidad de una instancia de clase.

Ahora modificaremos el archivo `services.py` donde estará el objeto de servicio `ClientService`.

```py
import csv

from clients.models import Client


class ClientService:

    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())            
```


## Manejo de errores

Python tiene una amplia jerarquía de errores que nos da posibilidades para manejar errores en distintos casos, como por ejemplo cuando no se pueda leer un archivo, cuando se trata de dividir entre cero, entre otros problemas que puedan surgir en nuestro código Python. Es importante manejar los errores ya que cuando no se hace y se ejecuta el programa, este termina cuando encuentra un error. Por otra parte, cuando hay un error de sintaxis nuestro programa nunca se ejecuta.

Para definir un error en Python utilizamos la palabra `raise`. Aunque Python nos ofrece muchas maneras de manejar nuestros errores, es buena práctica definir errores específicos de nuestra aplicación y usar los de Python para extenderlos.

Podemos generar nuestros propios errores creando una clase que extienda `BaseException`.

Si queremos evitar que termine nuestro programa cuando ocurra un error, se debe tener una estrategia. Para esto utilizamos `try/except/else/finally` según sea el caso cuando existela posibilidad de que una parte de nuestro código falle.

- **try:** Es el código a probar. Si es posible, ponemos una sola línea de código ahí como buena práctica.

- **except:** Es lo que haremos si ocurre el error. Debemos ser específicos con el tipo de error que vamos a manejar.

- **else:** Es código que se ejecuta cuando no ocurre ningún error.

- **finally:** Nos permite definir un bloque de código que se va a ejecutar al final sin importar lo que pase.


### Jerarquía de clases para las built-in Exceptions:

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```


## Context Managers

Context managers allow you to allocate and release resources precisely when you want to. The most widely used example of context managers is the `with` statement. Suppose you have two related operations which you’d like to execute as a pair, with a block of code in between. Context managers allow you to do specifically that. For example:

```py
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```

The above code opens the file, writes some data to it and then closes it. If an error occurs while writing the data to the file, it tries to close it. The above code is equivalent to:

```py
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
```

While comparing it to the first example we can see that a lot of boilerplate code is eliminated just by using `with`. The main advantage of using a `with` statement is that it makes sure our file is closed without paying attention to how the nested block exits.

A common use case of context managers is locking and unlocking resources and closing opened files (as I have already shown you).

Let’s see how we can implement our own Context Manager. This should allow us to understand exactly what’s going on behind the scenes.


### Implementing a Context Manager as a Class

At the very least a context manager has an `__enter__` and `__exit__` method defined. Let’s make our own file-opening Context Manager and learn the basics.

```py
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

```

Just by defining `__enter__` and `__exit__` methods we can use our new class in a with statement. Let’s try:

```py
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
```

Our `__exit__` method accepts three arguments. They are required by every `__exit__` method which is a part of a Context Manager class. Let’s talk about what happens under-the-hood.

1. The with statement stores the `__exit__` method of the `File` class.

2. It calls the `__enter__` method of the `File` class.

3. The `__enter__` method opens the file and returns it.

4. The opened file handle is passed to `opened_file`.

5. We write to the file using `.write()`.

6. The `with` statement calls the stored `__exit__` method.

7. The `__exit__` method closes the file.


### Handling Exceptions

We did not talk about the `type`, `value` and `traceback` arguments of the `__exit__` method. Between the 4th and 6th step, if an exception occurs, Python passes the type, value and traceback of the exception to the `__exit__` method. It allows the `__exit__` method to decide how to close the file and if any further steps are required. In our case we are not paying any attention to them.

What if our file object raises an exception? We might be trying to access a method on the file object which it does not supports. For instance:

```py
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

Let’s list the steps which are taken by the `with` statement when an error is encountered:

1. It passes the type, value and traceback of the error to the `__exit__` method.

2. It allows the `__exit__` method to handle the exception.

3. If `__exit__` returns `True` then the exception was gracefully handled.

4. If anything other than `True` is returned by the `__exit__` method then the exception is raised by the `with` statement.

In our case the `__exit__` method returns `None` (when no return statement is encountered then the method returns `None`). Therefore, the `with` statement raises the exception:

```shell
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'undefined_function'
```

Let’s try handling the exception in the `__exit__` method:

```py
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled
```

Our `__exit__` method returned `True`, therefore no exception was raised by the `with` statement.

This is not the only way to implement Context Managers. There is another way and we will be looking at it in the next section.


### Implementing a Context Manager as a Generator

We can also implement Context Managers using decorators and generators. Python has a contextlib module for this very purpose. Instead of a class, we can implement a Context Manager using a generator function. Let’s see a basic, useless example:

```py
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    try:
        yield f
    finally:
        f.close()
```

Okay! This way of implementing Context Managers appear to be more intuitive and easy. However, this method requires some knowledge about generators, yield and decorators. In this example we have not caught any exceptions which might occur. It works in mostly the same way as the previous method.

Let’s dissect this method a little.

1. Python encounters the yield keyword. Due to this it creates a generator instead of a normal function.

2. Due to the decoration, contextmanager is called with the function name (open_file) as its argument.

3. The contextmanager decorator returns the generator wrapped by the GeneratorContextManager object.

4. The GeneratorContextManager is assigned to the open_file function. Therefore, when we later call the open_file function, we are actually calling the GeneratorContextManager object.

So now that we know all this, we can use the newly generated Context Manager like this:

```py
with open_file('some_file') as f:
    f.write('hola!')
```
