def morse_archivo():
  """Recibe un archivo de texto con el nombre 'mensaje.txt' y devuelve uno llamado 'morse.txt' con el mensaje traducido"""
  caracter_a_morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'Ñ': '--.--', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '&': '.-...',
    "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.', ':': '---...', ',': '--..--', '=': '-...-',
    '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.', ' ': ' '
  }
  a = open("mensaje.txt","r")
  mensaje = a.read()
  mensaje = mensaje.upper()
  mensaje = list(mensaje)
  resultado = ''
  for i in mensaje:
    for n in caracter_a_morse:
      if n == i:
        resultado = resultado + caracter_a_morse[n] + ' '
  resultado = resultado[0:-1]

  b = open('morse.txt', 'w')
  for n in resultado:
    b.write(n)
  b.close()
  
