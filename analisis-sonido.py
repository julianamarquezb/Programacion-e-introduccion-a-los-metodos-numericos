inicial=input('Introduzca la direccion del archivo wav que desea traducir')
muestra=wavio.read('inicial').data
ar=[]
for y in muestra:
  ar.append(y)

m=open("morse.txt","w")

for x in ar:
  
  i=0
  j=0
  for i in x:
    if x!=0:
     y=y+1
     if y<8800:
       m.write("-")
       y==0
     elif y>=3000: 
       m.write(".")
       y==0
    for j in x:
      if x==0:
       z=z+1
       
       if z<=8800:
        
        m.write(" ")
        z==0
       elif z>28600:
        m.write("/")
        z==0

m.close()


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
