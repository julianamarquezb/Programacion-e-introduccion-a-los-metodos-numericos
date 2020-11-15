# Programación e introducción a los métodos numéricos - Proyecto Final

Integrantes del grupo:
  - Gabriel Romero
  - Juliana Márquez
  - David Aparicio
  - Pedro Jaramillo


Proyecto Traductor de codigo MORSE.

El objetivo de este proyecto era el de crear un programa capaz de traducir un archivo de texto, o audio, en codigo MORSE, a un archivo de texto en español, y viceversa.

FUNCIONAMIENTO:

Para empezar, el programa define dos listas del mismo tamaño: una contiene todo el alfabeto español y muchos simbolos especiales que se utilizan con regularidad, y la otra lista contiene los mismo elementos (en las mismas posiciones) pero en codigo MORSE.

Luego, el programa tiene una seccion que se encarga de pedirle al usuario que ingrese la direccion en donde esta el archivo .txt que desea traducir. Posteriormente, se pasa todos los caracteres del archivo de texto a mayusculas para facilitar el proceso de traducción.
El programa luego procede a separar todo el texto en palabras individuales definiendo la variable "palabras" y ademas se define la listas "traudccion" vacia en la cual se agregaran las palabras ya traducidas.

Por otro lado, en el proceso de traduccion en si, el programa se encarga de identificar si el arhcivo de texto esta en MORSE o en español, y basandose en eso utiliza ciclos for anidados en un condicional para poder identificar a que lista, y a que indice, corresponden cada letra del texto a traducir. Ahora, con esta informacion, el programa se encarga de intercambiar cada palabra de la lista "palabra" con el indice que le corresponde en la lista del lenguaje al que se quiere traducir.
Por ultimo cada palabra traducida se agrega a la lista "traduccion" y se finaliza el proceso uniendo todas las letras de la lista "traduccion" y volviendolas otra vez una cadena de texto con el comando ".join", y se muestra el texto traducido al final.

