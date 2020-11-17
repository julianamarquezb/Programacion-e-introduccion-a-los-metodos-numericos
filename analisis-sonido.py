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
