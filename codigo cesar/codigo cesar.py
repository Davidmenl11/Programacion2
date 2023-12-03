def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for i in range(len(texto)):
        char = texto[i]

        if (char.isupper()):
            resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
        else:
            resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)

    return resultado

def descifrado_cesar(texto, desplazamiento):
    return cifrado_cesar(texto, 26 - desplazamiento)

texto = input("Por favor, ingresa una frase: ")
desplazamiento = 3
texto_cifrado = cifrado_cesar(texto, desplazamiento)
texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)

print("Texto original : ", texto)
print("Después del cifrado César: ", texto_cifrado)
print("Después del descifrado César: ", texto_descifrado)
