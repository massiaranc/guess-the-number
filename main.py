import random
import time
def mensaje_inicio():
   print ("""
          Bienvenid@ al juego 
      *** Adivina el Numero***
      """)
   
def generar_numero_secreto():
        return random.randint(1, 100)

def intento_usuario(historial):
     
    while True:
        try:
            numero_usuario = int(input("Digita un número entre 1 y 100: ")) 
            time.sleep(1)
            if 1 <= numero_usuario <= 100:
                historial.append(numero_usuario)
                return numero_usuario
            else:
                print("Error, el número debe estar entre 1 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def obtener_nombre_usuario():
    while True:
        nombre_usuario = input("Ingresa tu nombre: ")
        if nombre_usuario.isalpha():
            return nombre_usuario
        else:
            print("Entrada no válida. Por favor, ingresa solo letras.")

historial_intentos = []
historial_compu = []

def juego():
    mensaje_inicio()

    nombre_usuario = obtener_nombre_usuario()
    print(f"\nBienvenid@ {nombre_usuario}")
    
   
    #generar número secreto
    numero_secreto = generar_numero_secreto()
    print(f"numero secreto es {numero_secreto}")

    


    # Inicializar números para el usuario y la computadora
    numero_usuario = None
    numero_compu = random.randint(1, 100)
    
  
    print(f"""
    El número inicial de la computadora es {numero_compu}""")

   

    #bucle mientras sea true
    while True:

        numero_usuario = intento_usuario(historial_intentos)

        # Verificar si el usuario adivinó el número secreto
        if numero_usuario == numero_secreto:
            print(f"¡Felicidades {nombre_usuario} ! Adivinaste el número secreto. ")
          
            break

        # Verificar si el intento del usuario es mayor o menor que el número secreto
        if numero_usuario > numero_secreto:
            print("Tu número es muy alto.")
        else:
            print("Tu número es muy bajo.")

      

    #turno de la compu
        ajuste_compu = random.randint(1, 10) #numero aleatorio para hacer el ajuste
        if numero_compu > numero_secreto:
            numero_compu -= ajuste_compu
            if numero_compu < 1:
                numero_compu = 1
        else:
            numero_compu += ajuste_compu
            if numero_compu > 100:
                numero_compu = 100
                
    
        historial_compu.append(numero_compu)

        

        #nuevo intento de la computadora
        print(f"""
    La computadora ajusta su número a: {numero_compu}
    """)

        # Verificar si la computadora adivinó el número secreto
        if numero_compu == numero_secreto:
            print("""
    La computadora ha adivinado el número secreto. ¡La computadora gana!
    """)
            break
    
    
    print(f"\nHistorial de intentos de {nombre_usuario}:")
    for i, intento in enumerate(historial_intentos, 1):
        print(f"Intento {i}: {intento}")

    print("\nHistorial de intentos de la computadora:")
    for i, intento in enumerate(historial_compu, 1):
        print(f"Intento {i}: {intento}")


def jugar_otra_vez():
 while True:
        respuesta = input("¿Deseas jugar de nuevo? (SI o NO): ").strip().upper()  # Normaliza la entrada
        if respuesta == "SI":
            global historial_intentos, historial_compu  # Para reiniciar los historiales
            historial_intentos = []  # Reiniciar historial de intentos del usuario
            historial_compu = [] 
            juego()  # Llama a la función juego si la respuesta es "SI"
            break  # Salimos del bucle después de jugar de nuevo
        elif respuesta == "NO":
            print("Gracias por jugar.")
            break  # Salimos del bucle si la respuesta es "NO"
        else:
            print("Entrada no válida. Por favor, ingresa 'SI' o 'NO'.")
    


if __name__ == '__main__':
    juego()
    jugar_otra_vez()