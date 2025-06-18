
# Ejercicio 1
# Crea una clase llamada Persona que siga las siguientes condiciones:

# Sus atributos son:

# ●      documento (string)

# ●      nombre (string)

# ●      edad (int)

# ●      sexo (M masculino, F femenino) (char)

# ●      peso (double)

# ●      altura (double)

# ●      DNI (int)

# No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo. Si quieres añadir algún atributo, método puedes hacerlo.

# Por defecto, todos los atributos serán valores por defecto según su tipo (0 números (enteros y double), cadena vacía (string), etc.).

# El sexo por defecto será M.

# Se implantaran varios constructores:

# ●      Un constructor por defecto que no recibe ni tiene ninguna funcionalidad dentro de él.

# ●      Un constructor con el documento, nombre, edad y sexo

# ●      Un constructor con todos los atributos como parámetro.

# Los métodos que se implementaran son:

# ●      calcularIMC(): calculara si la persona está en su peso ideal, devuelve un -1 si está por debajo de su peso ideal, un 0 si está en su peso ideal y un 1 si tiene sobrepeso, un 2 si esta obeso, y 3 si esta en obesidad extrema o de alto riesgo. Recomendado usar enums para devolver estos valores.

 

# Para calcular el IMC (Índice de masa corporal) tenga en cuenta lo siguiente:

 

# INDICE DE MASACORPORAL (IMC)

 

# CATEGORÍA

# Menor de 18.5   

# Por debajo del peso

# Mayor o igual a 18.5 y menor o igual a 24.9  

# Normal

# Mayor o igual a 25.0 y menor o igual a 29.9         

# Con sobrepeso

# Mayor o igual a 30.0 y menor o igual a 39.9

# Obesidad

# Mayor o igual a 40.0

# Obesidad extrema o de alto riesgo

 

# Además la fórmula para calcularla es: peso / ((altura/100)^2)

 

# ●      esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.

# ●      comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, será M. Su modificador de acceso no debe permitir que sea visible al exterior.

# ●      listarInformacion(): devuelve toda la información del objeto.

# ●      generaDNI(): genera un numero auto-incrementable. Este método será invocado cuando se construya el objeto. Su modificador de acceso no debe permitir que sea visible al exterior.

# ●      Métodos get y set de cada parámetro, excepto de DNI.

# Ahora, crea una clase ejecutable que haga lo siguiente:

# ●      Pide por teclado el documento, nombre, la edad, sexo, peso y altura.

# ●      Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.

# ●      Para cada objeto, deberá comprobar el IMC y mostrar un mensaje con su respectiva categoría.

# ●      Indicar para cada objeto si es mayor de edad.

# ●      Mostrar la información de cada objeto. Por ejemplo: “Hola Andrés Martinez, tu código dentro del sistema es 1. Tu identificación es 1214788900. Tu edad es 21 años. Tu género es Masculino. Tu Peso es 69 kg y tu Altura es 179 cm. Al calcular tu IMC concluimos que tu peso esta: Normal”.

# ●      Al final debe permitir ingresar otra persona y realizar todo el proceso anterior.






import random

class Persona():
    def __init__(self, nombre: str = "" , documento :str = "", edad : int = None , sexo : str = "m", peso : float = None ,altura : float = None):

       self.__documento  = documento

       self.__nombre = nombre

       self.__edad = edad

       self.__sexo = sexo
       self.__peso  = peso

       self.__altura = altura

       self._DNI = random.randint(10_000_000, 99_999_999)
       



    def get_documento(self):
        return self.__documento

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura


    def set_documento(self, documento):
       self.__documento = documento

    def set_nombre(self, nombre):
       self.__nombre = nombre

    def set_edad(self, edad):
       self.__edad = edad

    def set_sexo(self, sexo):
       self.__sexo = sexo 

    def set_peso(self, peso):
       self.__peso = peso

    def set_altura(self, altura):
       self.__altura = altura


    def comprobar_sexo():
        pass


    def calcularIMC():
        pass

    def esMayorDeEdad(self):
        edad = self.get_edad()
        mensaje = "Es mayor" if edad >= 18 else "Es menor"
        print(mensaje)
        
    def listarInformacion():
        pass


