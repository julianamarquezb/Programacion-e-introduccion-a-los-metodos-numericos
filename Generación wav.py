import numpy as np
import wavio
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
rate = 22050  # samples per second
f = 750.0     # sound frequency (Hz)
xp = np.linspace(0, 0.2, int(0.2*rate), endpoint=False)
p=np.piecewise(xp,[np.logical_and(0.05<=xp,xp<=0.15)],[lambda xp: np.sin(np.pi*f*(xp-0.05)),0])
xr = np.linspace(0, 0.5, int(0.5*rate), endpoint=False)
r=np.piecewise(xr,[np.logical_and(0.05<=xr,xr<=0.45)],[lambda xr: np.sin(np.pi*f*(xr-0.05)),0])
xe= np.linspace(0,0.3,int(0.3*rate),endpoint=False)
elt= 0*xe
epb= np.concatenate((elt,elt)) 
gen={".":p,"-":r," ":elt,"/":epb}
def genwav():
  txt=input("Texto a generar wav o dirección del archivo txt:")
  try: 
      caracteres= open(txt,"r").read().upper()
  except FileNotFoundError:
      caracteres= txt.upper()
  palabras= caracteres.split()
  l=[]
  if all(x in morse for x in palabras):    
      for i in caracteres:
          l.append(gen[i])
  elif all(x in caracter for x in caracteres):
      lp=[]
      for i in caracteres:
          lp.append(morse[caracter.index(i)]+" ")
      for i in "".join(lp):
          l.append(gen[i])
  else:
      print("Hay un caracter no válido en el texto o seleccionó un archivo no existente.")  
  wavio.write("MorseGen.wav", np.concatenate(tuple(l)), rate, sampwidth=3)