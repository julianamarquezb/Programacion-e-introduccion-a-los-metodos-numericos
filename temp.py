def traduccion():
  """Recibe un archivo de texto con el nombre 'mensaje.txt' y devuelve uno llamado 'morse.txt' con el mensaje traducido"""
  caracter=["A",'B','C','D','E','F','G','H','I','J','K', 
            'L','M','N','Ñ','O','P','Q','R','S','T','U', 
            'V','W','X','Y','Z','0','1','2','3','4','5',
            '6','7','8','9','&',"'",'@',')','(',':',',',
            '=','!','.','-','+','"','?','/',' ']
  morse=['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-',
         '.-..','--','-.','--.--','---','.--.','--.-','.-.','...','-','..-',
         '...-','.--','-..-','-.--','--..','-----','.----','..---','...--','....-','.....',
         '-....','--...','---..','----.','.-...','.----.','.--.-.','-.--.-','-.--.','---...','--..--',
         '-...-','-.-.--','.-.-.-','-....-','.-.-.','.-..-.','..--..','-..-.',"/"]
  txt=input("Dirección del archivo txt:")
  texto = open(txt,"r")
  caracteres= texto.read().upper()
  palabras= caracteres.split()
  traduccion = []
  if any(x in caracter for x in palabras):    
      for i in palabras:
       traduccion.append(caracter[morse.index(i)]) 
  elif any(x in caracter for x in caracteres):
      for i in caracteres:
       traduccion.append(morse[caracter.index(i)]+" ")
  print("".join(traduccion))   
      
traduccion()