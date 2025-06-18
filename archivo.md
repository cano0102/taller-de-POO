Apertura: lunes, 16 de junio de 2025, 10:00
Cierre: lunes, 16 de junio de 2025, 16:00
En esta actividad desarrollaran los siguientes ejercicios usando los conocimientos que tienen en algoritmos y los conceptos adquridos en POO.

Ejercicio 1
Crea una clase llamada Persona que siga las siguientes condiciones:

Sus atributos son:

●      documento (string)

●      nombre (string)

●      edad (int)

●      sexo (M masculino, F femenino) (char)

●      peso (double)

●      altura (double)

●      DNI (int)

No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo. Si quieres añadir algún atributo, método puedes hacerlo.

Por defecto, todos los atributos serán valores por defecto según su tipo (0 números (enteros y double), cadena vacía (string), etc.).

El sexo por defecto será M.

Se implantaran varios constructores:

●      Un constructor por defecto que no recibe ni tiene ninguna funcionalidad dentro de él.

●      Un constructor con el documento, nombre, edad y sexo

●      Un constructor con todos los atributos como parámetro.

Los métodos que se implementaran son:

●      calcularIMC(): calculara si la persona está en su peso ideal, devuelve un -1 si está por debajo de su peso ideal, un 0 si está en su peso ideal y un 1 si tiene sobrepeso, un 2 si esta obeso, y 3 si esta en obesidad extrema o de alto riesgo. Recomendado usar enums para devolver estos valores.

 

Para calcular el IMC (Índice de masa corporal) tenga en cuenta lo siguiente:

 

INDICE DE MASACORPORAL (IMC)

 

CATEGORÍA

Menor de 18.5   

Por debajo del peso

Mayor o igual a 18.5 y menor o igual a 24.9  

Normal

Mayor o igual a 25.0 y menor o igual a 29.9         

Con sobrepeso

Mayor o igual a 30.0 y menor o igual a 39.9

Obesidad

Mayor o igual a 40.0

Obesidad extrema o de alto riesgo

 

Además la fórmula para calcularla es: peso / ((altura/100)^2)

 

●      esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.

●      comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, será M. Su modificador de acceso no debe permitir que sea visible al exterior.

●      listarInformacion(): devuelve toda la información del objeto.

●      generaDNI(): genera un numero auto-incrementable. Este método será invocado cuando se construya el objeto. Su modificador de acceso no debe permitir que sea visible al exterior.

●      Métodos get y set de cada parámetro, excepto de DNI.

Ahora, crea una clase ejecutable que haga lo siguiente:

●      Pide por teclado el documento, nombre, la edad, sexo, peso y altura.

●      Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.

●      Para cada objeto, deberá comprobar el IMC y mostrar un mensaje con su respectiva categoría.

●      Indicar para cada objeto si es mayor de edad.

●      Mostrar la información de cada objeto. Por ejemplo: “Hola Andrés Martinez, tu código dentro del sistema es 1. Tu identificación es 1214788900. Tu edad es 21 años. Tu género es Masculino. Tu Peso es 69 kg y tu Altura es 179 cm. Al calcular tu IMC concluimos que tu peso esta: Normal”.

●      Al final debe permitir ingresar otra persona y realizar todo el proceso anterior.


Ejercicio 2
Crea una clase Cuenta (bancaria) con atributos para el número de cuenta, el Documento de identidad del cliente, el saldo actual y el interés anual que se aplica a la cuenta (porcentaje).

Define en la clase los siguientes métodos:

o   Constructor por defecto y constructor con DNI, saldo e interés

o   actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365 aplicado al saldo actual).

o   ingresar(double): permitirá ingresar una cantidad en la cuenta.

o   retirar(double): permitirá sacar una cantidad de la cuenta (si hay saldo).

o   Método que nos permita mostrar todos los datos de la cuenta.

El número de cuenta se asignará de forma correlativa a partir de 100001, asignando el siguiente número al último asignado.

Crear una vista que nos permita realizar las operaciones.

Ejercicio 3
Desarrolla una clase Cafetera con atributos capacidadMaxima (la cantidad máxima de café que puede contener la cafetera) y cantidadActual (la cantidad actual de café que hay en la cafetera).

Implementa, al menos, los siguientes métodos:

Constructor predeterminado: establece la capacidad máxima en 1000 (c.c.) y la actual en cero (cafetera vacía).
Constructor(int capacidadMaxima, int cantidad actual) Si la cantidad actual es mayor que la capacidad máxima de la cafetera, la ajustará al máximo.
llenarCafetera(): pues eso, hace que la cantidad actual sea igual a la capacidad.
servirTaza(int): simula la acción de servir una taza con la capacidad indicada. Si la cantidad actual de café “no alcanza” para llenar la taza, se sirve lo que quede.
vaciarCafetera(): pone la cantidad de café actual en cero.  agregarCafe(int): añade a la cafetera la cantidad de café indicada.
Se debe construir el método main que me manipule la clase Cafetera.

Todos los ejercicios tienen que ser subidos a un repositorio en Github y deben adjuntar el enlace a dicho repositorio. 

ESTE TRABAJO ES INDIVIDUAL