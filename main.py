import csv
import random
import interfaz

if __name__ == "__main__":
    print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
    max_cantidad_intentos = 7
    intentos = 0
    letras_usadas = []
    es_ganador = False

    # Leer la palabra secreta de un archivo csv.
    def leer_palabra_secreta():
        with open ('palabras.csv','r') as f:
            lista_palabras = list(csv.DictReader(f))
            listado = []
            for fila in lista_palabras:
                listado.extend(fila.values())

            f.close()
            return random.choice(listado)
        
    def pedir_letra(letras_usadas):
        ingreso = str.lower(input("Ingrese una letra: ")) 
        while len(ingreso) != 1 or not ingreso.isalpha():
            ingreso = str.lower(input("Ingrese solo una letra: "))
        if ingreso in letras_usadas:
            ingreso = str.lower(input("Ingrese una letra que no haya sido usada: "))
        letras_usadas.append(ingreso)
        return ingreso



    
    def verificar_letra(letra, palabra_secreta):
        if isinstance(letra, str) and len(letra) == 1:
            if letra in palabra_secreta:
                return True
        return False

    def validar_palabra(letras_usadas, palabra_secreta):
        for letra in palabra_secreta:
            if letra not in letras_usadas:
                return False
        return True



 

     
    palabra_secreta = leer_palabra_secreta()
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
    interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
   
   
    
    while  intentos < max_cantidad_intentos and not es_ganador:
        print("La cantidad de intentos que restan son: ", 7-intentos)
        # Pedir una nueva letra
        
        
        
        letra = pedir_letra(letras_usadas)

        # Verificar si la letra es parte de la palabra secreta
              
        if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
            intentos += 1
        
        # Dibujar la interfaz
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado               
        if validar_palabra(letras_usadas, palabra_secreta) == True:
            es_ganador = True
            break
    
    if es_ganador:
            print(f'\n¡Usted ha ganado la partida!, palabra secreta {palabra_secreta}!\n')
    else:
        print('\n¡Ahorcado!')
        print(f'\n¡Usted ha perdido la partida!, palabra secreta {palabra_secreta}!\n')