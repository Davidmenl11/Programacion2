import random
num_random=random.randint(1,20)
intentos=6
intentos_us=0
dificultad=0
print("¿que difucultad quiere elegir?")
print("1:facil")
print("2:dificil")
dificultad=int(input("ingrese una dificultad : "))
if(dificultad==1):
     num_random=random.randint(1,20)
     intentos=6
else:
     num_random=random.randint(1,200)
     intentos=7
while(intentos_us<intentos):
     num_in=int(input("ingrese un numero"))
     intentos_us=intentos_us+1
     if(num_in>num_random):
          print("el numero es mayor al numero secreto")
          
     else:
          if(num_in<num_random):
              print("el numero es el menor al numero secrteto")

          else:
               if(num_in==num_random):
                 break
                 print("el numero numero secreto es :"+ num_random)
                 print(num_random)
          
        
        
    
    
