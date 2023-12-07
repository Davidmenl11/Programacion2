import random		
IMAGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']		
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()

def OptenerPalabras(ListaDePalabras):
    x=random.randint(0,len(ListaDePalabras)-1)
    PalabraSecreta=ListaDePalabras[x]
    return PalabraSecreta

def JugarDeNuevo():
    print('¿quiere jugar de nuevo?(si o no)')
    return input("ingrese su respuesta: ").lower().startswith('s')

def mostrarTablero(IMAGENES_AHORCADO,letrasCorrectas,letrasIncorrectas,palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()
    print("lestras incorresctas:", end=" ")
    for letra in letrasIncorrectas:
        print(letra, end=" ")
    print()

    espaciosVacios= "_"* len(letrasCorrectas)
    
    for i in range(len(palabraSecreta)):
        espaciosVacios= espaciosVacios[:i]+palabraSecreta[i]+ espaciosVacios[i+1]

    for letra in espaciosVacios:
        print(letra, end=" ")
        print
        
def intentos(letrasProbadas):
    print("adivina la letra")
    intento= input()
    if intento != 1:
        print("por favor introdusca una letra")
    elif intento in letrasProbadas:
        print("ya has probado esta letrea, pruebe con otra")
    elif intento not in 'abcdefghijklmnopqrstuvwxyz':
        print("por favor ingrese una letra")
    else:
        return intento
print("A H O R C A D O")
letrasincorrectas=''
letrasorrectas=''
palabraSecreta=OptenerPalabras(palabras)
juegoTerminado=False
while True:
    mostrarTablero(IMAGENES_AHORCADO,letrasCorrectas,letrasIncorrectas,palabraSecreta)
    intento=intentos(letrasincorrectas + letrasCorrectas)
    if intento in palabraSecreta:
        letrasCorrectas= letrasCorrectas + intento
        EcontrarLetras=True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                EcontrarLetras=False
                break
        if EcontrarLetras:
            print('si la palabra secreta es ' + palabraSecreta + 'has ganado') 
            juegoTerminado=True
               
        else:
            letrasincorrectas= letrasincorrectas + intento
            mostrarTablero(IMAGENES_AHORCADO,letrasCorrectas,letrasIncorrectas,palabraSecreta)
            if len(letrasincorrectas)==len(IMAGENES_AHORCADO)-1:
                mostrarTablero
                print('te has quedado sin intentos despues de ' + str(len(letrasIncorrectas)) + 'intentos fallidos y ' + str(len(letrasCorrectas)) + 'aciertos, la palabra era'+ palabraSecreta)
                juegoTerminado=True
                if juegoTerminado:
                    if JugarDeNuevo():
                        letrasCorrectas=''
                        letrasincorrectas=''
                        juegoTerminado=False
                        palabraSecreta= OptenerPalabras(palabras)
                    else:
                        break
                
                
