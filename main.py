# Librería String - texto 1
print("Librería string - texto 1: 'La joya del monje'")

import string
# Creación del primer archivo de texto en replit, que contendrá los ejercicios de librería string del texto 'jota_monje.txt'
file_monje = open('libreria-string_monje.txt', 'w')

# Primera frase del archivo nuevo
file_monje.write("Respuestas de ejercicios de la librería string en el texto 'La joya del monje'\n")
file_monje.write("\n")

# Para acceder al archivo de texto de 'La joya del monje' debemos abrir el texto en forma de lectura y utilizar el método read()
monje = open('joya_monje.txt','r')
texto1 = monje.read()
# Es importante cerrar este archivo antes de proseguir con el código
monje.close()

# Ahora, con el método write, plasmaremos el texto del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas aplicaciones de la librería string
file_monje.write("- El texto del archivo de 'La joya del monje' es: \n")
file_monje.write("\n")

# Forma de mostrar el texto tomado del archivo subido 'joya_monje.txt'
file_monje.write(texto1)
# Este representa otra manera de imprimir tal texto, obteniendo el mismo resultado anterior
#for i in (texto1):
  #file_monje.write(i)

# Comenzaremos a escribir algunos ejercicios
file_monje.write("\n")
file_monje.write("\n- Ejercicios: \n")

# En este caso utilizamos el método capwords() para obtener el mismo texto anterior, pero con el método que pone en mayúsculas, todas las primeras letras de cada palabra, y además combina los métodos split() y join() haciéndolo imprimir todo junto.
texto1cap = string.capwords(texto1)
file_monje.write("\n- capwords(): \n")

# Creación del ciclo for para poder ejecutar el método correctamente en el texto
for i in (texto1cap):
  #file_monje.write("\n")
  file_monje.write(i)

# Hacer un salto de linea 
file_monje.write("\n")

# método find(): lo utilizaremos para encontrar la palabra 'regalo' en el texto. Este método, nos retornará los bytes en donde se ubica tal palabra
file_monje.write("\n- find(): \n")

# Hacer un salto de linea 
file_monje.write("\n")
# Creación de la variable que usa el método find()
texto1find = texto1.find("regalo")
# Este método da como resultado un int, write()  solo admite argumentos de string, por esto lo convertimos a string dentro del write()
file_monje.write("La palabra 'regalo' está en el texto en el  byte: ")
file_monje.write(str(texto1find))

# Hacer un salto de linea 
file_monje.write("\n")

# Es necesario abrir nuevamente el archivo 'joya_monje.txt' en modo lectura para indicar en read() los bytes específicos que queremos observar en el siguiente ejercicio
monje = open('joya_monje.txt','r')
texto1w = monje.read(320)
# Es importante cerrar este archivo para continuar con el código sin problemas
monje.close()

# método upper(): convierte todas las letras en mayúsculas. En este caso imprimiremos, hasta los 320 bytes del texto original, pero en mayúsculas
file_monje.write("\n- upper(): \n")

# Hacer un salto de linea 
file_monje.write("\n")
# Creación de las variables y aplicación del método upper()
texto1upper = texto1w.upper()
file_monje.write((texto1upper))

# Es necesario abrir nuevamente el archivo 'joya_monje.txt' en modo lectura para indicar en read() los bytes específicos que queremos observar en el siguiente ejercicio
monje = open('joya_monje.txt','r')
texto1t = monje.read(251)
# Es importante cerrar este archivo para continuar con el código sin problemas
monje.close()

# Hacer un salto de linea 
file_monje.write("\n")

# método split(): permite escribir cada palabra en el rango de los 0 y los 250 bytes, como elementos de una lista
file_monje.write("\n- split(): \n")

# Hacer un salto de linea 
file_monje.write("\n")

# Creación de las variables y aplicación del método upper()
texto1split = (texto1t.split())
file_monje.write(str(texto1split))

# Cerramos el archivo donde guardamos los ejercicios de la librería string del texto 'La joya del monje'
file_monje.close()

print("--------"*7)
# Librería String - texto 2
print("Librería string - texto 2: '¡Suelta el vaso!'")

# Creación del segundo archivo de texto en replit, que contendrá los ejercicios de librería string del texto 'suelta_el_vaso.txt'
file_vaso = open('libreria-string_vaso.txt', 'w')

# Primera frase del archivo nuevo
file_vaso.write("Respuestas de ejercicios de la librería string en el texto '¡Suelta el vaso!'\n")
file_vaso.write("\n")

# Para acceder al archivo de texto de '¡Suelta el vaso!' debemos abrir el texto en forma de lectura y utilizar el método read()
vaso = open('suelta _el _vaso.txt','r')
texto2 = vaso.read()
# Es importante cerrar este archivo antes de proseguir con el código
vaso.close()

# Ahora, con el método write, plasmaremos el texto del archivo subido, en el archivo de texto creado desde acá, y ejecutaremos algunas aplicaciones de la librería string
file_vaso.write("- El texto del archivo de '¡Suelta el vaso!' es: \n")
file_vaso.write("\n")

# Forma de mostrar el texto tomado del archivo subido 'suelta_el_vaso.txt'

for i in (texto2):
  file_vaso.write(i)

# Este representa otra manera de imprimir tal texto, obteniendo el mismo resultado anterior
#file_vaso.write(texto2)


# Comenzaremos a escribir algunos ejercicios
file_vaso.write("\n")
file_vaso.write("\n- Ejercicios: \n")

#  método count(): es para ver la cantidad de veces que una palabra específica se encuentra en el texto 2
file_vaso.write("\n- count(): \n")

# Creación de las variables y uso del método count()
texto2count = (texto2.count("peso"))
# Imprimir la respuesta
file_vaso.write("\nCantidad de veces que la palabra 'peso' está en el texto: ")
file_vaso.write(str(texto2count))

# Hacer un salto de linea 
file_vaso.write("\n")

# método isalpha(): retorna True si todos los caracteres del archivo de texto 2 son letras. Como en este ejemplo, eso no es verdad, el programa deberá retornar False
file_vaso.write("\n- isalpha(): \n")

# Hacer un salto de linea 
file_vaso.write("\n")
# Creación de la variable que usa el método isalpha()
texto2alpha = texto2.isalpha()
# Imprimir la respuesta
file_vaso.write("Todos los caracteres de este texto son letras?: ")
file_vaso.write(str(texto2alpha))

# Hacer un salto de linea 
file_vaso.write("\n")

# Es necesario abrir nuevamente el archivo 'suelta_el_vaso.txt' en modo lectura para indicar en read() los bytes específicos que queremos observar en el siguiente ejercicio
vaso = open('suelta _el _vaso.txt','r')
texto2w = vaso.read(565)
# Es importante cerrar este archivo para continuar con el código sin problemas
vaso.close()

# método lower(): convierte todas las letras en minúsculas. En este caso imprimiremos, hasta los 565 bytes del texto original, pero en minúsculas
file_vaso.write("\n- lower(): \n")

# Hacer un salto de linea 
file_vaso.write("\n")
# Creación de las variables y aplicación del método lower()
texto2lower = texto2w.lower()
file_vaso.write((texto2lower))

# Hacer un salto de linea 
file_vaso.write("\n")

# método endswith(): retorna True si se indica el caracter exacto en el que termina el texto, en este caso hasta el byte 565 del texto 2
file_vaso.write("\n- endswith(): \n")

# Hacer un salto de linea 
file_vaso.write("\n")

# Creación de las variables y aplicación del método endswith()
texto2ends = texto2w.endswith("á")
# Imprimir la respuesta
file_vaso.write("La última letra de la última palabra hasta el byte 565 es 'á'?: ")
file_vaso.write(str(texto2ends))

# Es necesario abrir nuevamente el archivo 'suelta_el_vaso.txt' en modo lectura para indicar en read() los bytes específicos que queremos observar en el siguiente ejercicio
vaso = open('suelta _el _vaso.txt','r')
texto2t = vaso.read(324)
# Es importante cerrar este archivo para continuar con el código sin problemas
vaso.close()

# Hacer un salto de linea 
file_vaso.write("\n")

# método isalpha(): retorna True si los caracteres seleccionados del archivo de texto 2 son espacios en blanco. Como en este ejemplo, eso no es verdad, el programa deberá retornar False
file_vaso.write("\n- isspace(): \n")

# Hacer un salto de linea 
file_vaso.write("\n")
# Creación de la variable que usa el método isalpha()
texto2space = texto2t.isspace()
# Imprimir la respuesta
file_vaso.write("Todos los caracteres de esta porción de texto (hasta 324 bytes) son espacios en blanco?: ")
file_vaso.write(str(texto2space))


# Cerramos el archivo donde guardamos los ejercicios de la librería string del texto 'La joya del monje'
file_vaso.close()